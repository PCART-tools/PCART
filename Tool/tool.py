## @package tool
#  Provides utility functions for processing API calls and source files
#
#  More details (TODO)  

import re
import os
import ast
import json
import hashlib
from Path.getPath import Path

#将参数字符串拆分成单个的参数
#apiName(x,y="<bold>Hello, World!</bold>",z:int,w=(p1,p2={1,(1m,23)}),device: Union[Device, int] = None, abbreviated: bool ={'a','b'}) -> str
#默认按逗号进行拆分,也可按'.'进行拆分，比如a.b.c
#拆分参数的时候没有考虑到x="hello,wolrd"带冒号的情况，会错误拆成两个
def get_parameter(p_string,separator=',',space=1):
    #库定义的参数去空格，项目中的参数不去空格，防止出问题
    if space: #默认是去空格的
        p_string=p_string.replace(' ','') #去掉参数中的空格
    
    if p_string=='':
        return []
    
    parameters=[]
    stack=[]
    count_left_min=0 #统计'('的个数
    count_right_min=0 #统计')'的个数

    count_left_middle=0 #统计'['的个数
    count_right_middle=0 #统计']'的个数

    count_left_hua=0 #统计'{'的个数
    count_right_hua=0 #统计'}'的个数

    count_single_yinhao=0 #统计单引号的引号的个数
    count_double_yinhao=0 #统计双引号的引号的个数

    for index,value in enumerate(p_string):
        stack.append(value)
        if (value=="'" or count_single_yinhao) and not count_double_yinhao: #若上一步出现了双引号，则说明此处的单引号是在双引号内的，所以不计算单引号的个数
            if value=="'":
                count_single_yinhao+=1
            if count_single_yinhao&1:
                continue
        
        elif (value=='"' or count_double_yinhao) and not count_single_yinhao: #若上一步出现了单引号，则说明此处的双引号是在单引号内的，所以不计算双引号的个数
            if value=='"':
                count_double_yinhao+=1
            if count_double_yinhao&1:
                continue
        
        count_single_yinhao=0 #重置为0
        count_double_yinhao=0

        #只计算引号之外的括号是否成对出现 
        if value=='(':
            count_left_min+=1
        elif value==')':
            count_right_min+=1
        
        elif value=='[':
            count_left_middle+=1
        elif value==']':
            count_right_middle+=1

        elif value=='{':
            count_left_hua+=1
        elif value=='}':
            count_right_hua+=1
        
    
        #弹栈,遇到分隔符或达到字符串末尾
        if value==separator:
            flagMin=1 #假设左右括号的个数都是相等的
            flagMid=1
            flagHua=1
            if '(' in stack:
                if count_left_min!=count_right_min:
                    flagMin=0
            if '[' in stack:
                if count_left_middle!=count_right_middle:
                    flagMid=0
            if '{' in stack:
                if count_left_hua!=count_right_hua:
                    flagHua=0

            if flagMin and flagMid and flagHua:
                parameters.append(''.join(stack[0:-1]))
                stack.clear()
    
        elif index==len(p_string)-1:
            parameters.append(''.join(stack))


    return parameters


#将代码转化为Ast树
def getAst(filePath,strFlag=0): #若strFlag=1,则表明传进来的是一个api，而不是一个路径
    if strFlag==0:
        with open(filePath,'r') as f:
            s=f.read()
        root=ast.parse(s,filename='<unknown>',mode='exec')
        return root
    root=ast.parse(filePath,filename='<unknown>',mode='exec')
    return root



def getImportLst(filePath):
    #把当前文件中和torch相关的import语句以及调用语句筛选出来,之后写入runTask.py文件中 
    importLst=[]            
    with open(filePath,'r',encoding='UTF-8') as f:
        lstR=f.readlines()
    for it in lstR:
        #这个判断条件在后续应该将其设置为通用的，不同的库判断条件不同
        if (it[0:6]=='import' or it[0:4]=='from') and 'torch' in it and 'torchvision' not in it and 'torch_' not in it and '.torch' not in it:
            importLst.append(it)
    return importLst



#去掉API中的参数部分
#比如a.b(x,y(2)).c(z=1).d(w=[(1,2)])变成a.b.c.d
def removeParameter(s,flag=0): 
    if '->' in s: #若有返回值，则把返回值也去掉
        s=s.split('->')[0] 
    if flag==0:   #去掉API中所有参数
        stack=[]
        left=0
        right=0
        ans=''
        for index,value in enumerate(s):
            #进栈
            stack.append(value)
            if value=='(':
                left+=1
            if value==')':
                right+=1
            #出栈
            if left==right and left>0 and right>0:
                pos=stack.index('(')
                ans+=''.join(stack[0:pos])
                stack.clear()
                left=0
                right=0
            elif index==len(s)-1:
              ans+=''.join(stack)
    else:  #只去除最后一个API的参数
        i=len(s)-1
        left=0  #记录左括号的个数
        right=0
        pos=len(s)
        while i>=0:
            if s[i]==')':
                right+=1
            if s[i]=='(':
                left+=1
            if left==right and left>0 and right>0:
                pos=i #更新pos
                break
            i-=1
        ans=s[0:pos]

    return ans




#获取最后一个API参数
#a(x).b(x=c.d(1),y=b((1,2),5),w).c(1,2,3,4)
#获取c的参数1,2,3,4
def getLastAPIParameter(apiStr):
    ans=''
    left=0 #记录左括号的个数
    right=0 #记录右括号的个数
    pos=len(apiStr)
    i=len(apiStr)-1
    while i>=0:
        if apiStr[i]==')':
            right+=1
        if apiStr[i]=='(':
            left+=1
        if left==right and left>0 and right>0:
            pos=i
            break
        i-=1
    if pos!=len(apiStr):
        ans=apiStr[pos+1:-1]
    return ans  




#拆分API，比如a.b(x).c(y).d(z)
#拆成3个API，分别是a.b(x),a.b(x).c(y), a.b(x).c(y).d(z)
#还有特殊的调用形式a.b['x'](y)
def departAPI(s):
    ansLst=[]
    stack=''
    leftMin=0 #记录左'('的个数
    rightMin=0
    leftMid=0
    rightMid=0
    for i in range(len(s)):
        stack+=s[i]
        if s[i]=='(':
            leftMin+=1
        if s[i]==')':
            rightMin+=1
        if s[i]=='[':
            leftMid+=1
        if s[i]==']':
            rightMid+=1
        
        flagMid=1
        if '[' in stack:
            if leftMid!=rightMid:
                flagMid=0
        
        #拆分函数字符串里面必须要出现() 
        if  leftMin and rightMin and leftMin==rightMin and flagMid:
            ansLst.append(stack[0:i+1])
            leftMin=0
            rightMin=0
            if leftMid and rightMid:
                leftMin=0
                rightMid=0
        
        elif i==len(s)-1:
            ansLst.append(stack[0:i+1])

    return ansLst


def departAPI2(s,separator='.'):
    ansLst=[]
    lst=[]
    count_left_min=0 #统计左'('的个数
    count_right_min=0 #统计右')'的个数

    count_left_middle=0 #统计左'['的个数
    count_right_middle=0 #统计左']'的个数
    for index,value in enumerate(s):
        #入栈，分两种情况
        if value!=separator:
            lst.append(value)
            if value=='(':
                count_left_min+=1
            if value==')':
                count_right_min+=1
            if value=='[':
                count_left_middle+=1
            if value==']':
                count_right_middle+=1
        
        elif value==separator and ((count_left_min>count_right_min) or (count_left_middle>count_right_middle)):
            lst.append(value)

        #弹栈，分三种情况
        if value==separator:
            flagMin=1 #假设左右括号的个数都是相等的
            flagMid=1
            if '(' in lst:
                if count_left_min!=count_right_min:
                    flagMin=0
            if '[' in lst:
                if count_left_middle!=count_right_middle:
                    flagMid=0
            if flagMin and flagMid:
                ansLst.append(''.join(lst))
                lst.clear()
        elif index==len(s)-1:
            ansLst.append(''.join(lst))

    return ansLst



def isDynamic(dic):
    lst=list(dic.values())
    for it in lst:
        if isinstance(it,str):
            return 1
    return 0  #空字典也看作是模糊匹配的字典 



#/home/zhang/Packages/scikit-learn
#给定库的路径，获得该库的所有版本号
def getVersionLst(libPath):
    obj=Path('D')
    versionLst=[]
    obj.getPath(libPath)
    path=obj.path
    for p in path:
        p=p.split('/')[-1]
        index=-1
        for i in range(len(p)):
            if p[i].isdigit():
                index=i
                break
        versionLst.append(p[index:])
    versionLst.sort(key=lambda it:cmp(it))
    return versionLst


#将版本号格式统一为x.xx.xx.小数部分
#比如3.10.12与4.2.8，则将4.2.8转化为4.02.08
#4.5.0rc1转化为(4.05.00).3即40500.01
#4.5.0rc10转化为(4.05.00).3即40500.10
#整数部分模拟大版本，小数部分模拟大版本下的小版本，比如rc,a,b
def cmp(version):
    index=len(version)
    innerVersion=""
    for i in range(len(version)):
        if version[i].isalpha():
            index=i
            break
    if index!=len(version):
        innerVersion=re.findall(r'\d+',version[index:])[0]
        Type=re.findall(r'[a-zA-Z]+',version[index:])[0] #type='rc' or type='b' or type='a'
        if Type=='a': #alpha版
            if len(innerVersion)==1:
                innerVersion='0.00000'+innerVersion
            else:
                innerVersion='0.0000'+innerVersion #为了确保a10<b1
        elif Type=='b':#beta版
            if len(innerVersion)==1:
                innerVersion='0.000'+innerVersion
            else:
                innerVersion='0.00'+innerVersion #为了确保b10<rc1
        elif Type=='rc': #release版
            if len(innerVersion)==1:
                innerVersion='0.0'+innerVersion
            else:
                innerVersion='0.'+innerVersion
            
    
    lst=version[0:index].split('.')
    if len(lst)==2:
        lst.append('0')
    if len(lst[1])==1:
        lst[1]='0'+lst[1]
    if len(lst[2])==1:
        lst[2]='0'+lst[2]
    v=''.join(lst)
    if innerVersion=="":
        return float(v)
    else:
        return float(v)-(1-float(innerVersion)) #转化为浮点数形式



#给文件取名字
def getFileName(fileName,extension):
    #step1:先把fileName中的非法字符去除
    fileName=fileName.replace(' ','')
    fileName=fileName.replace('/','')
    fileName=fileName.replace('\\','')
    if len(extension) != 0:
        length=255-len(extension)
        #if len(fileName)>length:
            #fileName=fileName[0:length] #如果超出了长度，就进行截断
        fileName=fileName.split('(')[0] + '_' + hashlib.md5(fileName.encode()).hexdigest()[:16] # 2025.7.18 More robust file name processing
        fileName=fileName[0:length]

    fileName+=extension 
    return fileName
    



#规定文件中每行的字符串的宽度，如果超出宽度就换行写,如果换行之后还超过了最大宽度，则继续向下换行
def writeLine(width,s,fw):
    if len(s)<=width-4:
        tailSpaceNum=width-2-len(s)-1
        fw.write('| '+s+' '*tailSpaceNum+'|'+'\n')
    else:
        s1=s[0:width-4]
        s1='| '+s1+' |'+'\n'
        fw.write(s1)
        s2=s[width-4:]
        if len(s2)<=width-4:
            tailSpaceNum=width-2-len(s2)-1
            s2='| '+s2+' '*tailSpaceNum+'|'+'\n'
            fw.write(s2)
            return
        else:
            writeLine(width,s2,fw) #递归拆分



def save2txt(lst,libName,runCommand,savePath):
    fw=open(savePath,'w')
    totalFileNum=0
    totalAPINum=0
    compatibleNum=0
    incompatibleNum=0
    unknownCompatibleNum=0
    notCoverNum=0
    successRepairNum=0
    failedRepairNum=0
    unknownRepairNum=0
    for Tuple in lst: #计数
        totalFileNum+=1
        totalAPINum+=Tuple[2]
        dic=Tuple[0]
        for callAPI,subDict in dic.items():
            if subDict['Coverage']=='No':
                notCoverNum+=1
                continue
            
            if subDict['Compatible']=='Yes':
                compatibleNum+=1
            elif subDict['Compatible']=='No':
                incompatibleNum+=1
            else:
                unknownCompatibleNum+=1
            
            if 'Repair <Successful>' in subDict: 
                successRepairNum+=1
            elif 'Repair <Failed>' in subDict:
                failedRepairNum+=1
            elif 'Repair <Unknown>' in subDict:
                unknownRepairNum+=1
    
    #写结果
    libName=libName.capitalize()
    fw.write(f"Run Command: {runCommand}\n")
    fw.write(f"Total File Number: {totalFileNum}\n")
    fw.write(f"Total {libName} Invoked API Number: {totalAPINum}\n")
    fw.write(f"Not Covered {libName} Invoked API Number: {notCoverNum}/{totalAPINum}\n")
    fw.write(f"Covered {libName} Invoked API Number: {totalAPINum-notCoverNum}/{totalAPINum}\n\n")
    
    fw.write(f"Compatible {libName} Invoked API Number: {compatibleNum}/{totalAPINum-notCoverNum}\n")
    fw.write(f"Unknown Compatible {libName} Invoked API Number: {unknownCompatibleNum}/{totalAPINum-notCoverNum}\n\n")
    
    fw.write(f"Incompatible {libName} Invoked API Number: {incompatibleNum}/{totalAPINum-notCoverNum}\n")
    fw.write(f"-> Successfully Repaired {libName} Invoked API number: {successRepairNum}/{incompatibleNum}\n")
    fw.write(f"-> Failed to Repair {libName} Invoked API Number: {failedRepairNum}/{incompatibleNum}\n")
    fw.write(f"-> Unknown Repair Status {libName} Invoked API Number: {unknownRepairNum}/{incompatibleNum}\n\n")
    fileCount=0
    for Tuple in lst:
        dic=Tuple[0]
        filePath=Tuple[1]
        invokedAPINum=Tuple[2]
        fileCount+=1
        width=102 #设置列表总宽度175个字符
        title=f"File #{fileCount}: {filePath} has {invokedAPINum} {libName}-Invoked API(s)"
        line='='*width+'\n'
        fontSpaceNum=(width-len(title)-2)//2
        tailSpaceNum=width-2-fontSpaceNum-len(title)
        title='|'+' '*fontSpaceNum+title+' '*tailSpaceNum+'|'+'\n'
        fw.write(line)
        fw.write(title)
        fw.write(line)
        index=1
        for callAPI,subDict in dic.items():
            tempStr1=f"Invoked API #{index}: {callAPI.split('#_')[0]}"
            writeLine(width,tempStr1,fw)
            fw.write('|'+' '*(width-2)+'|'+'\n')
            cnt=1
            for k,v in subDict.items():
                tempStr2=f"{k}: {v}"
                writeLine(width,tempStr2,fw)
                if cnt!=len(subDict):
                    fw.write('|'+' '*(width-2)+'|'+'\n')
                cnt+=1
            
            fw.write('|'+' '*(width-2)+'|'+'\n')
            fw.write('|'+'-'*(width-2)+'|'+'\n')
            if index!=len(dic):
                fw.write('|'+' '*(width-2)+'|'+'\n')
            index+=1 
        fw.write('\n\n')

    fw.close()


def loadConfig(configPath):
    with open(configPath,'r') as fr:
        dic=json.load(fr)
    runCommand=dic['runCommand'].lstrip('python')
    return dic['projPath'],runCommand,dic['runFilePath'],dic['libName'],dic['currentVersion'],dic['targetVersion'],dic['currentEnv'],dic['targetEnv']



def findPythonDir(basePath):
    if not os.path.exists(basePath):
        print(f"Path is not exist: {basePath}")
        return None
    
    for entry in os.listdir(basePath):
        full_path = os.path.join(basePath, entry)
        if os.path.isdir(full_path):
            if entry.startswith("python"):
                # print(f"find the path: {full_path}")
                return full_path
    
    print(f"Can not find {basePath}/pythonxx.xx")
    return None


#f"/dataset/zhang/anaconda3/envs/3d/lib/{pythonxx.xx}/" + f"site-packages/{torch}"
def getSourceCodePath(configPath):
    with open(f"Configure/{configPath}",'r') as fr:
        dic=json.load(fr)
    libName=dic['libName']
    currentVersion=dic['currentVersion']
    targetVersion=dic['targetVersion']
    currentEnvPath=dic['currentEnv']
    targetEnvPath=dic['targetEnv']
    
    currentSourceCodePath=findPythonDir(f"{currentEnvPath}/lib")+f"/site-packages/{libName}" 
    targetSourceCodePath=findPythonDir(f"{targetEnvPath}/lib")+f"/site-packages/{libName}" 

    return currentVersion, targetVersion, currentSourceCodePath, targetSourceCodePath


#展开单行条件返回语句为多行if-else结构
class ConditionalReturnTransformer(ast.NodeTransformer):
    def visit_Return(self, node):
        #检查return语句是否为单行条件语句（IfExp)
        if isinstance(node, ast.Return) and isinstance(node.value, ast.IfExp):
            ifExp = node.value
            newIf = ast.If(
                           test=ifExp.test,
                           body=[ast.Return(value=ifExp.body)],
                           orelse=[ast.Return(value=ifExp.orelse)]
                          )
            return newIf
        return node
