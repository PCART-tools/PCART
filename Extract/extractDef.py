import ast
class FunctionDefVisitor(ast.NodeVisitor):
    def __init__(self):
        self._defNodes=[]
    
    def functionNodes(self):
        return self._defNodes

    def visit_FunctionDef(self, node):
        self._defNodes.append(node)



class FromImport(ast.NodeVisitor):
    def __init__(self, currentLevel):
        self._importDict={}
        self._currentLevel=currentLevel

    @property
    def importDict(self):
        return self._importDict

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


class Def2format:
    def __init__(self):
        self._prefix=''
        self._relativePath='' #记录包的相对路径，例如numpy/core/func.py
    
    @property
    def prefix(self):
        return self._prefix
    
    @property
    def relativePath(self):
        return self._relativePath
    
    
    def toFormat(self,filePath):
        s=filePath.split(f"site-packages/")[-1]
        self._relativePath=s
        s=s.replace('/','.')
        pos=s.rfind('.')
        s=s[0:pos]
        self._prefix=s.replace('/', '.')