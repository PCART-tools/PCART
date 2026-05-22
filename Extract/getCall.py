## @package getCall
#  Extract lib API calls from project source code
#
#
#  Extracts all target-library API calls from a project source file. Restores
#  conventional API paths by resolving assignment chains, import aliases, and
#  with/async-with context manager aliases. Produces structured CallsiteRecord
#  dictionaries keyed by artifact id.
#  从项目源文件中提取所有目标库API调用。通过解析赋值链、import别名和with/async-with
#  上下文管理器别名来还原完整API路径。生成以artifact id为键的结构化CallsiteRecord字典。



import ast
from Extract.extractCall import *
from Tool.callsite import makeCallsiteRecord



## Extract method calls in a custom class inherited from a lib class
## 获取从库API继承的自定义类中的库API方法调用
#
#  @param root The AST node of the parsed project file 
#  @param importDict Module names identified from import statements 
#  @param libName The target lib name (e.g., torch) 
#  @return list of extracted inherited method calls 
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



## Restore the conventional API call path by modifying the first name of the API prefix 
## 通过修改API赋值调用前缀还原完整的API调用路径
#
#  For example: 
#  A=polars()
#  A=A.a(x)
#  A=A.b(y)
#  A=A.a(z)
#  A.a(z)-->A.b(y).a(z)-->A.a(x).b(y).a(z)-->polars.a(x).b(y).a(z)
#  存在的异常情况：中间函数的返回值可能会改变
#
#  @param prefix Prefix of the API call (e.g., A.a(z), A is the prefix)
#  @param callName API call item in source code 
#  @param paraStr Parameter string
#  @param codeLst Source file code list
#  @return The conventional API call path  
def modifyFirstName(prefix, callName, paraStr, codeLst):
    name_parts=callName.split('.') #按.进行字段拆分
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
        for i in range(len(codeLst)):
            if f"{prefix}(".replace(' ','') in codeLst[i].replace(' ','').rstrip('\n'):
                index=i
                break
    
    modifyFlag=0
    if index!=-1:
        index-=1
        while index>=0: #看是否能在前面找到相关的赋值语句
            s=codeLst[index].strip() #去除字符串首尾空格以及换行符
            if '#' in s and '=' in s:
                try:
                    tempNode=ast.parse(s)
                    s=ast.unparse(tempNode)
                except:
                    pass
            s=s.replace(' ','')
            
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



## Restore the conventional API call path in the withitem (including AsyncWith) call form
## 还原withitemAPI调用的完整API调用路径
#
#  For example:
#  async with Client("test.mosquitto.org") as client:
#      await client.publish("temperature", payload="25.3")
#  client.publish("temperature", payload="25.3") --> Client("test.mosquitto.org").publish("temperature", payload="25.3")
#
#  @param callName API call item in source code
#  @param withitemCallName A dict that stores the alias and its counterpart withitem call name
#  @param lineno Optional callsite line number used to select the active withitem scope
#  @return The conventional API call path
def modifyWithName(callName, withitemCallName, lineno=None):
    name_parts = callName.split('.') #按.进行字段拆分
    firstModify = callName
    modifyFlag = 0
    if name_parts[0] in withitemCallName:
        withitem = withitemCallName[name_parts[0]]
        if isinstance(withitem, list):
            candidates = withitem
            if lineno is not None:
                # with别名同名时，只使用覆盖当前调用行号的候选，避免外层/兄弟作用域误还原
                scoped = []
                for item in candidates:
                    start = item.get('lineno')
                    end = item.get('end_lineno')
                    if start is not None and end is not None and start <= lineno <= end:
                        scoped.append(item)
                candidates = scoped
            if candidates:
                # 嵌套with中内层别名优先；行号越靠后的候选作用域越内层
                candidates = sorted(candidates, key=lambda item: item.get('lineno') or -1)
                withitem = candidates[-1].get('callName')
            else:
                withitem = None
        if withitem:
            firstModify = withitem + '.' + '.'.join(name_parts[1:])
            modifyFlag = 1

    #找到了withitem call，重新试探一下前面是否还有withitem call语句
    if modifyFlag:
        return modifyWithName(firstModify, withitemCallName, lineno)
    #若没有，则直接结束 
    else:
        return callName 
        
          

## Extract all API calls from a given .py file
## 每次传进来一个.py文件，抽取所有的调用API
#
#  @param filePath The .py file path
#  @param libName The target lib name (e.g., torch)
#  @param projPath The project root path
#  @param pcresolveLookup Optional pre-built PCResolve lookup table:
#         {filePath: {callId: CallsiteRecord_dict, ...}, ...}.
#         When provided and filePath is present, returns the pre-computed
#         records directly instead of re-extracting.
#  @return Callsite record dictionaries keyed by artifact id
#  @return 返回以运行产物id为key的调用点记录字典
def getCallFunction(filePath,libName,projPath=None,pcresolveLookup=None):
    # If PCResolve lookup is available for this file, use it directly
    # 若PCResolve查找表中有此文件，直接使用预计算结果
    if pcresolveLookup is not None and filePath in pcresolveLookup:
        records = pcresolveLookup[filePath]
        return records, records

    with open(filePath,'r',encoding='UTF-8') as f:
        codeText=f.read()
        f.seek(0)
        codeLst=f.readlines()
    try:
        root_node=ast.parse(codeText,filename='<unknown>',mode='exec')
    
        #找出树中所有的模块名
        import_visitor=Import()
        import_visitor.visit(root_node)
        md_names=import_visitor.get_md_name() #dict

        #找出树中所有withitem call节点 -- 2025/5/19
        withitem_visitor = WithVisitor()
        withitem_visitor.visit(root_node)
        withitem_call_names = withitem_visitor.get_withitem_call() #dict

        # 找出树中所有的Call节点
        call_visitor=GetFuncCall()
        call_visitor.dfsVisit(root_node)
        all_func_calls=call_visitor.func_call #[(api1,para1,callState, lineno,col,...),(api2,para2, callState, lineno,col,...),...()]
        
        # 通过赋值语句和import字典来还原每个调用的API
        apiFormatDict={} #保存还原前的API后还原后的API的对应关系
        selfAPIs=[] #保存通过self调用的API
        for callName,paraStr,callState,lineno,colOffset,endLineNo,endColOffset in all_func_calls:
            name_parts=callName.split('.') #按.进行字段拆分
            if 'self' in name_parts[0]:
                selfAPIs.append((callName,paraStr,callState,lineno,colOffset,endLineNo,endColOffset))

            # #先通过赋值语句进行还原
            firstModify=modifyFirstName(callName,callName,paraStr,codeLst)
            secondModify=firstModify

            # #再将withitem call的别名还原为真名（如有）-- 2025/5/19
            if len(withitem_call_names) !=0:
                firstModify = modifyWithName(callName, withitem_call_names, lineno)
                secondModify = firstModify

            # #最后将import的别名还原成真名
            # #from faker import Fake as A
            # # A(x).b(y) --> faker.Fake(x).b(y)
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
            

            #函数名和参数分开放，key和value都是tuple
            apiFormatDict[(secondModify,paraStr,callState,lineno,colOffset,endLineNo,endColOffset)]=(callName,paraStr,callState,lineno,colOffset,endLineNo,endColOffset)
        
        # 对self调用的API进行还原
        if len(selfAPIs)>0:
            selfInfo=getSelfAPI(root_node,md_names,libName)
            if len(selfInfo)>0: 
                for callName,paraStr,callState,lineno,colOffset,endLineNo,endColOffset in selfAPIs:
                    name_parts=callName.split('.')
                    for bases,defLst,callLst in selfInfo:
                        if callName in callLst and name_parts[-1] not in defLst:
                            name=bases[0]+'.'+'.'.join(name_parts[1:])
                            apiFormatDict[(name,paraStr,callState,lineno,colOffset,endLineNo,endColOffset)]=(callName,paraStr,callState,lineno,colOffset,endLineNo,endColOffset)

        #把和指定第三方库相关的callAPI都筛选出来
        callsiteRecords={}
        callsiteParamRecords={}
        for key,value in apiFormatDict.items(): #key是还原后的API，value是还原前的API
            if key[0].split('.')[0]==libName:
                formatAPI=f"{key[0]}({key[1]})"
                record=makeCallsiteRecord(
                    filePath,
                    value[2],
                    formatAPI,
                    value[1],
                    value[3],
                    value[4],
                    value[5],
                    value[6],
                    projPath,
                )
                callsiteRecords[record['id']]=record
                callsiteParamRecords[record['id']]=record

        #按API的行号从小到大排序,便于之后的插桩 
        sortedCallsiteRecords=dict(sorted(callsiteRecords.items(),key=lambda x:(x[1]['lineno'],x[1]['col_offset'])))
        sortedCallsiteParamRecords=dict(sorted(callsiteParamRecords.items(),key=lambda x:(x[1]['lineno'],x[1]['col_offset'])))
        return sortedCallsiteRecords,sortedCallsiteParamRecords 
    
    except SyntaxError as e:
        print(f"when extract invoked API, parsed {filePath} failed: {e}")
        return {},{}       #若对当前文件解析失败，则返回空字典
