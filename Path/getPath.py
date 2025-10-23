## @package getPath 
#  Provide the class definition for obtaining source files and directories from a project/lib 
#
#  More details (TODO)



import os
import copy



## The Path class definition
## 路径定义类
#
#  provide functionalities for obtaining the paths of source files and directories  
#  提供源码和文件夹路径获取功能
class Path:
    def __init__(self,mode):
        #mode='D' 表示只获取根目录下的一级子目录
        #mode='F' 表示只获取根目录下的一级子文件
        #mode='DF'表示获取根目录下所有的子目录和文件
        self._mode=mode
        self._filePath=[]
        self._dirPath=[]
        self._requirements=[] #同一个项目中可能有多个requirements,来自第三方库，如aepx

    @property
    def path(self):
        if self._mode=='D': #D表示只获得一级子目录
            return copy.deepcopy(self._dirPath)
        else:
            return copy.deepcopy(self._filePath) #DF表示获得所有的子目录和文件


    #当需要重复使用一个对象时，清空它之前保存的数据
    def clc(self):
        self._dirPath.clear()
        self._filePath.clear()


    def getPath(self,rootDir):
        for root, dirs, files in os.walk(rootDir, followlinks=True):
            files=[f for f in files if f[0]!='.']  # 过滤掉以.开头的隐藏文件
            dirs=[d for d in dirs if d[0]!='.' and d!= '__pycache__' and d!='include']  # 过滤掉当前路径./和上一级路径../
            if self._mode=='F':
                for f in files:
                    self._filePath.append(os.path.join(root,f))
                break
            
            elif self._mode=='D':
                for dir in dirs:
                    self._dirPath.append(os.path.join(root,dir))
                break
            
            elif self._mode=='DF':
                for f in files:
                    if f.endswith('.py') or f.endswith('.pyi'): #在抽取库的时候需要.pyi,但在抽取项目代码时不需要.pyi文件
                        self._filePath.append(os.path.join(root, f))
                    if 'requirements.txt' in f:
                        self._requirements.append(os.path.join(root,f))
        

        #判断项目中是否有requirements.txt
        if len(self._requirements)>0:
            return self._requirements[0] #返回一个要求的版本号
        else:
            return None
