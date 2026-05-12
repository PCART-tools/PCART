## @package getPath 
#  Provide the class definition for obtaining source files and directories from a project/lib 
#
#
#  Provides the Path class for traversing project and library directories to
#  collect source files. Supports three modes: D (first-level subdirectories),
#  F (first-level files), DF (all files and subdirectories recursively).
#  提供Path类遍历项目和库目录以收集源文件。支持三种模式：D（一级子目录）、
#  F（一级文件）、DF（递归所有文件和子目录）。



import os
import copy



## The Path class definition
## 路径定义类
#
#  provide functionalities for obtaining the paths of source files and directories  
#  提供源码和文件夹路径获取功能
class Path:
    ## Initialize the Path object with a traversal mode
    ## 使用遍历模式初始化Path对象
    #
    #  @param mode Path traversal mode:
    #   - 'D'  Get first-level subdirectories only    只获取根目录下的一级子目录
    #   - 'F'  Get first-level files only             只获取根目录下的一级子文件
    #   - 'DF' Get all files and subdirectories       获取根目录下所有的子目录和文件
    def __init__(self,mode):
        self._mode=mode
        self._filePath=[]
        self._dirPath=[]
        self._requirements=[] #同一个项目中可能有多个requirements,来自第三方库，如aepx

    ## Return collected paths (deep copy to avoid mutation)
    ## 返回收集到的路径（深拷贝以避免被修改）
    #
    #  @return List of file paths (for F/DF modes) or directory paths (for D mode)
    #  @fn path
    @property
    def path(self):
        if self._mode=='D':
            return copy.deepcopy(self._dirPath)
        else:
            return copy.deepcopy(self._filePath)

    ## Clear previously collected path data for reuse
    ## 清空之前收集的路径数据以便复用
    def clc(self):
        self._dirPath.clear()
        self._filePath.clear()

    ## Traverse the root directory and collect file and directory paths
    ## 遍历根目录，收集文件和目录路径
    #
    #  @param rootDir The root directory to traverse
    #  @return Path to the first requirements.txt found, or None
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
