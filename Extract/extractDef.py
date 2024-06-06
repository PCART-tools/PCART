import ast
class FunctionDefVisitor(ast.NodeVisitor):
    def __init__(self):
        self._defNodes=[]
    
    def functionNodes(self):
        return self._defNodes

    def visit_FunctionDef(self, node):
        self._defNodes.append(node)



class FromImport(ast.NodeVisitor):
    def __init__(self):
        self._importDict={}

    @property
    def importDict(self):
        return self._importDict

    def visit_ImportFrom(self, node):
        if node.module is not None:
            module=node.module
            if node.level==0:#若是绝对导入，比如from A.B.C import d，则key只取C
                module=module.split('.')[-1]
            lst=[{'name':name.name,'alias':name.asname} for name in node.names] #可能会import个多个,from A import a,b,c 
            for dic in lst: #lst中每个元素都是字典
                key=module+'.'+dic['name'] #dic['name']可能是*
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
    
    # /home/zhang/Packages/Pytorch/torchxx.xx
    # /home/zhang/Packages/Matplotlib/matplotlibxx.xx
    # 前缀就是包名去掉版本号 
    # f"/dataset/zhang/anaconda3/envs/3d/lib/{pythonxx.xx}/site-packages/{torch}"
    # def toFormat(self,filePath,projName):
    #     filePath=filePath.split()
    #     index=-1
    #     for i in range(len(projName)):
    #         if projName[i].isdigit():
    #             index=i
    #             break
    #     #rstrip在去除的时候是不考虑字符的顺序的，比如"xxxxapi.py".rstrip(',pyi')就会出错
    #     #s=filePath.split(f"{projName}")[-1].replace('/','.').rstrip('.pyi').rstrip('.py')
    #     s=filePath.split(f"{projName}")[-1].replace('/','.')
    #     pos=s.rfind('.') #bug修复2023.9.8
    #     s=s[0:pos]
    #     self._prefix=projName[0:index]+s
    #     self._relativePath=projName[0:index]+filePath.split(projName)[-1]


    # def toFormat(self,filePath):
    #     s=filePath.split(f"site-packages/")[-1].replace('/','.')
    #     pos=s.rfind('.')
    #     s=s[0:pos]
    #     self._prefix=s.replace('/', '.')
    #     self._relativePath=s    
    
    def toFormat(self,filePath):
        s=filePath.split(f"site-packages/")[-1]
        self._relativePath=s
        s=s.replace('/','.')
        pos=s.rfind('.')
        s=s[0:pos]
        self._prefix=s.replace('/', '.')