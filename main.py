## @file main.py 
#  PCART's main function entry   
# 
#
#  Entry point for the full PCART pipeline: preprocess → extract → map →
#  compatibility analysis → repair → report. Supports multiprocessing for
#  parallel file processing with shared matching dictionaries.
#  PCART完整流水线入口：预处理→提取→映射→兼容性分析→修复→报告。
#  支持多进程并行文件处理，使用共享匹配字典。



import os
import sys
import json
import time
import shutil
import subprocess
from Path.getPath import *
from Map.map import mapAPI
from multiprocessing import Pool
from multiprocessing import Manager
from Extract.getCall import getCallFunction
from Extract.pcresolveBridge import buildCallsiteLookup
from Preprocess.preprocess import codeProcess
from Repair.repair import repairTask,validateByRun
from Tool.tool import getAst,save2txt,loadConfig,removeParameter,buildRunCommand,resolveConfigFilePath,resolveConfigValuePath
from Tool.workspace import createRunWorkspace,exportRunReport,getRepoRoot,getRuntimePaths,workspaceCwd
from Change.changeAnalyze import isCompatible,addValueForAPI,updateSharedDict,querySharedDict,updateErrorLst


## One process handles one file
## 一个进程处理一个文件
#
#  @param args Input parameters for processing one project file (13 values normally, 14 values with a PCResolve lookup)
#  @return (ansDict,fileRelativePath,invokedAPINum) ansDict: detection and repair results;
#          fileRelativePath: the file being processed; invokedAPINum: number of invoked APIs
def backwardTask(args):
    ansDict={} #保存每个文件处理的情况
    if len(args)==13:
        projName,libName,file,currentVersion,currentEnv,targetVersion,targetEnv,runCommand,runPath,lock,sharedDict,coverSet,runtimePaths=args
        pcresolveLookup=None
    else:
        projName,libName,file,currentVersion,currentEnv,targetVersion,targetEnv,runCommand,runPath,lock,sharedDict,coverSet,runtimePaths,pcresolveLookup=args
    copyRoot=runtimePaths['copy_root']
    dataDir=runtimePaths['data_dir']
    reportDir=runtimePaths['report_dir']
    # fileName=file.split('/')[-1][0:-3]
    fileName = os.path.basename(file)[:-3]
    
    #step1:将源代码文件映射到Copy目录中
    # tempLst=file.split('/')
    normalized_file = file.replace('\\', '/')
    tempLst = normalized_file.split('/')
    pos=tempLst.index(projName)
    realProjPath='/'.join(tempLst[0:pos+1])
    fileRelativePath='/'.join(tempLst[pos:])
    copyFile = os.path.join(copyRoot, *fileRelativePath.split('/'))
    #step2:先把当前文件中指定的第三方库的API抽取出来
    callAPIDict,_=getCallFunction(file,libName,realProjPath,pcresolveLookup=pcresolveLookup) #key是artifact id，value是结构化调用点记录
    os.makedirs(dataDir, exist_ok=True)
    with open(os.path.join(dataDir, f'{fileName}_callAPIDict.json'), 'w', encoding='utf-8') as fw:
        json.dump(callAPIDict, fw, indent=4, ensure_ascii=False)
    root=None
    astError=None
    try: 
        root=getAst(file) #获取当前文件的AST，便于修复使用
    except Exception as e:
        astError=e
    invokedAPINum=len(callAPIDict)
    errorLog = os.path.join(reportDir, f'{projName}_fixed_log.txt')
    for key,record in callAPIDict.items():
        errLst=[] #记录错误信息
        ansDict[key]={}
        callAPI=record['call_text']
        lineNum=record['lineno']
        formatAPI=record['format_api']
        callKey=record['id']
        ansDict[key]['Invoked API']=callAPI
        ansDict[key]['Location']=f"At Line {lineNum} in {fileRelativePath}"

        if callKey not in coverSet:
            ansDict[key]['Coverage']='No' 
            continue
        
        ansDict[key]['Coverage']='Yes' 
        formatAPI=removeParameter(formatAPI)
        #step3:将项目中的API与库API进行匹配，获得参数定义
        #首先判断一下这个API是否匹配过，若之前匹配过了，就不用再匹配了
        with lock:
            matchDict=querySharedDict(callKey,sharedDict) #当查询操作发生在更新操作之前，可能会查询失败
        if len(matchDict)>0:
            currentMatch=matchDict['current']
            targetMatch=matchDict['target']
        else:
            currentMatch=mapAPI(callAPI,runCommand,runPath,formatAPI,projName,libName,copyFile,currentVersion,currentEnv,lock,errLst,callKey=callKey,runtimePaths=runtimePaths)
            targetMatch=mapAPI(callAPI,runCommand,runPath,formatAPI,projName,libName,copyFile,targetVersion,targetEnv,lock,errLst,curr=0,callKey=callKey,runtimePaths=runtimePaths)
            with lock:
                updateSharedDict(callKey,currentMatch,targetMatch,sharedDict)#更新sharedDict
        
        
        ansDict[key][f"Definition @{currentVersion} <{currentMatch['matchMethod']}>"]=str(currentMatch['match'])
        ansDict[key][f"Definition @{targetVersion} <{targetMatch['matchMethod']}>"]=str(targetMatch['match'])
        
        #step4:变更分析,若不兼容则返回需要修复的操作
        repairLst=isCompatible(currentMatch,targetMatch) #repairLst中每个元素都是tuple
        if repairLst==None:
            ansDict[key]['Compatible']="Unknown"
            if len(errLst)>0:
                errorMsg = f"Error occurred, please check the {projName}_fixed_log.txt"
                with lock:
                    updateErrorLst(errorLog,errLst)
            continue
        
        if len(repairLst)==0: #若返回修复字典的个数为零，则一定是兼容的
            ansDict[key]['Compatible']='Yes'
        else:
            if root is None:
                ansDict[key]['Compatible']='Unknown'
                ansDict[key]['Repair <Unknown>']='AST parse failed'
                errLst.append(f"{callAPI}, AST parse failed in {fileRelativePath}: {astError}\n")
            else:
                apiWithValue=addValueForAPI(callAPI,projName,runPath,runCommand,currentEnv,targetEnv,errLst,callKey=callKey,runtimePaths=runtimePaths) #apiWithValue为空表示添加参数失败
                fixedAPI,compatibilityLabel,repairStatus=repairTask(root,callAPI,apiWithValue,projName,runPath,runCommand,repairLst,targetEnv,errLst,callKey=callKey,runtimePaths=runtimePaths)
                if compatibilityLabel=='Compatible':
                    ansDict[key]['Compatible']='Yes'
                else:
                    if compatibilityLabel=='Incompatible':
                        ansDict[key]['Compatible']='No'
                    else:
                        ansDict[key]['Compatible']='Unknown'

                    if repairStatus=='Successful':
                        ansDict[key]['Repair <Successful>']=f"{fixedAPI}"
                    elif repairStatus=='Failed':
                        ansDict[key]['Repair <Failed>']=f"{fixedAPI}"
                    else:
                        ansDict[key]['Repair <Unknown>']=f"{fixedAPI}"


        if len(errLst)>0:
            errorMsg = f"Error occurred, please check the {projName}_fixed_log.txt"
            with lock:
                updateErrorLst(errorLog,errLst)


    #将修改操作更新到代码源文件
    # with open(f"{file.rsplit('/',1)[0]}/new_{fileName}.py",'w') as fw:
    #     repairCode=ast.unparse(root)
    #     fw.write(repairCode+'\n') 
    return ansDict,fileRelativePath,invokedAPINum



## Generate pkl files and perform detection and repair tasks
## 生成项目调用API的pkl文件以及执行检测与修复任务
#
#  @param projPath  The path to the project / 项目路径
#  @param libName   The upgraded Python third-party library name / 升级的第三方库名
#  @param currentVersion The upgraded lib's current version / 库的当前版本
#  @param currentEnv Current version's virtual environment / 当前版本的虚拟环境
#  @param targetVersion The upgraded lib's target version / 库的目标版本
#  @param targetEnv Target version's virtual environment / 目标版本的虚拟环境
#  @param runCommand The run command of the project / 项目运行命令
#  @param runPath   The relative path of the run file / 运行文件的相对路径
#  @param workspace RunWorkspace object for this execution / 本次执行的运行工作区
#  @param pcresolveLookup Optional pre-built PCResolve lookup table shared with preprocessing
def backward(projPath,libName,currentVersion,currentEnv,targetVersion,targetEnv,runCommand,runPath,workspace,pcresolveLookup=None):
    runtimePaths=getRuntimePaths(workspace)
    copyRoot=runtimePaths['copy_root']
    dataDir=runtimePaths['data_dir']
    tempDir=runtimePaths['temp_dir']
    reportDir=runtimePaths['report_dir']
    pathObj=Path('DF')
    pathObj.getPath(projPath)
    filePath=[it for it in pathObj.path if it.endswith('py')] #保留项目中的.py文件
    projName=os.path.basename(projPath)
    errorLog = os.path.join(reportDir, f'{projName}_fixed_log.txt')
    if os.path.exists(errorLog):
        os.remove(errorLog)
    
    #先在起始版本中生成每个API的pkl
    # cwd 自动适配：使用 subprocess cwd 参数替代 shell cd
    if runPath and runPath not in runCommand:
        cwd = os.path.join(copyRoot, projName, runPath)
    else:
        cwd = os.path.join(copyRoot, projName)
    print('Running the project...')
    cmd=buildRunCommand(runCommand,currentEnv)
    createResult = subprocess.run(
        cmd, cwd=cwd, capture_output=True, text=True, encoding='utf-8'
    )
    if createResult.returncode!=0:
        print(f'Failure to generate PKL in current version')
        print(createResult.stderr)
        return
    print("Running complete")
     
    #生成pkl成功后，将项目恢复成原样，便于之后对其中某个API单独插桩
    os.makedirs(tempDir,exist_ok=True)
    tempProjPath=os.path.join(tempDir,projName)
    if os.path.exists(tempProjPath):
        shutil.rmtree(tempProjPath)
    shutil.move(os.path.join(copyRoot, projName), tempProjPath)
    shutil.move(os.path.join(copyRoot, f'bak_{projName}'), os.path.join(copyRoot, projName))
    shutil.move(tempProjPath, os.path.join(copyRoot, f'bak_{projName}'))


    #用PCResolve进行全项目API调用识别，结果在所有任务间复用
    if pcresolveLookup is None:
        pcresolveLookup=buildCallsiteLookup(projPath,libName)

    #这里用进程池同时处理多个任务，但对于torch库可能会报错RuntimeError:CUDA out or memory
    #对数据库的读写需要加锁
    coverSet=set()
    coverSet_path = os.path.join(copyRoot, 'pkl', 'coverSet')
    if os.path.exists(coverSet_path):
        with open(coverSet_path, 'r', encoding='utf-8') as fr:
            tempLst=fr.readlines()
        for it in tempLst:
            it=it.rstrip('\n').replace(' ','')
            coverSet.add(it)
    manager=Manager()
    lock=manager.Lock() #创建一个共享锁
    sharedDict=manager.dict() #创建一个共享字典
    tasks=[(projName,libName,file,currentVersion,currentEnv,targetVersion,targetEnv,runCommand,runPath,lock,sharedDict,coverSet,runtimePaths,pcresolveLookup) for file in filePath]
    pool=Pool(processes=1)
    resultLst=pool.map(backwardTask,tasks)
    pool.close() #关闭进程池，使其不再接受新的任务
    pool.join() #等待进程池中所有的任务执行完，否则主进程可能继续往下执行提前结束，而导致部分任务没有执行完
    save2txt(resultLst, libName, runCommand, os.path.join(reportDir, f'{projName}.txt'))


## Run PCART with an isolated workspace
## 在隔离工作区中运行PCART
#
#  This function keeps old config fields unchanged, creates a RunWorkspace,
#  runs preprocessing and analysis inside the workspace, then exports reports.
#  该函数保持旧配置字段不变，创建运行工作区，在工作区内完成预处理和分析，
#  最后导出用户可见报告。
#
#  @param config The config file path or config file name under Configure
#  @return RunWorkspace object for this execution
def run(config):
    repoRoot=getRepoRoot()
    configPath=resolveConfigFilePath(config,repoRoot)

    #加载配置
    projPath,runCommand,runPath,libName,currentVersion,targetVersion,currentEnv,targetEnv=loadConfig(configPath)
    projPath=resolveConfigValuePath(repoRoot,projPath)
    currentEnv=resolveConfigValuePath(repoRoot,currentEnv)
    targetEnv=resolveConfigValuePath(repoRoot,targetEnv)

    workspace=createRunWorkspace(
        repoRoot,
        projPath,
        runCommand,
        runPath,
        libName,
        currentVersion,
        targetVersion,
        currentEnv,
        targetEnv,
    )
    print(f"Run workspace: {workspace.workspace_root}")
    print("Code preprocessing...")

    pcresolveLookup=buildCallsiteLookup(projPath,libName)

    with workspaceCwd(workspace.workspace_root):
        #首先对代码进行预处理
        codeProcess(projPath,runCommand,runPath,libName,workspace=workspace,pcresolveLookup=pcresolveLookup)
        print("Code preprocess complete")

        #执行主逻辑
        backward(projPath,libName,currentVersion,currentEnv,targetVersion,targetEnv,runCommand,runPath,workspace=workspace,pcresolveLookup=pcresolveLookup)

    exportRunReport(workspace)
    print(f"Report output: {workspace.report_root}")
    return workspace


## Main function of PCART
## PCART主函数
def main():
    if len(sys.argv) < 3:
       print("Usage: python main.py -cfg config.json")
       sys.exit(1)

    config=sys.argv[2]
    start=time.time()

    run(config)

    end=time.time()
    print(f"Total run time={int(end-start)}s")


if __name__=='__main__':
    main()
