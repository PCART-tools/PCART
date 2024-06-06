#!/bin/bash

# 函数：递归处理目录
process_directory() {
  local dir=$1

  # 遍历目录下的所有文件和子目录
  for entry in "$dir"/*; do
    if [[ -f "$entry" && ${entry##*.} == "py" ]]; then
      # 处理 .py 文件
      process_file "$entry"
    elif [[ -d "$entry" ]]; then
      # 递归处理子目录
      process_directory "$entry"
    fi
  done
}

# 函数：处理文件
process_file() {
  local file=$1

  # 检查文件是否可读
  if [[ -r "$file" ]]; then
    # 将制表符转换为空格，并覆盖原文件
    expand -t 4 "$file" > "$file.tmp" && mv "$file.tmp" "$file"
    # echo "已转换文件: $file"
  fi
}

# 指定目标目录
# target_dir="/home/zhang/Code/Python/Automatic-Repair-Tool/Copy/3d_ken_burns"
target_dir="Copy"

# 开始处理目录
process_directory "$target_dir"
