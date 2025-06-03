## @package fuzzyMatch 
#  Provide class definitions for statically mapping API parameter definitions   
#
#  More details (TODO)

import re


class fuzzyMatch:
    def __init__(self):
        self.alias=''
    

    #fmatch即可以在抽取阶段的匹配使用，也可以在分析变更阶段使用
    def fmatch(self,callAPI,libAPIs):
        ans=[] 
        cnamelst=callAPI.split('.')
        lst=[]
        #对库API进行预处理
        for libAPI in libAPIs:
            dname=libAPI.split('(')[0] #此处丢掉参数，只保留函数名
            dnamelst=dname.split('.')
            if cnamelst[-1]==dnamelst[-1]: #先按最后一个名字确定对应关系，若相同则将其保存
                lst.append(libAPI)
        #模糊匹配找到的结果包含两种，同名的+同名的重载 
        if len(lst)>0:
            ans=lst
            return ans 
        #如果没找到，则再判断是否为python内置api
        buildIns=[]
        for it in dir(str)+dir(list)+dir(dict):
            if it[0]!='_':
                buildIns.append(it)
        if cnamelst[-1] in buildIns and len(cnamelst)!=2:
            return []
        
        #否则认为该API可能是库中的一个别名
        self.alias=callAPI
        return ans
        
        
