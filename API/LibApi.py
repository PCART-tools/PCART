## @package LibApi 
#  Provide some class definitions for API objects
#
#  More details (TODO)



import copy
import re
from Tool.tool import get_parameter



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
    def __hash__(self):
        return hash(self.fullItem)
   
    ## Determine whether two parameter objects are equal
    ## 判断两个参数对象是否相等 
    def __eq__(self,other):
        return self.fullItem==other.fullItem
   
    ## Return the string representation of the parameter
    ## 返回参数的字符串表示形式 
    def __repr__(self):
        return self.fullItem



#暂时只考虑同名Api的变更情况
class Api:
    def __init__(self):
        self.full_item="" #full_item=APIName+parameters
        self.name=""
        self.parameters=[] #参数的个数,其中每个元素都是一个参数对象
        self.parameters_string="" #将api的所有参数整体保存为字符串
        self.rType=""
        self.version="" #库版本
    
    def __hash__(self):
        return hash(self.parameters_string)

    def __eq__(self,other):
        #利用API中的参数字符串来判断两个API是否相同
        #list去重时，也会根据这个值的来去重
        return self.parameters_string==other.parameters_string

    #控制打印信息，当打印一个类的时候，不会打印object，而是打印指定的字符串，即self.full_item
    def __repr__(self):
        return self.full_item 



class APIOBJ:
    def __init__(self):
        self.objLst=[]

    def toAPIObj(self,version,APIStringLst):
        patternP='.*?\((.*)\)' #匹配函数参数
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
                lst=get_parameter(pString[0]) #拆分参数
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
