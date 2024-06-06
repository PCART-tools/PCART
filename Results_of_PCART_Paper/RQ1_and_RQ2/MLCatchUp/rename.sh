#!/bin/bash

# 要搜索的目录
# search_dir="pandas/DataFrame.to_excel@1.5.3-2.0.0"

# # 使用find命令查找所有包含'YN'的目录
# # -type d 表示搜索目录
# # -name '*YN*' 表示目录名中包含YN
# find "$search_dir" -type d -name '*YN*' | while read -r dir; do
#     # 新的目录名，用NN替换YN
#     new_dir=$(echo "$dir" | sed 's/YN/NN/g')

#     # 重命名目录
#     mv "$dir" "$new_dir"
# done



# 目标目录路径
dir_path="matplotlib/matplotlib.axes.Axes.imshow@3.4.3-3.5.0"  # 替换为你的目录路径

# 读取文件内容到数组
lines=("${(@f)$(<temp.txt)}")

# 遍历目录的一级子目录
for subdir in "$dir_path"/*; do
    if [ -d "$subdir" ]; then  # 确保是目录
        subdir_name=$(basename "$subdir")
        num="${subdir_name#*#}"
        #检查每个列表项是否在子目录名中
        for line in "${lines[@]}"; do
            if [[ "$num" == "$line" ]]; then
                # 替换YY为NY
                new_name="${subdir_name/YY/NY}"
                mv "$subdir" "${subdir%$subdir_name}$new_name"
                echo "Renamed $subdir_name to $new_name"
                # 如果目录已经成功重命名，接下来更改目录内文件名
                for file in "${subdir%$subdir_name}${new_name}"/*.py; do
                    if [ -f "$file" ]; then
                        file_name=$(basename "$file")
                        new_file_name="${file_name/YY/NY}"
                        mv "$file" "${file%$file_name}$new_file_name"
                        echo "Renamed $file_name to $new_file_name within $new_name"
                    fi
                done
                # 删除新目录中AYY中以.json和.txt结尾的文件
                find "${subdir%$subdir_name}${new_name}" -type f \( -name "*.json" -o -name "*.txt" \) -delete
                echo "Deleted .json and .txt files in $new_name"
                break
            fi
        done
    fi
done