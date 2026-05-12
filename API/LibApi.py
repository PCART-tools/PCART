## @package LibApi 
#  Provide some class definitions for API objects
#
#
#  Defines Parameter (single API parameter), Api (full API signature), and
#  APIOBJ (container for converting string API definitions into Api objects).
#  These classes are used throughout the pipeline for compatibility analysis.
#  定义Parameter（单个API参数）、Api（完整API签名）、APIOBJ（将字符串API定义
#  转换为Api对象的容器）。这些类用于整个流水线的兼容性分析。



import copy
import re
from Tool.tool import getParameter



## Parameter class for Library APIs
## API参数类
#
#  Parameter object: for storing the information of one parameter 
#  参数对象:用于保存一个参数的信息 
class Parameter():
    
    ## The constructor
    ## 构造函数
    def __init__(self):

        ## The full string of the parameter
        ## 参数字符串
        self.fullItem=""

        ## The parameter name
        ## 参数名称
        self.name=""

        ## The parameter position
        ## 参数位置
        self.position=""

        ## The parameter default value
        ## 参数默认值
        self.value=""
 
        ## The parameter type
        ## 参数类型
        self.type=""

        ## The star symbol position
        ## 星号位置
        self.star_position=-1  #记录'*'的位置,便于拆分位置参数和关键字参数

    ## Return the hash value of the parameter
    ## 返回参数哈希值
    #  @return Hash value of the parameter name
    def __hash__(self):
        return hash(self.fullItem)
   
    ## Determine whether two parameter objects are equal
    ## 判断两个参数对象是否相等 
    #  @param other The parameter object to compare
    #  @return True if the parameter names are equal
    def __eq__(self,other):
        return self.fullItem==other.fullItem
   
    ## Return the string representation of the parameter
    ## 返回参数的字符串表示形式 
    #  @return Original parameter string
    def __repr__(self):
        return self.fullItem



## API class for storing a single API definition
## API类，用于存储单个API的定义
#
#  Currently only considers changes to APIs with the same name.
#  暂时只考虑同名Api的变更情况
class Api:
    ## Initialize the API fields
    ## 初始化API字段
    def __init__(self):
        ## The full API string including name and parameters
        ## API完整字符串，包含名称和参数
        self.full_item=""
        ## The API name without parameters
        ## API名称（不含参数）
        self.name=""
        ## List of Parameter objects
        ## 参数对象列表
        self.parameters=[]
        ## All parameters stored as a single string
        ## 所有参数保存为单个字符串
        self.parameters_string=""
        ## The return type annotation (if any)
        ## 返回值类型注释（如有）
        self.rType=""
        ## The library version
        ## 库版本
        self.version=""

    ## Return the hash value based on the parameters string
    ## 基于参数字符串返回哈希值
    #  @return Hash value of the API parameter string
    def __hash__(self):
        return hash(self.parameters_string)

    ## Determine equality based on the parameters string
    ## 基于参数字符串判断两个API是否相同
    #
    #  list去重时，也会根据这个值的来去重
    #  @param other The API object to compare
    #  @return True if both API objects have the same parameter string
    def __eq__(self,other):
        return self.parameters_string==other.parameters_string

    ## Return the full API string as the representation
    ## 返回完整API字符串作为对象表示形式
    #
    #  When printing an instance, prints the full API string instead of the default object representation.
    #  当打印一个类的时候，不会打印object，而是打印指定的字符串，即self.full_item
    #  @return Full API string
    def __repr__(self):
        return self.full_item



## API list container for converting string definitions to API objects
## API列表容器，将字符串形式的API定义转换为API对象
class APIOBJ:
    ## Initialize the API object list
    ## 初始化API对象列表
    def __init__(self):
        self.objLst=[]

    ## Convert API string definitions to API objects
    ## 将API字符串定义转换为API对象
    #
    #  @param version The library version
    #  @param APIStringLst List of API definition strings
    #  @return None. Parsed Api objects are appended to self.objLst
    def toAPIObj(self,version,APIStringLst):
        patternP=r'.*?\((.*)\)' #匹配函数参数
        objP=re.compile(patternP)
        Lst=copy.copy(APIStringLst)
        for item in Lst:
            api=Api()               
            #获取api的完整形式
            api.full_item=item
            
            #获取函数名
            api.name=item.split('(')[0]
            
            #当前Api所对应的版本
            api.version=version 
            
            #获取返回值类型，如果有的话
            if '->' in item:
                api.rType=item.split('->')[1]

            pString=objP.findall(item) #获取函数参数
            api.parameters_string=''.join(pString) #保存参数整体的字符串
            if len(pString)>0:
                lst=getParameter(pString[0]) #拆分参数
                #把self和cls去掉
                if 'self' in lst:
                    lst.remove('self')
                if 'cls' in lst:
                    lst.remove('cls')
                for para in lst:
                    parameter=Parameter()
                    parameter.fullItem=para #记录参数的完整名字
                    parameter.position=lst.index(para) #获取参数的位置
                    if ':' in para:
                        l=para.split(':')
                        parameter.name=l[0]
                        #若参数的默认值存在于类型注释中
                        if '=' in l[1]:
                            ll=l[1].split('=')
                            parameter.type=ll[0]
                            parameter.value=ll[1]
                        else:
                            parameter.type=l[1]

                    elif '=' in para:
                        l=para.split('=')
                        parameter.name=l[0]
                        parameter.value=l[1]
                    else:
                        parameter.name=para
                    api.parameters.append(parameter)
            
            self.objLst.append(api)
