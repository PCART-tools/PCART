## @package fuzzyMatch
#  Provide class definitions for statically mapping API parameter definitions
#
#
#  Provides fuzzyMatch class for static API signature mapping. Matches called
#  APIs to library definitions by last-segment name matching, with built-in
#  method filtering and alias fallback.
#  提供fuzzyMatch类进行静态API签名映射。通过最后一段名称匹配将调用API
#  与库定义对应，包含内置方法过滤和别名回退。



## Static mapping class for lib API definitions
## 库API定义静态匹配类
class fuzzyMatch:
    ## Initialize the fuzzy matcher
    ## 初始化模糊匹配器
    def __init__(self):
        ## The alias name used when no direct match is found
        ## 未找到直接匹配时使用的别名
        self.alias=''

    ## Fuzzy match the called API against the library API definitions
    ## 将调用API与库API定义进行模糊匹配
    #
    #  Matches by the last segment of the API name. If no match is found and the
    #  last segment matches a Python built-in method, returns empty list.
    #  Otherwise, records the callAPI as a potential alias.
    #  按API名称的最后一个字段进行匹配。未匹配且是Python内置方法时返回空列表，
    #  否则将callAPI作为可能的别名记录。
    #
    #  fmatch既可以在抽取阶段的匹配使用，也可以在分析变更阶段使用
    #
    #  @param callAPI The called API string (dotted name)
    #  @param libAPIs List of library API definition strings
    #  @return List of matching API definition strings, or empty list
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
