## @package map 
#  Dynamic mapping and static mapping of API parameter definitions   
#
#  More details (TODO)

import os
import json
import shutil
import subprocess
from Map.fuzzyMatch import *
from Load.loadData import loadLib
from Tool.tool import removeParameter,getFileName
from Extract.getCall import getCallFunction
from Preprocess.preprocess import addDictSingle

## Check the last name in an API call is an alias or not
## 判断一个callAPI最后一个名字是否为库中的别名
#  @param callApi The called API to be check
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


## Dynamic mapping of API signatures
## API签名动态匹配 
#  @param callAPI The called API
#  @param runCommand Project's run command
#  @param runPath Project's run path
#  @param projName Project name
#  @param copyFile project's copied file
#  @param version  The lib's version
#  @param virtualEnv The lib's virtual environment
#  @param lock The lock flag 
#  @param errLst Error list
#  @param curr=1 Current version flag
#  @return dynamicMatchDict Mapped API signatures 
def dynamicMatch(callAPI,runCommand,runPath,projName,copyFile,version,virtualEnv,lock,errLst,curr=1):
    pythonPath=f"{virtualEnv}/bin/python" #先指定python解释器的路径 
    pklFile=getFileName(callAPI,'.pkl')
    pklStr=pklFile.replace('"','\\"')
    callStr=callAPI.replace('"','\\"')
    pklPrefix='../..'
    jsonPrefix='../..'
    
    #当runPath不在runCommand中时，需要切换到运行文件所在的目录执行命令
    #而文件操作的相对路径就是相对于命令执行的路径
    if runPath!='' and runPath not in runCommand:
        l=len(runPath.split('/'))
        while l>0:
            pklPrefix='../'+pklPrefix
            jsonPrefix='../'+jsonPrefix
            l-=1
    
    if not os.path.exists(f"Copy/pkl/{pklFile}"):
        return False
    
    if runPath!='':
        if runPath not in runCommand:
            command=f'cd Dynamic/{projName}/{runPath};{pythonPath} dynamicMatch.py "{pklPrefix}/Copy/pkl/{pklStr}" "{callStr}" "{jsonPrefix}"'
        else:
            command=f'cd Dynamic/{projName};{pythonPath} {runPath}/dynamicMatch.py "{pklPrefix}/Copy/pkl/{pklStr}" "{callStr}" "{jsonPrefix}"'
    else: #大部分属于这种情况
        command=f'cd Dynamic/{projName};{pythonPath} dynamicMatch.py "{pklPrefix}/Copy/pkl/{pklStr}" "{callStr}" "{jsonPrefix}"'

    matchResult=subprocess.run(command,shell=True,executable='/bin/bash',stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    # print(f"{callAPI}{version}")
    # print(matchResult.stdout,matchResult.stderr)
    # print('\n')
    # print(command)
    # print(f"{pklFile}-->{matchResult.stdout}")
    if matchResult.returncode!=0:
        if curr:
            errLst.append(f"{callAPI}, Failed to load pkl in current version{version}: {matchResult.stderr}\n") 
            return False
        
        #若在新版本中无法加载旧版本的pkl文件，则尝试在新版本中重新生成
        #什么情况下不需要在目标版本重新生成？什么情况下需要在mu
        elif 'Ran out of input' not in matchResult.stderr: 
            loadError=f"{callAPI}, Failed to load pkl in target version{version}: {matchResult.stderr}\n" 
            with lock:
                shutil.copy2(copyFile,f"{copyFile}.bak")
                addDictSingle(callAPI,copyFile) #添加字典并运行，在当前文件中添加字典，在运行文件中
                pklFile='new_'+pklFile #更新pkl文件名
                if runPath in runCommand:
                    command=f'cd Copy/{projName};{pythonPath} {runCommand};' #运行项目指令的时候需要考虑运行文件目录是否已经包含到runCommand中了
                else:
                    command=f'cd Copy/{projName}/{runPath};{pythonPath} {runCommand};'
                generateResult=subprocess.run(command,shell=True,executable='/bin/bash',stderr=subprocess.PIPE,text=True)
                if generateResult.returncode==0:
                    pklStr=pklFile.replace('"','\\"')
                    command=f'cd Copy/pkl;mv paraValue.pkl "{pklStr}"'
                    subprocess.run(command,shell=True,executable='/bin/bash',stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
            
                #插桩完后，再将备份后的文件进行还原
                os.remove(copyFile)
                shutil.move(f'{copyFile}.bak',copyFile)
        
            if generateResult.returncode!=0:
                errLst.append(loadError)
                errLst.append(f'[{version}]{callAPI}, generate new pkl failed: {generateResult.stderr}\n')
                return False
            else:
                if runPath!='':
                    if runPath not in runCommand:#需要切换到运行文件所在的目录执行命令
                        command=f'cd Dynamic/{projName}/{runPath};{pythonPath} dynamicMatch.py "{pklPrefix}/Copy/pkl/{pklStr}" "{callStr}" "{jsonPrefix}"'
                    else:
                        command=f'cd Dynamic/{projName};{pythonPath} {runPath}/dynamicMatch.py "{pklPrefix}/Copy/pkl/{pklStr}" "{callStr}" "{jsonPrefix}"'
                else: #大部分属于这种情况
                    command=f'cd Dynamic/{projName};{pythonPath} dynamicMatch.py "{pklPrefix}/Copy/pkl/{pklStr}" "{callStr}" "{jsonPrefix}"'
                matchResult=subprocess.run(command,shell=True,executable='/bin/bash',stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
                if matchResult.returncode!=0:
                    errLst.append(f"[{version}]{callAPI}, load new pkl failed: {matchResult.stderr}\n") 
                    return False
                else:
                    fileName=getFileName(callAPI,'_dynamicMatch.json')
                    with open(f"data/{fileName}",'r',encoding='UTF-8') as fr:
                        try:
                            dynamicMatchDict=json.load(fr)
                        except Exception as e:
                            print(f"json load data/{fileName} failed: {e}\n")
                    return dynamicMatchDict

        else:
            return False    

    else:
        fileName=getFileName(callAPI,'_dynamicMatch.json')
        with open(f"data/{fileName}",'r',encoding='UTF-8') as fr:
            try:
                dynamicMatchDict=json.load(fr)
            except Exception as e:
                print(f"json load data/{fileName} failed: {e}\n")
        return dynamicMatchDict


## Construct the mapping between the invoked API and the lib API to obtain its signature 
## 建立invoked API与 lib API之间的映射关系，从而获取其参数定义
## 先进行动态匹配，动态匹配的结果是保存在api_dynamic.json文件中的
## 动态匹配的成功包括3步：1.加载PKL； 2.动态脚本执行成功，3.动态获取参数成功（部分内置api无法获取参数）
#  @param callAPI The called API
#  @param runCommand Project's run command
#  @param runPath Project's run path
#  @param projName Project name
#  @param libName The lib's name
#  @param copyFile project's copied file
#  @param version  The lib's version
#  @param virtualEnv The lib's virtual environment
#  @param lock The lock flag 
#  @param errLst Error list
#  @param curr=1 Current version flag
#  @ans Mapped API signatures 
def mapAPI(callAPI,runCommand,runPath,formatAPI,projName,libName,copyFile,version,virtualEnv,lock,errLst,curr=1):
    dynamicMatchDict=dynamicMatch(callAPI,runCommand,runPath,projName,copyFile,version,virtualEnv,lock,errLst,curr)
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
    
