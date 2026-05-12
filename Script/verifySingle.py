## @file verifySingle.py
## A dynamic script used for dynamic validation of single API call
## @ingroup script
## @page verify_single Validate Single API Call
##
## Used by Repair/repair.py

import sys
import dill

# Load the pkl file containing the repaired API's receiver object and parameter values
# 加载pkl文件，其中包含修复后API的接收者对象和参数值
pklPath=sys.argv[1]
callAPI=sys.argv[2]
with open(pklPath,'rb') as fr:
    paraValueDict=dill.load(fr)

# The callAPI string is a pre-constructed Python expression that includes
# parameter values filled in from the pkl (by addValueForAPI.py).
# Evaluating it executes the call in the target environment to verify it runs.
# callAPI是addValueForAPI.py填入了pkl参数值后预构造的Python表达式，
# eval执行它以在目标环境中验证修复后调用是否能成功运行。
print(callAPI)
eval(callAPI)
