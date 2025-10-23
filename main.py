## @file main.py 
#  PCART's main function entry   
# 
#  More details (TODO)



import os
import sys
import ast
import json
import time
import shutil
import subprocess
import platform
from Path.getPath import *
from Map.map import mapAPI
from multiprocessing import Pool
from multiprocessing import Manager
from Extract.getCall import getCallFunction
from Preprocess.preprocess import codeProcess
from Repair.repair import repairTask,validateByRun
from Tool.tool import getAst,save2txt,loadConfig,removeParameter,getFileName
from Change.changeAnalyze import isCompatible,addValueForAPI,updateSharedDict,querySharedDict,updateErrorLst



## One process handles one file 
## 一个进程处理一个文件
#
#  @param args Input parameters for processing one project file 
#  @return (ansDict,fileRelativePath,invokedAPINum) ansDict: API parameter compatibility issue detection and repair results; fileRelativePath: The detected and repaired project file; invokedAPINum: The number of invoked APIs 
def backwardTask(args):
    ansDict={} #保存每个文件处理的情况
    projName,libName,file,currentVersion,currentEnv,targetVersion,targetEnv,runCommand,runPath,lock,sharedDict,coverSet=args
    # fileName=file.split('/')[-1][0:-3]
    fileName = os.path.basename(file)[:-3]
    
    #step1:先把当前文件中指定的第三方库的API抽取出来
    callAPIDict,_=getCallFunction(file,libName) #key是还原前的API，value是还原后的API
    # with open(f'data/{fileName}_callAPIDict.json','w') as fw:
    os.makedirs('data', exist_ok=True)
    with open(os.path.join('data', f'{fileName}_callAPIDict.json'), 'w', encoding='utf-8') as fw:
        json.dump(callAPIDict, fw, indent=4, ensure_ascii=False)
    try: 
        root=getAst(file) #获取当前文件的AST，便于修复使用
    except:
        pass
    #step2:将源代码文件映射到Copy目录中
    # tempLst=file.split('/')
    normalized_file = file.replace('\\', '/')
    tempLst = normalized_file.split('/')
    pos=tempLst.index(projName)
    realProjPath='/'.join(tempLst[0:pos+1])
    fileRelativePath='/'.join(tempLst[pos:])
    # copyFile='./Copy/'+fileRelativePath
    copyFile = os.path.join('.', 'Copy', *fileRelativePath.split('/'))
    invokedAPINum=len(callAPIDict)
    # errorLog=f"Report/{projName}_fixed_log.txt"
    errorLog = os.path.join('Report', f'{projName}_fixed_log.txt')
    for key,formatAPI in callAPIDict.items():
        errLst=[] #记录错误信息
        ansDict[key]={}
        callAPI=key.split('#_')[0]
        lineNum=key.split('#_')[1]
        ansDict[key]['Location']=f"At Line {lineNum} in {fileRelativePath}"
        #判断有没有覆盖有两个条件，先看是否有pkl，再看是否在coverSet中
        # if not os.path.exists(f"Copy/pkl/{pklName}") and f"{fileName}##{lineNum}##{callAPI}".replace(' ','') not in coverSet:
        #有些API虽然有pkl但实际上是与它同名的其它API的pkl，即它并没有被真正覆盖
        #所以不能以pkl是否存在来判断其是否被覆盖了
        # if f"{fileName}##{lineNum}##{callAPI}".replace(' ','') not in coverSet:
        #     ansDict[key]['Coverage']='No'
        #     print(f"{fileName}##{lineNum}##{callAPI}".replace(' ',''))
        #     continue
        
        flag=0
        for it in coverSet:
            if f"{fileName}##{lineNum}##{callAPI}".split('(')[0].replace(' ','') in it:
                flag=1
                break
        if flag==0:
            ansDict[key]['Coverage']='No' 
            continue
        
        ansDict[key]['Coverage']='Yes' 
        formatAPI=removeParameter(formatAPI)
        #step3:将项目中的API与库API进行匹配，获得参数定义
        #首先判断一下这个API是否匹配过，若之前匹配过了，就不用再匹配了
        with lock:
            matchDict=querySharedDict(callAPI,sharedDict) #当查询操作发生在更新操作之前，可能会查询失败
        if len(matchDict)>0:
            currentMatch=matchDict['current']
            targetMatch=matchDict['target']
        else:
            currentMatch=mapAPI(callAPI,runCommand,runPath,formatAPI,projName,libName,copyFile,currentVersion,currentEnv,lock,errLst)
            targetMatch=mapAPI(callAPI,runCommand,runPath,formatAPI,projName,libName,copyFile,targetVersion,targetEnv,lock,errLst,curr=0)
            with lock:
                updateSharedDict(callAPI,currentMatch,targetMatch,sharedDict)#更新sharedDict
        
        
        ansDict[key][f"Definition @{currentVersion} <{currentMatch['matchMethod']}>"]=str(currentMatch['match'])
        ansDict[key][f"Definition @{targetVersion} <{targetMatch['matchMethod']}>"]=str(targetMatch['match'])
        
        #step4:变更分析,若不兼容则返回需要修复的操作
        repairLst=isCompatible(currentMatch,targetMatch) #repairLst中每个元素都是tuple
        if repairLst==None:
            ansDict[key]['Compatible']="Unknown"
            if len(errLst)>0:
                errorMsg = f"Error occurred, please check the {projName}_fixed_log.txt"
                # print(errorMsg)
                with lock:
                    updateErrorLst(errorLog,errLst)
            continue
        
        if len(repairLst)==0: #若返回修复字典的个数为零，则一定是兼容的
            ansDict[key]['Compatible']='Yes'
        else:
            apiWithValue=addValueForAPI(callAPI,projName,runPath,runCommand,currentEnv,targetEnv,errLst) #apiWithValue为空表示添加参数失败
            fixedAPI,compatibilityLabel,repairStatus=repairTask(root,callAPI,apiWithValue,projName,runPath,runCommand,repairLst,targetEnv,errLst)
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
            # print(errorMsg)
            with lock:
                updateErrorLst(errorLog,errLst)


    #将修改操作更新到代码源文件
    # with open(f"{file.rsplit('/',1)[0]}/new_{fileName}.py",'w') as fw:
    #     repairCode=ast.unparse(root)
    #     fw.write(repairCode+'\n') 
    return ansDict,fileRelativePath,invokedAPINum



## Generate pkl files and perform detection and repair task
## 生成项目调用API的pkl文件以及执行检测与修复任务
#
#  @param projPath The path to the project
#  @param libName  The upgraded Python third-party library name
#  @param currentVersion The upgraded lib's current version
#  @param currentEnv Current version's virtual environment
#  @param targetVersion The upgraded lib's target version
#  @param targetEnv Target version's virtual environment
#  @param runCommand The run command of the project
#  @param runPath The relative path of the run file
def backward(projPath,libName,currentVersion,currentEnv,targetVersion,targetEnv,runCommand,runPath):
    pathObj=Path('DF')
    pathObj.getPath(projPath)
    filePath=[it for it in pathObj.path if it.endswith('py')] #保留项目中的.py文件
    projName=projPath.split('/')[-1]
    projName=projPath.split('/')[-1]
    #先在起始版本中生成每个API的pkl
    # pythonPath=f"{currentEnv}/bin/python"
    # if runPath in runCommand: #针对于python src/run.py这种情况
    #     command=f'cd Copy/{projName};{pythonPath}{runCommand}'
    # else: #针对于python run.py,但执行路径位于scr下,此处的runPath也可能为空
    #     command=f'cd Copy/{projName}/{runPath};{pythonPath}{runCommand}'
    # 1. python 路径自动适配
    if platform.system() == 'Windows':
        currentEnv = currentEnv.replace('/', '\\')
        pythonPath = os.path.join(currentEnv, 'python.exe')
    else:
        pythonPath = os.path.join(currentEnv, 'bin', 'python')
    # 2. 运行命令自动适配
    if platform.system() == 'Windows':
        if runPath in runCommand:
            command = f'cd Copy\\{projName} && {pythonPath} {runCommand}'
        else:
            command = f'cd Copy\\{projName}\\{runPath} && {pythonPath} {runCommand}'
    else:
        if runPath in runCommand:
            command = f'cd Copy/{projName};{pythonPath} {runCommand}'
        else:
            command = f'cd Copy/{projName}/{runPath};{pythonPath} {runCommand}'
    print('Running the project...')
    # createResult=subprocess.run(command,shell=True,executable='/bin/bash',stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    createResult = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if createResult.returncode!=0:
        print(f'Failure to generate PKL in current version')
        print(createResult.stderr)
        return
    print("Running complete")
    #print(createResult.stdout)
     
    #生成pkl成功后，将项目恢复成原样，便于之后对其中某个API单独插桩
    # shutil.move(f'Copy/{projName}','temp')
    shutil.move(os.path.join('Copy', projName), 'temp')
    # shutil.move(f'Copy/bak_{projName}',f'Copy/{projName}')
    shutil.move(os.path.join('Copy', f'bak_{projName}'), os.path.join('Copy', projName))
    # shutil.move('temp',f'Copy/bak_{projName}')
    shutil.move('temp', os.path.join('Copy', f'bak_{projName}'))


    # dir=f"Report/{projName}/{libName}"
    # os.makedirs(dir,exist_ok=True)
    #这里用进程池同时处理多个任务，但对于torch库可能会报错RuntimeError:CUDA out or memory
    #对数据库的读写需要加锁
    coverSet=set()
    # if os.path.exists('Copy/pkl/coverSet'):
    coverSet_path = os.path.join('Copy', 'pkl', 'coverSet')
    if os.path.exists(coverSet_path):
        # with open('Copy/pkl/coverSet','r') as fr:
        with open(coverSet_path, 'r', encoding='utf-8') as fr:
            tempLst=fr.readlines()
        for it in tempLst:
            it=it.rstrip('\n').replace(' ','')
            coverSet.add(it)  
    manager=Manager()
    lock=manager.Lock() #创建一个共享锁
    sharedDict=manager.dict() #创建一个共享字典
    tasks=[(projName,libName,file,currentVersion,currentEnv,targetVersion,targetEnv,runCommand,runPath,lock,sharedDict,coverSet) for file in filePath]
    pool=Pool(processes=1)
    resultLst=pool.map(backwardTask,tasks)
    pool.close() #关闭进程池，使其不再接受新的任务
    pool.join() #等待进程池中所有的任务执行完，否则主进程可能继续往下执行提前结束，而导致部分任务没有执行完
    runCommand=f"python {runCommand}"
    # save2txt(resultLst,libName,runCommand,f"Report/{projName}.txt")
    save2txt(resultLst, libName, runCommand, os.path.join('Report', f'{projName}.txt'))



## Main function of PCART
## PCART主函数
def main():
    if len(sys.argv) < 3:
       print("Usage: python main.py -cfg config.json")
       sys.exit(1)

    config=sys.argv[2]
    start=time.time()

    #加载配置
    projPath,runCommand,runPath,libName,currentVersion,targetVersion,currentEnv,targetEnv=loadConfig(f'Configure/{config}')
    print("Code preprocessing...")

    #首先对代码进行预处理
    codeProcess(projPath,runCommand,runPath,libName) 
    print("Code preprocess complete")

    #执行主逻辑 
    backward(projPath,libName,currentVersion,currentEnv,targetVersion,targetEnv,runCommand,runPath)

    end=time.time()
    print(f"Total run time={int(end-start)}s")


if __name__=='__main__':
    main()
