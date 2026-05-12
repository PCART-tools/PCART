## @file extractLibAPI.py
#  Extract library Python APIs
#  提取库的Python API定义
#
#  This script takes the configuration file (e.g., config.json) as input, and
#  extracts library APIs from the current and target versions.
#  此脚本以配置文件（如config.json）为输入，从当前版本和目标版本中提取库的API定义。
#  Run command: python extractLibAPI.py -cfg config.json



import os
import sys
from Extract.getDef import getDefFunction
from Tool.tool import getSourceCodePath



## Extract API definitions for a given library version
## 抽取给定库版本的API定义
#
#  @param version A specific library version
#  @param sourceCodePath The source code path of the library
def getLibAPI(version, sourceCodePath):
    libName=os.path.basename(sourceCodePath)
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
