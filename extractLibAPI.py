## @file extractLibAPI.py
#  Extract library Python APIs
#
#  This script takes the configuration file (e.g., config.json) as the input, and extracts library APIs from the current and target versions. 
#  Run command: python extractLibAPI.py -cfg config.json



import sys
import json
from Path.getPath import *
from Extract.getDef import getDefFunction
from multiprocessing import Pool
from Tool.tool import getSourceCodePath



## Extract API definitions for a given library version
## 抽取给定库版本的API定义
#
#  @param version An specific library version
#  @param sourceCodePath The source code path of the library
def getLibAPI(version, sourceCodePath):
    libName=sourceCodePath.split('/')[-1]
    getDefFunction((libName, version, sourceCodePath))



## Main function of extracting lib API definitions
## 抽取库API定义主函数 
def main():
    if len(sys.argv) < 3:
        print("Usage: python extractLibAPI.py -cfg config.json")
        sys.exit(1)
 
    config=sys.argv[2]

    #加载配置
    currentVersion, targetVersion, currentSourceCodePath, targetSourceCodePath = getSourceCodePath(config)
   
    #抽取起始版本API定义
    print(currentVersion, currentSourceCodePath)
    getLibAPI(currentVersion, currentSourceCodePath)
    
    #抽取目标版本API定义 
    print(targetVersion, targetSourceCodePath)
    getLibAPI(targetVersion, targetSourceCodePath) 

if __name__=='__main__':
    main()
