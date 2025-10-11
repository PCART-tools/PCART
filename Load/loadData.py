## @package loadData
#  Provide utility functions for loading and processing lib APIs 
#
#  More details (TODO) 

import re
import json
import time
from Path.getPath import Path
from API.LibApi import *
from Tool.tool import cmp


## Load the extracted definitions of lib APIs for static signature mapping
## 把之前抽取出来的库API加载到字典中，在项目API与库API匹配的时候需要用到
#  @param libName The upgraded lib name
#  @version version The lib's version
#  @return tempLst The APIs' definitions
#  @return assignDict The assign dict stores the alias of APIs
#  @return libAPIins The built-in APIs' definitions 
def loadLib(libName,version):
    # f=open(f'LibAPIExtraction/{libName}/{libName}{version}','r')
    f = open(f'LibAPIExtraction/{libName}/{libName}{version}', 'r', encoding='utf-8')
    lst=f.readlines()
    f.close()
    libAPIs=[] #既包含了非内置也包含了内置
    libAPIIns=[] #记录内置的API
    assignDict={}
    pyiFlag=0
    for item in lst:
        if item[0]!='\n' and item[0]!='-':
            item=item.replace(' ','').replace('\n','') #去掉空格和结尾的换行符
            if item[0]=='A':
                item=item.replace('\n','')
                pos=item.find(':')
                s=item[pos+1:]
                temp=s.split('->')
                assignDict[temp[0]]=temp[1]
            else:
                libAPIs.append(item)
        
        if '.pyi' in item:
            pyiFlag=1
            continue

        if pyiFlag==1:
            if item[0]!='\n' and item[0]!='A':
                item=item.replace('\n','')
                libAPIIns.append(item)
            elif item[0]=='\n':
                pyiFlag=0

    #再单独对Asssign字典进行处理
    #a1:r1，a2:a1防止值也是别名,最后a2:r1
    for k,v in assignDict.items():
        #判断值是否也可能是别名,即key
        if v in assignDict: #若值也是个别名
            assignDict[k]=assignDict[v] 
    
    tempLst=list(set(libAPIs))
    tempLst.sort(key=libAPIs.index) #去重之后保持原来的顺序
    return tempLst,assignDict,libAPIIns



def func(libApiObjLst,libApiName):
    lst=[]
    for it in libApiObjLst:
        if it.name==libApiName:
            lst.append(it.full_item)
    return lst


## 这个应该和loadlib合并到一起
def getAPILst(filePath):
    # pattern_v='.*?Torch(.*).txt'
    pattern_v='\d+\.(?:\d+\.)*\d+'
    obj_v=re.compile(pattern_v)
    version=obj_v.findall(filePath)[0]
    # f=open(filePath,'r')
    f = open(filePath, 'r', encoding='utf-8')
    apiLst=f.readlines()
    ans=[]
    for it in apiLst:
        if it[0]!='A' and it[0]!='-' and it[0]!='\n':
            it=it.replace(' ','').replace('\n','') #去掉空格和换行
            ans.append(it)
            
    #这一步要对ans进行去重，因为在提取库API的时候，分别从.py和.pyi文件中提取
    #所以肯定会包含重复的部分
    tempLst=list(set(ans))
    tempLst.sort(key=ans.index)
    return version,tempLst




## 遍历所有版本的库API，将其整理成一个json格式的文件
## {APIName: {'1.1.0': [LibAPI1,LibAPI2,...]}, {...}, {...}}
def lib2json(sourceFilePath,saveFilePath):
    pathObj=Path('F') #只获取当前目录下的一级子文件
    pathObj.getPath(sourceFilePath)
    path=pathObj.path
    #dic的value是一个列表，列表中的每个元素都是一个字典
    # libAPI1与libAPI2之间是重载的关系
    dic={}      #{libAPI: [ {'1.1.0': [libAPI1,LibAPI2,...]}, {'1.2.0': [libAPI1,libAPI2,...] },{'1.3.0': [...] }]}
    for item in path: #每个item对应一个版本的库所在的路径
        version,apiLst=getAPILst(item)
        apiObj=APIOBJ()
        apiObj.toAPIObj(version,apiLst) #把字符串API转化为API对象
        for it in apiObj.objLst:
            if it.name not in dic:
                dic[it.name]=[]
            #首先在当前版本中找出所有和it.name同名的API，构造一个字典元素，即{version:[libAPI1,libAPI2,...]}
            #此处的list可能为空，即API在当前的版本中找不到，说明在该版本中被删除了
            lst=func(apiObj.objLst,it.name) #lst中的元素是API字符串
            subDic={}  # {'1.1.0': [LibAPI1,LibAPI2,...]}
            subDic[version]=lst
            if subDic not in dic[it.name]: #防止同名的API反复加入字典
                dic[it.name].append(subDic)
    
    #再对dic中的列表元素，按版本号从小到大进行排序
    for value in dic.values():
        value.sort(key=lambda it:cmp([v for v in it.keys()][0])) #it就是value中的每个元素,即字典

    #再把dic字典保存为json格式的文件
    # fw=open(saveFilePath,'w')
    fw = open(saveFilePath, 'w', encoding='utf-8')
    json.dump(dic,fw,indent=4,ensure_ascii=False)
    fw.close()
    print(f"API total number={len(dic)}")
    #再判断是否有超过两个以上的API
    for api,subLst in dic.items():
        for subDict in subLst:
            breakFlag=0
            for version,ssubLst in subDict.items():
                if len(ssubLst)>1:
                    print(f"Multiple over loads:{api} at {version}")
                    breakFlag=1
                    break
            if breakFlag==1:
                break

    
