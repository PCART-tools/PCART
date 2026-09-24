## @package getDef 
#  Extract API definitions from lib source code 
#
#
#  Extracts API definitions from library source files by parsing AST for class
#  definitions, function definitions, and __init__.py assignment aliases. Handles
#  .py/.pyi deduplication and API path shortening via __init__.py imports.
#  通过解析AST提取库源码中的类定义、函数定义和__init__.py赋值别名。处理.py/.pyi
#  去重，通过__init__.py导入缩短API路径。



import ast
import io
import os
import re
import tokenize
from Path.getPath import *
from Extract.extractDef import *
from Extract.extractCall import *


## Parse library source with supported legacy syntax in the Python 3.9 runtime
## 在Python 3.9环境中解析含有受支持旧语法的库源码
#  @param source Library source code
#  @param filename Source filename for syntax errors
#  @return Parsed AST with the original names restored
def parseLibrarySource(source,filename='<unknown>'):
    replacements={}
    docstrings=[]
    python2Tried=False
    while True:
        try:
            try:
                # Use the memory source for error positions instead of the disk file.
                # 按内存源码定位语法错误，避免Python 3.9回读磁盘原文。
                root=ast.parse(source,filename='<unknown>',mode='exec')
            except SyntaxError:
                # Use the old grammar to preserve async/await identifiers.
                # 使用旧语法保留async/await名称，不替换真正的关键字。
                root=ast.parse(source,filename='<unknown>',mode='exec',feature_version=(3,6))
            break
        except SyntaxError as error:
            error.filename=filename
            lines=io.StringIO(source).readlines()
            try:
                tokens=list(tokenize.generate_tokens(io.StringIO(source).readline))
            except (tokenize.TokenError,IndentationError):
                raise error

            if error.lineno and error.offset and error.lineno<=len(lines):
                line=lines[error.lineno-1]
                offset=error.offset-1
                token=next((it for it in tokens if it.type==tokenize.NAME and
                            it.start==(error.lineno,offset)),None)
                if token and token.string in ('True','False'):
                    placeholder=f'__pcart_keyword_{len(replacements)}__'
                    while placeholder in source:
                        placeholder+='_'
                    replacements[placeholder]=token.string
                    lines[error.lineno-1]=line[:offset]+placeholder+line[token.end[1]:]
                    source=''.join(lines)
                    continue

            if isinstance(error,TabError):
                # Expand code indentation using Python 2's eight-column rule.
                # 按Python 2的八列规则展开代码缩进，保留多行字符串内容。
                stringRows={row for token in tokens if token.type==tokenize.STRING
                            for row in range(token.start[0]+1,token.end[0]+1)}
                for row,line in enumerate(lines,1):
                    if row not in stringRows:
                        prefix=re.match(r'[ \t]*',line).group()
                        lines[row-1]=prefix.expandtabs(8)+line[len(prefix):]
                converted=''.join(lines)
                if converted!=source:
                    source=converted
                    continue

            if 'unicodeescape' in error.msg:
                # Plain Python 2 docstrings leave Unicode-only escapes literal.
                # 仅处理Python 2普通文档字符串中的Unicode专用转义。
                statement=[]
                for token in tokens:
                    if token.type in (tokenize.NL,tokenize.COMMENT,tokenize.INDENT,tokenize.DEDENT):
                        continue
                    if token.type==tokenize.NEWLINE or token.string==';':
                        if statement[:3]==['from','__future__','import'] and 'unicode_literals' in statement:
                            raise error
                        statement=[]
                    else:
                        statement.append(token.string)
                for i,token in enumerate(tokens):
                    if (token.type!=tokenize.STRING or not token.string.startswith(('"',"'")) or
                            not token.start[0]<=error.lineno<=token.end[0]):
                        continue
                    previous=i-1
                    while previous>=0 and tokens[previous].type in (tokenize.NL,tokenize.COMMENT):
                        previous-=1
                    following=i+1
                    while following<len(tokens) and tokens[following].type in (tokenize.NL,tokenize.COMMENT):
                        following+=1
                    if ((previous>=0 and tokens[previous].type not in (tokenize.NEWLINE,tokenize.INDENT) and
                         tokens[previous].string!=':') or following>=len(tokens) or
                            tokens[following].type not in (tokenize.NEWLINE,tokenize.ENDMARKER)):
                        continue
                    converted=re.sub(r'(\\+)([uUN])',
                                     lambda it: it[1]+('\\' if len(it[1])%2 else '')+it[2],token.string)
                    if converted==token.string:
                        continue
                    startRow,startColumn=token.start
                    endRow,endColumn=token.end
                    source=(''.join(lines[:startRow-1])+lines[startRow-1][:startColumn]+
                            converted+lines[endRow-1][endColumn:]+''.join(lines[endRow:]))
                    docstrings.append((startRow,converted,error))
                    break
                else:
                    raise error
                continue

            if error.msg=='Generator expression must be parenthesized' and error.lineno:
                brackets=[]
                for i,token in enumerate(tokens):
                    if token.type==tokenize.NAME and token.string=='for' and brackets:
                        brackets[-1][1]=True
                    if token.type!=tokenize.OP:
                        continue
                    if token.string in '([{':
                        brackets.append([token.string,False,token.start[0]])
                    elif token.string in ')]}':
                        if brackets:
                            brackets.pop()
                    elif (token.string==',' and brackets and brackets[-1][:2]==['(',True] and
                          brackets[-1][2]<=error.lineno<=token.start[0]):
                        nextToken=i+1
                        while nextToken<len(tokens) and tokens[nextToken].type in (tokenize.NL,tokenize.COMMENT):
                            nextToken+=1
                        if nextToken<len(tokens) and tokens[nextToken].string==')':
                            row,column=token.start
                            lines[row-1]=lines[row-1][:column]+lines[row-1][column+1:]
                            source=''.join(lines)
                            break
                else:
                    raise error
                continue

            # Only run the three syntax fixers needed by old library sources.
            # 仅使用旧库源码所需的三种Python 2语法转换。
            python2Pattern=r'(?m)^\s*(?:print\s+(?!\()|exec\s+(?!\()|except\s+[^:\n]+,\s*\w+\s*:)'
            if not python2Tried and re.search(python2Pattern,source):
                python2Tried=True
                try:
                    from lib2to3.refactor import RefactoringTool
                    fixers=['lib2to3.fixes.fix_print','lib2to3.fixes.fix_except','lib2to3.fixes.fix_exec']
                    text=source if source.endswith('\n') else source+'\n'
                    converted=str(RefactoringTool(fixers).refactor_string(text,filename))
                except Exception:
                    raise error
                if converted!=source:
                    source=converted
                    continue
            raise error

    # Check that every repaired string is a real module, class or function docstring.
    # 确认修复的字符串确实是模块、类或函数的文档字符串。
    positions=set()
    for node in ast.walk(root) if docstrings else ():
        if isinstance(node,(ast.Module,ast.ClassDef,ast.FunctionDef,ast.AsyncFunctionDef)) and node.body:
            first=node.body[0]
            if isinstance(first,ast.Expr) and isinstance(first.value,ast.Constant) and isinstance(first.value.value,str):
                positions.add((first.value.lineno,ast.get_source_segment(source,first.value)))
    for row,text,error in docstrings:
        if (row,text) not in positions:
            raise error

    if not replacements:
        return root

    # Restore original names so extracted API paths and signatures are unchanged.
    for node in ast.walk(root):
        for field,value in ast.iter_fields(node):
            if isinstance(value,str):
                for placeholder,original in replacements.items():
                    value=value.replace(placeholder,original)
                setattr(node,field,value)
            elif isinstance(value,list):
                for i,item in enumerate(value):
                    if isinstance(item,str):
                        for placeholder,original in replacements.items():
                            item=item.replace(placeholder,original)
                        value[i]=item
    return root



## Regular expression match class 
## 正则表达式匹配类
#
#  Match a given pattern from code text
class RegexMatch:
    
    ## The constructor
    ## 构造函数
    #  @param code_text Source code text to search
    #  @param pattern Regular expression pattern
    def __init__(self,code_text,pattern):
        self._code_text=code_text
        self._pattern=pattern
        self._result=[]

    ## Return the match result
    ## 返回匹配结果
    #  @return List of regex match results
    def get_result(self):
        return self._result

    ## Perform the regular expression match
    ## 执行正则表达式匹配
    #  @return 1 if a match is found, otherwise 0
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



## Extract all assign node from a .py file's AST
## 通过AST获取.py文件的Assign语句
#
#  @param root_node The ast node of the .py file
#  @param filePath Source filename for diagnostics
def getAssign(root_node,filePath=None):
    #找出树中所有的模块名
    import_visitor=Import()
    try:
        # Preserve NodeVisitor's depth-first order without recursive calls.
        nodes=[root_node]
        while nodes:
            node=nodes.pop()
            if isinstance(node,(ast.Import,ast.ImportFrom)):
                import_visitor.visit(node)
            nodes.extend(reversed(list(ast.iter_child_nodes(node))))
    except Exception as e:
        print(f"{filePath or '<unknown>'} import visit failed: {e}")
    md_names=import_visitor.get_md_name() #dict

    #找出所有的Assign节点
    assign_visitor=AssignVisitor()
    nodes=[root_node]
    while nodes:
        node=nodes.pop()
        if isinstance(node,ast.Assign):
            assign_visitor.visit(node)
        nodes.extend(reversed(list(ast.iter_child_nodes(node))))
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



## Shorten the API path based on __init__.py and import alias 
## 通过解析__init__.py和import别名,把源码中的部分API路径缩短
#
#  缩短API路径可能会将不同文件中的API还原成相同的形式，比如A.b.f,A.c.f都还原成A.f
#
#  @param lst An API path. Initially, lst is the fully qualified API name. 
#  @param fileDict A file with a dictionary format {absolute path of the file: relative path of the file}. The relative path begins with the lib name, separated by "/", e.g., lib/a/b/c.py 
#  @param importCache Cache of __init__.py import mappings, keyed by (init path, current level).
def shortenPath(lst,fileDict,importCache=None): #lst是传入传出参数，保存修正之后的API路径
    absolutePath=[k for k in fileDict.keys()][0] #/home/zhang/pkg/file.py
    relativePath=[v for v in fileDict.values()][0] #pkg/file.py
    norm_relative=relativePath.replace('\\','/')
    norm_absolute=absolutePath.replace('\\','/')
    pos1=norm_relative.rfind('/')
    if pos1==-1:
        return
    relativePath=relativePath[0:pos1] #更新relativatePath
    pos2=norm_absolute.rfind('/')
    absolutePath=absolutePath[0:pos2] #更新absolutePath,使其和relativatePath保持一致
    initPath=f"{absolutePath}/__init__.py"
    api=lst[0]
    if os.path.exists(initPath): #判断当前目录中是否有__init__.py
        currentLevel=relativePath.replace('\\','/').split('/')[-1]
        cacheKey=(initPath,currentLevel)
        if importCache is not None and cacheKey in importCache:
            importDict=importCache[cacheKey]
        else:
            try:
                with tokenize.open(initPath) as f:
                    root=parseLibrarySource(f.read(),initPath)
            except Exception as e:
                print(f"shortenPath --> ast.parse failed: {e}")
                return
            obj=FromImport(currentLevel)
            obj.visit(root)
            importDict=obj.importDict
            if importCache is not None:
                importCache[cacheKey]=importDict
        replaceKey1=''
        replaceVal1=''
        replaceKey2=''
        replaceVal2=''
        packagePrefix=relativePath.replace('\\','/').replace('/','.')+'.'
        for key,value in importDict.items():
            if key[-1]=='*':
                key=packagePrefix+key[:-1]
                if api.startswith(key):
                    replaceKey1=key
                    replaceVal1=packagePrefix
            else:
                key=packagePrefix+key
                #只替换当前包下完整的导出路径，避免匹配同名前缀或其他模块
                if api==key or api.startswith(key+'.'):
                    replaceKey2=key
                    replaceVal2=packagePrefix+value
        if replaceKey2: #优先使用第二种替换方式
            api=replaceVal2+api[len(replaceKey2):]
        elif replaceKey1:
            api=replaceVal1+api[len(replaceKey1):]
    lst[0]=api 
    shortenPath(lst,{absolutePath:relativePath},importCache)



## Build the re-export mapping of library API definitions
## 构建库API定义的重导出映射
#
#  Scan module-level FromImport nodes in all __init__.py files and map source
#  definition paths to their package export paths.
#  扫描所有__init__.py中的模块级FromImport节点，建立源码定义路径到包导出路径的映射。
#
#  @param filePath All Python source files under the library package
#  @return A dictionary mapping source definition paths to package export paths
def getExportMap(filePath):
    exportMap={}
    for file in filePath:
        #只处理包初始化文件，函数内部导入和普通源码文件不属于包重导出
        if os.path.basename(file)!='__init__.py':
            continue

        #根据__init__.py路径得到当前导出包名
        def2format=Def2format()
        def2format.toFormat(file)
        package=def2format.prefix.rsplit('.__init__',1)[0]
        packageParts=package.split('.')
        try:
            with tokenize.open(file) as f:
                root=parseLibrarySource(f.read(),file)
        except Exception as e:
            print(f"getExportMap --> ast.parse failed: {e}")
            continue

        #只访问模块顶层节点，避免把函数或类中的局部导入识别为包导出
        for node in root.body:
            if not isinstance(node,ast.ImportFrom):
                continue

            #将绝对导入和相对导入统一还原为完整源码路径
            if node.level==0:
                module=node.module or ''
            else:
                parentCount=node.level-1
                if parentCount>len(packageParts):
                    continue
                moduleParts=packageParts[:len(packageParts)-parentCount]
                if node.module:
                    moduleParts.extend(node.module.split('.'))
                module='.'.join(moduleParts)

            for name in node.names:
                #星号导入无法静态确定具体导出对象，暂不处理
                if name.name=='*':
                    continue
                sourcePath='.'.join(it for it in (module,name.name) if it)
                publicPath=f"{package}.{name.asname or name.name}"
                if sourcePath and sourcePath!=publicPath:
                    exportMap.setdefault(sourcePath,set()).add(publicPath)
    return exportMap



## Get all available paths of a library API definition
## 获取库API定义的所有可用路径
#
#  Preserve the original path, reuse shortenPath for parent package aliases,
#  and expand transitive package re-exports on demand.
#  保留原始路径，复用shortenPath处理父包别名，并按需展开多级包重导出路径。
#
#  @param apiPath The original fully qualified API path
#  @param fileDict The absolute and relative paths of the source file
#  @param importCache Cache of __init__.py import mappings used by shortenPath
#  @param exportMap Reverse mapping from definition paths to package export paths
#  @return A list containing the original path and all resolved alias paths
def getApiPaths(apiPath,fileDict,importCache=None,exportMap=None):
    paths=[apiPath]
    #保留现有父目录__init__.py路径缩短结果
    shortenedPath=[apiPath]
    shortenPath(shortenedPath,fileDict,importCache)
    if shortenedPath[0] not in paths:
        paths.append(shortenedPath[0])

    #按需展开多级重导出，paths同时记录已访问路径以防止循环
    index=0
    while index<len(paths):
        currentPath=paths[index]
        for publicPath in sorted((exportMap or {}).get(currentPath,set())):
            if publicPath not in paths:
                paths.append(publicPath)
        index+=1
    return paths



## Extract class method definitions from a give class.
## 抽取类中方法定义。递归访问类中所有节点，主要解决嵌套类的问题
#
#  @param lst List of lib API definitions extracted from a lib source file 
#  @param root The class type ast node
#  @param prefix The fully qualified name of a source file. For example, the prefix for lib/a/b/c.py is lib.a.b.c.
#  @param fileDict A file with a dictionary format {absolute path of the file: relative path of the file}. The relative path begins with the lib name, separated by "/", e.g., lib/a/b/c.py 
#  @param pyiFlag A flag denotes whether the Python source file is .pyi file.
#  @param importCache Cache of __init__.py import mappings used to shorten API paths.
#  @param exportMap Reverse mapping from definition paths to package re-export paths.
def getClass(lst,root,prefix,fileDict, pyiFlag=0, importCache=None, exportMap=None): #lst是传入传出参数
    className=root.name
    classPath=f"{prefix}.{className}"
    #类的导出路径同样适用于其构造方法和普通方法
    classPaths=getApiPaths(classPath,fileDict,importCache,exportMap)
    flagInit=0
    flagNew=0
    flagCall=0
    #首先抽取当前类中的所有函数
    for n in ast.iter_child_nodes(root): 
        #if isinstance(n,ast.FunctionDef):
        # Add the support of extracting AsyncFunctionDef type node -- 2025/5/19
        if isinstance(n,(ast.FunctionDef, ast.AsyncFunctionDef)):
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
                methodPath=f"{classPath}.{funcName}"
                methodPaths=getApiPaths(methodPath,fileDict,importCache,exportMap)
                for currentClassPath in classPaths:
                    publicMethodPath=f"{currentClassPath}.{funcName}"
                    if publicMethodPath not in methodPaths:
                        methodPaths.append(publicMethodPath)
                for currentMethodPath in methodPaths:
                    lst.append(f"{currentMethodPath}({arg}){ret}")
     
    if flagInit==1:
        para=f"({init})"
        specialMethod='__init__'
    elif flagNew==1:#若class中不含init,再看是否有new
        para=f"({new})"
        specialMethod='__new__'
    elif flagCall==1:
        para=f"({call})"
        specialMethod='__call__'
    else: #若类中不含init,new,call,就将类的继承作为类的参数
        specialMethod=''
        pattern=fr"class {re.escape(className)}(\(.*?):"
        codeText=ast.unparse(root)
        R=RegexMatch(codeText,pattern)
        flag=R.regex_match()
        if flag==1:
            args=R.get_result()
        else:
            args=['']
        para=args[0]
    for currentClassPath in classPaths:
        if specialMethod:
            lst.append(f"{currentClassPath}.{specialMethod}{para}")
        lst.append(f"{currentClassPath}{para}")
        
    #然后再判断当前类节点下是否还有嵌套类，有的话就往下递归
    prefix+=f".{className}" #更新前缀
    for n in ast.iter_child_nodes(root):
        if isinstance(n,ast.ClassDef):
            getClass(lst,n,prefix,fileDict,pyiFlag,importCache,exportMap)



## Extract all lib API definitions from a source file
## 抽取库源码API定义任务
#
#  @param codeText The code text of a source file, read by f.read()
#  @param libApi List of lib API definitions extracted from a lib source file 
#  @param prefix The fully qualified name of a source file. For example, the prefix for lib/a/b/c.py is lib.a.b.c.
#  @param fileDict A file with a dictionary format {absolute path of the file: relative path of the file}. The relative path begins with the lib name, separated by "/", e.g., lib/a/b/c.py 
#  @param pyiFlag A flag denotes whether the Python source file is .pyi file.
#  @param importCache Cache of __init__.py import mappings used to shorten API paths.
#  @param exportMap Reverse mapping from definition paths to package re-export paths.
def task(codeText,libApi,prefix,fileDict, pyiFlag=0, importCache=None, exportMap=None): #这里的prefix只到文件名
    try:
        rootNode=parseLibrarySource(codeText,list(fileDict.keys())[0])
    except Exception as e:
        file = list(fileDict.keys())[0]
        print(f"{file} ast.parse falied: {e}")
        return
    for node in ast.iter_child_nodes(rootNode):
        if isinstance(node, ast.ClassDef): #抽取类内API
            getClass(libApi,node,prefix,fileDict,pyiFlag,importCache,exportMap)

        #if isinstance(node,ast.FunctionDef): #再抽取类外的API
        # Add the support of extracting AsyncFunctionDef type node -- 2025/5/19
        if isinstance(node,(ast.FunctionDef, ast.AsyncFunctionDef)):
            if 'overload' in ast.unparse(node.decorator_list) and not pyiFlag: #遇到含overload装饰器的就跳过 
                continue
            funcName=node.name
            arg=ast.unparse(node.args)
            arg=arg.replace(' ','')
            try:
                ret='->'+ast.unparse(node.returns)
            except:
                ret=''
            apiPath=f"{prefix}.{funcName}"
            for currentPath in getApiPaths(apiPath,fileDict,importCache,exportMap):
                libApi.append(f"{currentPath}({arg}){ret}")



## Return a public alias line for source-root API lines
## 为源码根路径API行生成公开路径别名
#
#  @param line A lib API output line
#  @param sourceRoot The source package root name, e.g., tensorflow_core
#  @param publicRoot The public package root name, e.g., tensorflow
def getPublicAliasLine(line,sourceRoot,publicRoot):
    if not sourceRoot or not publicRoot:
        return None
    sourcePrefix=sourceRoot+'.'
    publicPrefix=publicRoot+'.'
    assignSourcePrefix='A:'+sourcePrefix
    assignPublicPrefix='A:'+publicPrefix
    if line.startswith(sourcePrefix):
        return publicPrefix+line[len(sourcePrefix):]
    if line.startswith(assignSourcePrefix):
        return assignPublicPrefix+line[len(assignSourcePrefix):]
    return None



## Write one lib API line and its public alias if needed
## 写出一行库API，并按需写出公开路径别名
#
#  @param fw Output file object
#  @param line A lib API output line
#  @param sourceRoot The source package root name
#  @param publicRoot The public package root name
def writeApiLine(fw,line,sourceRoot='',publicRoot=''):
    fw.write(f"{line}\n")
    aliasLine=getPublicAliasLine(line,sourceRoot,publicRoot)
    if aliasLine and aliasLine!=line:
        fw.write(f"{aliasLine}\n")



## Extract all lib API definitions from a specified version
## 抽取给定版本的库API定义
#
#  @param args The arguments include the lib name, lib version, and the lib path 
def getDefFunction(args):
    libName, version, libPath=args
    fileObj=Path('DF')
    fileObj.getPath(libPath)
    #filePath是库下所有文件对应的路径
    filePath=fileObj.path
    if not os.path.exists(f"LibAPIExtraction/{libName}"):
        try:
            os.mkdir(f"LibAPIExtraction/{libName}") #多进程可能同时执行这句，所以这个结构需要修改
        except:
            pass
    f=open(f'LibAPIExtraction/{libName}/{libName}{version}','w',encoding='UTF-8')
    
    
    fileVisitLst=[]
    importCache={}
    #在逐文件抽取定义前统一构建重导出映射，避免对每个API重复扫描
    exportMap=getExportMap(filePath)
    publicAliasSource=''
    publicAliasTarget=''
    if libName=="tensorflow" and os.path.basename(os.path.normpath(libPath))=="tensorflow_core":
        publicAliasSource="tensorflow_core"
        publicAliasTarget="tensorflow"
    for file in filePath:
        pyLst=[] #保存每个.py文件中的API
        pyiLst=[] #保存每个.pyi文件中的API
        def2format=Def2format()
        def2format.toFormat(file)
        prefix=def2format.prefix #前缀，包名.文件名
        relativePath=def2format.relativePath #相对路径，只从包名开始
        fileDict={file:relativePath}
        #对于每个file，首先判断一下他是.py文件还是.pyi文件
        if file[-1]=='y' and file not in fileVisitLst:
            fileVisitLst.append(file)
            #对于每一个.py文件,首先看它有没有.pyi，若无，则直接以.py中的API定义为准
            #若有，则再抽取.pyi中的API，最后保留.pyi和.py的差集
            pyiFlag=0
            if file+'i' not in fileVisitLst: #判断.pyi之前是否访问过
                try:
                    with tokenize.open(file+'i') as fr:
                        code_text=fr.read()
                    task(code_text,pyiLst,prefix,fileDict, 1, importCache,exportMap) #抽取.pyi中的API
                    pyiFlag=1
                    fileVisitLst.append(file+'i')
                except FileNotFoundError:
                    pass
        
            with tokenize.open(file) as fr:
                try:
                    code_text=fr.read()
                except Exception as e:
                    print(f"{file} read failed: {e}")
                    continue
            try:
                root_node=parseLibrarySource(code_text,file)
            except Exception as e:
                print(f'{file} ast.parse failed: {e}')
                continue
            assignDict=getAssign(root_node,file) #抽取.py中的所有Assign Node
            f.write('\n'+'-' * 40 + f"{file}" + '-' * 40+'\n')
            for key,val in assignDict.items():
                writeApiLine(f,f'A:{prefix}.{key}->{val}',publicAliasSource,publicAliasTarget)
            #抽取.py中的Definition Node
            task(code_text,pyLst,prefix,fileDict,0,importCache,exportMap)
            pyLst=sorted(set(pyLst)) #按完整定义去重，保留不同签名
            for it in pyLst:
                writeApiLine(f,it,publicAliasSource,publicAliasTarget)
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
                pyiLst=sorted(set(pyiLst))
                f.write('\n'+'-' * 40 + f"{file}"+'i' + '-' * 40+'\n')
                for it in pyiLst:
                    writeApiLine(f,it,publicAliasSource,publicAliasTarget)
                f.write('\n')

        elif file[-1]=='i' and file not in fileVisitLst:
            fileVisitLst.append(file)
            if file.rstrip('i') not in fileVisitLst:
                try:
                    with tokenize.open(file.rstrip('i')) as fr:
                        code_text=fr.read()
                    task(code_text,pyLst,prefix,fileDict,0,importCache,exportMap) #抽取.py中的API
                    fileVisitLst.append(file.rstrip('i'))
                    root_node=parseLibrarySource(code_text,file.rstrip('i'))
                    assignDict=getAssign(root_node,file.rstrip('i'))
                    f.write('\n'+'-' * 40 + f"{file.rstrip('i')}" + '-' * 40+'\n')
                    for key,value in assignDict.items():
                        writeApiLine(f,f'A:{prefix}.{key}->{value}',publicAliasSource,publicAliasTarget)
                    pyLst=sorted(set(pyLst))
                    for it in pyLst:
                        writeApiLine(f,it,publicAliasSource,publicAliasTarget)
                    f.write('\n')
                except FileNotFoundError:
                    pass
                
            with tokenize.open(file) as fr:
                code_text=fr.read()
            task(code_text,pyiLst,prefix,fileDict,1,importCache,exportMap) #抽取.pyi中的API
            removeLst=[]
            pyiLst=sorted(set(pyiLst))
            for it1 in pyiLst:
                for it2 in pyLst:
                    if it2.split('(')[0]==it1.split('(')[0]:
                        removeLst.append(it1)
                        break
            for it in removeLst:
                pyiLst.remove(it)
                    
            f.write('\n'+'-' * 40 + f"{file}" + '-' * 40+'\n')
            for it in pyiLst:
                writeApiLine(f,it,publicAliasSource,publicAliasTarget)
            f.write('\n')

    f.close()
