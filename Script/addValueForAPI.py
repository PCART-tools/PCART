## @file addValueForAPI.py
## @brief A dynamic script loads parameter values (pkl) for a single API call  
## @ingroup script
## @page add_value_for_api Load Values for API Call
##
## Used by Change/changeAnalyze.py

import sys
import dill
from codeUtils import getFileName, removeParameter, departAPI, departAPI2, get_parameter, getLastAPIParameter


#首先加载PKL
pklPath=sys.argv[1]
with open(pklPath,'rb') as fr:
    paraValueDict=dill.load(fr)
print("load pkl successfully")


callAPI=sys.argv[2]
lookupKey=sys.argv[3] if len(sys.argv)>3 else callAPI
lst1=departAPI(callAPI) #将API按点进行拆分a.b(y).c(z)拆分成a.b(y), a.b(y).c(z)
lst2=departAPI2(callAPI) #拆分成a(x), b(y), c(z)
tempLst=[]
cnt=0
s=''
#给API填上参数的具体值
for key in paraValueDict.keys():
    #if callAPI.replace(' ','')==key.replace(' ',''):
    if getFileName(lookupKey,'')==getFileName(key,''): # 2025/5/25 Fix inconsistency between callAPI name and the key name
        # 2025/5/25 将复杂API参数键替换为简单键，例如复杂的引号符号
        newKey = "callKey"  
        if newKey not in paraValueDict:
            paraValueDict[newKey] = paraValueDict[key]  

        lastAPI=lst2[-1]
        paraStr=getLastAPIParameter(lastAPI)
        paraLst=get_parameter(paraStr,space=0)
        s=removeParameter(lastAPI,1)+'('

        #先把API的参数值填上
        for i in range(len(paraLst)):
            para=paraLst[i]
            if '=' in para and "'='" not in para and '"="' not in para and '==' not in para: 
                pos=para.find('=')
                if '(' not in para[0:pos] and "'" not in para[0:pos] and '"' not in para[0:pos]: #等号前面也不能出现引号，比如f('x= ',y=1)
                    para=para[0:pos+1] #获取关键字参数'keyName='表示关键字参数的名字
                else:
                    para=''
            else:
                para='' #若para中不含等于号则置为空表示不含参数名
            s+='{}paraValueDict["{}"][{}],'.format(para,newKey,i) #参数key=paraValueDict['API'][i]
        
        s=s.rstrip(',')+')'

        #再把函数的上文依赖给填上,比如self.a(x)中的self, a.b(2).c(3)中的a.b(2)
        k='@{}'.format(key)
        firstPart=lst2[0]    
        if k in paraValueDict:
            receiver = paraValueDict.get(k)
            # 新版withitem pkl可能保存object/expr候选；旧版pkl仍是单个接收者
            if isinstance(receiver, dict):
                if 'object' in receiver:
                    receiver = receiver['object']
                elif 'expr' in receiver:
                    receiver = receiver['expr']
                paraValueDict[k] = receiver
            # 2025/5/25 将复杂API参数键替换为简单键，例如复杂的引号符号
            newK = '@' + newKey 
            if newK not in paraValueDict:
                paraValueDict[newK] = receiver 

            if isinstance(receiver, str):
                s=receiver+'.'+s
            else:
                s='paraValueDict["{}"]'.format(newK)+'.'+s
        else:#比如torch.func(x),还有类似于tornado.web.Application()的形式
            prefix=''
            for it in lst2:
                if '(' not in it:
                    prefix+=it+'.'
                else:
                    break
            s=prefix+s
        break

#重新保存修改后的字典，以便后续动态运行加载 -- 2025/5/25
with open(pklPath,'wb') as fw:
    dill.dump(paraValueDict,fw)
print("save pkl successfully")

api=s
try:
    eval(api)
    ans='##'+api+'##'
    print(ans)
except Exception as e:
    print(e)
    pass
