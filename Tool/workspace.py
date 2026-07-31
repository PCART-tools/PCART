## @package workspace
#  Run workspace helpers for isolating PCART execution artifacts
#
#  Provides createRunWorkspace() to create isolated run directories under
#  PCARTRuns/runs/ with unique run_id and command_id, exportRunReport() to
#  export internal reports to Report/runs/, and workspaceCwd() for temporary
#  working directory switching. Each workspace contains Copy/, Dynamic/, data/,
#  temp/, Report/ subdirectories and a metadata.json snapshot.
#  提供createRunWorkspace()在PCARTRuns/runs/下创建带唯一run_id和command_id的
#  隔离运行目录，exportRunReport()导出内部报告到Report/runs/，workspaceCwd()
#  用于临时切换工作目录。每个工作区包含Copy/、Dynamic/、data/、temp/、Report/
#  子目录和metadata.json快照。
#
#  提供PCART运行工作区的创建、编号、元数据记录和报告导出能力


import json
import os
import re
import shutil
from contextlib import contextmanager
from dataclasses import asdict,dataclass
from datetime import datetime


## @class RunWorkspace
## Run workspace path object
## PCART单次运行的工作区路径对象
#
#  This object keeps all paths generated for one command execution.
#  该对象集中保存一次命令执行产生的所有运行目录。
@dataclass
class RunWorkspace:
    repo_root: str
    run_id: str
    command_id: str
    run_root: str
    workspace_root: str
    copy_root: str
    dynamic_root: str
    data_dir: str
    temp_dir: str
    internal_report_dir: str
    report_root: str
    metadata_path: str


## Get PCART repository root path
## 获取PCART仓库根目录路径
#
#  @return The absolute repository root path
def getRepoRoot():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


## Convert project path/name to a filesystem-safe slug
## 将项目路径或项目名转换为可作为目录名使用的slug
#
#  @param projPath The project path or project name
#  @return A safe project slug used in run id
def slugifyProjectName(projPath):
    normalized=str(projPath).strip().rstrip('/\\')
    if not normalized:
        return 'project'
    name=re.split(r'[\\/]+',normalized)[-1]
    slug=re.sub(r'[^A-Za-z0-9._-]+','-',name).strip('.-_')
    return slug or 'project'


## Allocate next run id under runs root
## 在运行目录下分配下一个run id
#
#  The directory is created with os.mkdir so concurrent PCART processes do not
#  acquire the same id.
#  通过os.mkdir原子创建目录，避免并发运行获取到相同编号。
#
#  @param runsRoot The root directory containing all run instances
#  @param projectSlug The safe project slug
#  @param timestamp Timestamp string used in run id
#  @return (runId, runRoot) tuple
def _nextRunId(runsRoot,projectSlug,timestamp):
    prefix=f'{projectSlug}__{timestamp}'
    for index in range(1, 1000):
        runId=f'{prefix}-{index:03d}'
        runRoot=os.path.join(runsRoot,runId)
        try:
            os.mkdir(runRoot)
            return runId, runRoot
        except FileExistsError:
            continue
    raise RuntimeError(f'Cannot allocate run id for {prefix}')


## Create an isolated workspace for one PCART run command
## 为一次PCART运行命令创建隔离工作区
#
#  The workspace stores intermediate Copy/Dynamic/data/temp/Report artifacts
#  under PCARTRuns, while user-visible reports are exported under Report/runs.
#  运行中间态保存在PCARTRuns中，用户可见报告导出到Report/runs中。
#
#  @param repoRoot The PCART repository root path
#  @param projPath The project path under test
#  @param runCommand The project run command
#  @param runPath The relative path of the run file
#  @param libName The upgraded Python third-party library name
#  @param currentVersion The current library version
#  @param targetVersion The target library version
#  @param currentEnv The virtual environment for current library version
#  @param targetEnv The virtual environment for target library version
#  @param commandId The command id under this run, default cmd-001
#  @param timestamp Optional timestamp, mainly used by tests
#  @return RunWorkspace object
def createRunWorkspace(
    repoRoot,
    projPath,
    runCommand,
    runPath,
    libName,
    currentVersion,
    targetVersion,
    currentEnv,
    targetEnv,
    commandId='cmd-001',
    timestamp=None,
):
    repoRoot=os.path.abspath(repoRoot)
    timestamp=timestamp or datetime.now().strftime('%Y%m%d-%H%M%S')
    projectSlug=slugifyProjectName(projPath)
    runsRoot=os.path.join(repoRoot,'PCARTRuns','runs')
    os.makedirs(runsRoot, exist_ok=True)
    runId,runRoot=_nextRunId(runsRoot,projectSlug,timestamp)

    workspaceRoot=os.path.join(runRoot,commandId)
    os.mkdir(workspaceRoot)
    copyRoot=os.path.join(workspaceRoot,'Copy')
    dynamicRoot=os.path.join(workspaceRoot,'Dynamic')
    dataDir=os.path.join(workspaceRoot,'data')
    tempDir=os.path.join(workspaceRoot,'temp')
    internalReportDir=os.path.join(workspaceRoot,'Report')
    reportRoot=os.path.join(repoRoot,'Report','runs',runId,commandId)
    metadataPath=os.path.join(workspaceRoot,'metadata.json')

    for path in (
        copyRoot,
        dynamicRoot,
        dataDir,
        tempDir,
        internalReportDir,
        reportRoot,
        os.path.join(reportRoot,'patches'),
        os.path.join(reportRoot,'fixed_project'),
    ):
        os.makedirs(path,exist_ok=True)

    workspace=RunWorkspace(
        repo_root=repoRoot,
        run_id=runId,
        command_id=commandId,
        run_root=runRoot,
        workspace_root=workspaceRoot,
        copy_root=copyRoot,
        dynamic_root=dynamicRoot,
        data_dir=dataDir,
        temp_dir=tempDir,
        internal_report_dir=internalReportDir,
        report_root=reportRoot,
        metadata_path=metadataPath,
    )
    writeMetadata(
        workspace,
        {
            'project_slug': projectSlug,
            'project_path': projPath,
            'run_command': runCommand,
            'run_file_path': runPath,
            'lib_name': libName,
            'current_version': currentVersion,
            'target_version': targetVersion,
            'current_env': currentEnv,
            'target_env': targetEnv,
        },
    )
    return workspace


## Write workspace metadata
## 写入运行工作区元数据
#
#  @param workspace The RunWorkspace object
#  @param metadata Additional metadata collected from config
#  @return None
def writeMetadata(workspace,metadata):
    content=asdict(workspace)
    content.update(metadata)
    with open(workspace.metadata_path,'w',encoding='utf-8') as fw:
        json.dump(content,fw,ensure_ascii=False,indent=2)


## Return runtime artifact paths for the current execution
## 返回当前执行使用的运行产物路径
#
#  Internal pipeline code should use these paths instead of cwd-relative
#  Copy/Dynamic/data/Report paths.
#  流水线内部代码应使用这些路径，而非相对于当前工作目录的Copy/Dynamic/data/Report路径。
#  @param workspace RunWorkspace object
#  @return Dict of Copy/Dynamic/data/temp/Report roots
def getRuntimePaths(workspace):
    return {
        'workspace_root': workspace.workspace_root,
        'copy_root': workspace.copy_root,
        'dynamic_root': workspace.dynamic_root,
        'data_dir': workspace.data_dir,
        'temp_dir': workspace.temp_dir,
        'report_dir': workspace.internal_report_dir,
    }


## Temporarily switch current working directory
## 临时切换当前工作目录
#
#  @param path The working directory used during the context
#  @return Context manager that restores the previous working directory
#  @fn workspaceCwd
@contextmanager
def workspaceCwd(path):
    previous=os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(previous)


## Export internal report files to user-visible report directory
## 将工作区内部报告导出到用户可见报告目录
#
#  @param workspace The RunWorkspace object
#  @return None
def exportRunReport(workspace):
    os.makedirs(workspace.report_root, exist_ok=True)
    os.makedirs(os.path.join(workspace.report_root,'patches'),exist_ok=True)
    os.makedirs(os.path.join(workspace.report_root,'fixed_project'),exist_ok=True)
    if not os.path.isdir(workspace.internal_report_dir):
        return
    for name in os.listdir(workspace.internal_report_dir):
        source=os.path.join(workspace.internal_report_dir,name)
        target=os.path.join(workspace.report_root,name)
        if os.path.isdir(source):
            if os.path.exists(target):
                shutil.rmtree(target)
            shutil.copytree(source,target)
        else:
            shutil.copy2(source,target)


## Remove one completed PCART run workspace
## 删除一次已完成的PCART运行工作区
#
#  Only a direct child of <repo>/PCARTRuns/runs can be removed.
#  只允许删除<repo>/PCARTRuns/runs的直接子目录。
#
#  @param workspace RunWorkspace object for this execution
#  @return None
def cleanupRunWorkspace(workspace):
    runsRoot=os.path.realpath(
        os.path.join(workspace.repo_root,'PCARTRuns','runs')
    )
    runRoot=os.path.realpath(workspace.run_root)
    normalizedRunsRoot=os.path.normcase(os.path.normpath(runsRoot))
    normalizedParent=os.path.normcase(
        os.path.normpath(os.path.dirname(runRoot))
    )

    if normalizedParent!=normalizedRunsRoot:
        raise ValueError(
            f'Refuse to remove workspace outside PCARTRuns/runs: {runRoot}'
        )

    if os.path.isdir(runRoot):
        shutil.rmtree(runRoot)
