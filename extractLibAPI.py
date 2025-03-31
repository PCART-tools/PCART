## @package extractLibAPI
#  Extract library APIs
#
#  This script takes the configuration file (e.g., config.json) as the input, and extracts library APIs from the current and target versions. 
#  Run command: python extractLibAPI.py -cfg config.json

import sys
import json
from Path.getPath import *
from Extract.getDef import getDefFunction
from multiprocessing import Pool
from Tool.tool import getSourceCodePath


## This function extracts APIs for a given library version
#  @param version An specific library version
#  @param sourceCodePath The source code path of the library
def extractLibAPI(version, sourceCodePath):
    libName=sourceCodePath.split('/')[-1]
    getDefFunction((libName, version, sourceCodePath))



if __name__=='__main__':
    
    config=sys.argv[2]
    currentVersion, targetVersion, currentSourceCodePath, targetSourceCodePath = getSourceCodePath(config)
    
    print(currentVersion, currentSourceCodePath)
    extractLibAPI(currentVersion, currentSourceCodePath)
    print(targetVersion, targetSourceCodePath)
    extractLibAPI(targetVersion, targetSourceCodePath) 
