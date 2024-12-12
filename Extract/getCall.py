import ast
from Extract.extractCall import *


def getSelfAPI(root,importDict,libName):
    ansLst=[]
    for node in ast.iter_child_nodes(root):
        if isinstance(node,ast.ClassDef):
            if len(node.bases)==0: #只关注有继承的类
                continue
            
            bases=[] #可能含有多个继承
            callLst=[]
            defLst=[]
            
            #收集基类信息
            flag=0
            for it in node.bases:
                base=ast.unparse(it)
                if base.split('.')[0] in importDict:
                    base=importDict[base.split('.')[0]]
                if libName in base:
                    flag=1
                    bases.append(base)
            if flag==0: #基类中是否含有指定的第三方库
                continue

            #收集定义的信息
            for n in ast.iter_child_nodes(node):
                if isinstance(n,ast.FunctionDef):
                    defLst.append(n.name)
            
            #递归搜索call节点
            callVisitor=GetFuncCall()
            callVisitor.dfsVisit(node)
            callInfos=callVisitor.func_call
            for Tuple in callInfos:
                callLst.append(Tuple[0])
            
            ansLst.append((bases,defLst,callLst))
    
    return ansLst


    
#A=polars()
#A=A.a(x)
#A=A.b(y)
#A=A.a(z)
#A.a(z)-->A.b(y).a(z)-->A.a(x).b(y).a(z)-->polars.a(x).b(y).a(z)
#存在的异常情况：中间函数的返回值可能会改变
def modifyFirstName(prefix, callName, paraStr, codeLst):
    name_parts=callName.split('.') #按.进行字段拆分
    # print(callName)
    #先通过赋值语句进行还原
    #a=A(x)
    #a.b(y) --> A(x).b(y)
    firstModify=callName #此处考虑了第一个名字
    index=-1 #此处改成直接从源码中按行查找 2023.6.15
    for i in range(len(codeLst)):
        #这个条件有点苛刻，因为这里是抽取源码中的API（目的是为了获取API在源码中的真实位置）
        #但当源码中参数换行写的时候，这个条件就无法满足
        if f"{prefix}({paraStr})".replace(' ','').replace("'",'').replace('"','') in codeLst[i].replace(' ','').replace("'",'').replace('"','').rstrip('\n'):
            index=i
            break
    
    if index==-1:
        # print(f"{callName}({paraStr})")
        for i in range(len(codeLst)):
            if f"{prefix}(".replace(' ','') in codeLst[i].replace(' ','').rstrip('\n'):
                # print(codeLst[i])
                index=i
                break
    
    modifyFlag=0
    if index!=-1:
        index-=1
        while index>=0: #看是否能在前面找到相关的赋值语句
            s=codeLst[index].replace(' ','').rstrip('\n')
            if name_parts[0]!='self':
                if f"{name_parts[0]}="==s[0:len(name_parts[0])+1]:
                    pos=s.find('=')
                    firstModify=s[pos+1:]+'.'+'.'.join(name_parts[1:])
                    prefix=s[pos+1:]
                    prefix=s[pos+1:].split('(',1)[0]
                    paraStr=s[pos+1:].split('(',1)[-1].rstrip(')')
                    modifyFlag=1
                    break
            
            else: #self.a=A(), self.a.f() --> A.f()
                if len(name_parts)>2 and f"{'.'.join(name_parts[0:2])}=" in s:
                    pos=s.find('=')
                    firstModify=s[pos+1:]+'.'+'.'.join(name_parts[2:])
                    prefix=s[pos+1:].split('(',1)[0] #更新prefix
                    paraStr=s[pos+1:].split('(',1)[-1].rstrip(')') #更新参数
                    modifyFlag=1
                    break
            index-=1


    if modifyFlag: #若找到了赋值语句，再试探一下赋值语句是否还有赋值语句
        return modifyFirstName(prefix, firstModify, paraStr, codeLst)
    else: #若没有找到赋值语句，则直接结束
        return callName





# 每次传进来一个.py文件，抽取所有的调用API
# 返回值是一个字典，key是还原后的API+参数，value是还原前的API+参数
def getCallFunction(filePath,libName):
    with open(filePath,'r',encoding='UTF-8') as f:
        codeText=f.read()
        f.seek(0)
        codeLst=f.readlines()
        # for it in codeLst:
        #     print(it)
    try:
        root_node=ast.parse(codeText,filename='<unknown>',mode='exec')

        #找出树中所有的模块名
        import_visitor=Import()
        import_visitor.visit(root_node)
        md_names=import_visitor.get_md_name() #dict


        # 找出树中所有的Call节点
        call_visitor=GetFuncCall()
        call_visitor.dfsVisit(root_node)
        all_func_calls=call_visitor.func_call #[(api1,para1,callState, lineno),(api2,para2, callState, lineno),...()]
        
        # 通过赋值语句和import字典来还原每个调用的API
        apiFormatDict={} #保存还原前的API后还原后的API的对应关系
        selfAPIs=[] #保存通过self调用的API
        for callName,paraStr,callState,lineno in all_func_calls:
            # print(f"{callName}({paraStr})")
            name_parts=callName.split('.') #按.进行字段拆分
            if 'self' in name_parts[0]:
                selfAPIs.append((callName,paraStr,callState,lineno))
            #     # continue
            
            # #先通过赋值语句进行还原
            # #a=A(x)
            # #a.b(y) --> A(x).b(y)
            # firstModify=callName #此处只考虑了第一个名字
            # index=-1 #此处改成直接从源码中按行查找 2023.6.15
            # for i in range(len(codeLst)):
            #     #这个条件有点苛刻，因为这里是抽取源码中的API（目的是为了获取API在源码中的真实位置）
            #     #但当源码中参数换行写的时候，这个条件就无法满足
            #     if f"{callName}({paraStr})".replace(' ','') in codeLst[i].replace(' ','').rstrip('\n'):
            #         index=i
            #         break
            
            # if index==-1:
            #     for i in range(len(codeLst)):
            #         if f"{callName}(".replace(' ','') in codeLst[i].replace(' ','').rstrip('\n'):
            #             index=i
            #             break

            
            # if index!=-1:
            #     index-=1
            #     while index>=0:
            #         s=codeLst[index].replace(' ','').rstrip('\n')
            #         if name_parts[0]!='self':
            #             # if callName=='df.to_latex':
            #             #     print(11111)
            #             if f"{name_parts[0]}="==s[0:len(name_parts[0])+1]:
            #                 pos=s.find('=')
            #                 # print(f"{callName}({paraStr})")
            #                 firstModify=s[pos+1:]+'.'+'.'.join(name_parts[1:])
            #                 break
            #         else: #self.a=A(), self.a.f() --> A.f()
            #             if len(name_parts)>2 and f"{'.'.join(name_parts[0:2])}=" in s:
            #                 pos=s.find('=')
            #                 firstModify=s[pos+1:]+'.'+'.'.join(name_parts[2:])
            #                 break
            #         index-=1
            
            
            # #再将import的别名还原成真名
            # #from faker import Fake as A
            # # A(x).b(y) --> faker.Fake(x).b(y)
            firstModify=modifyFirstName(callName,callName,paraStr,codeLst)
            # print(callName, '-->', firstModify) 
            secondModify=firstModify
            # if 'save' in firstModify:
            #     print(firstModify)

            #2024-1-29修改 
            name_parts=secondModify.split('.')
            firstParts=name_parts[0]
            pos=firstParts.find('(')
            if pos!=-1:
                temp=firstParts[0:pos]
                res=firstParts[pos:]
            else:
                temp=firstParts
                res=''
            if temp in md_names:
                secondModify=(md_names[temp]+res+'.'+'.'.join(name_parts[1:])).rstrip('.') #当nameparts只有一个元素的会在最后多个点，需要去掉
                # if 'save' in secondModify:
                #     print(secondModify) 
            #函数名和参数分开放，key和value都是tuple
            apiFormatDict[(secondModify,paraStr,callState,lineno)]=(callName,paraStr,callState,lineno)
        
        # 对self调用的API进行还原
        if len(selfAPIs)>0:
            selfInfo=getSelfAPI(root_node,md_names,libName)
            if len(selfInfo)>0: 
                for callName,paraStr,callState,lineno in selfAPIs:
                    name_parts=callName.split('.')
                    for bases,defLst,callLst in selfInfo:
                        if callName in callLst and name_parts[-1] not in defLst:
                            name=bases[0]+'.'+'.'.join(name_parts[1:])
                            apiFormatDict[(name,paraStr,callState,lineno)]=(callName,paraStr,callState,lineno)


        #把和指定第三方库相关的callAPI都筛选出来
        callDict={} #词字典用于之后的匹配和变更分析
        callDict2={} #此处的字典用于预处理插桩
        for key,value in apiFormatDict.items(): #key是还原后的API，value是还原前的API
            if key[0].split('.')[0]==libName:
                callDict[f"{value[2]}#_{value[3]}"]=f"{key[0]}({key[1]})" #2023.10.23，确保预处理插桩和在目标版本插桩字典的键都是一样的
                callDict2[f"{value[2]}#_{value[3]}"]=value[1]

        #按API的行号从小到大排序,便于之后的插桩 
        sortedCallDict=dict(sorted(callDict.items(),key=lambda x:int(x[0].split('#_')[-1])))
        sortedCallDict2=dict(sorted(callDict2.items(),key=lambda x:int(x[0].split('#_')[-1])))
        return sortedCallDict,sortedCallDict2 
    
    except SyntaxError as e:
        print(f"when extract invoked API, parsed {filePath} failed: {e}")
        return {},{}       #若对当前文件解析失败，则返回空字典