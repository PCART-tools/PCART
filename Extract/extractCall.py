import ast
#访问import节点和importFrom节点
class Import(ast.NodeVisitor):
    def __init__(self):
        self._md_name={}

    def get_md_name(self):
        return self._md_name

    def visit_Import(self, node):
        item=[nn.__dict__ for nn in node.names] #item中每个元素都是一个字典
        for it in item:
            if it["asname"] is None:
                self._md_name[it["name"]]=it["name"]
            else:
                self._md_name[it["asname"]]=it["name"]

    def visit_ImportFrom(self, node):
        if node.module is not None:
            item=[nn.__dict__ for nn in node.names]
            for it in item:
                if it["asname"] is None:
                    self._md_name[it["name"]]=node.module+'.'+it["name"]
                else:
                    self._md_name[it["asname"]]=node.module+'.'+it["name"]



#从根节点开始，直接找根节点的孩子，Call存在于Expr和Assign节点中
class GetFuncCall:
    def __init__(self):
        self._func_call=[] #list中每个元素都是一个tuple

    @property
    def func_call(self):
        return self._func_call

    #采用深度遍历,先一直往下走
    #结束条件：遇到Call节点或当前节点无子节点
    def dfsVisit(self,node):
        #先递推再回归 
        for n in ast.iter_child_nodes(node):
            self.dfsVisit(n)
        
        if isinstance(node,ast.Call):
            callName=ast.unparse(node.func)
            callState=ast.unparse(node) #还原之后的语句可能和项目中的语句存在差异，比如空格等
            argLst=[]
            for arg in node.args:
                argLst.append(ast.unparse(arg))
            for keyword in node.keywords:
                argLst.append(ast.unparse(keyword))
            parameters=','.join(argLst)
            if (callName,parameters,callState,node.lineno) not in self._func_call:
                # print(node.lineno,'<-->',callState)
                self._func_call.append((callName,parameters,callState,node.lineno)) #四元组：callAPI名，callAPI参数，...
            else:
                pass
                # print(node.lineno,'<-->',callState)
            return


#找到所有的Assign节点
#对于Assign节点，只需要关注等号左右两边的名字   
class AssignVisitor(ast.NodeVisitor):
    def __init__(self):
        self._targetCall={}

    def get_target_call(self):
        return self._targetCall

    def visit_Assign(self,node):
        if isinstance(node.value,ast.Call):
            targetName=ast.unparse(node.targets)
            valueExpr=ast.unparse(node.value)
            self._targetCall[targetName]=valueExpr

