## @package map 
#  Dynamic mapping and static mapping of API parameter definitions   
#
#
#  Core mapping module: dynamicMatch() reconstructs API callables from runtime
#  pkl data and uses inspect.signature() to extract signatures; fuzzymatch()
#  provides static fallback via fuzzy name matching. mapAPI() orchestrates the
#  two-tier strategy and manages pkl regeneration, manifest tracking, and result
#  snapshots.
#  核心映射模块：dynamicMatch()从运行时pkl数据重建API可调用对象并使用
#  inspect.signature()提取签名；fuzzymatch()通过模糊名称匹配提供静态回退。
#  mapAPI()编排两级策略，管理pkl重新生成、manifest跟踪和结果快照。



import os
import json
import shutil
import subprocess
from Map.fuzzyMatch import *
from Load.loadData import loadLib
from Tool.tool import removeParameter,getFileName,resolvePythonExecutable,buildRunCommand,getArtifactHash,getArtifactDisplayName
from Extract.getCall import getCallFunction
from Preprocess.preprocess import addDictSingle



## Check whether the last name in an API call is an alias
## 判断一个callAPI最后一个名字是否为库中的别名
#
#  @param callApi The called API to be checked
#  @param assignDict The assign dict stores the alias of APIs
#  @return realName The real name of the called API or None
def isAlias(callApi,assignDict):
    capilst=callApi.split('.')
    candidate={}
    for k in assignDict:
        keylst=k.split('.')
        if capilst[-1]==keylst[-1]:
            candidate[k]=len(set(capilst)&set(keylst))/len(keylst)
    if len(candidate)>0:
        ansKey=sorted(candidate,key=lambda i:candidate[i],reverse=True)[0]
        realName=assignDict[ansKey]
        return realName
    return None



## Static mapping of API signatures
## API签名静态匹配
#
#  @param formatAPI The called API
#  @param libName The upgraded lib 
#  @param version The upgraded lib's version 
#  @param builtinFlag Built-in API flag
#  @return ansDict Mapped API signatures 
def fuzzymatch(formatAPI,libName,version,builtinFlag): #callAPIDict是传入传出参数
    libAPIs,assignDict,libAPIIns=loadLib(libName,version)
    Fuzz=fuzzyMatch()
    if builtinFlag and len(libAPIIns)>0:
        ans=Fuzz.fmatch(formatAPI,libAPIIns) #只从.pyi文件里找,但如果没有注释的话,也不一定能找到，
    else:
        ans=Fuzz.fmatch(formatAPI,libAPIs)

    if len(ans)==0 and not builtinFlag:
        aliasName=Fuzz.alias
        realName=isAlias(aliasName,assignDict) #检查是否是别名，是的话就将别名还原成真名，然后再进行模糊匹配
        if realName is not None: 
            ans=Fuzz.fmatch(realName,libAPIs)
    
    #对匹配出的结果按照不同的函数名进行分类,得到一个形式为{同名:[重载]}字典
    ansDict={}
    for it in ans: #ans是模糊得到的结果，当然也可能为空
        pos=it.find('(')
        if pos!=-1:
            apiName=it[0:pos]
            parameters=it[pos:]
            if removeParameter(it)==formatAPI:#若和formatAPI完全相等，则说明匹配的结果是唯一且正确
                return {apiName:[parameters]}
            
            if apiName not in ansDict:
                ansDict[apiName]=[] #初始化字典，把同一个API的不同重载放到一起
            ansDict[apiName].append(parameters)
    return ansDict 


## Save dynamic match result snapshot
## 保存动态匹配结果快照
#
#  @param pklKey The callsite key used to locate the pkl/json data
#  @param version The lib version used in this dynamic match
#  @param curr Current version flag, 1 for current and 0 for target
#  @param dynamicMatchDict Dynamic match result loaded from dynamicMatch.py
#  @param pklFile The pkl candidate file used by this dynamic match
#  @param runtimePaths Runtime artifact paths for the current PCART workspace
#  @return None
def saveDynamicMatchSnapshot(pklKey,version,curr,dynamicMatchDict,pklFile=None,*,runtimePaths):
    if not isinstance(dynamicMatchDict,dict):
        return
    dataDir=runtimePaths['data_dir']
    phase='current' if curr else 'target'
    # getFileName(...,'.json')会处理Windows非法文件名字符，再去掉扩展名用于拼接快照文件名
    safeKey=getFileName(pklKey,'.json')[:-5]
    safeVersion=str(version).replace(os.sep,'_').replace('/','_').replace('\\','_')
    snapshotDict=dict(dynamicMatchDict)
    # 保留current/target最终动态匹配结果，原dynamicMatch.json仍作为子进程通信文件
    snapshotDict['_pcart']={
        'phase': phase,
        'version': str(version),
        'callKey': pklKey,
        'artifact': pklKey,
        'artifactHash': getArtifactHash(pklKey),
        'debugName': getArtifactDisplayName(pklKey),
    }
    if pklFile is not None:
        snapshotDict['_pcart']['pklFile']=pklFile
    os.makedirs(dataDir,exist_ok=True)
    fileName=f"{phase}_{safeKey}_{safeVersion}_dynamicMatch.json"
    with open(os.path.join(dataDir,fileName),'w',encoding='UTF-8') as fw:
        json.dump(snapshotDict,fw,indent=4,ensure_ascii=False)


## Check whether a callsite candidate manifest records pkl save failure
## 检查调用点候选清单是否记录了pkl保存失败
#
#  @param pklKey The callsite key used to locate the manifest
#  @param runtimePaths Runtime artifact paths for the current PCART workspace
#  @return result Whether any candidate was covered but failed to save
def hasSaveFailedManifest(pklKey,*,runtimePaths):
    copyRoot=runtimePaths['copy_root']
    manifestPath=os.path.join(copyRoot,'pkl',getFileName(pklKey,'.manifest.json'))
    if not os.path.exists(manifestPath):
        return False
    try:
        with open(manifestPath,'r',encoding='UTF-8') as fr:
            manifest=json.load(fr)
    except Exception:
        return False
    if not manifest.get('covered'):
        return False
    for candidate in manifest.get('candidates',[]):
        if candidate.get('status')=='save_failed':
            return True
    return False



## Dynamic mapping of API signatures
## API签名动态匹配 
#
#  @param callAPI The called API
#  @param runCommand The run command of the project
#  @param runPath The relative path of the run file
#  @param projName Project name
#  @param copyFile project's copied file
#  @param version  The lib's version
#  @param virtualEnv The lib's virtual environment
#  @param lock The lock flag 
#  @param errLst Error list
#  @param curr=1 Current version flag
#  @param callKey Unique callsite artifact id
#  @param runtimePaths Runtime artifact paths for the current PCART workspace
#  @return dynamicMatchDict Mapped API signatures 
def dynamicMatch(callAPI,runCommand,runPath,projName,copyFile,version,virtualEnv,lock,errLst,curr=1,*,callKey,runtimePaths):
    # pythonPath=f"{virtualEnv}/bin/python" #先指定python解释器的路径
    pythonPath = resolvePythonExecutable(virtualEnv)
    copyRoot=runtimePaths['copy_root']
    dynamicRoot=runtimePaths['dynamic_root']
    dataDir=runtimePaths['data_dir']
    pklKey = callKey
    pklFile=getFileName(pklKey,'.pkl')
    # withitem调用优先尝试运行时对象，其次尝试还原表达式，最后尝试通用pkl候选
    pklCandidateFiles=[pklFile[:-4]+'__object.pkl',pklFile[:-4]+'__expr.pkl',pklFile]

    #当runPath不在runCommand中时，需要切换到运行文件所在的目录执行命令
    #而文件操作的相对路径就是相对于命令执行的路径
    if runPath and runPath not in runCommand:
        dynamic_cwd = os.path.join(dynamicRoot, projName, runPath)
        dynamic_script = 'dynamicMatch.py'
    else:
        dynamic_cwd = os.path.join(dynamicRoot, projName)
        dynamic_script = os.path.join(runPath, 'dynamicMatch.py') if runPath else 'dynamicMatch.py'
    lastResult = None
    lastDynamicMatchDict = None
    existingPklFiles=[file for file in pklCandidateFiles if os.path.exists(os.path.join(copyRoot,'pkl',file))]
    if not existingPklFiles:
        if curr or not hasSaveFailedManifest(pklKey,runtimePaths=runtimePaths):
            return False
        lastResult=subprocess.CompletedProcess([],1,'','manifest save_failed')
    else:
        for candidatePklFile in existingPklFiles:
            # 某个候选返回nullptr时继续尝试下一个候选，避免可inspect调用被提前判为static
            pkl_arg = os.path.join(copyRoot, 'pkl', candidatePklFile)
            matchResult = subprocess.run(
                [pythonPath, dynamic_script, pkl_arg, callAPI, dataDir, pklKey],
                cwd=dynamic_cwd, capture_output=True, text=True, encoding='utf-8'
            )
            lastResult = matchResult
            if matchResult.returncode == 0:
                fileName=getFileName(pklKey,'_dynamicMatch.json')
                matchJsonPath=os.path.join(dataDir,fileName)
                with open(matchJsonPath,'r',encoding='UTF-8') as fr:
                    try:
                        dynamicMatchDict=json.load(fr)
                    except Exception as e:
                        dynamicMatchDict=None
                        print(f"json load {matchJsonPath} failed: {e}\n")
                lastDynamicMatchDict = dynamicMatchDict
                if dynamicMatchDict and dynamicMatchDict.get('match') != 'nullptr':
                    saveDynamicMatchSnapshot(pklKey,version,curr,dynamicMatchDict,candidatePklFile,runtimePaths=runtimePaths)
                    return dynamicMatchDict
                continue
            continue

    if lastResult is None:
        return False

    stdout = lastResult.stdout
    stderr = lastResult.stderr
    matchResult = lastResult

    if matchResult.returncode!=0:
        if curr:
            errLst.append(f"{callAPI}, Failed to load pkl in current version{version}: {matchResult.stderr}\n") 
            return False
        
        #若在新版本中无法加载旧版本的pkl文件，则尝试在新版本中重新生成
        #什么情况下不需要在目标版本重新生成？什么情况下需要在mu
        # elif 'Ran out of input' not in matchResult.stderr:
        elif stderr and 'Ran out of input' not in stderr:
            loadError=f"{callAPI}, Failed to load pkl in target version{version}: {matchResult.stderr}\n" 
            with lock:
                shutil.copy2(copyFile,f"{copyFile}.bak")
                addDictSingle(callAPI,copyFile,pklKey) #添加字典并运行，在当前文件中添加字典，在运行文件中
                regeneratedPklFiles=[]
                if runPath and runPath not in runCommand:
                    copy_cwd = os.path.join(copyRoot, projName, runPath)
                else:
                    copy_cwd = os.path.join(copyRoot, projName)
                # generateResult=subprocess.run(command,shell=True,executable='/bin/bash',stderr=subprocess.PIPE,text=True)
                cmd=buildRunCommand(runCommand,virtualEnv)
                generateResult = subprocess.run(
                    cmd, cwd=copy_cwd, capture_output=True, text=True, encoding='utf-8'
                )
                if generateResult.returncode==0:
                    # target环境重生成时保留object/expr候选顺序，避免退回混合老格式pkl
                    regeneratedCandidates=[
                        ('paraValue__object.pkl','new_'+pklFile[:-4]+'__object.pkl'),
                        ('paraValue__expr.pkl','new_'+pklFile[:-4]+'__expr.pkl'),
                        ('paraValue.pkl','new_'+pklFile),
                    ]
                    for sourceName,targetName in regeneratedCandidates:
                        sourcePath=os.path.join(copyRoot,'pkl',sourceName)
                        if os.path.exists(sourcePath):
                            targetPath=os.path.join(copyRoot,'pkl',targetName)
                            os.replace(sourcePath,targetPath)
                            regeneratedPklFiles.append(targetName)
             
                #插桩完后，再将备份后的文件进行还原
                os.remove(copyFile)
                shutil.move(f'{copyFile}.bak',copyFile)
        
            if generateResult.returncode!=0:
                errLst.append(loadError)
                errLst.append(f'[{version}]{callAPI}, generate new pkl failed: {generateResult.stderr}\n')
                return False
            else:
                if not regeneratedPklFiles:
                    errLst.append(f'[{version}]{callAPI}, generate new pkl failed: no pkl file generated\n')
                    return False
                for regeneratedPklFile in regeneratedPklFiles:
                    pkl_arg = os.path.join(copyRoot, 'pkl', regeneratedPklFile)
                    matchResult = subprocess.run(
                        [pythonPath, dynamic_script, pkl_arg, callAPI, dataDir, pklKey],
                        cwd=dynamic_cwd, capture_output=True, text=True, encoding='utf-8'
                    )
                    if matchResult.returncode!=0:
                        continue
                    fileName=getFileName(pklKey,'_dynamicMatch.json')
                    matchJsonPath=os.path.join(dataDir,fileName)
                    with open(matchJsonPath,'r',encoding='UTF-8') as fr:
                        try:
                            dynamicMatchDict=json.load(fr)
                        except Exception as e:
                            dynamicMatchDict=None
                            print(f"json load {matchJsonPath} failed: {e}\n")
                    if dynamicMatchDict and dynamicMatchDict.get('match') != 'nullptr':
                        saveDynamicMatchSnapshot(pklKey,version,curr,dynamicMatchDict,regeneratedPklFile,runtimePaths=runtimePaths)
                        return dynamicMatchDict
                    lastDynamicMatchDict=dynamicMatchDict
                if lastDynamicMatchDict:
                    saveDynamicMatchSnapshot(pklKey,version,curr,lastDynamicMatchDict,runtimePaths=runtimePaths)
                    return lastDynamicMatchDict
                errLst.append(f"[{version}]{callAPI}, load new pkl failed: {matchResult.stderr}\n") 
                return False

        else:
            return False    

    else:
        if lastDynamicMatchDict:
            saveDynamicMatchSnapshot(pklKey,version,curr,lastDynamicMatchDict,runtimePaths=runtimePaths)
        return lastDynamicMatchDict



## Construct the mapping between the invoked API and the lib API to obtain its signature 
## 建立invoked API与 lib API之间的映射关系，从而获取其参数定义
#
#  先进行动态匹配，动态匹配的结果是保存在api_dynamic.json文件中的
#  动态匹配的成功包括3步：1.加载PKL； 2.动态脚本执行成功，3.动态获取参数成功（部分内置api无法获取参数）
#
#  @param callAPI The called API
#  @param runCommand The run command of the project
#  @param runPath The relative path of the run file
#  @param formatAPI The restored API string used for static matching
#  @param projName Project name
#  @param libName The lib's name
#  @param copyFile project's copied file
#  @param version  The lib's version
#  @param virtualEnv The lib's virtual environment
#  @param lock The lock flag 
#  @param errLst Error list
#  @param curr=1 Current version flag
#  @param callKey Unique callsite artifact id
#  @param runtimePaths Runtime artifact paths for the current PCART workspace
#  @return ans Mapped API signatures 
def mapAPI(callAPI,runCommand,runPath,formatAPI,projName,libName,copyFile,version,virtualEnv,lock,errLst,curr=1,*,callKey,runtimePaths):
    dynamicMatchDict=dynamicMatch(callAPI,runCommand,runPath,projName,copyFile,version,virtualEnv,lock,errLst,curr,callKey=callKey,runtimePaths=runtimePaths)
    ans={}
    ans['format']=formatAPI
    if dynamicMatchDict!=False: #若动态匹配成功,还要对动态匹配的结果进行检查
        result=dynamicMatchDict['match']
        ans['error']=dynamicMatchDict['error']
        if 'internalPath' in dynamicMatchDict:
            ans['internalPath']=dynamicMatchDict['internalPath']
        else:
            ans['internalPath']=formatAPI 
    
        if 'builtin' in dynamicMatchDict['error']: #这里的内置不一定是库的内置，有可能是python内置,如何区分?
            ans['match']=fuzzymatch(formatAPI,libName,version,1) #目前只发现pytorch中把内置记录到了.pyi中
            ans['matchMethod']='static'
        elif result=='nullptr': #若inspect失败
            ans['match']=fuzzymatch(formatAPI,libName,version,0)
            ans['matchMethod']='static'
        else:
            ans['match']=result
            ans['matchMethod']='dynamic'
    else:
        ans['match']=fuzzymatch(formatAPI,libName,version,0)
        ans['matchMethod']='static'

    return ans
