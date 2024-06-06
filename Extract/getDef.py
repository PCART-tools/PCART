import os
import re
from Path.getPath import *
from Extract.extractDef import *
from Extract.extractCall import *
from Tool.tool import getAst

class RegexMatch:
    def __init__(self,code_text,pattern):
        self._code_text=code_text
        self._pattern=pattern
        self._result=[]

    def get_result(self):
        return self._result

    def regex_match(self):
        obj=re.compile(self._pattern,re.DOTALL)
        lst=obj.findall(self._code_text)
        if len(lst)>0:
            #对找到的所有参数字符串进行处理
            for index in range(0,len(lst)):
                if lst[index].find('\n')!=-1: #若参数字符串含有换行符'\n'
                    lst[index]=lst[index].replace('\n','') #去掉所有的换行符
                lst[index]=lst[index].replace(' ','') #去掉所有的空格
            
            self._result=lst
            return 1
        else:
            self._result=[]
            return 0



#获取.py文件的Assign语句
def getAssign(root_node):
    #找出树中所有的模块名
    import_visitor=Import()
    import_visitor.visit(root_node)
    md_names=import_visitor.get_md_name() #dict

    #找出所有的Assign节点
    assign_visitor=AssignVisitor()
    assign_visitor.visit(root_node)
    target_call=assign_visitor.get_target_call()
    
    for key,val in target_call.items():
        name_parts=val.split('.')
        if name_parts[0] in target_call:
            target_call[key]=target_call[name_parts[0]]+'.'+'.'.join(name_parts[1:])
    
    for key,val in target_call.items():
        name_parts=val.split('.')
        if name_parts[0] in md_names:
            target_call[key]=(md_names[name_parts[0]]+'.'+'.'.join(name_parts[1:])).rstrip('.')
    
    return target_call





#通过解析__init__.py,把源码中的部分API路径缩短
#缩短API路径可能会将不同文件中的API还原成相同的形式，比如A.b.f,A.c.f都还原成A.f
def shortenPath(lst,fileDict): #lst是传入传出参数，保存修正之后的API路径
    absolutePath=[k for k in fileDict.keys()][0] #pkg/file.py 
    relativePath=[v for v in fileDict.values()][0] #/home/zhang/pkg/file.py
    pos1=relativePath.rfind('/')
    if pos1==-1:
        return
    relativePath=relativePath[0:pos1] #更新relativatePath
    pos2=absolutePath.rfind('/') 
    absolutePath=absolutePath[0:pos2] #更新absolutePath,使其和relativatePath保持一致
    initPath=f"{absolutePath}/__init__.py"
    api=lst[0]
    if os.path.exists(initPath): #判断当前目录中是否有__init__.py
        try:
            root=getAst(initPath)
        except Exception as e:
            print(f"shortenPath --> ast.parse failed:{e}")
            return
        obj=FromImport()
        obj.visit(root)
        replaceKey1=''
        replaceVal1=''
        replaceKey2=''
        replaceVal2=''
        for key,value in obj.importDict.items():
            # print(key, '-->', value)
            if key[-1]=='*':
                key=key.rstrip('*')
                if key in api:
                    replaceKey1=key
                    replaceVal1=''
            elif key in api:
                # print(key,'-->', value)
                # if key.split('.')[-1]==api.split('.')[-1]: #key的最后一个字段要和api的最后一个字段相同
                replaceKey2=key
                replaceVal2=value
        if replaceKey2: #优先使用第二种替换方式
            api=api.replace(replaceKey2,replaceVal2)
        elif replaceKey1:
            api=api.replace(replaceKey1,replaceVal1)
    lst[0]=api 
    shortenPath(lst,{absolutePath:relativePath})


#递归访问类中所有节点，主要解决嵌套类的问题
def getClass(lst,root,prefix,fileDict, pyiFlag=0): #lst是传入传出参数
    className=root.name
    flagInit=0
    flagNew=0
    flagCall=0
    #首先抽取当前类中的所有函数
    for n in ast.iter_child_nodes(root): 
        if isinstance(n,ast.FunctionDef):
            if 'overload' in ast.unparse(n.decorator_list) and not pyiFlag: #非pyi文件中，遇到带有overload装饰器的就跳过
                continue
            funcName=n.name
            arg=ast.unparse(n.args) #从args节点出解析出函数参数
            arg=arg.replace(' ','') #去掉字符串中的空格
            try:
                ret='->'+ast.unparse(n.returns)
            except:
                ret=''
            if funcName=='__init__': #一个class中也可能存在多个init,即class API的重载
                init=arg
                flagInit=1
            elif funcName=='__new__':
                new=arg
                flagNew=1
            elif funcName=='__call__':
                call=arg
                flagCall=1
            else:
                lst.append(f"{prefix}.{className}.{funcName}({arg}){ret}")
                #尝试缩短API路径
                apiPath=[f"{prefix}.{className}.{funcName}"]
                flag=0
                if "click.types.Choice.convert" in apiPath:
                    # print(apiPath, fileDict)
                    flag=1
                if flag:
                    # print(apiPath)
                    # shortenPath(apiPath,fileDict,1)
                    flag=0
                else:
                    shortenPath(apiPath,fileDict)

                if apiPath[0]!=f"{prefix}.{className}.{funcName}":
                    lst.append(f"{apiPath[0]}({arg}){ret}")
     
    if flagInit==1:
        para=f"({init})"
    elif flagNew==1:#若class中不含init,再看是否有new
        para=f"({new})"
    elif flagCall==1:
        para=f"({call})"
    else: #若类中不含init,new,call,就将类的继承作为类的参数
        pattern=f"class {className}(\(.*?):" 
        codeText=ast.unparse(root)
        R=RegexMatch(codeText,pattern)
        flag=R.regex_match()
        if flag==1:
            args=R.get_result()
        else:
            args=['']
        para=args[0]
    lst.append(f"{prefix}.{className}{para}")
    
    #尝试缩短API路径
    apiPath=[f"{prefix}.{className}"]
    shortenPath(apiPath,fileDict)
    if apiPath[0]!=f"{prefix}.{className}":
        lst.append(f"{apiPath[0]}{para}")
        
    #然后再判断当前类节点下是否还有嵌套类，有的话就往下递归
    prefix+=f".{className}" #更新前缀
    for n in ast.iter_child_nodes(root):
        if isinstance(n,ast.ClassDef):
            getClass(lst,n,prefix,fileDict,pyiFlag)





def task(codeText,libApi,prefix,fileDict, pyiFlag=0): #这里的prefix只到文件名
    rootNode=ast.parse(codeText,filename='<unknown>',mode='exec')
    for node in ast.iter_child_nodes(rootNode):
        if isinstance(node, ast.ClassDef): #抽取类内API
            getClass(libApi,node,prefix,fileDict,pyiFlag)

        if isinstance(node,ast.FunctionDef): #再抽取类外的API
            if 'overload' in ast.unparse(node.decorator_list) and not pyiFlag: #遇到含overload装饰器的就跳过 
                continue
            funcName=node.name
            arg=ast.unparse(node.args)
            arg=arg.replace(' ','')
            try:
                ret='->'+ast.unparse(node.returns)
            except:
                ret=''
            libApi.append(f"{prefix}.{funcName}({arg}){ret}")
            
            #尝试缩短API路径
            lst=[f"{prefix}.{funcName}"]
            shortenPath(lst,fileDict)
            if lst[0]!=f"{prefix}.{funcName}":
                libApi.append(f"{lst[0]}({arg}){ret}")




#filePath是库下所有文件对应的路径
def get_def_function(args):
    libName, version, libPath=args
    fileObj=Path('DF')
    fileObj.getPath(libPath)
    filePath=fileObj.path
    if not os.path.exists(f"LibAPIExtraction/{libName}"):
        try:
            os.mkdir(f"LibAPIExtraction/{libName}") #多进程可能同时执行这句，所以这个结构需要修改
        except:
            pass
    f=open(f'LibAPIExtraction/{libName}/{version}','w',encoding='UTF-8')
    
    # if not os.path.exists(f"LibTest/{libName}"):
    #     try:
    #         os.mkdir(f"LibTest/{libName}")
    #     except:
    #         pass
    # f=open(f'LibTest/{libName}/{libName}{version}','w',encoding='UTF-8')
    
    fileVisitLst=[]
    for file in filePath:
        pyLst=[] #保存每个.py文件中的API
        pyiLst=[] #保存每个.pyi文件中的API
        def2format=Def2format()
        def2format.toFormat(file)
        prefix=def2format.prefix #前缀，包名.文件名
        relativePath=def2format.relativePath #相对路径，只从包名开始
        fileDict={file:relativePath}
        # print(fileDict)
        #对于每个file，首先判断一下他是.py文件还是.pyi文件
        if file[-1]=='y' and file not in fileVisitLst:
            fileVisitLst.append(file)
            #对于每一个.py文件,首先看它有没有.pyi，若无，则直接以.py中的API定义为准
            #若有，则再抽取.pyi中的API，最后保留.pyi和.py的差集
            pyiFlag=0
            if file+'i' not in fileVisitLst: #判断.pyi之前是否访问过
                try:
                    with open(file+'i','r') as fr:
                        code_text=fr.read()
                    task(code_text,pyiLst,prefix,fileDict, 1) #抽取.pyi中的API
                    pyiFlag=1
                    fileVisitLst.append(file+'i')
                except FileNotFoundError:
                    pass
        
            with open(file,'r') as fr:
                try:
                    code_text=fr.read()
                except Exception as e:
                    print(f"{file} read failed: {e}")
                    continue
            try:
                root_node=ast.parse(code_text,filename='<unknown>',mode='exec')
            except Exception as e:
                print(f'{file} ast parse falied')
                print(e)
                print('\n\n')
                continue
            assignDict=getAssign(root_node) #抽取.py中的所有Assign Node
            f.write('\n'+'-' * 40 + f"{file}" + '-' * 40+'\n')
            for key,val in assignDict.items():
                f.write(f'A:{prefix}.{key}->{val}\n')
            #抽取.py中的Definition Node
            task(code_text,pyLst,prefix,fileDict)
            pyLst.sort()
            for it in pyLst:
                f.write(f"{it}\n")
            f.write('\n') 
            
            if pyiFlag:
                removeLst=[]
                for it1 in pyiLst:
                    for it2 in pyLst:
                        if it2.split('(')[0]==it1.split('(')[0]:
                            removeLst.append(it1)
                            break
                for it in removeLst:
                    pyiLst.remove(it)
                
                #此时.pyi中保存的都是内置的API注释 
                pyiLst.sort()
                f.write('\n'+'-' * 40 + f"{file}"+'i' + '-' * 40+'\n')
                for it in pyiLst:
                    f.write(f"{it}\n")
                f.write('\n')

        elif file[-1]=='i' and file not in fileVisitLst:
            fileVisitLst.append(file)
            if file.rstrip('i') not in fileVisitLst:
                try:
                    with open(file.rstrip('i'),'r') as fr:
                        code_text=fr.read()
                    task(code_text,pyLst,prefix,fileDict) #抽取.py中的API
                    fileVisitLst.append(file.rstrip('i'))
                    root_node=ast.parse(code_text,filename='<unknown>',mode='exec')
                    assignDict=getAssign(root_node)
                    f.write('\n'+'-' * 40 + f"{file.rstrip('i')}" + '-' * 40+'\n')
                    for key,value in assignDict.items():
                        f.write(f'A:{prefix}.{key}->{value}\n')
                    pyLst.sort()
                    for it in pyLst:
                        f.write(f'{it}\n')
                    f.write('\n')
                except FileNotFoundError:
                    pass
                
            with open(file,'r') as fr:
                code_text=fr.read()
            task(code_text,pyiLst,prefix,fileDict,1) #抽取.pyi中的API
            removeLst=[]
            pyiLst.sort()
            for it1 in pyiLst:
                for it2 in pyLst:
                    if it2.split('(')[0]==it1.split('(')[0]:
                        removeLst.append(it1)
                        break
            for it in removeLst:
                pyiLst.remove(it)
                    
            f.write('\n'+'-' * 40 + f"{file}" + '-' * 40+'\n')
            for it in pyiLst:
                f.write(f'{it}\n')
            f.write('\n')

    f.close()

        