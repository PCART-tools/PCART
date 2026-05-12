## @file addValueForAPI.py
## A dynamic script that loads parameter values (pkl) for a single API call
## @ingroup script
## @page add_value_for_api Load Values for API Call
##
## Used by Change/changeAnalyze.py

import sys
import dill
from codeUtils import removeParameter, departAPI2, getParameter, getLastAPIParameter


# Load the pkl file containing runtime API call data
# 加载包含运行时API调用数据的pkl文件
if len(sys.argv)<4:
    print('lookupKey is required',file=sys.stderr)
    sys.exit(2)

pklPath=sys.argv[1]
with open(pklPath,'rb') as fr:
    paraValueDict=dill.load(fr)
print("load pkl successfully")


callAPI=sys.argv[2]
lookupKey=sys.argv[3]
lst2=departAPI2(callAPI) #Split into a(x), b(y), c(z) / 拆分成a(x), b(y), c(z)
s=''
# Fill in concrete parameter values for the API call
# 给API填上参数的具体值
for key in paraValueDict.keys():
    if lookupKey==key:
        # Replace complex API parameter keys with a simple key for reliable lookup
        # 将复杂API参数键替换为简单键，保证可靠查找
        newKey = "callKey"
        if newKey not in paraValueDict:
            paraValueDict[newKey] = paraValueDict[key]

        lastAPI=lst2[-1]
        paraStr=getLastAPIParameter(lastAPI)
        paraLst=getParameter(paraStr,space=0)
        s=removeParameter(lastAPI,1)+'('

        # Fill in API parameter values first
        # 先把API的参数值填上
        for i in range(len(paraLst)):
            para=paraLst[i]
            if '=' in para and "'='" not in para and '"="' not in para and '==' not in para:
                pos=para.find('=')
                if '(' not in para[0:pos] and "'" not in para[0:pos] and '"' not in para[0:pos]:
                    para=para[0:pos+1] #Extract keyword parameter name / 获取关键字参数名
                else:
                    para=''
            else:
                para='' #No parameter name / 不含参数名
            s+='{}paraValueDict["{}"][{}],'.format(para,newKey,i)

        s=s.rstrip(',')+')'

        # Fill in the upstream call dependency (self, chained receiver, etc.)
        # 再把函数的上文依赖给填上，比如self.a(x)中的self, a.b(2).c(3)中的a.b(2)
        k='@{}'.format(key)
        firstPart=lst2[0]
        if k in paraValueDict:
            receiver = paraValueDict.get(k)
            # Replace complex receiver keys with a simple key for reliable lookup
            # 将复杂接收者键替换为简单键，保证可靠查找
            newK = '@' + newKey
            if newK not in paraValueDict:
                paraValueDict[newK] = receiver

            if isinstance(receiver, str):
                s=receiver+'.'+s
            else:
                s='paraValueDict["{}"]'.format(newK)+'.'+s
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

# Re-save the modified dictionary for subsequent dynamic validation
# 重新保存修改后的字典，以便后续动态验证加载
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
