## @file dynamicMatch.py
## @brief A dynamic script dynamically maps the signature of a single API call 
## @ingroup script
## @page dynamic_match Dynamic Mapping of API Signature
##
## Used by Map/map.py

import sys
import json
import inspect
import dill
from codeUtils import getFileName, removeParameter, departAPI, departAPI2



#step1: 加载PKL
pklPath=sys.argv[1]
with open(pklPath,'rb') as fr:
    paraValueDict=dill.load(fr)
print("load pkl successfully")



#step2: 动态匹配
callAPI=sys.argv[2]
jsonPrefix=sys.argv[3]
matchDict={}
tempLst=[]
s=''
lst1=departAPI(callAPI) #将API按点进行拆分a(x).b(y).c(z)拆分成a(x), a(x).b(y), a(x).b(y).c(z)
lst2=departAPI2(callAPI) #拆分成a(x), b(y), c(z)

lastAPI=lst2[-1]
s=removeParameter(lastAPI,1)

#给API填上参数的具体值
for key in paraValueDict.keys():
    #if callAPI.replace(' ','')==key.replace(' ',''):
    # 2025/5/25 Fix inconsistency between callAPI name and the key name
    if getFileName(callAPI,'')==getFileName(key,''): 
        #把函数的上文依赖给填上,比如self.a(x)中的self, a.b(2).c(3)中的a.b(2)
        k='@{}'.format(key)
        firstPart=lst2[0]
        if k in paraValueDict:
            #新增类Contenxt Manager对象动态匹配支持 -- 2025/5/20
            if isinstance(eval('paraValueDict.get(k)'),str):
                s=eval('paraValueDict.get(k)')+'.'+s
            else:
                s='paraValueDict.get(k)'+'.'+s
        else: #比如torch.func(x),还有类似于tornado.web.Application()的形式
            prefix=''
            for it in lst2:
                if '(' not in it:
                    prefix+=it+'.'
                else:
                    break
            s=prefix+s
        break


# print(s)
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



# print("match:",matchDict['match'])
#动态匹配若失败，则没有internalPath,和addValue这两个属性的
fileName=getFileName(callAPI,'_dynamicMatch.json')

with open('{}/data/{}'.format(jsonPrefix,fileName),'w',encoding='UTF-8') as fw:
    json.dump(matchDict,fw,indent=4,ensure_ascii=False)

# print("保存文件成功：{}_dynamicMatch.json".format(callAPI.replace(' ','')))

