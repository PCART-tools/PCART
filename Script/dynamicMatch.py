## @file dynamicMatch.py
## @brief A dynamic script dynamically maps the signature of a single API call 
## @ingroup script
## @page dynamic_match Dynamic Mapping of API Signature
##
## Used by Map/map.py

import sys
import json
import inspect
import copy
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



## @cond SCRIPT_ONLY
#去掉API中的参数部分
def removeParameter(s,flag=0): 
    if '->' in s: #若有返回值，则把返回值也去掉
        s=s.split('->')[0] 
    if flag==0:   #去掉API中所有参数
        stack=[]
        left=0
        right=0
        ans=''
        for index,value in enumerate(s):
            #进栈
            stack.append(value)
            if value=='(':
                left+=1
            if value==')':
                right+=1
            #出栈
            if left==right and left>0 and right>0:
                pos=stack.index('(')
                ans+=''.join(stack[0:pos])
                stack.clear()
                left=0
                right=0
            elif index==len(s)-1:
              ans+=''.join(stack)
    else:  #只去除最后一个API的参数
        i=len(s)-1
        left=0  #记录左括号的个数
        right=0
        pos=len(s)
        while i>=0:
            if s[i]==')':
                right+=1
            if s[i]=='(':
                left+=1
            if left==right and left>0 and right>0:
                pos=i #更新pos
                break
            i-=1
        ans=s[0:pos]

    return ans
## @endcond


## @cond SCRIPT_ONLY
#拆分API，比如a.b(x).c(y).d(z)
#拆成3个API，分别是a.b(x),a.b(x).c(y), a.b(x).c(y).d(z)
#还有特殊的调用形式a.b['x'](y)
def departAPI(s):
    ansLst=[]
    stack=''
    leftMin=0 #记录左'('的个数
    rightMin=0
    leftMid=0
    rightMid=0
    for i in range(len(s)):
        stack+=s[i]
        if s[i]=='(':
            leftMin+=1
        if s[i]==')':
            rightMin+=1
        if s[i]=='[':
            leftMid+=1
        if s[i]==']':
            rightMid+=1
        
        flagMid=1
        if '[' in stack:
            if leftMid!=rightMid:
                flagMid=0
        
        #拆分函数字符串里面必须要出现() 
        if  leftMin and rightMin and leftMin==rightMin and flagMid:
            ansLst.append(stack[0:i+1])
            leftMin=0
            rightMin=0
            if leftMid and rightMid:
                leftMin=0
                rightMid=0
        
        elif i==len(s)-1:
            ansLst.append(stack[0:i+1])

    return ansLst
## @endcond


## @cond SCRIPT_ONLY
def departAPI2(s,separator='.'):
    ansLst=[]
    lst=[]
    count_left_min=0 #统计左'('的个数
    count_right_min=0 #统计右')'的个数

    count_left_middle=0 #统计左'['的个数
    count_right_middle=0 #统计左']'的个数
    for index,value in enumerate(s):
        #入栈，分两种情况
        if value!=separator:
            lst.append(value)
            if value=='(':
                count_left_min+=1
            if value==')':
                count_right_min+=1
            if value=='[':
                count_left_middle+=1
            if value==']':
                count_right_middle+=1
        
        elif value==separator and ((count_left_min>count_right_min) or (count_left_middle>count_right_middle)):
            lst.append(value)

        #弹栈，分三种情况
        if value==separator:
            flagMin=1 #假设左右括号的个数都是相等的
            flagMid=1
            if '(' in lst:
                if count_left_min!=count_right_min:
                    flagMin=0
            if '[' in lst:
                if count_left_middle!=count_right_middle:
                    flagMid=0
            if flagMin and flagMid:
                ansLst.append(''.join(lst))
                lst.clear()
        elif index==len(s)-1:
            ansLst.append(''.join(lst))

    return ansLst
## @endcond



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

