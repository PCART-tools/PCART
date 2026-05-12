## @package extractDef
#  Provide some class definitions for extracting lib API definitions from lib source files
#
#
#  Contains AST NodeVisitor classes for extracting API definitions from library
#  source code: FunctionDefVisitor, FromImport, Def2format, and AssignVisitor.
#  Used by getDef.py during library API extraction.
#  包含从库源码中提取API定义的AST NodeVisitor类：FunctionDefVisitor、FromImport、
#  Def2format和AssignVisitor。由getDef.py在库API提取阶段使用。


 
import ast
import os



## Function definition node visitor
## 函数定义节点遍历器
#
#  Inherits from ast.NodeVisitor 
class FunctionDefVisitor(ast.NodeVisitor):
    ## Initialize the function definition node container
    ## 初始化函数定义节点容器
    def __init__(self):
        self._defNodes=[]

    ## Return collected function definition nodes
    ## 返回收集到的函数定义节点
    #  @return list of AST FunctionDef nodes
    def functionNodes(self):
        return self._defNodes

    ## Visit a FunctionDef node and record it
    ## 访问FunctionDef节点并记录
    #  @param node The FunctionDef AST node
    #  @return None
    def visit_FunctionDef(self, node):
        self._defNodes.append(node)



## From import statement node visitor
## From import语句节点遍历器
#
#  Inherits from ast.NodeVisitor 
class FromImport(ast.NodeVisitor):
    ## Initialize the from-import visitor for a given package level
    ## 初始化from-import遍历器，传入当前包层级
    #  @param currentLevel The current package level name
    def __init__(self, currentLevel):
        self._importDict={}
        self._currentLevel=currentLevel

    ## Return the import dictionary
    ## 返回导入字典
    #  @return dict mapping module+name to alias or name
    #  @fn importDict
    @property
    def importDict(self):
        return self._importDict

    ## Visit an ImportFrom node and resolve relative imports
    ## 访问ImportFrom节点，解析相对导入
    #  @param node The ImportFrom AST node
    #  @return None
    def visit_ImportFrom(self, node):
        if node.module is not None:
            module=node.module
            if node.level==0:#若是绝对导入，需考虑层级
                tempLst=module.split('.')
                if len(tempLst)==1:
                    module=''
                elif self._currentLevel in tempLst:
                    index=tempLst.index(self._currentLevel)
                    module='.'.join(tempLst[index+1:])
            
            lst=[{'name':name.name,'alias':name.asname} for name in node.names] #可能会import个多个,from A import a,b,c 
            for dic in lst: #lst中每个元素都是字典
                key=module+'.'+dic['name'] #dic['name']可能是*
                key=key.lstrip('.')
                if dic['alias']:
                    self._importDict[key]=dic['alias']
                else:
                    self._importDict[key]=dic['name']



## Get prefix and relative path of a source file
## 获取源码文件路径前缀和相对路径
#
#  The prefix denotes the fully qualified name of a source file. For example, the prefix for lib/a/b/c.py is lib.a.b.c.
#  The relative path denotes the relative path of a source file, e.g., lib/a/b/c.py
class Def2format:
    ## Initialize the prefix and relative path containers
    ## 初始化前缀和相对路径容器
    def __init__(self):
        self._prefix=''
        self._relativePath='' #记录包的相对路径，例如numpy/core/func.py

    ## Return the fully qualified prefix of the source file
    ## 返回源文件的完整路径前缀
    #  @return str, e.g., lib.a.b.c
    #  @fn prefix
    @property
    def prefix(self):
        return self._prefix

    ## Return the relative path of the source file
    ## 返回源文件的相对路径
    #  @return str, e.g., lib/a/b/c.py
    #  @fn relativePath
    @property
    def relativePath(self):
        return self._relativePath

    ## Convert a source file path to package prefix and relative path
    ## 将源码文件路径转换为包前缀和相对路径
    #  @param filePath The absolute path of the source file
    #  @return None
    def toFormat(self,filePath):
        s=filePath.rsplit(f"site-packages{os.sep}", 1)[-1]
        self._relativePath=s
        s=s.replace('\\','.').replace('/','.')
        pos=s.rfind('.')
        s=s[0:pos]
        self._prefix=s.replace('\\','.').replace('/','.')



## Get all assign nodes from a lib source file 
## 源码Assign节点遍历器
#
#  For an assign node, extract the values before (the variable name) and after (the value expression) the assignment operator 
#  对于Assign节点，只需要关注等号左右两边的名字   
class AssignVisitor(ast.NodeVisitor):
    ## Initialize the assign node container
    ## 初始化赋值节点容器
    def __init__(self):
        self._targetCall={}

    ## Return the assign target-to-value dictionary
    ## 返回赋值目标到值的字典
    #  @return dict mapping target variable name to value expression
    def get_target_call(self):
        return self._targetCall

    ## Visit an Assign node and record Call-type values
    ## 访问Assign节点，记录Call类型的值
    #  @param node The Assign AST node
    #  @return None
    def visit_Assign(self,node):
        if isinstance(node.value,ast.Call):
            targetName=ast.unparse(node.targets)
            valueExpr=ast.unparse(node.value)
            self._targetCall[targetName]=valueExpr
