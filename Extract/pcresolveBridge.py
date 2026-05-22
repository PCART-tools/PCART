## @package pcresolveBridge
#  Bridge PCResolve analysis results into PCART CallsiteRecord format
#
#
#  Converts PCResolve's cross-file ProjectAnalysis output into PCART's
#  CallsiteRecord dictionaries, matching the return format of
#  Extract/getCall.getCallFunction(). Supports libName filtering, caching
#  by (projPath, libName), and graceful degradation when PCResolve is not
#  installed.
#  将PCResolve的跨文件ProjectAnalysis结果转换为PCART的CallsiteRecord字典，
#  匹配Extract/getCall.getCallFunction()的返回格式。支持libName过滤、
#  按(projPath, libName)缓存，以及PCResolve未安装时的静默降级。



try:
    from pcresolve import analyze_project as _pcresolveAnalyze
except ImportError:
    _pcresolveAnalyze = None

_lookupCache = {}



## Build a CallsiteRecord lookup table from PCResolve analysis
## 从PCResolve分析结果构建CallsiteRecord查找表
#
#  Runs pcresolve.analyze_project() once per (projPath, libName) pair,
#  filters results to calls matching the target library, and converts
#  each ApiCall into a CallsiteRecord dict sorted by source position.
#  Results are cached at module level for the lifetime of the process.
#  对每个(projPath, libName)对运行一次pcresolve.analyze_project()，
#  过滤匹配目标库的调用，将每个ApiCall转换为按源码位置排序的
#  CallsiteRecord字典。结果在模块级别缓存，进程生命周期内有效。
#
#  @param projPath Absolute path to the project root
#  @param libName Target library name (e.g. "polars", "aiofiles")
#  @return Dict of {filePath: {callId: CallsiteRecord_dict}}.
#          Empty dict when PCResolve is unavailable or no calls match.
def buildCallsiteLookup(projPath, libName):
    global _lookupCache
    cacheKey = (projPath, libName)
    if cacheKey in _lookupCache:
        return _lookupCache[cacheKey]

    if _pcresolveAnalyze is None:
        _lookupCache[cacheKey] = {}
        return _lookupCache[cacheKey]

    try:
        result = _pcresolveAnalyze(projPath)
    except Exception:
        _lookupCache[cacheKey] = {}
        return _lookupCache[cacheKey]

    lookup = {}
    for call in result.all_api_calls:
        if not _matchesLibname(call, libName):
            continue

        record = _convertApiCall(call, projPath)
        filePath = call.file_path
        if filePath not in lookup:
            lookup[filePath] = {}
        lookup[filePath][record['id']] = record

    # Sort by source position within each file, matching getCallFunction ordering
    # 在每个文件内按源码位置排序，与getCallFunction排序一致
    for filePath in lookup:
        lookup[filePath] = dict(sorted(
            lookup[filePath].items(),
            key=lambda kv: (kv[1]['lineno'], kv[1]['col_offset']),
        ))

    _lookupCache[cacheKey] = lookup
    return lookup



## Clear the module-level lookup cache
## 清除模块级查找缓存
#
#  Exposed for testing. After calling _resetCache(), the next call to
#  buildCallsiteLookup() will re-run analyze_project() instead of
#  returning the cached result.
#  供测试使用。调用_resetCache()后，下一次调用buildCallsiteLookup()
#  将重新运行analyze_project()，而不是返回缓存结果。
def _resetCache():
    global _lookupCache
    _lookupCache = {}



## Convert a single PCResolve ApiCall to a CallsiteRecord dict
## 将一个PCResolve ApiCall转换为CallsiteRecord字典
#
#  Maps ApiCall fields to CallsiteRecord fields:
#    expression -> call_text
#    resolved_func(parameters) -> format_api
#    lineno/col_offset/end_lineno/end_col_offset -> source location
#    file_path + projPath -> rel_path
#  将ApiCall字段映射到CallsiteRecord字段：
#    expression -> call_text
#    resolved_func(parameters) -> format_api
#    lineno/col_offset/end_lineno/end_col_offset -> 源码位置
#    file_path + projPath -> rel_path
#
#  @param callObj pcresolve.ApiCall object
#  @param projPath Absolute project root path for rel_path calculation
#  @return Dict matching CallsiteRecord.toDict() format
def _convertApiCall(callObj, projPath):
    from Tool.callsite import makeCallsiteRecord

    resolved = callObj.resolved_func or callObj.func_name or ''

    return makeCallsiteRecord(
        file_path=callObj.file_path,
        call_text=callObj.expression,
        format_api=f"{resolved}({callObj.parameters})" if resolved else callObj.expression,
        parameters=callObj.parameters,
        lineno=callObj.lineno,
        col_offset=callObj.col_offset,
        end_lineno=callObj.end_lineno or None,
        end_col_offset=callObj.end_col_offset or None,
        proj_path=projPath,
    )



## Check whether an ApiCall belongs to the target library
## 判断一个ApiCall是否属于目标库
#
#  Matching is performed in three tiers:
#    1. Exact match on top_library (PCResolve's top-level origin)
#    2. Prefix match on resolved_func (handles submodules)
#    3. Prefix match on func_name (fallback for unresolved calls)
#  Local definitions and Python builtins are always excluded.
#  匹配分为三级：
#    1. top_library精确匹配（PCResolve的顶层来源）
#    2. resolved_func前缀匹配（处理子模块情况）
#    3. func_name前缀匹配（未解析调用的回退）
#  本地定义和Python内置始终被排除。
#
#  @param callObj pcresolve.ApiCall object
#  @param libName Target library name (e.g. "polars")
#  @return True if the call matches the target library
def _matchesLibname(callObj, libName):
    # Exclude local definitions and Python builtins
    # 排除本地定义和Python内置
    if callObj.top_library in ('local', 'python'):
        return False

    # Exact match on top-level origin
    # 顶层来源精确匹配
    if callObj.top_library == libName:
        return True

    # Match by resolved function prefix
    # 按解析后函数名前缀匹配
    if callObj.resolved_func:
        if callObj.resolved_func == libName or callObj.resolved_func.startswith(libName + '.'):
            return True

    # Fallback: match by original function name prefix
    # 回退：按原始函数名前缀匹配
    if callObj.func_name:
        if callObj.func_name == libName or callObj.func_name.startswith(libName + '.'):
            return True

    return False
