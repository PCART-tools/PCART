## @package extractCall 
#  Provide some class definitions for extracting lib API calls from project source files
#
#
#  Contains AST NodeVisitor classes: Import (resolves import aliases),
#  GetFuncCall (DFS-based Call node extraction), and WithVisitor (records
#  withitem/async-with context expressions and alias names).
#  包含AST NodeVisitor类：Import（解析import别名）、GetFuncCall（基于DFS的
#  Call节点提取）、WithVisitor（记录withitem/async-with上下文表达式和别名）。



import ast



## Import and ImportFrom node visitor
## Import和ImportFrom节点遍历器
#
#  Inherits from ast.NodeVisitor  
class Import(ast.NodeVisitor):
    ## Initialize the module name dictionary
    ## 初始化模块名字典
    def __init__(self):
        self._md_name={}

    ## Return the module name dictionary
    ## 返回模块名字典
    #  @return dict mapping alias to full module name
    def get_md_name(self):
        return self._md_name

    ## Visit an Import node and record alias-to-name mappings
    ## 访问Import节点，记录别名到模块名的映射
    #  @param node The Import AST node
    #  @return None
    def visit_Import(self, node):
        item=[nn.__dict__ for nn in node.names] #item中每个元素都是一个字典
        for it in item:
            if it["asname"] is None:
                self._md_name[it["name"]]=it["name"]
            else:
                self._md_name[it["asname"]]=it["name"]

    ## Visit an ImportFrom node and record alias-to-qualified-name mappings
    ## 访问ImportFrom节点，记录别名到完整限定名的映射
    #  @param node The ImportFrom AST node
    #  @return None
    def visit_ImportFrom(self, node):
        if node.module is not None:
            item=[nn.__dict__ for nn in node.names]
            for it in item:
                if it["asname"] is None:
                    self._md_name[it["name"]]=node.module+'.'+it["name"]
                else:
                    self._md_name[it["asname"]]=node.module+'.'+it["name"]



## Extract all call type nodes from a project source file
## 抽取项目源码中的所有call类型节点
#
#  Use a DFS algorithm to traverse the call type node from the root node. Each API call is stored in a tuple (API name, parameters, call statement, line/column span)
#  从根节点开始，直接找根节点的孩子，Call存在于Expr和Assign节点中。每个API调用存储调用语句及其行列位置
class GetFuncCall:
    ## Initialize the function call list
    ## 初始化函数调用列表
    def __init__(self):
        self._func_call=[] #list中每个元素都是一个tuple

    ## Return collected function call tuples
    ## 返回收集到的函数调用元组
    #  @return list of (call_name, parameters, call_state, lineno, col_offset, end_lineno, end_col_offset) tuples
    #  @fn func_call
    @property
    def func_call(self):
        return self._func_call

    ## Depth-first search visit that extracts Call nodes
    ## 深度优先遍历，提取Call节点
    #
    #  Terminates when a Call node is found or the current node has no children.
    #  结束条件：遇到Call节点或当前节点无子节点
    #  @param node The AST node to traverse
    #  @return None
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
            callInfo=(
                callName,
                parameters,
                callState,
                node.lineno,
                node.col_offset,
                getattr(node,'end_lineno',None),
                getattr(node,'end_col_offset',None),
            )
            if callInfo not in self._func_call:
                self._func_call.append(callInfo)
            else:
                pass
            return



## Get all with nodes from a project source file
## 项目源码with节点遍历器
#
#  For a withitem node, extract the call name in the context_expr and its alias name (if any) in the optional_vars
#  对于withitem节点，提取其中的call节点和别名（如果有）
class WithVisitor(ast.NodeVisitor):
    ## Initialize the withitem call dictionary
    ## 初始化withitem调用字典
    #
    #  同名with别名可能在不同作用域重复出现，因此按别名保存所有候选及其行号范围
    def __init__(self):
        self._withitemCall={}

    ## Return the withitem call dictionary
    ## 返回withitem调用字典
    #  @return dict mapping alias name to list of {callName, lineno, end_lineno} items
    def get_withitem_call(self):
        return self._withitemCall

    ## Visit a With node and record withitem context expressions
    ## 访问With节点，记录withitem上下文表达式
    #
    #  手动遍历body，避免generic_visit再次访问withitem导致重复记录
    #  @param node The With AST node
    #  @return None
    def visit_With(self, node):
        self._visit_with_items(node)
        for stmt in node.body:
            self.visit(stmt)

    ## Visit an AsyncWith node with the same alias resolution rules as With
    ## 访问AsyncWith节点，与With保持相同的别名还原规则
    #  @param node The AsyncWith AST node
    #  @return None
    def visit_AsyncWith(self, node):
        self._visit_with_items(node)
        for stmt in node.body:
            self.visit(stmt)

    ## Iterate over all withitems in a with statement
    ## 遍历with语句中的所有withitem
    #  @param node The With or AsyncWith AST node
    #  @return None
    def _visit_with_items(self, node):
        for item in node.items:
            self._record_withitem(item, node)

    ## Visit a standalone withitem node (top-level visitor entry)
    ## 访问独立的withitem节点
    #  @param node The withitem AST node
    #  @return None
    def visit_withitem(self, node):
        self._record_withitem(node)

    ## Record a single withitem's context expression and alias
    ## 记录单个withitem的上下文表达式和别名
    #
    #  lineno/end_lineno用于后续按调用点选择当前作用域内的withitem
    #  @param node The withitem AST node
    #  @param parent The parent With or AsyncWith node (for line range)
    #  @return None
    def _record_withitem(self, node, parent=None):
        if isinstance(node.context_expr, ast.Call):
            if node.optional_vars:
                callName =  ast.unparse(node.context_expr)
                aliasName = ast.unparse(node.optional_vars)
                # lineno/end_lineno用于后续按调用点选择当前作用域内的withitem
                item = {
                    'callName': callName,
                    'lineno': getattr(parent, 'lineno', None),
                    'end_lineno': getattr(parent, 'end_lineno', None),
                }
                self._withitemCall.setdefault(aliasName, []).append(item)
