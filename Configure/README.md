#  Configure Directory 配置文件目录

##  English Description

This directory contains input configuration files (in JSON format) for PCART.

Each configuration file includes:
- `projPath`: Path to the project directory.
- `runCommand`: The exact command to run the project.
- `runFilePath`: Specific run file path if not directly in the first-level subdirectory, or set to "".
- `libName`: Name of the upgraded Python library used (e.g., `torch`, `tensorflow`).
- `currentVersion`: Version of the library currently in use.
- `targetVersion`: Version intended to be used for migration.
- `currentEnv`: Path to the conda environment of the library's current version.
- `targetEnv`: Path to the conda environment of the library's upgraded version.


---

## 中文说明

该目录用于存放PCART的输入配置脚本。

每个配置文件包含以下字段：
- `projPath`：项目所在路径。
- `runCommand`：实际运行命令。
- `runFilePath`：若运行文件不在项目的一级子目录，则填写目录名称，否则留空""。
- `libName`：待升级的Python库名称，如 `torch` 或 `tensorflow`。
- `currentVersion`：当前使用的库版本。
- `targetVersion`：计划迁移的目标库版本。
- `currentEnv`：当前库版本的conda虚拟环境路径。
- `targetEnv`：目标库版本虚拟环境路径。


---

## Example Configuration File (AIBO.json)

```json
{
    "projPath": "Example/AIBO",
    "runCommand": "python run.py --func=Ackley --dim=100 --method=anneal --iters=5000 --batch-size=10",
    "runFilePath":"",
    "libName": "scipy",
    "currentVersion": "1.7.3",
    "targetVersion": "1.10.0",
    "currentEnv": "/dataset/zhang/anaconda3/envs/AIBO1.7.3",
    "targetEnv": "/dataset/zhang/anaconda3/envs/AIBO1.10.0"
}


