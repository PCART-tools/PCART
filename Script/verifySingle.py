## @file verifySingle.py 
## @brief A dynamic script used for dynamic validation of single API call 
## @ingroup script
## @page verify_single Validate Single API Call
##
## Used by Repair/repair.py

import sys
import dill

pklPath=sys.argv[1]
callAPI=sys.argv[2]
with open(pklPath,'rb') as fr:
    paraValueDict=dill.load(fr)

print(callAPI)
eval(callAPI)
