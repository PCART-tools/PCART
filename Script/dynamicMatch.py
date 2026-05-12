## @file dynamicMatch.py
## A dynamic script that maps the signature of a single API call
## @ingroup script
## @page dynamic_match Dynamic Mapping of API Signature
##
## Used by Map/map.py

import sys
import json
import inspect
import os
import dill
from codeUtils import getFileName, removeParameter, departAPI2


#step1: Load the pkl file containing runtime API call data
#step1: 加载包含运行时API调用数据的pkl文件
if len(sys.argv)<5:
    print('lookupKey is required',file=sys.stderr)
    sys.exit(2)

pklPath=sys.argv[1]
with open(pklPath,'rb') as fr:
    paraValueDict=dill.load(fr)
print("load pkl successfully")


#step2: Dynamic signature matching
#step2: 动态签名匹配
callAPI=sys.argv[2]
dataDir=sys.argv[3]
lookupKey=sys.argv[4]
matchDict={}
s=''
lst2=departAPI2(callAPI) #Split into a(x), b(y), c(z) / 拆分成a(x), b(y), c(z)

lastAPI=lst2[-1]
s=removeParameter(lastAPI,1)

# Fill in concrete parameter values for the API call
# 给API填上参数的具体值
for key in paraValueDict.keys():
    if lookupKey==key:
        # Fill in the upstream call dependency (self, chained receiver, withitem, etc.)
        # 把函数的上文依赖给填上，比如self.a(x)中的self, a.b(2).c(3)中的a.b(2)
        k='@{}'.format(key)
        firstPart=lst2[0]
        if k in paraValueDict:
            #Context manager object dynamic matching support
            #上下文管理器对象动态匹配支持
            receiver = paraValueDict.get(k)
            if isinstance(receiver,str):
                s=receiver+'.'+s
            else:
                s='paraValueDict.get(k)'+'.'+s
        else: #Top-level imports like torch.func(x), tornado.web.Application()
            #例如torch.func(x)、tornado.web.Application()等形式
            prefix=''
            for it in lst2:
                if '(' not in it:
                    prefix+=it+'.'
                else:
                    break
            s=prefix+s
        break


api=s
err=''
try:
    result=str(inspect.signature(eval(api)))
    matchDict['match']=result
    matchDict['error']=''
    try:
        internalPath=inspect.getfile(eval(api))
        internalPath = internalPath.replace('\\', '/')
        internalPath=internalPath.split('site-packages/')[-1].replace('.py','').replace('/','.')
        matchDict['internalPath']=internalPath
    except:
        pass
except Exception as e:
    matchDict['match']='nullptr'
    matchDict['error']='sigError={}: {}'.format(type(e).__name__,e)


# If dynamic matching fails, internalPath and addValue attributes are not available
# 动态匹配若失败，则没有internalPath和addValue这两个属性
fileName=getFileName(lookupKey,'_dynamicMatch.json')

os.makedirs(dataDir,exist_ok=True)
with open(os.path.join(dataDir,fileName),'w',encoding='UTF-8') as fw:
    json.dump(matchDict,fw,indent=4,ensure_ascii=False)
