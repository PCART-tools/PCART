## @file recordValue.py
## @brief Runtime value recorder used by instrumented project files
## @ingroup script
## @page record_value Runtime Value Recording
##
## Used by Preprocess/preprocess.py

import os
import atexit
import dill
import json
from codeUtils import getFileName


PCART_PKL_REL_PATH='__PCART_PKL_REL_PATH__'
PCART_USE_CALLSITE_NAME=__PCART_USE_CALLSITE_NAME__

paraValueDict={}
apiCoveredSet=set()


## Save collected runtime values to pkl files
## 将收集到的运行时值保存到pkl文件
def savePkls():
    pklDir=os.path.join(os.path.dirname(os.path.abspath(__file__)),PCART_PKL_REL_PATH)
    os.makedirs(pklDir,exist_ok=True)
    for key, value in paraValueDict.items():
        if '@' in key:
            continue
        k='@{}'.format(key)
        receiver=paraValueDict.get(k)
        candidates=[]
        # Receiver may have two fallback forms: runtime object first, expression second
        # 调用者对象可能有两种回退形式：优先运行时对象，其次还原表达式
        if isinstance(receiver,dict) and ('object' in receiver or 'expr' in receiver):
            if 'object' in receiver:
                candidates.append(('__object',receiver['object']))
            if 'expr' in receiver:
                candidates.append(('__expr',receiver['expr']))
        else:
            candidates.append(('',receiver))
        candidateManifest={
            'callsite': key,
            'covered': True,
            'candidates': [],
        }
        manifestName=getFileName(key,'.manifest.json')
        for suffix, receiverValue in candidates:
            candidateKind=suffix[2:] if suffix else 'object'
            candidateInfo={
                'callsite': key,
                'kind': candidateKind,
                'status': 'pending',
                'pkl': None,
            }
            tempDict={}
            tempDict[key]=value
            if receiverValue is not None:
                tempDict[k]=receiverValue
            # PCART_USE_CALLSITE_NAME controls whether pkl files are named by callsite
            # PCART_USE_CALLSITE_NAME控制pkl是否使用调用点命名
            if PCART_USE_CALLSITE_NAME:
                pklName=getFileName(key,'.pkl')
                if suffix:
                    pklName=pklName[:-4]+suffix+'.pkl'
            else:
                pklName='paraValue'+suffix+'.pkl'
            candidateInfo['pkl']=pklName
            tmpPath=os.path.join(pklDir,pklName+'.tmp')
            try:
                # Write tmp file first to avoid leaving broken pkl on dump failure
                # 先写临时文件，避免dump失败时留下损坏的pkl
                with open(tmpPath,'wb') as fw:
                    dill.dump(tempDict,fw)
                os.replace(tmpPath,os.path.join(pklDir,pklName))
                candidateInfo['status']='saved'
            except BaseException as e:
                if os.path.exists(tmpPath):
                    os.remove(tmpPath)
                candidateInfo['status']='save_failed'
                candidateInfo['error']=str(e)
                print('save to pkl error: {}'.format(e))
            candidateManifest['candidates'].append(candidateInfo)
        with open(os.path.join(pklDir,manifestName),'w',encoding='utf-8') as fw:
            json.dump(candidateManifest,fw,indent=4,ensure_ascii=False)
    with open(os.path.join(pklDir,'coverSet'),'w',encoding='utf-8') as fw:
        for it in apiCoveredSet:
            fw.write(it+'\n')


atexit.register(savePkls)
