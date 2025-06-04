## @file fixTool 
#  A dynamic script provides utility functions for generating pkl file  

import dill

## Normalize file name
## 给文件取名字
def getFileName(fileName,extension):
    #step1:先把fileName中的非法字符去除
    fileName=fileName.replace(' ','')
    fileName=fileName.replace('/','')
    fileName=fileName.replace('\\','')
    length=255-len(extension)
    if len(fileName)>length:
        fileName=fileName[0:length] #如果超出了长度，就进行截断
    fileName+=extension 
    return fileName

