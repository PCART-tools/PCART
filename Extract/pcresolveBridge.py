## @package pcresolveBridge
#  Bridge PCResolve analysis results into PCART CallsiteRecord format
#
#
#  Converts PCResolve's cross-file ProjectAnalysis output into PCART's
#  CallsiteRecord dictionaries, matching the return format of
#  Extract/getCall.getCallFunction(). Supports libName filtering,
#  two-layer caching (raw analysis + per-lib lookup), and graceful
#  degradation when PCResolve is not installed.
#  将PCResolve的跨文件ProjectAnalysis结果转换为PCART的CallsiteRecord字典，
#  匹配Extract/getCall.getCallFunction()的返回格式。支持libName过滤、
#  双层缓存（原始分析+按库查找），以及PCResolve未安装时的静默降级。

import os

try:
    from pcresolve import analyze_project as _pcresolveAnalyze
except ImportError:
    _pcresolveAnalyze = None

_analysisCache = {}
_lookupCache = {}



def _normPath(path):
    """Normalize a filesystem path for stable cache keys."""
    return os.path.normcase(os.path.abspath(os.path.normpath(path)))



def _normProjectPath(path, projPath):
    """Resolve a project file path (relative or absolute) to a normalized key."""
    if not os.path.isabs(path):
        path = os.path.join(projPath, path)
    return _normPath(path)




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
    global _analysisCache, _lookupCache
    normPath = _normPath(projPath)
    cacheKey = (normPath, libName)
    if cacheKey in _lookupCache:
        return _lookupCache[cacheKey]

    if _pcresolveAnalyze is None:
        _lookupCache[cacheKey] = {}
        return _lookupCache[cacheKey]

    # Two-layer cache: raw analysis (projPath) → filtered lookup (projPath, libName)
    # 双层缓存：原始分析（projPath）→ 过滤查找（projPath, libName）
    if normPath in _analysisCache:
        result = _analysisCache[normPath]
    else:
        try:
            result = _pcresolveAnalyze(projPath, scope_model="v2")
        except Exception:
            _analysisCache[normPath] = None
            _lookupCache[cacheKey] = {}
            return _lookupCache[cacheKey]
        _analysisCache[normPath] = result

    if result is None:
        _lookupCache[cacheKey] = {}
        return _lookupCache[cacheKey]

    # Seed empty entries for every file PCResolve analyzed, so that
    # "0 target calls" is distinguishable from "not analyzed" in
    # getCallFunction — avoids falling back to the old extractor for
    # files that PCResolve already determined have no target library calls.
    # 为所有已分析的文件初始化空记录，"0调用"与"未分析"可由getCallFunction
    # 区分——避免对PCResolve已判无目标库调用的文件回退到旧提取器。
    lookup = {}
    for fileResult in result.files:
        lookup[_normProjectPath(fileResult.file_path, projPath)] = {}

    for call in result.all_api_calls:
        if not _matchesLibname(call, libName):
            continue

        record = _convertApiCall(call, projPath)
        key = _normProjectPath(call.file_path, projPath)
        if key not in lookup:
            lookup[key] = {}
        lookup[key][record['id']] = record

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
    global _analysisCache, _lookupCache
    _analysisCache = {}
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
#  Uses only stable attribution fields:
#    1. Exact match on top_library (PCResolve's top-level origin)
#    2. decorated_by match (decorator evidence, e.g. @app.route)
#  resolved_func / func_name are reserved for format_api display and
#  must not gate library membership — those fields are interpretive
#  and can pull non-target calls back in.
#  仅使用稳定归属字段：
#    1. top_library精确匹配（PCResolve的顶层来源）
#    2. decorated_by匹配（装饰器证据）
#  resolved_func / func_name仅用于format_api展示，不判断库归属——
#  这些字段是解释性的，可能把非目标库调用重新纳入。
#
#  @param callObj pcresolve.ApiCall object
#  @param libName Target library name (e.g. "polars")
#  @return True if the call matches the target library
def _matchesLibname(callObj, libName):
    deco = getattr(callObj, 'decorated_by', []) or []
    return callObj.top_library == libName or libName in deco
