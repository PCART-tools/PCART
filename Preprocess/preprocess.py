## @package preprocess 
#  Preprocess project source files for preparing API parameter compatibility issue detection and repair   
#
#  More details (TODO)



import re
import ast
import shutil
from Path.getPath import *
from Extract.getCall import getCallFunction, modifyWithName
from Extract.extractCall import WithVisitor
from Tool.tool import getAst,getParameter,getLastAPIParameter,departAPI,departAPI2,ConditionalReturnTransformer, getFileName, getRunFile
from Tool.workspace import getRuntimePaths



## Count the number of different types of brackets ((), [], {}) in a string
## 计算字符串中各类括号((), [], {})的个数
#  @param s The string
#  @return (minL, minR, midL, midR, huaL, huaR) minL, minR: the number of "(" and ")"; midL, midR: the number of "[" and "]"; huaL, huaR: the number of "{" and "}" 
def countBracket(s):
    minL=0
    minR=0
    midL=0
    midR=0
    huaL=0
    huaR=0
    flag=1
    cnt=0 #计算引号的个数
    for it in s:
        if it=='\'': #引号内的括号不计数
            flag=0
            cnt+=1
            if cnt%2==0:
                flag=1
        elif flag==1:
            if it=='(':
                minL+=1
            elif it==')':
                minR+=1
            elif it=='[':
                midL+=1
            elif it==']':
                midR+=1
            elif it=='{':
                huaL+=1
            elif it=='}':
                huaR+=1
    return minL,minR,midL,midR,huaL,huaR



## Convert the multi-line parameter calls in the code into a single line to facilitate insertion into dictionary statements 
## 把代码中换行写的参数调用，合并成一行，目的是便于插入字典语句
#  @param filePath The source file path
def oneLine(filePath):
    try:
        root=getAst(filePath)
        #重写回文件
        with open(filePath,'w',encoding='UTF-8') as fw:
            newCode=ast.unparse(root)
            # newCode=re.sub(r'""".*?"""','pass',newCode,flags=re.DOTALL) #去掉代码中的注释
            fw.write(f"{newCode}\n")
    except Exception as e:
        print(f"oneLine --> {filePath} parse to ast failed: {e}")


    
## Expand the single-line conditional return statement into a multi-line if-else structure  
## 展开单行条件return语句为多行if-else结构
#  @param filePath The source file path 
def expandConditionalReturn(filePath):
    try:
        root=getAst(filePath)
        transformer = ConditionalReturnTransformer()
        new_root = transformer.visit(root)
        #print(ast.unparse(new_root)) 
        #重写回文件
        with open(filePath,'w',encoding='UTF-8') as fw:
            newCode=ast.unparse(root)
            fw.write(f"{newCode}\n")
    except Exception as e:
        print(f"expandConditionalReturn --> {filePath} parse to ast failed: {e}")
 


## Get the local variable in the list comprehension
## 获取列表推导式中的局部变量
#
#  For example, [x**2 for x in range(10)] --> x=[x for x in range(10)][0]
#  比如[x**2 for x in range(10)]转换为 x=[x for x in range(10)][0]
#
#
#  @param root The AST root of the line of code
#  @param ansLst List of coverted local variable(s) in list comprehension
def getListVar(root,ansLst):
    for node in ast.iter_child_nodes(root):
        if isinstance(node,ast.ListComp):
            s=ast.unparse(node.generators).lstrip(' ')
            pattern="for (.*?) in"
            lst=re.findall(pattern,s)
            if len(lst)==1:
                temp=lst[0]
                if temp[0]=='(':
                    var=temp[1:-1]
                else:
                    var=temp
                s1=f"{var}=[{temp} {s}][0]"
                ansLst.append(s1)

        getListVar(node,ansLst)    



## Get the local variable in the dictionary comprehension
## 获取字典推导式中的局部变量
#
#  For example, {k:v for k,v in {'a': 1, 'b': 2, 'c': 3}.items()} --> k, v=[(k, v) for (k, v) in {'a': 1, 'b': 2, 'c': 3}.items()][0] 
#  比如{k:v for k,v in {'a': 1, 'b': 2, 'c': 3}.items()}转换后为k, v=[(k, v) for (k, v) in {'a': 1, 'b': 2, 'c': 3}.items()][0] 
#
#  @param root The AST root of the line of code
#  @param ansLst List of coverted local variable(s) in dictionary comprehension
def getDictVar(root,ansLst):
    for node in ast.iter_child_nodes(root):
        if isinstance(node,ast.DictComp):
            s=ast.unparse(node.generators).lstrip(' ')
            pattern="for (.*?) in"
            lst=re.findall(pattern,s)
            if len(lst)==1:
                temp=lst[0]
                if temp[0]=='(':
                    var=temp[1:-1]
                else:
                    var=temp
                s1=f"{var}=[{temp} {s}][0]"
                ansLst.append(s1)

        getDictVar(node,ansLst)    



## Convert the ListComp and DictComp statements to variable assignment statements 
## 将列表推导式listComp和字典推导式DictComp转换为变量赋值表达式
#
#  @param filePath The source file path
#  @param libName The name of the lib
def convertLocalVar(filePath,libName):
    with open(filePath,'r',encoding='UTF-8') as fr:
        codeLst=fr.readlines()
    
    for i in range(len(codeLst)):
        s=codeLst[i].lstrip(' ').rstrip(' ')
        try:
            root=ast.parse(s,filename='<unknown>',mode='exec')
        except Exception as e:
            # print(f"converLocalVar: ast.parse error，{e}")
            continue
        
        #step1:判断代码语句中是否含有列表推导式或字典推导式
        listComp=0
        dictComp=0
        for node in ast.walk(root):
            if isinstance(node,ast.ListComp):
                listComp=1
            if isinstance(node,ast.DictComp):
                dictComp=1

        if not listComp and not dictComp:
            continue

        #step2:判断列表推导式中是否含有第三方库调用的API
        flag=0
        _,callDict=getCallFunction(filePath,libName)
        callLst=[record['call_text'] for record in callDict.values()]
        flag=0
        for node in ast.walk(root):
            if isinstance(node, ast.Call):
                callState=ast.unparse(node)
                callState=callState.replace(' ','').replace('"','').replace("'",'')
                for it in callLst:
                    if callState==it.replace(' ','').replace('"','').replace("'",''):
                        flag=1
                        break
                if flag==1:
                    break
        if flag==0:
            continue
        
        #step3:提取出列表推导式中的变量
        ansLst=[]
        if listComp:
            getListVar(root,ansLst)
            spaceNum=countSpace(codeLst[i])
            temp=''
            for it in ansLst:
                tryStr="try:\n"
                exceptStr="except:\n"
                passStr="pass\n"
                if spaceNum:
                    tryStr=' '*spaceNum*1+tryStr
                    it=' '*spaceNum*1+' '*4+it+'\n'
                    exceptStr=' '*spaceNum*1+exceptStr
                    passStr=' '*spaceNum*1+' '*4+passStr
                else:
                    spaceNum=4
                    it=' '*spaceNum*1+it+'\n'
                    passStr=' '*spaceNum*1+passStr
                    spaceNum=0 #用完之后就置为0
            
                s=tryStr+it+exceptStr+passStr
                # print(filePath)
                # print(s)
                temp=temp+s
            temp+=codeLst[i]
            codeLst[i]=temp

        if dictComp:
            getDictVar(root,ansLst)
            spaceNum=countSpace(codeLst[i])
            temp=''
            for it in ansLst:
                tryStr="try:\n"
                exceptStr="except:\n"
                passStr="pass\n"
                if spaceNum:
                    tryStr=' '*spaceNum*1+tryStr
                    it=' '*spaceNum*1+' '*4+it+'\n'
                    exceptStr=' '*spaceNum*1+exceptStr
                    passStr=' '*spaceNum*1+' '*4+passStr
                else:
                    spaceNum=4
                    it=' '*spaceNum*1+it+'\n'
                    passStr=' '*spaceNum*1+passStr
                    spaceNum=0 #用完之后就置为0
            
                s=tryStr+it+exceptStr+passStr
                # print(filePath)
                # print(s)
                temp=temp+s
            temp+=codeLst[i]
            codeLst[i]=temp


    with open(filePath,'w',encoding='UTF-8') as fw:
        for it in codeLst:
            fw.write(it)



## Find assignment call statements
## 获取赋值调用语句
#
#  @param root The AST root of the source code
#  @return assignLst List of assignment call statements
def findAssignCall(root):
    assignLst=[]
    for node in ast.walk(root):
        if isinstance(node,ast.Assign) and isinstance(node.value,ast.Call):
            target=ast.unparse(node.targets)
            assignLst.append(target)
    return assignLst


## Resolve the source expression assigned to a receiver alias
## 还原调用者别名在当前作用域内的赋值来源表达式
#
#  @param root The AST root of the source code
#  @param source The original source code
#  @param aliasName The first name of the receiver alias
#  @param lineno The line number of the call site
#  @return expr The scoped assignment expression or None
def getAssignReceiverExpr(root,source,aliasName,lineno):
    expr=None
    bestLine=-1

    scopeBodies=[root.body]
    for node in ast.walk(root):
        if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)):
            start=node.lineno
            end=getattr(node,'end_lineno',start)
            if start<lineno<=end:
                scopeBodies.append(node.body)

    for body in scopeBodies:
        for stmt in body:
            if not hasattr(stmt,'lineno') or stmt.lineno>=lineno:
                continue
            if isinstance(stmt,(ast.If,ast.For,ast.AsyncFor,ast.While,ast.Try,ast.With,ast.AsyncWith)):
                continue
            value=None
            targets=[]
            if isinstance(stmt,ast.Assign):
                value=stmt.value
                targets=stmt.targets
            elif isinstance(stmt,ast.AnnAssign):
                value=stmt.value
                targets=[stmt.target]
            if value is None:
                continue
            for target in targets:
                if isinstance(target,ast.Name) and target.id==aliasName and stmt.lineno>bestLine:
                    sourceExpr=ast.get_source_segment(source,value)
                    if sourceExpr:
                        expr=sourceExpr.strip()
                        bestLine=stmt.lineno
    return expr


## Resolve the visible base-class expression for an inherited self receiver
## 还原继承场景中self调用者可见的基类表达式
#
#  @param root The AST root of the source code
#  @param lineno The line number of the call site
#  @param methodName The self method name
#  @return expr The base-class expression or None
def getSelfReceiverExpr(root,lineno,methodName):
    for node in ast.walk(root):
        if not isinstance(node,ast.ClassDef):
            continue
        start=node.lineno
        end=getattr(node,'end_lineno',start)
        if not (start<lineno<=end) or len(node.bases)==0:
            continue
        defNames=set()
        for item in ast.iter_child_nodes(node):
            if isinstance(item,(ast.FunctionDef,ast.AsyncFunctionDef)):
                defNames.add(item.name)
        if methodName in defNames:
            return None
        return ast.unparse(node.bases[0])
    return None

    

## Count the number of spaces at the beginning of a string 
## 计算字符串的前面有多少个空格
#
#  @param s The string
#  @return cntSpace The number of spaces
def countSpace(s):
    cntSpace=0
    for it in s:
        if it==' ':
            cntSpace+=1
        else:
            break
    return cntSpace



## Determine the instrumentation line for import statements
## 确定import语句插桩行
#  
#  Default line is 0. Avoid instrumenting import statements before __future__ statements) or between comments 
#  默认行为0，避免在__future__前或注释块中插入import语句
#
#  @param codeLst Code list read by f.readlines()
#  @return index The appropriate index for import statement instrumentation
def getImportLine(codeLst):
    #首先判断from import语句中是否含有特殊的__future__
    index=-1
    for i in range(len(codeLst)):
        if 'import' in codeLst[i] and '__future__' in codeLst[i]:
            index=i

    #若没有future,再判断开头是否存在'"""'注释 
    count=0
    if index==-1 and '"""' in codeLst[0]:
        for i in range(0,len(codeLst)):
            if '"""' in codeLst[i]:
                index=i
                count+=1
            if count==2:
                break

    index+=1
    
    return index



## Extract decorator API calls
## 抽取项目中第三方库装饰器调用
#
#  @param root The AST root of the source code file
#  @return decoratorLst The list of decorator API calls 
def extractDecorator(root):
    decoratorLst = []
    for n in ast.walk(root):
        if isinstance(n, (ast.FunctionDef, ast.ClassDef)) and n.decorator_list:
            for decorator in n.decorator_list:
                if isinstance(decorator, ast.Call): # and isinstance(decorator.func.value, ast.Name):
                    decoratorLst.append(ast.unparse(decorator.func))

    return decoratorLst 



## Code instrumentation for a single API call within a source file
## 源文件单个API调用代码插桩
#
#  @param callAPI The API call
#  @param filePath The source file path
#  @param callKey Unique callsite artifact id
def addDictSingle(callAPI,filePath,callKey):
    with open(filePath,'r',encoding='UTF-8') as fr:
        codeLst=fr.readlines()
    source=''.join(codeLst)
    
    lineno=getImportLine(codeLst)
    importDict='from recordValue import paraValueDict\nfrom recordValue import callsiteInfoDict\n'
    codeLst.insert(lineno,importDict)
    
    paraStr=getLastAPIParameter(callAPI) #获取最后一个API的参数
    parameterLst=getParameter(paraStr,space=0) #项目参数不去空格
    root=getAst(filePath)
    targetLst=findAssignCall(root)

    #找出树中所有withitem call节点 -- 2025/5/19
    withitem_visitor = WithVisitor()
    withitem_visitor.visit(root)
    withitem_call_names = withitem_visitor.get_withitem_call() #dict

    decoratorLine = list() #记录装饰器出现的行号 -- 2025.5.12
    for i in range(len(codeLst)): #每次只会往列表中插入一个元素
        if callAPI.replace(' ','') in codeLst[i].replace(' ','') and 'def ' not in codeLst[i] and 'paraValueDict' not in codeLst[i]:
            spaceNum=countSpace(codeLst[i])
            dicString1=''
            l=departAPI(callAPI)
            l2=departAPI2(callAPI)
            firstPart=''
            for it in l2:
                if '(' not in it:
                    firstPart+=it+'.'
            firstPart=firstPart.rstrip('.')
            
            key=callKey.replace('"','\\"')
            callsiteInfo={
                'call_text': callAPI,
                'format_api': callAPI,
            }
            dicString0=f'callsiteInfoDict[{repr(callKey)}]={repr(callsiteInfo)}\n'
            if firstPart and (firstPart.split('.')[0] in targetLst or firstPart.split('.')[0]=='self') and len(l)==1:
                lineNo = i + 1
                receiverExpr=None
                if firstPart.split('.')[0] in targetLst:
                    receiverExpr=getAssignReceiverExpr(root,source,firstPart.split('.')[0],lineNo)
                elif firstPart.split('.')[0]=='self':
                    methodName=callAPI.split('(')[0].split('.')[-1]
                    receiverExpr=getSelfReceiverExpr(root,lineNo,methodName)
                if receiverExpr:
                    receiverExpr=receiverExpr.replace('\\','\\\\').replace('"','\\"')
                    dicString1=f'paraValueDict[\"@{key}\"]={{}}; paraValueDict[\"@{key}\"][\"object\"]={firstPart}; paraValueDict[\"@{key}\"][\"expr\"]=\"{receiverExpr}\"\n'
                else:
                    dicString1=f'paraValueDict[\"@{key}\"]={firstPart}\n'
            elif len(l)>1: #df.a(x).b(y), np.max(...), torch.nn.Sequential(...)
                dicString1=f'paraValueDict[\"@{key}\"]={l[-2]}\n'

            #判断API是否为withitem中的别名调用 -- 2025/5/19 
            if firstPart and firstPart.split('.')[0] in withitem_call_names:
                lineNo = i + 1
                initialCallName = modifyWithName(firstPart, withitem_call_names, lineNo).rstrip('.')
                # withitem接收者同时保存运行时对象和还原表达式，动态阶段按可用候选依次尝试
                initialCallName=initialCallName.replace('\\','\\\\').replace('"','\\"')
                dicString1=f'paraValueDict[\"@{key}\"]={{}}; paraValueDict[\"@{key}\"][\"object\"]={firstPart}; paraValueDict[\"@{key}\"][\"expr\"]=\"{initialCallName}\"\n'
            
            #再保存API的参数值 
            dicString2=f'paraValueDict[\"{key}\"]'+'=['
            for para in parameterLst: #
                if '=' in para and "'='" not in para and '"="' not in para: #若参数的形式为key=f(x=1),只要确保=的前面不含括号即可
                    pos=para.find('=') #找到第一个=的位置
                    if '(' not in para[0:pos] and "'" not in para[0:pos] and '"' not in para[0:pos] and para[pos+1]!='=': #等号前面也不能出现引号，比如f('x= ',y=1)
                        para=para[pos+1:]
                
                para=para.lstrip('*') #有的参数会带*，2023-12-20
                dicString2=dicString2+para+','
            dicString2=dicString2.rstrip(',')+']\n'
            
            while spaceNum>0:
                dicString0=' '+dicString0
                if dicString1:
                    dicString1=' '+dicString1
                dicString2=' '+dicString2
                spaceNum-=1

            #插入的时候要考虑是否含有elif,如果有elif要把它插在elif后面
            if 'elif' not in codeLst[i]:
                #处理两个连续的装饰器@ -- 2025.5.12
                #不能在两个连续的decorator之间插入桩点
                if len(decoratorLine) > 1 and decoratorLine[-1] - decoratorLine[-2] == 3 and codeLst[i].replace(' ','')[0]=='@':
                    i = insertStartLine
                codeLst.insert(i,dicString2)
                if dicString1:
                    codeLst.insert(i,dicString1)
                codeLst.insert(i,dicString0)
            else:
                if dicString1:
                    dicString1=dicString1.lstrip(' ')#去掉之前添加的空格，重新计算开头的空格数
                dicString0=dicString0.lstrip(' ')
                dicString2=dicString2.lstrip(' ') 
                for j in range(i+1,len(codeLst)):
                    if codeLst[j]!='\n' and '#' not in codeLst[j]:
                        spaceNum=countSpace(codeLst[j])
                        while spaceNum>0:
                            dicString0=' '+dicString0
                            if dicString1:
                                dicString1=' '+dicString1
                            dicString2=' '+dicString2
                            spaceNum-=1
                        
                        codeLst.insert(j,dicString2)
                        if dicString1:
                            codeLst.insert(j,dicString1)
                        codeLst.insert(j,dicString0)
                        break

            break
        

    if codeLst[0]=='pass\n':
        codeLst=codeLst[1:]
    with open(filePath,'w',encoding='UTF-8') as fw:
        for it in codeLst:
            fw.write(it)



## Code instrumentation for all API calls within a project source file
## 项目源文件所有API调用代码插桩
#
#  @param projPath The project path 
#  @param projName The project name 
#  @param filePath The project source file path
#  @param copyRoot The runtime Copy directory
#  @param runFileLst The list of run files 
#  @param libName The lib name  
#  @param runPath The relative path of the run file 
#  @param runCommand The run command of the project 
def addDictAll(projPath,projName,filePath,copyRoot,runFileLst,libName,runPath,runCommand):
    with open(filePath,'r',encoding='UTF-8') as fr:
        code=fr.read()
        fr.seek(0) #将文件指针重新定位到文件的开头
        codeLst=fr.readlines()
    try:
        root=ast.parse(code,filename='<unknown>',mode='exec')
    except Exception as e:
        print(f"addDictAll --> ast.parse failed, {filePath}: {e}")
        return

    #处理相关路径
    fileName = os.path.basename(filePath)[0:-3]
    fileRelativePath=os.path.relpath(filePath,os.path.join(copyRoot,projName))
    fileAbsolutePath=os.path.join(projPath,fileRelativePath)
    
    lineno=getImportLine(codeLst)
    importDict='from recordValue import paraValueDict\nfrom recordValue import apiCoveredSet\nfrom recordValue import callsiteInfoDict\n'
    codeLst.insert(lineno,importDict)
    _,callDict=getCallFunction(fileAbsolutePath,libName,projPath)

    targetLst=findAssignCall(root) #用来区分调用者是否来自赋值语句，比如a.f(), tf.f(), or self.f()
 
    #找出树中所有withitem call节点 -- 2025/5/19
    try:
        withitem_root = getAst(fileAbsolutePath)
    except Exception:
        withitem_root = root
    withitem_visitor = WithVisitor()
    withitem_visitor.visit(withitem_root)
    withitem_call_names = withitem_visitor.get_withitem_call() #dict

    insertStartLine=0 #记录每次插桩的行
    preInsertAPI='' #记录上一个插桩的API是哪个
    preInsertAPICount=0 #记录上一个插桩行中出现了几次被插的API
    decoratorLine = list() #记录装饰器出现的行号 -- 2025.5.12
    for artifactId,record in callDict.items(): #key是调用点artifact id，value是结构化调用点记录
        flag=0 #标记API是否找到了插桩的位置
        lineno=int(record['lineno']) #这个lineno是原项目中的行数
        callState=record['call_text']
        paraStr=record['parameters']
        callAPI=callState.replace(' ','')
        if callAPI==preInsertAPI: #判断当前要处理的API与上一个API是否相同
            preInsertAPICount-=1
            if preInsertAPICount<=0:
                insertStartLine+=1
        
        i=insertStartLine #从第i行开始向后找
        while i<len(codeLst):
            #API调用在i行代码中，且i行代码不是函数定义语句、插桩语句paraValueDict和运行覆盖检查语句apiCoveredSet
            if callAPI in codeLst[i].replace(' ','') and 'def ' not in codeLst[i] and 'paraValueDict' not in codeLst[i] and 'apiCoveredSet' not in codeLst[i]:
                #记录装饰器出现的行号--2025.5.12
                if codeLst[i].replace(' ','')[0]=='@':
                    decoratorLine.append(i)              
                if callAPI!=preInsertAPI:#只有当前API不等于上一个被插API时，才需要重新计算preAPICount
                    preInsertAPICount=codeLst[i].replace(' ','').count(callAPI)
                    preInsertAPI=callAPI
                flag=1
                spaceNum=countSpace(codeLst[i])
                callSiteKey=artifactId
                callsiteInfo={
                    'artifact_hash': record.get('artifact_hash',''),
                    'rel_path': record.get('rel_path',''),
                    'lineno': record.get('lineno'),
                    'col_offset': record.get('col_offset'),
                    'end_lineno': record.get('end_lineno'),
                    'end_col_offset': record.get('end_col_offset'),
                    'call_text': record.get('call_text',''),
                    'format_api': record.get('format_api',''),
                }
                dicString0=f'callsiteInfoDict[{repr(callSiteKey)}]={repr(callsiteInfo)}\n'
                l=departAPI(callState)
                l2=departAPI2(callState)
                firstPart=''
                for it in l2:
                    if '(' not in it:
                        firstPart+=it+'.'
                firstPart=firstPart.rstrip('.')
                dicString1=''
                
                #判断API是否具有上文依赖，比如self.f(x), a(x).b(y)中的a(x)，或者a.f(x)中的a
                #df.a(x).b(y)这种情况如何解决
                #a.b.c(x)
                # if '(' not in firstPart and (firstPart in targetLst or firstPart=='self'):
                #self.f(x), a.f(x), a.b.c(x)
                if firstPart and (firstPart.split('.')[0] in targetLst or firstPart.split('.')[0]=='self') and len(l)==1:
                    receiverExpr=None
                    if firstPart.split('.')[0] in targetLst:
                        receiverExpr=getAssignReceiverExpr(root,code,firstPart.split('.')[0],lineno)
                    elif firstPart.split('.')[0]=='self':
                        methodName=callState.split('(')[0].split('.')[-1]
                        receiverExpr=getSelfReceiverExpr(root,lineno,methodName)
                    if receiverExpr:
                        receiverExpr=receiverExpr.replace('\\','\\\\').replace('"','\\"')
                        dicString1=f'paraValueDict[\"@{callSiteKey}\"]={{}}; paraValueDict[\"@{callSiteKey}\"][\"object\"]={firstPart}; paraValueDict[\"@{callSiteKey}\"][\"expr\"]=\"{receiverExpr}\"\n'
                    else:
                        dicString1=f'paraValueDict[\"@{callSiteKey}\"]={firstPart}\n'
                elif len(l)>1: #df.a(x).b(y), np.max(...), torch.nn.Sequential(...)
                    dicString1=f'paraValueDict[\"@{callSiteKey}\"]={l[-2]}\n'
               
                #判断API是否为withitem中的别名调用 -- 2025/5/19 
                if firstPart and firstPart.split('.')[0] in withitem_call_names:
                    initialCallName = modifyWithName(firstPart, withitem_call_names, lineno).rstrip('.')
                    initialCallName = initialCallName.rstrip('.')
                    # withitem接收者同时保存运行时对象和还原表达式，非withitem调用仍保持原有单值保存
                    initialCallName=initialCallName.replace('\\','\\\\').replace('"','\\"')
                    dicString1=f'paraValueDict[\"@{callSiteKey}\"]={{}}; paraValueDict[\"@{callSiteKey}\"][\"object\"]={firstPart}; paraValueDict[\"@{callSiteKey}\"][\"expr\"]=\"{initialCallName}\"\n'
                #再保存API的参数值
                dicString2=f'paraValueDict[\"{callSiteKey}\"]=['
                paraLst=getParameter(paraStr,space=0) #项目参数不去空格2023-12-14
                for para in paraLst: 
                    if '=' in para and "'='" not in para and '"="' not in para: #若参数的形式为key=f(x=1),只要确保=的前面不含括号即可
                        pos=para.find('=') #找到第一个=的位置,存在x=(a==b)和a==b形式
                        if '(' not in para[0:pos] and "'" not in para[0:pos] and '"' not in para[0:pos] and para[pos+1]!='=': #等号前面也不能出现引号，比如f('x= ',y=1)
                            para=para[pos+1:] #把参数的值保存下来
                    
                    para=para.lstrip('*') #有的参数会带*号，2023-12-20
                    dicString2=dicString2+para+','
                dicString2=dicString2.rstrip(',')+']\n'
                
                dicString3=f'apiCoveredSet.add(\"{callSiteKey}\")\n'
                while spaceNum>0:
                    dicString0=' '+dicString0
                    if dicString1:
                        dicString1=' '+dicString1
                    dicString2=' '+dicString2
                    dicString3=' '+dicString3
                    spaceNum-=1

                #插入的时候要考虑是否含有elif,如果有elif要把它插在elif后面
                #因为不能以相同的所以把字典插在if和elif之间
                if 'elif' not in codeLst[i]:
                    #处理两个连续的装饰器@ -- 2025.5.12
                    #不能在两个连续的decorator之间插入桩点
                    if len(decoratorLine) > 1 and  codeLst[i].replace(' ','')[0]=='@':
                        if decoratorLine[-1] - decoratorLine[-2] == 3 or decoratorLine[-1] - decoratorLine[-2] ==4:
                            i = insertStartLine 
                    codeLst.insert(i,dicString3)
                    codeLst.insert(i,dicString2)
                    if dicString1:
                        codeLst.insert(i,dicString1)
                    codeLst.insert(i,dicString0)
                    #记录当前插在了哪一行
                    if dicString1:
                        insertStartLine=i+4
                    else:
                        insertStartLine=i+3
                else:
                    if dicString1:
                        dicString1=dicString1.lstrip(' ') #去掉之前添加的空格，重新计算开头的空格数
                    dicString0=dicString0.lstrip(' ')
                    dicString2=dicString2.lstrip(' ') 
                    dicString3=dicString3.lstrip(' ') 
                    for j in range(i+1,len(codeLst)):
                        if codeLst[j]!='\n' and '#' not in codeLst[j]:
                            spaceNum=countSpace(codeLst[j])
                            while spaceNum>0:
                                dicString0=' '+dicString0
                                if dicString1:
                                    dicString1=' '+dicString1
                                dicString2=' '+dicString2
                                dicString3=' '+dicString3
                                spaceNum-=1
                            codeLst.insert(j,dicString3)
                            codeLst.insert(j,dicString2)
                            if dicString1:
                                codeLst.insert(j,dicString1)
                            codeLst.insert(j,dicString0)
                            #记录当前插在了哪一行
                            if dicString1:
                                insertStartLine=j+4
                            else:
                                insertStartLine=j+3
                            break
  
                break
            
            i+=1
        
        if flag==0:
            print(f"{fileName}#{lineno}-->{callState}\n")
            # with open('66666666666.py','a') as fw:
            with open('66666666666.py', 'a', encoding='UTF-8') as fw:
                fw.write('\n'+fileName+'='*100+'\n')
                fw.write(f"{fileName}#{lineno}--->{callState}\n")
                for it in codeLst[insertStartLine:]:
                    fw.write(it)

    if codeLst[0]=='pass\n':
        codeLst=codeLst[1:]
    with open(filePath,'w',encoding='UTF-8') as fw:
        for it in codeLst:
            fw.write(it)



## Code instrumentation for project run file
## 项目运行文件代码插桩
#
#  该函数用于动态匹配时候的时候对单个API进行插桩，除了要插桩当前文件
#  还要对运行文件进行插桩,所以提前把bak_Proj中的运行文件处理好
#
#  @param file The run file
#  @param runPath The relative path of the run file 
#  @param runCommand The run command of the project 
def handleRunFile(file,runPath,runCommand):
    with open(file,'r',encoding='UTF-8') as fr:
        codeLst=fr.readlines()
    lineno=getImportLine(codeLst)
    codeLst.insert(lineno,f"from recordValue import paraValueDict\n")

    if codeLst[0]=='pass\n':
        codeLst=codeLst[1:]
    with open(file,'w',encoding='UTF-8') as fw:
        for it in codeLst:
            fw.write(it)

def obtainDef(sourcePath):
    with open(sourcePath,'r',encoding='UTF-8') as fr:
        code=fr.read()
    try:
        root=ast.parse(code,filename='<unknown>',mode='exec') #将源码解析成AST语法树
    except:
        print(sourcePath)
        return
    fw=open('Copy/defFile.py','a',encoding='UTF-8')
    for node in ast.iter_child_nodes(root):
        if isinstance(node,ast.ClassDef) or isinstance(node,ast.FunctionDef):
            s=ast.unparse(node)
            fw.write(f"{s}\n")
    fw.close()


## Save import statement to source file
## 将import语句保存到源码中
#
#  @param filePath The source file path
#  @param importStatement The import statement to be saved
def modifyFromImport(filePath,importStatement):
    # with open(filePath,'r') as fr:
    with open(filePath, 'r', encoding='UTF-8') as fr:
        codeLst=fr.readlines()

    s='\n'.join(importStatement)+'\n'
    # print(s)
    codeLst.insert(0,s)
    # with open(filePath,'w') as fw:
    with open(filePath, 'w', encoding='UTF-8') as fw:
        for it in codeLst:
            fw.write(it)



## Save assignment statement with constant values
## 保存常量赋值语句
#
#  保留包含常量的全局赋值语句和装饰器调用相关的赋值语句，例如:
#  Case 1:
#  1.  a = 1
#  2.  b = 1
#  3.  c = a + b
#  4.  c = func(a,b)
#  仅保留1，2，3行代码
#  Case 2:
#  1. app = Flask(__name__)
#  2. @app.route("/")
#  保留 app = Flask(__name__)以解决NameError 
#
#  @param astNode The AST node
#  @param constantVar Constant variable
#  @param nonConstantVar Non-constant variable
#  @param decoratorLst Decorator API call list 
#  @return astBody The AST of the saved assignment statement; 1 for none
def saveConstantAssign(astNode, constantVar, nonConstantVar, decoratorLst):
    flag = 0
    astBody = []
    for n in ast.walk(astNode):
        if isinstance(n,ast.Assign):
            value = n.value
            valueAstContent = ast.dump(n.value)
            targetAstContent = ast.dump(n.targets[0])
            if isinstance(n.targets[0], ast.Name):
                varName = n.targets[0].id
                #如果赋值语句的变量名在装饰器列表中出现过，则保留该赋值语句 2025/5/13 
                if any(varName in decorator.split('.') for decorator in decoratorLst):
                    continue
                #如果赋值语句的变量名是常量变量名，则保留该赋值语句 2025/5/31 
                if isinstance(value, ast.Constant):
                    if varName in nonConstantVar:
                        flag=1
                        break
                    else:   
                        targets = n.targets
                        if targets:
                            target = targets[0]
                            if isinstance(target, ast.Name):
                                constantVar.append(target.id)
                else:
                    # 使用正则表达式匹配单引号包围的内容
                    pattern = r"id='([^']*)'"
                    valueMatches = re.findall(pattern, valueAstContent)
                    targetMatches = re.findall(pattern, targetAstContent)
                    if not len(valueMatches):
                        if targetMatches[0] in nonConstantVar:
                            flag=1
                            break
                    else:
                        for match in valueMatches:
                            if match not in constantVar:
                                nonConstantVar.append(targetMatches[0])
                                flag=1
                                break
            else:
                flag=1
                break
    if flag==1:
        return flag
    else:
        astBody.append(astNode)
        return astBody


 
## Save structure information of the project 
## 保存项目的结构信息
#
#  @param projPath The project path
#  @param libName The lib name
def saveStructure(projPath,libName):
    pathObj=Path('DF')
    pathObj.getPath(projPath)
    filePath=[it for it in pathObj.path if it.endswith('py')]
    for file in filePath:
        _,callDict=getCallFunction(file,libName)
        callLst=[record['call_text'] for record in callDict.values()]
        # with open(file,'r') as fr:
        with open(file, 'r', encoding='UTF-8') as fr:
            code=fr.read()
        try:
            root=ast.parse(code,filename='<unknown>',mode='exec')
        except Exception as e:
            print(f"saveStructure --> ast parse failed in {file}: {e}")
            continue
        newBody=[]
        constantVar = []
        nonConstantVar = []
        decoratorLst = extractDecorator(root)
        #保留Import语句、函数和类定义
        for node in root.body:
            #增加AsyncFunctionDef节点信息保存 -- 2025/5/19 
            if isinstance(node,ast.Import) or isinstance(node,ast.ImportFrom) or isinstance(node,ast.ClassDef) or isinstance(node,ast.FunctionDef) or isinstance(node,ast.AsyncFunctionDef):
                newBody.append(node)

            #保留包含常量的全局赋值语句和装饰器调用相关的赋值语句，例如:
            # Case 1:
            #1.  a = 1
            #2.  b = 1
            #3.  c = a + b
            #4.  c = func(a,b)
            #仅保留1，2，3行代码
            # Case 2:
            #1. app = Flask(__name__)
            #2. @app.route("/")
            #保留 app = Flask(__name__)以解决NameError 
            if isinstance(node,ast.Assign):
                result = saveConstantAssign(node,constantVar,nonConstantVar,decoratorLst)
                if result==1:
                    continue
                else:
                   newBody+=result

        #保留包含常量的局部赋值语句
        for node in ast.walk(root):
            if isinstance(node,ast.Assign):
                result = saveConstantAssign(node,constantVar,nonConstantVar,decoratorLst)
                if result==1:
                    continue
                else:
                   for item in result:
                       if ast.dump(item) not in [ast.dump(i) for i in newBody]: 
                           newBody.append(item)
    
        root.body=newBody
        newFile=ast.unparse(root)
        with open(file,'w',encoding='utf-8') as fw:
            fw.write(f"{newFile}\n")



## Determine the soft link files in a directory
## 确定文件夹中的软链接文件
#
#  @param directory The directory
#  @param files The files in the directory
#  @return [f for f in files if os.path.islink(os.path.join(directory, f))] List of soft link files
def ignore_sym_links(directory, files):
    return [f for f in files if os.path.islink(os.path.join(directory, f))]



## Get all lib-related import statements
## 获取所有第三方库相关的import语句
#
#  @param projPath The project path 
#  @param libName The project name
#  @return ansLst List of all lib-related import statements
def getLibImportLst(projPath,libName):
    lst=[]
    pathObj=Path('DF')
    pathObj.getPath(projPath)
    filePath=[file for file in pathObj.path if file.endswith('.py')]
    pattern=rf"(from {libName}|import {libName})" #确保库的前面不会出现其它字符
    for file in filePath:#下面的所有操作都是对项目副本进行的
        # with open(file,'r') as fr:
        with open(file, 'r', encoding='UTF-8') as fr:
            code=fr.read()
        try:
            root=ast.parse(code,filename='<unknown>',mode='exec')
            for node in ast.walk(root):
                if isinstance(node,ast.Import) or isinstance(node,ast.ImportFrom):
                    s=ast.unparse(node)
                    if bool(re.search(pattern,s)):
                        lst.append(s)
        except Exception as e:
            print(f"getLibImportLst: ast parse failed, {file}, {e}")


    ansLst=list(set(lst))
    ansLst.sort(key=lst.index) 
    return ansLst 



## Convert tabs to spaces in all Python files within a directory
## 将目录下所有Python文件中的制表符转换为空格
#
#  @param directory The directory path to process
def convertTabsToSpaces(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    # 将制表符转换为4个空格
                    content = content.expandtabs(4)
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                except Exception as e:
                    print(f"Error converting file {file_path}: {e}")



## Write recordValue.py used by instrumented project files
## 写入插桩文件共享的recordValue.py
#
#  @param filePath The path of recordValue.py
#  @param pklRelPath The relative path from recordValue.py to Copy/pkl
#  @param useCallsiteName Whether to save pkl with callsite filename
def writeRecordValue(filePath,pklRelPath,useCallsiteName):
    scriptPath=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                            'Script','recordValue.py')
    with open(scriptPath,'r',encoding='UTF-8') as fr:
        content=fr.read()
    content=content.replace("'__PCART_PKL_REL_PATH__'",repr(pklRelPath))
    content=content.replace('__PCART_USE_CALLSITE_NAME__',str(bool(useCallsiteName)))
    with open(filePath,'w',encoding='UTF-8') as fw:
        fw.write(content)


## Get source script path from PCART repository
## 获取PCART仓库中的辅助脚本路径
#
#  @param scriptName The script file name under Script/
#  @return Absolute script path
def scriptPath(scriptName):
    return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        'Script',scriptName)


## Code processing
## 代码预处理
#
#  #代码预处理目的：
#  1.修改一些动态运行的脚本
#  2.将用户代码的tab键用四个空格替换（因为不同编译器的tab键对应的空格数可能不同），再把换行写的语句集中到一行，目的是为了便于插桩处理
#  3.插入一些头文件
#  runCommand可能是 src/run.py --config json
#
#  @param projPath The project path
#  @param runCommand The run command of the project 
#  @param runPath The relative path of the run file 
#  @param libName The lib name 
def codeProcess(projPath,runCommand,runPath,libName,workspace):
    runtimePaths=getRuntimePaths(workspace)
    copyRoot=runtimePaths['copy_root']
    dynamicRoot=runtimePaths['dynamic_root']
    dataDir=runtimePaths['data_dir']
    #提取运行的文件
    runFileLst=[]
    runFile=getRunFile(runCommand)
    prefix='' #运行文件所在的目录，默认是在项目的一级子目录下
    # if '/' in runFile:
    if runFile and ('/' in runFile or '\\' in runFile):
        # prefix=runFile.rsplit('/',1)[0]
        prefix = os.path.dirname(runFile)
        # runFile=runFile.rsplit('/',1)[1] #去掉路径前缀，只保留文件名即run.py
        runFile = os.path.basename(runFile)
    if runFile:
        runFileLst.append(runFile)
    #这种情况针对于python run.py, run.py在其它目录中比如src，则prefix就是src 
    #若是python src/run.py, 则prexfix和runPath是一致的
    if runPath!='' and prefix!=runPath:
        prefix=runPath
    # projName=projPath.split('/')[-1]
    projName = os.path.basename(projPath)
    copyProjPath=os.path.join(copyRoot,projName)
    importStatement=''
    for it in runFileLst:
        # it=it.rstrip('.py') #把文件名中的后缀去掉，但遇到display.py会变成displa
        it=it[0:-3]
        importStatement+=f"from {it} import *\n"


    #找出项目中所有和第三方库相关的import语句
    libImportLst=getLibImportLst(projPath,libName)
    libImportLst.append(importStatement) 

    #清除Copy和Dynamic中遗留的项目信息，然后把新项目的信息拷贝进去
    # print(projPath)
    if os.path.isdir(copyRoot):
        shutil.rmtree(copyRoot)
    os.makedirs(os.path.dirname(copyRoot) or '.',exist_ok=True)
    shutil.copytree(projPath,os.path.join(copyRoot,projName),ignore=ignore_sym_links)
    os.mkdir(os.path.join(copyRoot,'pkl'))
    if os.path.isdir(dynamicRoot):
        shutil.rmtree(dynamicRoot)
    os.makedirs(os.path.dirname(dynamicRoot) or '.',exist_ok=True)
    shutil.copytree(projPath,os.path.join(dynamicRoot,projName),ignore=ignore_sym_links)
    
    #去掉项目代码中的冗余信息，仅保存项目代码的结构信息（import,functionDef, classDef）
    saveStructure(os.path.join(dynamicRoot,projName),libName)
    
    dynamicScriptDir=os.path.join(dynamicRoot,projName,prefix)
    shutil.copy2(scriptPath('addValueForAPI.py'),dynamicScriptDir)
    shutil.copy2(scriptPath('codeUtils.py'),dynamicScriptDir)
    shutil.copy2(scriptPath('dynamicMatch.py'),dynamicScriptDir)
    shutil.copy2(scriptPath('verifySingle.py'),dynamicScriptDir)
    
    #更新脚本中的from ... import ...语句,因为加载pkl的时候需要依赖于项目的结构信息
    modifyFromImport(os.path.join(dynamicScriptDir,'addValueForAPI.py'),libImportLst)
    modifyFromImport(os.path.join(dynamicScriptDir,'dynamicMatch.py'),libImportLst)
    modifyFromImport(os.path.join(dynamicScriptDir,'verifySingle.py'),libImportLst)
    
    #清除data中的数据
    if os.path.isdir(dataDir):
        shutil.rmtree(dataDir)
    os.makedirs(dataDir)
    
    
    #然后再把Copy中的项目制表符统一转化为空格,目的是为了插入字典的时候计算空格缩进
    convertTabsToSpaces(copyRoot)

    #把代码换行写的合成一行，并添加字典
    pathObj=Path('DF')
    pathObj.getPath(copyProjPath)
    filePath=[file for file in pathObj.path if file.endswith('.py')]
    for file in filePath:#下面的所有操作都是对项目副本进行的
        oneLine(file)
    
    #处理单行条件返回语句
    for file in filePath:
        expandConditionalReturn(file) 

    #处理局部变量
    for file in filePath:
        convertLocalVar(file,libName) 


    shutil.copytree(os.path.join(copyRoot,projName),os.path.join(copyRoot,f'bak_{projName}'))

    # 计算recordValue.py到Copy/pkl的相对路径
    pklDepth=1
    if prefix:
        pklDepth+=len([s for s in prefix.replace('\\','/').strip('/').split('/') if s])
    pklRelPath='/'.join(['..']*pklDepth+['pkl'])
    writeRecordValue(os.path.join(copyRoot,f'bak_{projName}',prefix,'recordValue.py'),pklRelPath,0)
    
    
    for file in filePath:
        addDictAll(projPath,projName,file,copyRoot,runFileLst,libName,runPath,runCommand)
    
    #再对bak_proj中的运行文件进行插桩
    for file in runFileLst:
        file=os.path.join(copyRoot,f'bak_{projName}',prefix,file)
        # print(prefix)
        handleRunFile(file,runPath,runCommand) 
    # bak项目会在current pkl生成后换回Copy/{projName}，其运行文件也依赖codeUtils
    shutil.copy2(scriptPath('codeUtils.py'),os.path.join(copyRoot,f'bak_{projName}',prefix))
    
    #处理完项目所有文件后，再给项目添加一个新的文件
    writeRecordValue(os.path.join(copyRoot,projName,prefix,'recordValue.py'),pklRelPath,1)
    
    shutil.copy2(scriptPath('codeUtils.py'),os.path.join(copyRoot,projName,runPath))
    if prefix!=runPath:
        shutil.copy2(scriptPath('codeUtils.py'),os.path.join(copyRoot,projName,prefix))
