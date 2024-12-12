import os
import sys
import ast
import json
import time
import shutil
import subprocess
from Path.getPath import *
from Map.map import mapAPI
from multiprocessing import Pool
from multiprocessing import Manager
from Extract.getCall import getCallFunction
from Preprocess.preprocess import codeProcess
from Repair.repair import repairTask,validateByRun
from Tool.tool import getAst,save2txt,loadConfig,removeParameter,getFileName
from Change.changeAnalyze import isCompatible,addValueForAPI,updateSharedDict,querySharedDict,updateErrorLst


#一个进程处理一个文件
def backwardTask(args):
    ansDict={} #保存每个文件处理的情况
    projName,libName,file,currentVersion,currentEnv,targetVersion,targetEnv,runCommand,runPath,lock,sharedDict,coverSet=args
    fileName=file.split('/')[-1][0:-3]
    
    #step1:先把当前文件中指定的第三方库的API抽取出来
    callAPIDict,_=getCallFunction(file,libName) #key是还原前的API，value是还原后的API
    with open(f'data/{fileName}_callAPIDict.json','w') as fw:
        json.dump(callAPIDict,fw,indent=4,ensure_ascii=False) 
    try: 
        root=getAst(file) #获取当前文件的AST，便于修复使用
    except:
        pass
    #将源代码文件映射到Copy目录中
    tempLst=file.split('/')
    pos=tempLst.index(projName)
    realProjPath='/'.join(tempLst[0:pos+1])
    fileRelativePath='/'.join(tempLst[pos:])
    copyFile='./Copy/'+fileRelativePath
    invokedAPINum=len(callAPIDict)
    errorLog=f"Report/{projName}_fixed_log.txt"
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
                print('Error occurred, please check the fixedErrorLog.txt')
                with lock:
                    updateErrorLst(errorLog,errLst)
            continue
        
        if len(repairLst)==0: #若返回修复字典的个数为零，则一定是兼容的
            ansDict[key]['Compatible']='Yes'
        else:
            apiWithValue=addValueForAPI(callAPI,projName,runPath,runCommand,currentEnv,targetEnv,errLst) #apiWithValue为空表示添加参数失败
            fixedAPI,label,exec=repairTask(root,callAPI,apiWithValue,projName,runPath,runCommand,repairLst,targetEnv,errLst)
            if label=='Compatible':
                ansDict[key]['Compatible']='Yes'
            else:
                if label=='Incompatible':
                    ansDict[key]['Compatible']='No'
                else:
                    ansDict[key]['Compatible']='Unknown'

                if exec=='Successful':
                    ansDict[key]['Repair <Successful>']=f"{fixedAPI}"
                elif exec=='Failed':
                    ansDict[key]['Repair <Failed>']=f"{fixedAPI}"
                else:
                    ansDict[key]['Repair <Unknown>']=f"{fixedAPI}"


        if len(errLst)>0:
            errorMsg = f"Error occurred, please check the {projName}_fixed_log.txt"
            print(errorMsg)
            with lock:
                updateErrorLst(errorLog,errLst)


    #将修改操作更新到代码源文件
    # with open(f"{file.rsplit('/',1)[0]}/new_{fileName}.py",'w') as fw:
    #     repairCode=ast.unparse(root)
    #     fw.write(repairCode+'\n') 
    
    return ansDict,fileRelativePath,invokedAPINum




def backward(projPath,libName,currentVersion,currentEnv,targetVersion,targetEnv,runCommand,runPath):
    pathObj=Path('DF')
    pathObj.getPath(projPath)
    filePath=[it for it in pathObj.path if it.endswith('py')] #保留项目中的.py文件
    projName=projPath.split('/')[-1]
    projName=projPath.split('/')[-1]
    #先在起始版本中生成每个API的pkl
    pythonPath=f"{currentEnv}/bin/python" 
    if runPath in runCommand: #针对于python src/run.py这种情况
        command=f'cd Copy/{projName};{pythonPath}{runCommand}'
    else: #针对于python run.py,但执行路径位于scr下,此处的runPath也可能为空
        command=f'cd Copy/{projName}/{runPath};{pythonPath}{runCommand}'
    print('Running the project...')
    createResult=subprocess.run(command,shell=True,executable='/bin/bash',stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    if createResult.returncode!=0:
        print(f'Failure to generate PKL in current version')
        print(createResult.stderr)
        return
    print("Running complete")
    #print(createResult.stdout)
     
    #生成pkl成功后，将项目恢复成原样，便于之后对其中某个API单独插桩
    shutil.move(f'Copy/{projName}','temp')
    shutil.move(f'Copy/bak_{projName}',f'Copy/{projName}')
    shutil.move('temp',f'Copy/bak_{projName}')


    # dir=f"Report/{projName}/{libName}"
    # os.makedirs(dir,exist_ok=True)
    #这里用进程池同时处理多个任务，但对于torch库可能会报错RuntimeError:CUDA out or memory
    #对数据库的读写需要加锁
    coverSet=set()
    if os.path.exists('Copy/pkl/coverSet'):
        with open('Copy/pkl/coverSet','r') as fr:
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
    save2txt(resultLst,libName,runCommand,f"Report/{projName}.txt")





if __name__=='__main__':
    # python main.py -cfg config.json
    config=sys.argv[2]
    start=time.time()
    projPath,runCommand,runPath,libName,currentVersion,targetVersion,currentEnv,targetEnv=loadConfig(f'Configure/{config}')
    print("Code preprocessing...")
    codeProcess(projPath,runCommand,runPath,libName) #首先对代码进行预处理
    print("Code preprocess complete")
    backward(projPath,libName,currentVersion,currentEnv,targetVersion,targetEnv,runCommand,runPath)
    end=time.time()
    print(f"Total run time={int(end-start)}s")
