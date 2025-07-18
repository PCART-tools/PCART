## @file codeUtils.py 
## @brief A dynamic script provides utility functions for generating pkl file 
## @ingroup script
## @page code_utils Code Utils
##
## Used by Preprocess/preprocess.py

import dill
import hashlib

## @cond SCRIPT_ONLY
## Normalize file name
## 给文件取名字
def getFileName(fileName,extension):
    #step1:先把fileName中的非法字符去除
    fileName=fileName.replace(' ','')
    fileName=fileName.replace('/','')
    fileName=fileName.replace('\\','')
    if len(extension) != 0:
        length=255-len(extension)
        #if len(fileName)>length:
            #fileName=fileName[0:length] #如果超出了长度，就进行截断
        fileName=fileName.split('(')[0] + '_' + hashlib.md5(fileName.encode()).hexdigest()[:16] # 2025.7.18 More robust file name processing
        fileName=fileName[0:length]

    fileName+=extension 
    return fileName
## @endcond
