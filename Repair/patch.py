## @package patch
#  Generate repair patches without rewriting the source AST
#
#  Uses existing callsite spans and repair results to generate independent
#  Successful/Unknown/Failed patches. Only Successful edits enter the copied
#  project; original files and source bytes outside edited spans stay unchanged.
#  使用已有调用点范围和修复结果生成三类独立补丁，仅将Successful修复写入
#  项目副本，不修改原项目，保留替换范围之外的原始源码字节。



import ast
import difflib
import io
import ntpath
import os
import shutil
import tokenize



## Collect one unambiguous repair result with its original source span
## 收集唯一修复表达式及其原始源码范围
#
#  @param record Structured callsite record with original call text and source span
#  @param fixedAPI Fixed API call expression returned by repairTask
#  @param repairStatus Repair status: Successful, Unknown, or Failed
#  @return An edit dictionary, or None for ambiguous/empty/unchanged results
def makePatchEdit(record,fixedAPI,repairStatus):
    if not isinstance(fixedAPI,str) or repairStatus not in ('Successful','Unknown','Failed'):
        return None
    try:
        original=ast.parse(record['call_text'],mode='eval').body
        fixed=ast.parse(fixedAPI,mode='eval').body
    except (KeyError,SyntaxError,ValueError):
        return None
    if not isinstance(original,ast.Call) or not isinstance(fixed,ast.Call):
        return None
    if ast.dump(original)==ast.dump(fixed):
        return None
    edit={key:record.get(key) for key in (
        'id','rel_path','lineno','col_offset','end_lineno','end_col_offset','call_text',
    )}
    edit['fixed_api']=fixedAPI
    edit['repair_status']=repairStatus
    return edit



## Apply non-overlapping edits using UTF-8 byte offsets from the original AST
## 根据原始AST的UTF-8字节位置应用不重叠的修复
#
#  Unsafe edits are skipped and logged; a syntax-invalid file is not emitted.
#  不安全的修复跳过并记录日志，合并后语法无效的文件不输出。
#  @param sourceBytes Original UTF-8 source file bytes, optionally with BOM
#  @param edits List of edit dictionaries for this source file
#  @return (modifiedBytes,errorList)
def applyEdits(sourceBytes,edits):
    errLst=[]
    try:
        source=sourceBytes.decode('utf-8-sig')
        root=ast.parse(source)
        lines=source.splitlines(keepends=True)
        byteLines=sourceBytes.splitlines(keepends=True)
        lineOffsets=[]
        offset=0
        for line in byteLines:
            lineOffsets.append(offset)
            offset+=len(line)
        if sourceBytes.startswith(b'\xef\xbb\xbf'):
            lineOffsets[0]+=3
        callNodes={(node.lineno,node.col_offset,node.end_lineno,node.end_col_offset):node
                   for node in ast.walk(root) if isinstance(node,ast.Call)}
        commentOffsets=[]
        for token in tokenize.generate_tokens(io.StringIO(source).readline):
            if token.type==tokenize.COMMENT:
                line,column=token.start
                commentOffsets.append(lineOffsets[line-1]+len(lines[line-1][:column].encode('utf-8')))
    except (UnicodeError,SyntaxError,ValueError,tokenize.TokenError) as e:
        return sourceBytes,[f'Patch skipped: cannot parse source: {e}\n']

    candidates=[]
    for edit in edits:
        callId=edit.get('id','unknown')
        try:
            span=tuple(edit.get(key) for key in ('lineno','col_offset','end_lineno','end_col_offset'))
            if span not in callNodes:
                raise ValueError('missing or invalid callsite span')
            original=ast.parse(edit['call_text'],mode='eval').body
            if ast.dump(original)!=ast.dump(callNodes[span]):
                raise ValueError('original call does not match the source span')
            fixed=ast.parse(edit['fixed_api'],mode='eval').body
            if not isinstance(fixed,ast.Call):
                raise ValueError('repair result is not a single call expression')
            start=lineOffsets[span[0]-1]+span[1]
            end=lineOffsets[span[2]-1]+span[3]
            if any(start<=offset<end for offset in commentOffsets):
                raise ValueError('callsite contains comments that replacement would remove')
            candidates.append((start,end,edit))
        except (KeyError,TypeError,SyntaxError,ValueError) as e:
            errLst.append(f'Patch skipped for {callId}: {e}\n')

    candidates.sort(key=lambda item:item[0])
    overlaps=set()
    for index,(start,end,edit) in enumerate(candidates):
        for other in range(index+1,len(candidates)):
            if candidates[other][0]>=end:
                break
            overlaps.update((index,other))
    modified=sourceBytes
    newline='\r\n' if b'\r\n' in sourceBytes else '\n'
    for index in range(len(candidates)-1,-1,-1):
        start,end,edit=candidates[index]
        if index in overlaps:
            errLst.append(f"Patch skipped for {edit['id']}: overlapping callsite spans\n")
            continue
        replacement=edit['fixed_api'].replace('\r\n','\n').replace('\n',newline).encode('utf-8')
        modified=modified[:start]+replacement+modified[end:]
    try:
        ast.parse(modified.decode('utf-8-sig'))
    except (SyntaxError,ValueError) as e:
        errLst.append(f'Patch skipped: modified file has invalid syntax: {e}\n')
        return sourceBytes,errLst
    return modified,errLst



## Write independent category patches and a Successful-only project copy
## 写出三类独立补丁及仅含Successful修复的项目副本
#
#  Every category is compared with the original project, not another category.
#  各类别均与原项目比较，不在其他类别补丁上叠加。
#  @param projPath Original project root path
#  @param projName Project directory name used in fixed_project output
#  @param edits List of collected edit dictionaries from all project files
#  @param reportDir Internal report directory for the current run command
#  @return Error messages to append to the existing repair log
def writeRepairArtifacts(projPath,projName,edits,reportDir):
    errLst=[]
    projPath=os.path.realpath(projPath)
    reportDir=os.path.realpath(reportDir)
    try:
        if os.path.commonpath((projPath,reportDir))==projPath:
            return ['Patch skipped: report directory is inside the original project\n']
    except ValueError:
        pass #Windows的项目和报告允许位于不同盘符
    patchDir=os.path.join(reportDir,'patches')
    fixedDir=os.path.join(reportDir,'fixed_project')
    try:
        os.makedirs(patchDir,exist_ok=True)
        os.makedirs(fixedDir,exist_ok=True)
    except OSError as e:
        return [f'Patch output failed: {e}\n']

    fileEdits={}
    for edit in edits:
        try:
            relativePath=edit['rel_path'].replace('\\','/')
            if ntpath.isabs(relativePath) or ntpath.splitdrive(relativePath)[0] \
                    or any(part in ('','..','.') for part in relativePath.split('/')) \
                    or any(char in relativePath for char in '\t\r\n'):
                raise ValueError('invalid project-relative path')
            file=os.path.join(projPath,*relativePath.split('/'))
            if os.path.commonpath((projPath,os.path.realpath(file)))!=projPath:
                raise ValueError('source file is outside the original project')
            if os.path.realpath(file)!=os.path.abspath(file):
                raise ValueError('source file uses a symbolic link')
            status=edit['repair_status']
            if status not in ('Successful','Unknown','Failed'):
                raise ValueError('invalid repair status')
            fileEdits.setdefault(relativePath,{}).setdefault(status,[]).append(edit)
        except (KeyError,TypeError,AttributeError,ValueError) as e:
            errLst.append(f"Patch skipped for {edit.get('id','unknown')}: {e}\n")

    patches={status:[] for status in ('Successful','Unknown','Failed')}
    successfulFiles={}
    for relativePath in sorted(fileEdits):
        file=os.path.join(projPath,*relativePath.split('/'))
        try:
            with open(file,'rb') as fr:
                originalBytes=fr.read()
            for status,categoryEdits in fileEdits[relativePath].items():
                modifiedBytes,errors=applyEdits(originalBytes,categoryEdits)
                errLst.extend(f'{relativePath} <{status}>: {error}' for error in errors)
                if modifiedBytes==originalBytes:
                    continue
                #保留diff内容行的原始换行；无末尾换行时添加git补丁标记
                diff=difflib.unified_diff(
                    originalBytes.decode('utf-8').splitlines(keepends=True),
                    modifiedBytes.decode('utf-8').splitlines(keepends=True),
                    fromfile=f'a/{relativePath}\t',tofile=f'b/{relativePath}\t',
                )
                patch=[]
                for line in diff:
                    patch.append(line if line.endswith('\n') else line+'\n\\ No newline at end of file\n')
                patches[status].extend(patch)
                if status=='Successful':
                    successfulFiles[relativePath]=modifiedBytes
        except (OSError,UnicodeError,ValueError) as e:
            errLst.append(f'Patch skipped for {relativePath}: {e}\n')

    if successfulFiles:
        try:
            #不跟随项目中的链接，避免把项目外部内容复制进输出
            fixedProject=os.path.join(fixedDir,projName)
            shutil.copytree(projPath,fixedProject,ignore=lambda directory,names:[
                name for name in names if os.path.islink(os.path.join(directory,name))
            ])
            for relativePath,modifiedBytes in successfulFiles.items():
                with open(os.path.join(fixedProject,*relativePath.split('/')),'wb') as fw:
                    fw.write(modifiedBytes)
        except OSError as e:
            errLst.append(f'Fixed project output failed: {e}\n')

    for status,patch in patches.items():
        if patch:
            try:
                with open(os.path.join(patchDir,f'{status.lower()}.patch'),'wb') as fw:
                    fw.write(''.join(patch).encode('utf-8'))
            except OSError as e:
                errLst.append(f'Patch output failed for {status}: {e}\n')
    return errLst
