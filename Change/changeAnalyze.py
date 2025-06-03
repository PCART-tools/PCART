## @package changeAnalyze 
#  Analyze API parameter changes and compatibility 
#
#  More details (TODO)

import os
import re
import copy
import subprocess
from API.LibApi import Parameter 
from Tool.tool import get_parameter,removeParameter,getFileName


class Update():
    def __init__(self):
        self.pos=-1
        self.type=''
        self.rename=''
        self.rep=''
        self.value=''
        self.dele=''
        self.addPos='' #增加位置参数
        self.addKey='' #增加关键字参数
        self.pos2key=''
        self.key2pos=''


    def __repr__(self):
        # s=f"name:{self.name}, "
        s=''
        if self.pos:
            s+=f"posChange:{self.pos}, "
        if self.type:
            s+=f"typeChange:{self.type}, "
        if self.dele:
            s+=f"delte:{self.dele}, "
        if self.add:
            s+=f"add:{self.add}, "
        s=s.rstrip(', ')
        return s 



def updateErrorLst(errorLog,errorLst):
    with open(errorLog,'a') as fw:
        for it in errorLst:
            fw.write(it)
        fw.write('\n')




#查询字典
def querySharedDict(callAPI,sharedDict):
    ansDict={}
    k=removeParameter(callAPI)
    if k in sharedDict:
        ansDict['current']=sharedDict[k]['current']
        ansDict['target']=sharedDict[k]['target']
        return ansDict
    return ansDict


#更新的操作有两种：添加和修改
def updateSharedDict(callAPI,currentDict,targetDict,sharedDict):
    key=removeParameter(callAPI)
    if key not in sharedDict: #没有就添加
        sharedDict[key]={}
        innerDict=sharedDict[key]
        innerDict['current']=currentDict
        innerDict['target']=targetDict
        sharedDict[key]=innerDict #将修改操作更新到共享字典中
    else: #存在则再看是否需要修改
        innerDict=sharedDict[key]
        if sharedDict[key]['current']['matchMethod']=='static' and currentDict['matchMethod']=='dynamic':
            innerDict['current']=currentDict
        if sharedDict[key]['target']['matchMethod']=='static' and targetDict['matchMethod']=='dynamic':
            innerDict['target']=targetDict
        sharedDict[key]=innerDict #将修改操作更新到共享字典中



#判断两个参数的类型是否发生了变更,只要兼容，就认为相同
#Union[int,float],表示类型是int或float
#Optional[int],表示变量的类型是int或值为None,等价于Union[int,None]
#None即可以表示类型也可以表示值
#Optional[Union[int, str]]表示参数的类型为int,str或None
#Union[Callable[[torch.Tensor,str],torch.Tensor],torch.device,str,Dict[str,str],NoneType]=None
def isDifferType(oldType,newType):
    #先从字面值上判断看是否一样
    if oldType==newType:
        return False  
    #若至少存在一个类型注释为空，则认为二者的类型是相同的
    if oldType=="" or newType=="":
        return False
    #若都存在类型注释且注释不同时，才认为二者的类型不同
    else:
        oldLst=[]
        newLst=[]
        oldTypeSet=set() #将类型构造成集合进行比较
        newTypeSet=set()
        if oldType[0]=="'" and oldType[-1]=="'":
            oldType=oldType[1:-1]
        
        if newType[0]=="'" and newType[-1]=="'":
            newType=newType[1:-1]
        
        if 'Union' in oldType:
            pattern='.*?Union\[(.*)\].*?'
            result=re.findall(pattern,oldType)
            oldLst=get_parameter(result[0])
        elif 'Optional' in oldType:
            pattern='.*?Optional\[(.*)\].*?'
            result=re.findall(pattern,oldType)
            oldLst=get_parameter(result[0])
        elif '|' in oldType:
            oldLst=oldType.split('|')
        else: #当oldType就是一个具体的类型而不是集合时，比如int
            oldLst=[oldType]

        for it in oldLst:
            oldTypeSet.add(it.replace(' ',''))
        


        if 'Union' in newType:
            pattern='.*?Union\[(.*)\].*?'
            result=re.findall(pattern,newType)
            newLst=get_parameter(result[0])
        elif 'Optional' in newType:
            pattern='.*?Optional\[(.*)\].*?'
            result=re.findall(pattern,newType)
            newLst=get_parameter(result[0])
        elif '|' in newType:
            newLst=newType.split('|')
        else:
            newLst=[newType]

        for it in newLst:
            newTypeSet.add(it.replace(' ',''))

        # print(oldTypeSet,'-->', newTypeSet)
        #这里oldTypeSet>0是因为避免空集是任意集合的子集的情况
        if len(oldTypeSet)>0 and oldTypeSet.issubset(newTypeSet):
            return False
        else:
            return newType
    






def para2Obj(paraStr):
    paraStr=paraStr.replace(' ','') #去空格
    paraObjLst=[] #保存参数对象
    if '->' in paraStr: #若有有返回值的话去掉返回值
        paraStr=paraStr.split('->')[0]
    if '(' in paraStr[0]:
        paraStr=paraStr[1:-1]
    
    if paraStr:
        lst=get_parameter(paraStr)
    else:
        lst=[]
    if len(lst)>0:
        if 'self' in lst[0]: #self可能也存在类型注释
            lst.remove(lst[0])
        elif 'cls' in lst[0]:
            lst.remove(lst[0])
    for para in lst:
        parameter=Parameter()
        parameter.position=lst.index(para) #当列表中有相同元素时，lst.index会出现问题,但库定义中不会出现相同的参数
        parameter.fullItem=para
        flagMaohao=0
        if ':' in para:
            pos=para.find(':')
            flagMaohao=1 
        
        if flagMaohao and "'" not in para[0:pos] and '"' not in para[0:pos] and '<' not in para[0:pos]: #参数值为字符串时，字符串中也可能出现冒号
            l=para.split(':')
            parameter.name=l[0]
            if '=' in l[1]:
                ll=l[1].split('=')
                parameter.type=ll[0]
                parameter.value=ll[1]
            else:
                parameter.type=l[1]
        elif '=' in para:
            l=para.split('=')
            parameter.name=l[0]
            parameter.value=l[1]
        else:
            parameter.name=para
        paraObjLst.append(parameter)
    
    pos=len(paraObjLst)
    posStar=-1 #记录*的位置
    pos2Star=-1 #记录**的位置, 防止出现(x, y, **kwargs)的形式
    for para in paraObjLst:
        if '**' in para.name:
            pos2Star=para.position
        elif '*' in para.name:
            posStar=para.position
            break
    if posStar!=-1: #优先根据*号拆分
        pos=posStar
    elif pos2Star!=-1:
        pos=pos2Star
    
    posParameters=paraObjLst[0:pos]
    keyParameters=[]
    for para in paraObjLst[pos+1:]:
        if '**' not in para.name:
            keyParameters.append(para)
    
    return posParameters,keyParameters
        



#输入两个api参数部分，判断参数部分有何不同
def findDiffer(oldPara,newPara):
    oldPos,oldKey=para2Obj(oldPara) 
    newPos,newKey=para2Obj(newPara)
    oldPosParaNum=len(oldPos)
    dic={} #保存每个参数应该做哪些修改操作
    #第一轮筛选，先根据名字来找对应关系
    #处理位置参数
    for oldPara in copy.deepcopy(oldPos):
        sameFlag=0
        for newPara in newPos:
            if oldPara.name==newPara.name:
                up=Update()
                if oldPara.position!=newPara.position:
                    up.pos=newPara.position
                ty=isDifferType(oldPara.type,newPara.type)
                if ty: 
                    up.type=ty
                sameFlag=1
                oldPos.remove(oldPara)
                newPos.remove(newPara)
                break
        if sameFlag==1:
            dic[(oldPara.name,oldPara.position)]=up
    
    #处理关键字参数,旧版中没有找到相同名字的参数可能是重命名或删除了
    for oldPara in copy.deepcopy(oldKey):
        sameFlag=0
        for newPara in newKey:
            if oldPara.name==newPara.name:
                up=Update()
                ty=isDifferType(oldPara.type,newPara.type)
                if ty:
                    up.type=ty
                sameFlag=1
                oldKey.remove(oldPara)
                newKey.remove(newPara)
                break
        if sameFlag==1:
            dic[(oldPara.name,oldPara.position)]=up



    #第二轮筛选，根据名字找对应关系，判断是否存在位置参数变到了关键字参数
    for oldPara in copy.deepcopy(oldPos):
        sameFlag=0
        for newPara in newKey:
            if oldPara.name==newPara.name:
                up=Update()
                up.pos2key=oldPara.name #位置参数变成关键字参数
                ty=isDifferType(oldPara.type,newPara.type)
                if ty:
                    up.type=ty
                sameFlag=1
                oldPos.remove(oldPara)
                newKey.remove(newPara)
                break
        if sameFlag==1:
            dic[(oldPara.name,oldPara.position)]=up


    #再判断是否有关键字参数(起始版本)变到了位置参数(目标版本)
    for oldPara in copy.deepcopy(oldKey):
        sameFlag=0
        for newPara in copy.deepcopy(newPos):
            if oldPara.name==newPara.name:
                print(f"key2pos-->{oldPara.name}")
                up=Update()
                up.key2pos=oldPara.name
                ty=isDifferType(oldPara.type, newPara.type)
                if ty:
                    up.type=ty
                sameFlag=1
                oldKey.remove(oldPara)
                newPos.remove(newPara)
                break
        if sameFlag==1:
            dic[(oldPara.name,oldPara.position)]=up



    
    #第三轮筛选，根据对应位置和类型来筛选剩余的位置参数，判断其是否发生了重命名
    for oldPara in copy.deepcopy(oldPos):
        sameFlag=0
        for newPara in newPos:
            if oldPara.position==newPara.position and not isDifferType(oldPara.type,newPara.type): #这里需要加一个类型相同约束吗
                up=Update()
                if oldPara.name!=newPara.name: #参数发生了重命名
                    up.rename=newPara.name
                ty=isDifferType(oldPara.type,newPara.type)
                if ty:
                    up.type=ty
                sameFlag=1
                oldPos.remove(oldPara)
                newPos.remove(newPara)
                break
        if sameFlag==1:
            dic[(oldPara.name,oldPara.position)]=up
        else:#oldPos中剩下的就是删除的
            oldPos.remove(oldPara)
            up=Update()
            up.dele=1
            dic[(oldPara.name,oldPara.position)]=up

    #第四轮筛选，根据类型来判断，剩余的关键字参数是否发生了重命名
    for oldPara in copy.deepcopy(oldKey):
        sameFlag=0
        for newPara in newKey:
            if oldPara.type==newPara.type:
                sameFlag=1
                up=Update()
                up.rename=newPara.name
                oldKey.remove(oldPara)
                newKey.remove(newPara)
                break
        if sameFlag==1:
            dic[(oldPara.name,oldPara.position)]=up
        else:
            oldKey.remove(oldPara)
            up=Update()
            up.dele=1
            dic[(oldPara.name,oldPara.position)]=up
            

    #newPos中剩下的就是替换或新增的
    for para in newPos:
        s=f'{para.name}'
        if para.value:
            s+=f"={para.value}"
        if para.position>=0 and para.position<oldPosParaNum: #如果剩余参数的下标在旧版本参数下标的范围内，则认为是替换操作,反之则认为是新增的
            for key in dic:
                if key[1]==para.position:
                    dic[key].rep=s
                    break
        else:
            up=Update()
            up.addPos=s
            dic[(para.name,para.position)]=up
    
    #newKey中剩下的就是新增的,新增的关键字参数往往都带有默认值，一般不会引起兼容性问题
    for para in newKey:
        s=para.name
        if para.value:
            s+=f"={para.value}"
        up=Update()
        up.addKey=s
        dic[(para.name,para.position)]=up


    #构建修改操作的字典
    updateDict={}
    for key,value in dic.items():
        if key not in updateDict:
            updateDict[key]={}
        if value.dele:
            updateDict[key]['delete']=value.dele
        if value.type:
            updateDict[key]['typeChange']=value.type
        if value.rename:
            updateDict[key]['rename']=value.rename
        if value.pos!=-1:
            updateDict[key]['posChange']=value.pos
        if value.rep:
            updateDict[key]['replace']=value.rep
        if value.pos2key:
            updateDict[key]['pos2key']=value.pos2key
        if value.addPos:
            updateDict[key]['addPos']=value.addPos
        if value.addKey:
            updateDict[key]['addKey']=value.addKey

        if value.key2pos:
            updateDict[key]['key2pos']=value.key2pos
    
    #对字典按照参数的位置进行排序
    ansDict=dict(sorted(updateDict.items(), key=lambda it: it[0][1])) #it[0]代表字典的键，it[0][1]代表键中的第二个元素,即位置
    return ansDict



#判断两个重载API是否兼容
#分位置参数和关键字参数进行分析
#判断标准
#位置参数：位置和名称相同，且类型兼容，认为兼容
#关键字参数：名字相同且类型兼容，认为兼容
def analyzeCompatibility(oldPara,newPara):
    #将其转化为参数对象
    oldPos,oldKey=para2Obj(oldPara)
    newPos,newKey=para2Obj(newPara)
    #分析位置参数
    for oldPara in oldPos:
        flag=0
        for newPara in newPos:
            if oldPara.name==newPara.name and oldPara.position==newPara.position and not isDifferType(oldPara.type,newPara.type):
                flag=1
                break
        if flag==0: #若旧版本的位置参数没有在新版本中找到对应的
            return False
    
    #再分析新增的位置参数
    for newPara in newPos:
        if newPara.position>=len(oldPos):
            if newPara.value=='': #若新增的位置参数不带默认值
                return False

    #分析关键字参数
    for oldPara in oldKey:
        flag=0
        for newPara in newKey:
            if oldPara.name==newPara.name and not isDifferType(oldPara.type,newPara.type):
                flag=1
                break

        #再判断关键字参数是否变成了位置参数(这种改变是兼容的)
        if flag==0:
            for newPara in newPos:
                if oldPara.name==newPara.name and not isDifferType(oldPara.type,newPara.type):
                    flag=1
                    print(f"key2pos-->{oldPara.name}")
                    break

        if flag==0:
            return False
    
    #再分析新增的关键字参数
    #比如(*,x,y) --> (*,x,y,z)，其中z就是新增的
    for newPara in newKey:
        flag=0
        for oldPara in oldKey:
            if newPara.name==oldPara.name: #若找到同名的，则不是新增的
                flag=1
                break
        if flag==0:
            if newPara.value=='': #若新增的关键字参数不带默认值
                return False
    
    return True


#兼容返回空列表，不兼容返回则返回需要修复的字典，可能会有多个
def isCompatible(current,target):
    if len(current['match'])==0 or len(target['match'])==0:
        return None
    # if "*args" in target['match'] or "**kwargs" in target['match'] or "**" in target['match']: #默认此时是兼容的
    #     return []
    #先将数据结构统一化,便于之后的统一操作
    if isinstance(current['match'],str): #只要是str，一定是动态匹配
        currentDict={current['internalPath']:[current['match']]}
    else:
        currentDict=current['match']
    
    if isinstance(target['match'],str):
        targetDict={target['internalPath']:[target['match']]}
    else:
        targetDict=target['match']
    
    tempLst1=[] #保存找到了对应关系的配对的修复字典
    tempLst2=[] #保存未确定对应关系的配对的修复字典
    flag=0
    for currentSameAPI,currentOvLst in currentDict.items():
        for targetSameAPI,targetOvLst in targetDict.items():
            if currentSameAPI==targetSameAPI or (currentSameAPI+'.' in targetSameAPI) or (targetSameAPI+'.' in currentSameAPI) or len(currentDict)==1 and len(targetDict)==1:
                flag=1
                #第一轮遍历，筛选掉两个同名API确定对应关系的重载，这里对应关系的规则是字符串完全一致
                #只要能找到对应关系，就说明是兼容的
                #新版中完全对应的可以删除，但兼容的不能删除，防止它还可以兼容旧版本的其它重载
                for currentOvPara in copy.deepcopy(currentOvLst):
                    for targetOvPara in copy.deepcopy(targetOvLst):
                        if currentOvPara.split('->')[0]==targetOvPara.split('->')[0]:
                            currentOvLst.remove(currentOvPara)
                            targetOvLst.remove(targetOvPara)

                #第二轮遍历
                #只要旧版本的API在新版本中找到一个和它兼容的，那就认为旧版本的API在新版本中是兼容的，无需再进行其它的判断。
                #只有旧版本的API在新版本中都不兼容时，才认为它不兼容，不兼容就要依次尝试修复。
                for currentOvPara in currentOvLst:
                    compatibleFlag=0
                    for targetOvPara in targetOvLst: 
                        if analyzeCompatibility(currentOvPara,targetOvPara):
                            compatibleFlag=1
                            break
                    
                    if compatibleFlag==0: #如果都不兼容，则需要尝试修复
                        for targetOvPara in targetOvLst: #这里
                            repairDict=findDiffer(currentOvPara,targetOvPara)
                            tempLst1.append((repairDict,targetOvPara))
            
            else:
                for currentOvPara in currentOvLst:
                    compatibleFlag=0
                    for targetOvPara in targetOvLst: 
                        if analyzeCompatibility(currentOvPara,targetOvPara):
                            # print(currentSameAPI,currentOvPara)
                            # print(targetSameAPI,targetOvPara)
                            compatibleFlag=1
                            break
                    
                    if compatibleFlag==0: #如果都不兼容，则需要尝试修复
                        for targetOvPara in targetOvLst: #这里
                            repairDict=findDiffer(currentOvPara,targetOvPara)
                            tempLst2.append((repairDict,targetOvPara))

    if flag==1:
        return tempLst1
    else:
        return tempLst2
     

# def addValueForAPI(callAPI,projName,runPath,runCommand,virtualEnv,errLst):
def addValueForAPI(callAPI,projName,runPath,runCommand,currentEnv,targetEnv,errLst):
    pklName=getFileName(callAPI,'.pkl')
    flag=0
    if os.path.exists(f"Copy/pkl/new_{pklName}"):
        flag=1
        pklPath=f"../../Copy/pkl/new_{pklName}"
    elif os.path.exists(f"Copy/pkl/{pklName}"):
        pklPath=f"../../Copy/pkl/{pklName}"
    else:
        return ''
    
    # pklPath=f"../../Copy/pkl/{pklName}"
    #当runPath不在runCommand中时，需要切换到运行文件所在的目录执行命令
    #而文件操作的相对路径就是相对于命令执行的路径
    if runPath!='' and runPath not in runCommand:
        l=len(runPath.split('/'))
        while l>0:
            pklPath='../'+pklPath
            l-=1
    
    # pythonPath=f"{virtualEnv}/bin/python"
    if flag==0:
        pythonPath=f"{currentEnv}/bin/python"
    else:
        pythonPath=f"{targetEnv}/bin/python"
    
    pklStr=pklPath.replace('"','\\"')
    callStr=callAPI.replace('"','\\"')
    
    # if not os.path.exists(f"Copy/pkl/{pklName}"):
    #     return ''

    if runPath!='':
        if runPath not in runCommand:#需要切换到运行文件所在的目录执行命令
            command=f'cd Dynamic/{projName}/{runPath};{pythonPath} addValueForAPI.py  "{pklStr}" "{callStr}"'
        else:
            command=f'cd Dynamic/{projName};{pythonPath} {runPath}/addValueForAPI.py  "{pklStr}" "{callStr}"'
    else: #大部分属于这种情况
        command=f'cd Dynamic/{projName};{pythonPath} addValueForAPI.py  "{pklStr}" "{callStr}"'

    matchResult=subprocess.run(command,shell=True,executable='/bin/bash',stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    # print(command)
    # print(':',matchResult.stdout)
    if matchResult.returncode!=0:
        errLst.append(f"{callAPI}, addValueError: {matchResult.stderr}\n")
        return ''

    output=matchResult.stdout
    pattern="##(.*)##"
    obj=re.compile(pattern,re.DOTALL)
    lst=obj.findall(output)
    if len(lst)==1:
        return lst[0]
        
    return ''
