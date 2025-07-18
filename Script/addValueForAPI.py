## @file addValueForAPI.py
## @brief A dynamic script loads parameter values (pkl) for a single API call  
## @ingroup script
## @page add_value_for_api Load Values for API Call
##
## Used by Change/changeAnalyze.py

import sys
import inspect
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


## @cond SCRIPT_ONLY
#将参数字符串拆分成单个的参数
#apiName(x,y=1,z:int,w=(p1,p2={1,(1m,23)}),device: Union[Device, int] = None, abbreviated: bool ={'a','b'}) -> str
#默认按逗号进行拆分,也可按'.'进行拆分，比如a.b.c
def get_parameter(p_string,separator=','):
    #库定义的参数去空格，项目中的参数不去空格，防止出问题
    if p_string=='':
        return []
    
    parameters=[]
    stack=[]
    count_left_min=0 #统计'('的个数
    count_right_min=0 #统计')'的个数

    count_left_middle=0 #统计'['的个数
    count_right_middle=0 #统计']'的个数

    count_left_hua=0 #统计'{'的个数
    count_right_hua=0 #统计'}'的个数

    count_single_yinhao=0 #统计单引号的引号的个数
    count_double_yinhao=0 #统计双引号的引号的个数

    for index,value in enumerate(p_string):
        stack.append(value)
        if (value=="'" or count_single_yinhao) and not count_double_yinhao: #若上一步出现了双引号，则说明此处的单引号是在双引号内的，所以不计算单引号的个数
            if value=="'":
                count_single_yinhao+=1
            if count_single_yinhao&1:
                continue
        
        elif (value=='"' or count_double_yinhao) and not count_single_yinhao: #若上一步出现了单引号，则说明此处的双引号是在单引号内的，所以不计算双引号的个数
            if value=='"':
                count_double_yinhao+=1
            if count_double_yinhao&1:
                continue
        
        count_single_yinhao=0 #重置为0
        count_double_yinhao=0

        #只计算引号之外的括号是否成对出现 
        if value=='(':
            count_left_min+=1
        elif value==')':
            count_right_min+=1
        
        elif value=='[':
            count_left_middle+=1
        elif value==']':
            count_right_middle+=1

        elif value=='{':
            count_left_hua+=1
        elif value=='}':
            count_right_hua+=1
        
    
        #弹栈,遇到分隔符或达到字符串末尾
        if value==separator:
            flagMin=1 #假设左右括号的个数都是相等的
            flagMid=1
            flagHua=1
            if '(' in stack:
                if count_left_min!=count_right_min:
                    flagMin=0
            if '[' in stack:
                if count_left_middle!=count_right_middle:
                    flagMid=0
            if '{' in stack:
                if count_left_hua!=count_right_hua:
                    flagHua=0

            if flagMin and flagMid and flagHua:
                parameters.append(''.join(stack[0:-1]))
                stack.clear()
    
        elif index==len(p_string)-1:
            parameters.append(''.join(stack))


    return parameters
## @endcond


## @cond SCRIPT_ONLY
#获取最后一个API参数
#a(x).b(x=c.d(1),y=b((1,2),5),w).c(1,2,3,4)
#获取c的参数1,2,3,4
def getLastAPIParameter(apiStr):
    ans=''
    i=len(apiStr)-1
    left=0 #记录左括号的个数
    right=0 #记录右括号的个数
    pos=len(apiStr)
    while i>=0:
        if apiStr[i]==')':
            right+=1
        if apiStr[i]=='(':
            left+=1
        if left==right and left>0 and right>0:
            pos=i
            break
        i-=1
    if pos!=len(apiStr):
        ans=apiStr[pos+1:-1]
    return ans  
## @endcond


#首先加载PKL
pklPath=sys.argv[1]
with open(pklPath,'rb') as fr:
    paraValueDict=dill.load(fr)
print("load pkl successfully")


callAPI=sys.argv[2]
lst1=departAPI(callAPI) #将API按点进行拆分a.b(y).c(z)拆分成a.b(y), a.b(y).c(z)
lst2=departAPI2(callAPI) #拆分成a(x), b(y), c(z)
tempLst=[]
cnt=0
s=''
#给API填上参数的具体值
for key in paraValueDict.keys():
    #if callAPI.replace(' ','')==key.replace(' ',''):
    if getFileName(callAPI,'')==getFileName(key,''): # 2025/5/25 Fix inconsistency between callAPI name and the key name
        # 2025/5/25 将复杂API参数键替换为简单键，例如复杂的引号符号
        newKey = "callKey"  
        if newKey not in paraValueDict:
            paraValueDict[newKey] = paraValueDict[key]  

        lastAPI=lst2[-1]
        paraStr=getLastAPIParameter(lastAPI)
        paraLst=get_parameter(paraStr)
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
            # 2025/5/25 将复杂API参数键替换为简单键，例如复杂的引号符号
            newK = '@' + newKey 
            if newK not in paraValueDict:
                paraValueDict[newK] = paraValueDict[k] 

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
