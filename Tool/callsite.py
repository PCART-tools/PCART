## @package callsite
#  Provide structured callsite identity helpers
#
#
#  Defines CallsiteIdentity (structured source-location metadata) and
#  CallsiteRecord (artifact_id + format_api + parameters). The artifactId()
#  method produces a stable, readable SHA256-based key used for pkl naming,
#  manifest tracking, and shared dictionary lookups throughout the pipeline.
#  定义CallsiteIdentity（结构化源码位置元数据）和CallsiteRecord
#  （artifact_id + format_api + parameters）。artifactId()方法生成稳定可读的
#  SHA256-based键，用于pkl命名、manifest跟踪和共享字典查找。

import hashlib
import json
import os
import re
from dataclasses import dataclass
from typing import Optional


## @class CallsiteIdentity
## Callsite identity class
## 调用点身份类
#
#  A CallsiteIdentity describes one AST Call node with project-relative path,
#  source span and normalized call text.
#  CallsiteIdentity使用项目相对路径、源码位置和归一化调用文本描述一个AST调用节点。
@dataclass(frozen=True)
class CallsiteIdentity:
    ## The relative path from project root
    ## 相对于项目根目录的文件路径
    rel_path: str

    ## The line number of AST Call node
    ## AST调用节点所在行号
    lineno: int

    ## The column offset of AST Call node
    ## AST调用节点所在列偏移
    col_offset: int

    ## The end line number of AST Call node
    ## AST调用节点结束行号
    end_lineno: Optional[int]

    ## The end column offset of AST Call node
    ## AST调用节点结束列偏移
    end_col_offset: Optional[int]

    ## The original call text used for report display
    ## 报告展示用的原始调用文本
    call_text: str

    ## The normalized call text used for identity generation
    ## 生成调用点身份用的归一化调用文本
    normalized_call: str

    ## Return the payload used to generate artifact id
    ## 返回用于生成运行产物id的数据
    def artifactPayload(self):
        return {
            'rel_path': self.rel_path,
            'lineno': self.lineno,
            'col_offset': self.col_offset,
            'end_lineno': self.end_lineno,
            'end_col_offset': self.end_col_offset,
            'normalized_call': self.normalized_call,
        }

    ## Return stable artifact hash for a callsite
    ## 返回调用点稳定运行产物hash
    def artifactHash(self):
        payload = json.dumps(
            self.artifactPayload(),
            sort_keys=True,
            separators=(',', ':'),
        ).encode('utf-8')
        return hashlib.sha256(payload).hexdigest()

    ## Return stable readable artifact id for a callsite
    ## 返回调用点稳定可读运行产物id
    def artifactId(self):
        MAX_REL = 64   # max slug length for relative path
        MAX_CALL = 48  # max slug length for call name
        # slugify relative path
        rel_slug = re.sub(r'[^0-9A-Za-z]+', '_', str(self.rel_path)).strip('_').lower()
        rel_slug = re.sub(r'_+', '_', rel_slug)[:MAX_REL].strip('_') or 'source'
        # slugify call name (everything before the first '(')
        call_name = str(self.normalized_call).split('(', 1)[0]
        call_slug = re.sub(r'[^0-9A-Za-z]+', '_', call_name).strip('_').lower()
        call_slug = re.sub(r'_+', '_', call_slug)[:MAX_CALL].strip('_') or 'call'
        return f'{rel_slug}__L{self.lineno}C{self.col_offset}__{call_slug}__{self.artifactHash()}'


## @class CallsiteRecord
## Callsite record class
## 调用点记录类
#
#  A CallsiteRecord separates runtime artifact id, report display text and
#  static matching API.
#  CallsiteRecord用于分离运行产物id、报告展示文本和静态匹配API。
@dataclass(frozen=True)
class CallsiteRecord:
    ## The structured callsite identity
    ## 结构化调用点身份
    identity: CallsiteIdentity

    ## The stable id used by pkl/json/manifest/sharedDict
    ## pkl/json/manifest/sharedDict使用的稳定id
    artifact_id: str

    ## The restored API used for static matching
    ## 静态匹配用的还原API
    format_api: str

    ## The original parameter string of the callsite
    ## 调用点原始参数字符串
    parameters: str

    ## Convert callsite record to dictionary
    ## 将调用点记录转换为字典
    #  @return dict representation of the callsite record
    def toDict(self):
        return {
            'id': self.artifact_id,
            'artifact_hash': self.identity.artifactHash(),
            'rel_path': self.identity.rel_path,
            'lineno': self.identity.lineno,
            'col_offset': self.identity.col_offset,
            'end_lineno': self.identity.end_lineno,
            'end_col_offset': self.identity.end_col_offset,
            'call_text': self.identity.call_text,
            'normalized_call': self.identity.normalized_call,
            'format_api': self.format_api,
            'parameters': self.parameters,
        }


## Normalize call text for identity generation
## 归一化调用文本，用于生成调用点身份
#
#  @param call_text The original call text
#  @return normalized call text
def normalizeCallText(call_text):
    return call_text.replace(' ', '').replace('"', '').replace("'", '')


## Normalize source file path to project relative path
## 将源码路径归一化为项目相对路径
#
#  @param file_path The source file path
#  @param proj_path The project root path
#  @return normalized relative path
def normalizeRelPath(file_path, proj_path=None):
    normalized_file = os.path.abspath(file_path).replace('\\', '/')
    if proj_path:
        normalized_root = os.path.abspath(proj_path).replace('\\', '/').rstrip('/')
        try:
            rel_path = os.path.relpath(normalized_file, normalized_root).replace('\\', '/')
            if not rel_path.startswith('..'):
                return rel_path
        except ValueError:
            pass
    return normalized_file


## Make callsite record
## 构造调用点记录
#
#  @param file_path The source file path
#  @param call_text The original call text
#  @param format_api The restored API for static matching
#  @param parameters The parameter string
#  @param lineno The line number of callsite
#  @param col_offset The column offset of callsite
#  @param end_lineno The end line number of callsite
#  @param end_col_offset The end column offset of callsite
#  @param proj_path The project root path
#  @return callsite record dictionary
def makeCallsiteRecord(
    file_path,
    call_text,
    format_api,
    parameters,
    lineno,
    col_offset,
    end_lineno=None,
    end_col_offset=None,
    proj_path=None,
):
    identity = CallsiteIdentity(
        rel_path=normalizeRelPath(file_path, proj_path),
        lineno=int(lineno),
        col_offset=int(col_offset),
        end_lineno=end_lineno,
        end_col_offset=end_col_offset,
        call_text=call_text,
        normalized_call=normalizeCallText(call_text),
    )
    record = CallsiteRecord(
        identity=identity,
        artifact_id=identity.artifactId(),
        format_api=format_api,
        parameters=parameters,
    )
    return record.toDict()
