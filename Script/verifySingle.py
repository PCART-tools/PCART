## @file verifySingle 
#  A dynamic script used for dynamic validation of single API call 

import sys
import dill

pklPath=sys.argv[1]
callAPI=sys.argv[2]
with open(pklPath,'rb') as fr:
    paraValueDict=dill.load(fr)

print(callAPI)
eval(callAPI)
