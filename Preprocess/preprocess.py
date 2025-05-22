## @package preprocess 
#  Preprocess project source files for preparing API parameter compatibility issue detection and repair   
#
#  More details (TODO)

import re
import ast
import shutil
import subprocess
from Path.getPath import *
from Extract.getCall import getCallFunction
from Extract.extractCall import WithVisitor
from Tool.tool import getAst,get_parameter,getLastAPIParameter,departAPI,departAPI2,ConditionalReturnTransformer

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



#主要是列表推导式listComp和字典推导式DictComp
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
        callLst=[callAPI.split('#_')[0] for callAPI in callDict.keys()]
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



def findAssignCall(root):
    assignLst=[]
    for node in ast.walk(root):
        if isinstance(node,ast.Assign) and isinstance(node.value,ast.Call):
            target=ast.unparse(node.targets)
            assignLst.append(target)
    return assignLst

    


#计算字符串的前面有多少个空格
def countSpace(s):
    cntSpace=0
    for it in s:
        if it==' ':
            cntSpace+=1
        else:
            break
    return cntSpace

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

#抽取项目中第三方库装饰器调用
def extractDecorator(root):
    decoratorLst = []
    for n in ast.walk(root):
        if isinstance(n, (ast.FunctionDef, ast.ClassDef)) and n.decorator_list:
            for decorator in n.decorator_list:
                if isinstance(decorator, ast.Call): # and isinstance(decorator.func.value, ast.Name):
                    decoratorLst.append(ast.unparse(decorator.func))

    return decoratorLst 



def addDictSingle(callAPI,filePath):
    with open(filePath,'r',encoding='UTF-8') as fr:
        codeLst=fr.readlines()
    
    lineno=getImportLine(codeLst)
    importDict='from recordValue import paraValueDict\n'
    codeLst.insert(lineno,importDict)
    
    paraStr=getLastAPIParameter(callAPI) #获取最后一个API的参数
    parameterLst=get_parameter(paraStr,space=0) #项目参数不去空格
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
            
            key=callAPI.replace('"','\\"')
            if firstPart and (firstPart.split('.')[0] in targetLst or firstPart.split('.')[0]=='self') and len(l)==1:
                dicString1=f'paraValueDict[\"@{key}\"]={firstPart}\n'
            elif len(l)>1: #df.a(x).b(y), np.max(...), torch.nn.Sequential(...)
                dicString1=f'paraValueDict[\"@{key}\"]={l[-2]}\n'

            #判断API是否为withitem中的别名调用 -- 2025/5/19 
            if firstPart and firstPart.split('.')[0] in withitem_call_names:
                dicString1=f'paraValueDict[\"@{key}\"]=\"{withitem_call_names[firstPart.split(".")[0]]}\"\n'
            #     dicString1=f'paraValueDict[\"@{key}\"]={firstPart}\n'
            
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
            else:
                if dicString1:
                    dicString1=dicString1.lstrip(' ')#去掉之前添加的空格，重新计算开头的空格数
                dicString2=dicString2.lstrip(' ') 
                for j in range(i+1,len(codeLst)):
                    if codeLst[j]!='\n' and '#' not in codeLst[j]:
                        spaceNum=countSpace(codeLst[j])
                        while spaceNum>0:
                            if dicString1:
                                dicString1=' '+dicString1
                            dicString2=' '+dicString2
                            spaceNum-=1
                        
                        codeLst.insert(j,dicString2)
                        if dicString1:
                            codeLst.insert(j,dicString1)
                        break

            break
        

    if codeLst[0]=='pass\n':
        codeLst=codeLst[1:]
    with open(filePath,'w',encoding='UTF-8') as fw:
        for it in codeLst:
            fw.write(it)





def addDictAll(projPath,projName,filePath,runFileLst,libName,runPath,runCommand):
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
    fileName=filePath.split('/')[-1][0:-3]
    fileRelativePath=filePath.split(f'{projName}',1)[-1]
    fileAbsolutePath=projPath+fileRelativePath
    
    lineno=getImportLine(codeLst)
    importDict='from recordValue import paraValueDict\nfrom recordValue import apiCoveredSet\n'
    codeLst.insert(lineno,importDict)
    _,callDict=getCallFunction(fileAbsolutePath,libName)

    targetLst=findAssignCall(root) #用来区分调用者是否来自赋值语句，比如a.f(), tf.f(), or self.f()
 
    #找出树中所有withitem call节点 -- 2025/5/19
    withitem_visitor = WithVisitor()
    withitem_visitor.visit(root)
    withitem_call_names = withitem_visitor.get_withitem_call() #dict

    insertStartLine=0 #记录每次插桩的行
    preInsertAPI='' #记录上一个插桩的API是哪个
    preInsertAPICount=0 #记录上一个插桩行中出现了几次被插的API
    decoratorLine = list() #记录装饰器出现的行号 -- 2025.5.12
    for callState,paraStr in callDict.items(): #key是api调用表达式，value是list,保存所有参数
        flag=0 #标记API是否找到了插桩的位置
        lineno=int(callState.split('#_')[-1]) #这个lineno是原项目中的行数
        callState=callState.split('#_')[0]
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
                key=callState.replace('"','\\"') #把字符串中的"改成\"
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
                    dicString1=f'paraValueDict[\"@{key}\"]={firstPart}\n'
                elif len(l)>1: #df.a(x).b(y), np.max(...), torch.nn.Sequential(...)
                    dicString1=f'paraValueDict[\"@{key}\"]={l[-2]}\n'
               
                #判断API是否为withitem中的别名调用 -- 2025/5/19 
                if firstPart and firstPart.split('.')[0] in withitem_call_names:
                    dicString1=f'paraValueDict[\"@{key}\"]=\"{withitem_call_names[firstPart.split(".")[0]]}\"\n'
                #     dicString1=f'paraValueDict[\"@{key}\"]={firstPart}\n'

                #再保存API的参数值
                dicString2=f'paraValueDict[\"{key}\"]=['
                paraLst=get_parameter(paraStr,space=0) #项目参数不去空格2023-12-14
                for para in paraLst: 
                    if '=' in para and "'='" not in para and '"="' not in para: #若参数的形式为key=f(x=1),只要确保=的前面不含括号即可
                        pos=para.find('=') #找到第一个=的位置,存在x=(a==b)和a==b形式
                        if '(' not in para[0:pos] and "'" not in para[0:pos] and '"' not in para[0:pos] and para[pos+1]!='=': #等号前面也不能出现引号，比如f('x= ',y=1)
                            para=para[pos+1:] #把参数的值保存下来
                    
                    para=para.lstrip('*') #有的参数会带*号，2023-12-20
                    dicString2=dicString2+para+','
                dicString2=dicString2.rstrip(',')+']\n'
                
                dicString3=f'apiCoveredSet.add(\"{fileName}##{lineno}##{key}\")\n'
                # print(f"{fileName}##{lineno}##{key}") 
                while spaceNum>0:
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
                    #记录当前插在了哪一行
                    if dicString1:
                        insertStartLine=i+3
                    else:
                        insertStartLine=i+2
                else:
                    if dicString1:
                        dicString1=dicString1.lstrip(' ') #去掉之前添加的空格，重新计算开头的空格数
                    dicString2=dicString2.lstrip(' ') 
                    dicString3=dicString3.lstrip(' ') 
                    for j in range(i+1,len(codeLst)):
                        if codeLst[j]!='\n' and '#' not in codeLst[j]:
                            spaceNum=countSpace(codeLst[j])
                            while spaceNum>0:
                                if dicString1:
                                    dicString1=' '+dicString1
                                dicString2=' '+dicString2
                                dicString3=' '+dicString3
                                spaceNum-=1
                            codeLst.insert(j,dicString3)
                            codeLst.insert(j,dicString2)
                            if dicString1:
                                codeLst.insert(j,dicString1)
                            #记录当前插在了哪一行
                            if dicString1:
                                insertStartLine=j+3
                            else:
                                insertStartLine=j+2
                            break
  
                break
            
            i+=1
        
        if flag==0:
            print(f"{fileName}#{lineno}-->{callState}\n")
            with open('66666666666.py','a') as fw:
                fw.write('\n'+fileName+'='*100+'\n')
                fw.write(f"{fileName}#{lineno}--->{callState}\n")
                for it in codeLst[insertStartLine:]:
                    fw.write(it)

    
    #最后再判断一下该文件是否为该项目的运行文件
    fileName=filePath.split('/')[-1] #fileName带.py
    if fileName in runFileLst:
        #寻找__main__所在的行
        flag=0
        spaceNum=0
        lineno=getImportLine(codeLst)
        codeLst.insert(lineno,'import dill\n')
        codeLst.insert(lineno,'from fixTool import *\n')
        mainLineno=0
        #计算__main__第一个非空行开头的空格数
        for i in range(len(codeLst)):
            if "if__name__=='__main__':" in codeLst[i].replace(' ',''):
                flag=1
                mainLineno=i 
                continue
            
            if flag:
                if codeLst[i]!='\n' and '#' not in codeLst[i]: #这个#号的判断后面可以再细致点
                    spaceNum=countSpace(codeLst[i])
                    break
        
        #再判断if __name__=='__main__'后面是否有paraValueDict
        #若有的话，找到最后一个paraValueDict的位置，然后插入保存字典的代码块
        
        index=len(codeLst)-1
        # if flag:
        #     for i in range(mainLineno,len(codeLst)):
        #         if 'paraValueDict[' in codeLst[i]:
        #             spaceNum=countSpace(codeLst[i])
        #             index=i
        
        headLst=codeLst[0:index+1]
        trailLst=codeLst[index+1:]

        pklPrefix=f"../../Copy/pkl"
        
        #当runPath不在runCommand中时，需要切换到运行文件所在的目录执行命令
        #而文件操作的相对路径就是相对于命令执行的路径
        if runPath!='' and runPath not in runCommand:
            l=len(runPath.split('/'))
            while l>0:
                pklPrefix='../'+pklPrefix
                l-=1
        
        
        s1="for key,value in paraValueDict.items():\n"
        s2="if '@' in key:\n"
        s3="continue\n"        
        s4="tempDict={}\n"
        s5="tempDict[key]=value\n"
        s6="k='@{}'.format(key)\n"
        s7="if k in paraValueDict:\n"
        s8="tempDict[k]=paraValueDict[k]\n"
        s9="pklName=getFileName(key,'.pkl')\n"
        s10="try:\n"
        s11=f"with open('{pklPrefix}"+"/{}'.format(pklName),'wb') as fw:\n"
        s12="dill.dump(tempDict,fw)\n"
        s13="except BaseException as e:\n"
        s14="print('save to pkl error: {}'.format(e))\n"
        s15=f"with open('{pklPrefix}/coverSet','w') as fw:\n"
        s16="for it in apiCoveredSet:\n"
        s17="fw.write(it+'\\n')\n"  
        #添加空格
        #spaceNum不能为0,为0的时候，这个地方会出错，后面得修改一下,一个spaceNum就是一个tab块=4空格
        if spaceNum!=0:
            s1=' '*spaceNum*1+s1
            s2=' '*spaceNum*2+s2
            s3=' '*spaceNum*3+s3
            s4=' '*spaceNum*2+s4
            s5=' '*spaceNum*2+s5
            s6=' '*spaceNum*2+s6
            s7=' '*spaceNum*2+s7
            s8=' '*spaceNum*3+s8
            s9=' '*spaceNum*2+s9
            s10=' '*spaceNum*2+s10
            s11=' '*spaceNum*3+s11
            s12=' '*spaceNum*4+s12
            s13=' '*spaceNum*2+s13
            s14=' '*spaceNum*3+s14

            s15=' '*spaceNum*1+s15
            s16=' '*spaceNum*2+s16
            s17=' '*spaceNum*3+s17
        else:
            spaceNum=4
            s2=' '*spaceNum*1+s2
            s3=' '*spaceNum*2+s3
            s4=' '*spaceNum*1+s4
            s5=' '*spaceNum*1+s5
            s6=' '*spaceNum*1+s6
            s7=' '*spaceNum*1+s7
            s8=' '*spaceNum*2+s8
            s9=' '*spaceNum*1+s9
            s10=' '*spaceNum*1+s10
            s11=' '*spaceNum*2+s11
            s12=' '*spaceNum*3+s12
            s13=' '*spaceNum*1+s13
            s14=' '*spaceNum*2+s14
            
            s16=' '*spaceNum*1+s16
            s17=' '*spaceNum*2+s17

        headLst.append(s1)
        headLst.append(s2)
        headLst.append(s3)
        headLst.append(s4)
        headLst.append(s5)
        headLst.append(s6)
        headLst.append(s7)
        headLst.append(s8)
        headLst.append(s9)
        headLst.append(s10)
        headLst.append(s11)
        headLst.append(s12)
        headLst.append(s13)
        headLst.append(s14)
        headLst.append(s15)
        headLst.append(s16)
        headLst.append(s17)

        codeLst=headLst+trailLst    
    if codeLst[0]=='pass\n':
        codeLst=codeLst[1:]
    with open(filePath,'w',encoding='UTF-8') as fw:
        for it in codeLst:
            fw.write(it)


#该函数用于动态匹配时候的时候对单个API进行插桩，除了要插桩当前文件
#还要对运行文件进行插桩,所以提前把bak_Proj中的运行文件处理好
def handleRunFile(file,runPath,runCommand):
    with open(file,'r',encoding='UTF-8') as fr:
        codeLst=fr.readlines()
    lineno=getImportLine(codeLst)
    codeLst.insert(lineno,f"from recordValue import paraValueDict\n")
    codeLst.insert(lineno,'import dill\n')
    #寻找__main__所在的行
    flag=0
    spaceNum=0
    mainLineno=0
    #计算__main__第一个非空行开头的空格数
    for i in range(len(codeLst)):
        if "if__name__=='__main__':" in codeLst[i].replace(' ',''):
            flag=1
            mainLineno=i
            continue
    
        if flag:
            if codeLst[i]!='\n' and '#' not in codeLst[i]: #这个#号的判断后面可以再细致点
                spaceNum=countSpace(codeLst[i])
                break
    
    #再判断if __name__=='__main__'后面是否有paraValueDict
    #若有的话，找到最后一个paraValueDict的位置，然后插入保存字典的代码块
    index=len(codeLst)-1
    for i in range(mainLineno,len(codeLst)):
        if 'paraValueDict[' in codeLst[i]:
            index=i
    
    headLst=codeLst[0:index+1]
    trailLst=codeLst[index+1:]

    #当runPath不在runCommand中时，需要切换到运行文件所在的目录执行命令
    #而文件操作的相对路径就是相对于命令执行的路径
    pklPrefix=f"../../Copy/pkl"
    if runPath!='' and runPath not in runCommand:
        l=len(runPath.split('/'))
        while l>0:
            pklPrefix='../'+pklPrefix
            l-=1
    s1="try:\n"
    s2=f"with open('{pklPrefix}/paraValue.pkl','wb') as fw:\n"
    s3="dill.dump(paraValueDict,fw)\n"
    s4="except Exception as e:\n"
    s5="print('save to pkl error: {}'.format(e))\n"
    #spaceNum不能为0
    if spaceNum: 
        s1=' '*spaceNum*1+s1
        s2=' '*spaceNum*2+s2
        s3=' '*spaceNum*3+s3
        s4=' '*spaceNum*1+s4
        s5=' '*spaceNum*2+s5       
    else:
        spaceNum=4
        s1=' '*spaceNum*0+s1
        s2=' '*spaceNum*1+s2
        s3=' '*spaceNum*2+s3
        s4=' '*spaceNum*0+s4
        s5=' '*spaceNum*1+s5       


    headLst.append(s1)
    headLst.append(s2)
    headLst.append(s3)
    headLst.append(s4)
    headLst.append(s5)

    codeLst=headLst+trailLst

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




def modifyFromImport(filePath,importStatement):
    with open(filePath,'r') as fr:
        codeLst=fr.readlines()

    s='\n'.join(importStatement)+'\n'
    # print(s)
    codeLst.insert(0,s)
    with open(filePath,'w') as fw:
        for it in codeLst:
            fw.write(it)



#保存项目的结构信息
def saveStructure(projPath,libName):
    pathObj=Path('DF')
    pathObj.getPath(projPath)
    filePath=[it for it in pathObj.path if it.endswith('py')]
    for file in filePath:
        _,callDict=getCallFunction(file,libName)
        callLst=[callAPI.split('#_')[0] for callAPI in callDict.keys()] #去掉API中的行号信息
        with open(file,'r') as fr:
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
        for node in root.body:
            # if isinstance(node,ast.Expr) or isinstance(node,ast.Assign) or isinstance(node,ast.If):
            #     continue
            #if isinstance(node,ast.Import) or isinstance(node,ast.ImportFrom) or isinstance(node,ast.ClassDef) or isinstance(node,ast.FunctionDef):
            
            #增加AsyncFunctionDef节点信息保存 -- 2025/5/19 
            if isinstance(node,ast.Import) or isinstance(node,ast.ImportFrom) or isinstance(node,ast.ClassDef) or isinstance(node,ast.FunctionDef) or isinstance(node,ast.AsyncFunctionDef):
                newBody.append(node)


            #保留不含第三方库调用的赋值语句
            # if isinstance(node,ast.Assign):
            #     flag=0
            #     for n in ast.walk(node):
            #         if isinstance(n,ast.Call):
            #             callState=ast.unparse(n)
            #             callState=callState.replace(' ','').replace('"','').replace("'",'')
            #             for it in callLst:
            #                 if callState==it.replace(' ','').replace('"','').replace("'",''):
            #                     flag=1
            #                     break
            #             if flag==1:
            #                 break
            #     if flag==1:
            #         continue
            #     newBody.append(node) 
            
            #保留包含常量的赋值语句和装饰器调用相关的赋值语句，例如:
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
                flag = 0
                for n in ast.walk(node):
                    if isinstance(n,ast.Assign):
                        value = n.value
                        valueAstContent = ast.dump(n.value)
                        targetAstContent = ast.dump(n.targets[0])
                        #如果赋值语句的变量名在装饰器列表中出现过，则保留该赋值语句 2025.5.13 
                        if isinstance(n.targets[0], ast.Name):
                            varName = n.targets[0].id
                            if any(varName in decorator.split('.') for decorator in decoratorLst):
                                continue
                        if isinstance(value, ast.Constant):
                            pattern = r"id='([^']*)'"
                            targetMatches = re.findall(pattern, targetAstContent)
                            if targetMatches[0] in nonConstantVar:
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
             
                if flag==1:
                    continue
                newBody.append(node)
    
        root.body=newBody
        newFile=ast.unparse(root)
        with open(file,'w',encoding='utf-8') as fw:
            fw.write(f"{newFile}\n")




def ignore_sym_links(directory, files):
    return [f for f in files if os.path.islink(os.path.join(directory, f))]


def getLibImportLst(projPath,libName):
    lst=[]
    pathObj=Path('DF')
    pathObj.getPath(projPath)
    filePath=[file for file in pathObj.path if file.endswith('.py')]
    pattern=rf"(from {libName}|import {libName})" #确保库的前面不会出现其它字符
    for file in filePath:#下面的所有操作都是对项目副本进行的
        with open(file,'r') as fr:
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



#代码预处理目的：
#1.修改一些动态运行的脚本
#2.将用户代码的tab键用四个空格替换（因为不同编译器的tab键对应的空格数可能不同），再把换行写的语句集中到一行，目的是为了便于插桩处理
#3.插入一些头文件
# runCommand可能是 src/run.py --config json
def codeProcess(projPath,runCommand,runPath,libName):
    #提取运行的文件
    runFileLst=[]
    temp=runCommand.split(' ') #把命令按空格拆分
    runFile=temp[1]
    prefix='' #运行文件所在的目录，默认是在项目的一级子目录下
    if '/' in runFile:
        prefix=runFile.rsplit('/',1)[0]
        runFile=runFile.rsplit('/',1)[1] #去掉路径前缀，只保留文件名即run.py
    runFileLst.append(runFile)
    #这种情况针对于python run.py, run.py在其它目录中比如src，则prefix就是src 
    #若是python src/run.py, 则prexfix和runPath是一致的
    if runPath!='' and prefix!=runPath:
        prefix=runPath
    projName=projPath.split('/')[-1]
    copyProjPath=f"Copy/{projName}"
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
    if not os.path.isdir('Copy'):
        os.mkdir('Copy') 
    shutil.rmtree('Copy')
    shutil.copytree(projPath,f'Copy/{projName}',ignore=ignore_sym_links)
    os.mkdir('Copy/pkl')
    if not os.path.isdir('Dynamic'):
        os.mkdir('Dynamic') 
    shutil.rmtree('Dynamic')
    shutil.copytree(projPath,f'Dynamic/{projName}',ignore=ignore_sym_links)
    
    #去掉项目代码中的冗余信息，仅保存项目代码的结构信息（import,functionDef, classDef）
    saveStructure(f'Dynamic/{projName}',libName) 
    
    shutil.copy2('Script/addValueForAPI.py',f'Dynamic/{projName}/{prefix}')
    shutil.copy2('Script/dynamicMatch.py',f'Dynamic/{projName}/{prefix}')
    shutil.copy2('Verify/verifySingle.py',f'Dynamic/{projName}/{prefix}')
    
    #更新脚本中的from ... import ...语句,因为加载pkl的时候需要依赖于项目的结构信息
    modifyFromImport(f'Dynamic/{projName}/{prefix}/addValueForAPI.py',libImportLst)
    modifyFromImport(f'Dynamic/{projName}/{prefix}/dynamicMatch.py',libImportLst)
    modifyFromImport(f'Dynamic/{projName}/{prefix}/verifySingle.py',libImportLst)
    
    #情况data中的数据
    if not os.path.isdir('data'):
        os.mkdir('data') 
    shutil.rmtree('data')
    os.mkdir('data')
    
    
    #然后再把Copy中的项目制表符统一转化为空格,目的是为了插入字典的时候计算空格缩进
    command2=f'bash Preprocess/tab2space.sh;'
    subprocess.run(command2,shell=True,executable='/bin/bash')

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


    shutil.copytree(f'Copy/{projName}',f'Copy/bak_{projName}')
    with open(f"Copy/bak_{projName}/{prefix}/recordValue.py",'w') as fw:
        fw.write('paraValueDict={}\n')
        fw.write('apiCoveredSet=set()\n') 
    
    
    for file in filePath:
        addDictAll(projPath,projName,file,runFileLst,libName,runPath,runCommand)
    
    #再对bak_proj中的运行文件进行插桩
    for file in runFileLst:
        file=f'Copy/bak_{projName}/{prefix}/'+file
        # print(prefix)
        handleRunFile(file,runPath,runCommand) 
    
    #处理完项目所有文件后，再给项目添加一个新的文件
    with open(f"Copy/{projName}/{prefix}/recordValue.py",'w') as fw:
        fw.write('paraValueDict={}\n')
        fw.write('apiCoveredSet=set()\n')
    
    shutil.copy2('Tool/fixTool.py',f'Copy/{projName}/{runPath}') 
