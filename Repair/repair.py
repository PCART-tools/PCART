import os
import ast
import subprocess
from Tool.tool import getAst,getFileName,get_parameter,getLastAPIParameter
from Change.API import Parameter
from Change.changeAnalyze import para2Obj

    
def mapPos(pos,dic):
    for key in dic:
        try:
            if key[1]==pos:
                return dic[key]
        except:
            print(f"mapPos error, repairDict:{dic}")
    return {}


def mapName(name,dic):
    for key in dic:
        if key[0]==name:
            return dic[key]
    return {}


def findName(pos,dic):
    for key in dic.keys():
        if key[1]==pos:
            return key[0] #返回参数名
    print(f"findName error:{pos}")
    return ''


                



#给修复后API的参数填上参数名
def mirrorAPI(fixedAPI,dic):
    paraStr=getLastAPIParameter(fixedAPI)
    paraObjLst=[] #保存参数对象
    paraStr=paraStr.replace(' ','') #去空格
    if paraStr:
        lst=get_parameter(paraStr,space=0)
    else:
        lst=[]
    for i in range(len(lst)):
        para=lst[i]
        nameFlag=0
        parameter=Parameter()
        parameter.position=i #修复后参数的真实位置
        if '=' in para:
            pos=para.find('=')
            if '(' not in para[0:pos] and "'" not in para[0:pos] and '"' not in para[0:pos]: #等号前面也不能出现引号，比如f('x=2',y=1)
                nameFlag=1
                parameter.name=para[0:pos]
            else:
                nameFlag=0
        else:
            nameFlag=0
        
        if not nameFlag: #到修复字典中找到修复后的参数名
            flag=0
            for k,subDict in dic.items():
                if 'posChange' in subDict:
                    if subDict['posChange']==parameter.position: #(a,b)-->(b,a)
                        parameter.name=k[0]
                        flag=1
                        break
            if flag==0:
                for k,subDict in dic.items():
                    if parameter.position==k[1]:
                        if 'rename' in subDict:
                            parameter.name=subDict['rename']
                        elif 'replace' in subDict:
                            pos=subDict['replace'].find('=')
                            parameter.name=subDict['replace'][0:pos]
                        else:
                            parameter.name=k[0]


        if nameFlag:
            paraObjLst.append((parameter,1)) #1表示使用时带了参数名
        else:
            paraObjLst.append((parameter,0)) #1表示使用时没有带参数名
    return paraObjLst



def fix(callAPI,repairDict,node,starFlag,twoStarFlag):
    for n in ast.iter_child_nodes(node):
        fix(callAPI,repairDict,n,starFlag,twoStarFlag)

    if isinstance(node,ast.Call):
        #因为ast在对代码还原时会自动把原本的双引号解析为单引号，所以这里修正一下
        callState=ast.unparse(node).replace(' ','').replace('"','').replace("'",'') #确保函数名和参数都要一致
        if callState==callAPI.replace(' ','').replace('"','').replace("'",''):
            posLst=node.args
            keyLst=node.keywords
            newPosLst=[]
            newKeyLst=[]
            index=0
            insertParas=[] #记录待插入的参数，（insertPos, para）
            #step1: 先对位置参数进行处理
            for para in posLst:
                opDict=mapPos(index,repairDict)
                for op,v in opDict.items():
                    s=ast.unparse(para)
                    if op=='delete':
                        if starFlag:
                            if len(opDict)==1:
                                insertParas.append((index,-1,para))
                                break
                    
                    if op=='typeChange': #若有类型变化的话就无法修复
                        if len(opDict)==1: #typeChange的同时，可能还有其它变更，避免参数重复加入
                            insertParas.append((index,-1,para))
                            break
                    
                    if op=='rename': #当位置参数不带名字使用发生了rename,则无需改动
                        insertParas.append((index,-1,para))
                        break
                    
                    if op=='pos2key':
                        paraNode = ast.keyword(arg=v,value=ast.Name(id=s))
                        newKeyLst.append(paraNode)
                        break
                    
                    if op=='replace':
                        insertParas.append((index,-1,ast.Name(id=v.split('=')[-1])))

                    if op=='posChange':
                        insertParas.append((v,index,para))
                
                if len(opDict)==0:
                    insertParas.append((index,-1,para))
                index+=1
            
            #最后还要判断是否有新增的位置参数,新增的位置参数也需要具体的值,新增带默认值的位置参数可以不填
            # for key,value in repairDict.items():
            #     if 'addPos' in value:
            #         insertParas.append((key[1],ast.Name(id=value['addPos'].split('=')[-1])))
            insertParas.sort(key=lambda it:it[0]) #按照插入的位置进行从小到大排序
            for pos,moveFlag,para in insertParas:
                if pos<=len(newPosLst):
                    newPosLst.insert(pos,para)
                else:
                    if moveFlag==-1:
                        paraName=findName(pos,repairDict) #即使一个参数移到了其它位置，也要用它原本位置的名字
                    else:
                        paraName=findName(moveFlag,repairDict)
                    s=ast.unparse(para)
                    if paraName:
                        paraNode=ast.keyword(arg=paraName,value=ast.Name(id=s))
                        newKeyLst.append(paraNode)

            #保留API调用中存在的单独self或者cls参数
            try:
                if 'self' == posLst[0].id or 'cls' == posLst[0].id:
                    newPosLst.insert(0,posLst[0])
            except Exception as e:
                pass
            node.args=newPosLst
             
            #再对带参数名使用的参数进行处理(位置参数或关键字参数)
            for para in keyLst:
                k=para.arg
                opDict=mapName(k,repairDict)
                for op,v in opDict.items():
                    if op=='delete':
                        if twoStarFlag:
                            if len(opDict)==1:
                                newKeyLst.append(para)
                                break
                    
                    if op=='typeChange':
                        if len(opDict)==1:#typeChange的同时，还可能有其他变更(posChange)，避免重复加入
                            newKeyLst.append(para)
                            break
                    
                    if op=='posChange': #若带参数名使用的参数位置发生改变，则无需修改，直接添加到newKeyLst中即可
                        newKeyLst.append(para)
                    
                    # if op=='replace':
                    #     paraName=v.split('=',1)[0]
                    #     if '=' in v:
                    #         paraNode=ast.keyword(arg=paraName,value=ast.Name(id=v.split('=',1)[-1]))
                    #     else:
                    #         paraVal=ast.unparse(para).split('=',1)[-1]
                    #         paraNode=ast.keyword(arg=paraName,value=ast.Name(id=paraVal))
                    #     newKeyLst.append(paraNode)
                    
                    if op=='rename':
                        if not twoStarFlag:
                            para.arg=v #para.arg存放的就是参数名
                        newKeyLst.append(para)
                    
                    
                    if op=='pos2key' or op=='key2pos':
                        newKeyLst.append(para)


                if len(opDict)==0:
                    newKeyLst.append(para)
            
            #最后再判断新增关键字,但新增的关键字参数一般不会导致兼容性问题，所以暂不添加
            # for key,value in repairDict.items():
            #     if 'addKey' in value:
                    # newKeyLst.append(ast.keyword(arg=k,value=ast.Name(id=val)))
            node.keywords=newKeyLst #更新修改后的关键字参数




#修复完后动态验证
def validateByRun(callAPI,apiWithValue,projName,virtualEnv,runPath,runCommand):
    if apiWithValue=='':
        return None
    pklName=getFileName(callAPI,'.pkl')
    if os.path.exists(f"Copy/pkl/new_{pklName}"): #优先加载新版本的PKL
        pklPath=f"../../Copy/pkl/new_{pklName}"
    elif os.path.exists(f'Copy/pkl/{pklName}'):
        pklPath=f"../../Copy/pkl/{pklName}"
    else:
        return None

    #当runPath不在runCommand中时，需要切换到运行文件所在的目录执行命令
    #而文件操作的相对路径就是相对于命令执行的路径
    if runPath!='' and runPath not in runCommand:
        l=len(runPath.split('/'))
        while l>0:
            pklPath='../'+pklPath
            l-=1
    pythonPath=f"{virtualEnv}/bin/python"
    apiWithValue=apiWithValue.replace('"','\\"')
    pklPath=pklPath.replace('"','\\"')

    if runPath!='':
        if runPath not in runCommand:#需要切换到运行文件所在的目录执行命令
            command=f'cd Dynamic/{projName}/{runPath};{pythonPath} verifySingle.py "{pklPath}" "{apiWithValue}"'
        else:
            command=f'cd Dynamic/{projName};{pythonPath} {runPath}/verifySingle.py "{pklPath}" "{apiWithValue}"'
    else: #大部分属于这种情况
        command=f'cd Dynamic/{projName};{pythonPath} verifySingle.py "{pklPath}" "{apiWithValue}"'
    
    result=subprocess.run(command,shell=True,executable='/bin/bash',stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    return result





def validateByStr(fixedAPI,repairDict,targetAPIDefinition,starFlag,twoStarFlag):
    paraObjLst=mirrorAPI(fixedAPI,repairDict)
    posLst,keyLst=para2Obj(targetAPIDefinition)
    targetPara=posLst+keyLst
    
    for para,nameFlag in paraObjLst:
        compatible=0 #假设每个参数都不兼容
        for it in targetPara:
            if nameFlag: #带参数名使用的,要求修复完之后能在目标版本的参数定义中找到相同名字的参数
                if para.name==it.name:
                    compatible=1 
                    break
            else: #不带参数使用的要求修复完之后，位置和参数名都要能找到对应的
                if para.position==it.position and para.name==it.name:
                    compatible=1
                    break
        
        
        if not compatible:
            if nameFlag and not twoStarFlag:
                return False
            if not nameFlag and not starFlag:
                return False

    return True


#需要判断一下apiWithValue是否为空
#修复成功=形式上修复成功+成功运行
#是否兼容
#问题是修完之后，无法通过返回值来判断，到底是动态修复成功了还是只经过了静态验证,再返回一个标签？
#函数返回3个值：修复结果，形式上的兼容性，是否修复成功
def repairTask(root,callAPI,apiWithValue,projName,runPath,runCommand,repairLst,virtualEnv,errLst):
    #静态修复,pkl加载失败，只能进入静态修复
    repairCandidates=[]
    if apiWithValue=='':
        for repairDict,targetPara in repairLst:
            starFlag=0 #判断目标版本的参数定义中是否含有*args
            twoStarFlag=0 #判断目标版本的参数定义中是否含有*kwargs
            if '*args' in targetPara:
                starFlag=1
            if '**' in targetPara:
                twoStarFlag=1
            apiRoot=getAst(callAPI,1)
            fix(callAPI,repairDict,apiRoot,starFlag,twoStarFlag)
            fixedAPI=ast.unparse(apiRoot)
            if validateByStr(fixedAPI,repairDict,targetPara,starFlag,twoStarFlag):
                if fixedAPI not in repairCandidates:
                    repairCandidates.append(fixedAPI)
        
        # repairCandidates=list(set(repairCandidates))
        if len(repairCandidates)==0:
            return str(repairCandidates), 'Unknown', 'Unknown'
        elif len(repairCandidates)==1:
            fixedAPI=repairCandidates[0]
            if callAPI.replace(' ','').replace('"','').replace("'",'')==fixedAPI.replace(' ','').replace('"','').replace("'",''):
                return repairCandidates[0],"Compatible","Unknown"
            else:
                return repairCandidates[0],"Incompatible","Unknown"
        else:
            return str(repairCandidates),"Unknown", "Unknown"

    #pkl加载成功，但匹配的结果也可能是多个，内置API只能静态匹配
    failedLst=[]
    for repairDict,targetPara in repairLst:
        starFlag=0 #判断目标版本的参数定义中是否含有*args
        twoStarFlag=0 #判断目标版本的参数定义中是否含有*kwargs
        # 1.先进行静态验证
        if '*args' in targetPara:
            starFlag=1
        if '**' in targetPara:
            twoStarFlag=1
        apiRoot=getAst(callAPI,1)
        fix(callAPI,repairDict,apiRoot,starFlag,twoStarFlag)
        fixedAPI=ast.unparse(apiRoot)
        if not validateByStr(fixedAPI,repairDict,targetPara,starFlag,twoStarFlag):
            continue
        elif len(repairLst)==1:
            repairCandidates.append(fixedAPI)

        #2. 动态验证
        fixFlag='Failed'
        apiRoot=getAst(apiWithValue,1)
        fix(apiWithValue,repairDict,apiRoot,starFlag,twoStarFlag)
        apiWithValueFixed=ast.unparse(apiRoot)
        #1先通过动态运行,判断其是否修复成功
        result=validateByRun(callAPI,apiWithValueFixed,projName,virtualEnv,runPath,runCommand)
        if result==None:
            if fixedAPI not in repairCandidates:
                repairCandidates.append(fixedAPI)
            fixFlag='Unknown'
        elif result.returncode!=0:
            errLst.append(f"{callAPI}, validate error: {result.stderr}\n")
            failedLst.append(f"{callAPI}, validate error: {result.stderr}\n")
            if 'dill' in result.stderr:
                fixFlag='Unknown'
                if fixedAPI not in repairCandidates:
                    repairCandidates.append(fixedAPI)
            elif validateByStr(fixedAPI,repairDict,targetPara,starFlag,twoStarFlag):
                fixFlag='Unknown'
                if fixedAPI not in repairCandidates:
                    repairCandidates.append(fixedAPI)

        else:
            fixFlag='Successful'
            if fixedAPI not in repairCandidates:
                repairCandidates.append(fixedAPI)
            break
    
    # repairCandidates=list(set(repairCandidates)) 
    if len(repairCandidates)==0:
        return str(repairCandidates), 'Unknown' , 'Unknown'
    elif len(repairCandidates)==1:
        fixedAPI=repairCandidates[0]
        if callAPI.replace(' ','').replace('"','').replace("'",'')==fixedAPI.replace(' ','').replace('"','').replace("'",''):
            return repairCandidates[0],'Compatible',fixFlag
        else:
            return repairCandidates[0],'Incompatible',fixFlag
    else:
        return str(repairCandidates),'Unknown','Unknown'

        
# def repairTask(root,callAPI,apiWithValue,projName,runPath,runCommand,repairLst,virtualEnv,errLst):
#     #静态修复,pkl加载失败，只能进入静态修复
#     repairCandidates=[]
#     if apiWithValue=='':
#         for repairDict,targetPara in repairLst:
#             starFlag=0 #判断目标版本的参数定义中是否含有*args
#             twoStarFlag=0 #判断目标版本的参数定义中是否含有*kwargs
#             if '*args' in targetPara:
#                 starFlag=1
#             if '**' in targetPara:
#                 twoStarFlag=1
#             apiRoot=getAst(callAPI,1)
#             fix(callAPI,repairDict,apiRoot,starFlag,twoStarFlag)
#             fixedAPI=ast.unparse(apiRoot)
#             if validateByStr(fixedAPI,repairDict,targetPara,starFlag,twoStarFlag):
#                 if fixedAPI not in repairCandidates:
#                     repairCandidates.append((fixedAPI,repairDict))
        
#         if len(repairCandidates)==0:
#             return str(repairCandidates), 'Unknown', 'Unknown'
        
#         elif len(repairCandidates)==1:
#             fixedAPI=repairCandidates[0][0]
#             repairDict=repairCandidates[0][1]
#             fix(callAPI,repairDict,root,starFlag,twoStarFlag)
#             if callAPI.replace(' ','').replace('"','').replace("'",'')==fixedAPI.replace(' ','').replace('"','').replace("'",''):
#                 return fixedAPI,"Compatible","Unknown"
#             else:
#                 return fixedAPI,"Incompatible","Unknown"
        
#         else:
#             tempLst=[x[0] for x in repairCandidates]
#             return str(tempLst),"Unknown", "Unknown"


#     #pkl加载成功，但匹配的结果也可能是多个，内置API只能静态匹配
#     failedLst=[]
#     for repairDict,targetPara in repairLst:
#         starFlag=0 #判断目标版本的参数定义中是否含有*args
#         twoStarFlag=0 #判断目标版本的参数定义中是否含有*kwargs
#         # 1.先进行静态验证
#         if '*args' in targetPara:
#             starFlag=1
#         if '**' in targetPara:
#             twoStarFlag=1
#         apiRoot=getAst(callAPI,1)
#         fix(callAPI,repairDict,apiRoot,starFlag,twoStarFlag)
#         fixedAPI=ast.unparse(apiRoot)
#         if not validateByStr(fixedAPI,repairDict,targetPara,starFlag,twoStarFlag):
#             continue
#         elif len(repairLst)==1:
#             repairCandidates.append((fixedAPI,repairDict))

#         #2. 动态验证
#         fixFlag='Failed'
#         apiRoot=getAst(apiWithValue,1)
#         fix(apiWithValue,repairDict,apiRoot,starFlag,twoStarFlag)
#         apiWithValueFixed=ast.unparse(apiRoot)
#         #1先通过动态运行,判断其是否修复成功
#         result=validateByRun(callAPI,apiWithValueFixed,projName,virtualEnv,runPath,runCommand)
#         # print(result.stdout,result.stderr)
#         if result==None:
#             if (fixedAPI,repairDict) not in repairCandidates:
#                 repairCandidates.append((fixedAPI,repairDict))
#             fixFlag='Unknown'
        
#         elif result.returncode!=0:
#             errLst.append(f"{callAPI}, validate error: {result.stderr}\n")
#             failedLst.append(f"{callAPI}, validate error: {result.stderr}\n")
#             if 'dill' in result.stderr:
#                 fixFlag='Unknown'
#                 if (fixedAPI,repairDict) not in repairCandidates:
#                     repairCandidates.append((fixedAPI,repairDict))
#         else:
#             fixFlag='Successful'
#             # for k,v in repairDict.items():
#             #     print(k,v)
#             # print('\n')
#             # print(callAPI)
#             # print(fixedAPI)
#             if (fixedAPI,repairDict) not in repairCandidates:
#                 repairCandidates.append((fixedAPI,repairDict))
#             break
     
#     # repairCandidates=list(set(repairCandidates)) 
#     if len(repairCandidates)==0:
#         return str(repairCandidates), 'Unknown' , 'Unknown'
#     elif len(repairCandidates)==1:
#         fixedAPI=repairCandidates[0][0]
#         repairDict=repairCandidates[0][1]
#         fix(callAPI,repairDict,root,starFlag,twoStarFlag)
#         if callAPI.replace(' ','').replace('"','').replace("'",'')==fixedAPI.replace(' ','').replace('"','').replace("'",''):
#             return fixedAPI,'Compatible',fixFlag
#         else:
#             return fixedAPI,'Incompatible',fixFlag
#     else:
#         tempLst=[x[0] for x in repairCandidates]
#         return str(tempLst),'Unknown','Unknown'
