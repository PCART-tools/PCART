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


## Get the pkl output directory
## 获取pkl输出目录
#
#  @return The pkl output directory
def getPklDir():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), PCART_PKL_REL_PATH)


## Get the pkl file name for one callsite candidate
## 获取单个调用点候选的pkl文件名
#
#  @param key The callsite key
#  @param suffix The candidate suffix
#  @return The pkl file name
def getPklName(key,suffix):
    if PCART_USE_CALLSITE_NAME:
        pklName=getFileName(key,'.pkl')
        if suffix:
            pklName=pklName[:-4]+suffix+'.pkl'
    else:
        pklName='paraValue'+suffix+'.pkl'
    return pklName


## Build pkl candidate list for one receiver
## 构造单个接收者的pkl候选列表
#
#  @param receiver The receiver object or receiver candidate dict
#  @return The pkl candidate list
def getCandidateList(receiver):
    candidates=[]
    if isinstance(receiver, dict) and ('object' in receiver or 'expr' in receiver):
        if 'object' in receiver:
            candidates.append(('__object', receiver['object']))
        if 'expr' in receiver:
            candidates.append(('__expr', receiver['expr']))
    else:
        candidates.append(('', receiver))
    return candidates


## Write one pkl candidate file
## 写入单个pkl候选文件
#
#  @param pklDir The pkl output directory
#  @param pklName The pkl file name
#  @param tempDict The value dictionary to save
def writePklCandidate(pklDir,pklName,tempDict):
    tmpPklName=pklName+'.tmp'
    tmpPath=os.path.join(pklDir,tmpPklName)
    with open(tmpPath, 'wb') as fw:
        dill.dump(tempDict,fw)
    os.replace(tmpPath,os.path.join(pklDir,pklName))


## Save collected runtime values to pkl files
## 将收集到的运行时值保存到pkl文件
def savePkls():
    pklDir=getPklDir()
    os.makedirs(pklDir,exist_ok=True)
    for key, value in paraValueDict.items():
        if '@' in key:
            continue
        k='@{}'.format(key)
        receiver=paraValueDict.get(k)
        candidateManifest={
            'callsite': key,
            'covered': True,
            'candidates': [],
        }
        manifestName=getFileName(key,'.manifest.json')
        for suffix, receiverValue in getCandidateList(receiver):
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
            pklName=getPklName(key,suffix)
            candidateInfo['pkl']=pklName
            try:
                writePklCandidate(pklDir,pklName,tempDict)
                candidateInfo['status']='saved'
            except BaseException as e:
                tmpPath=os.path.join(pklDir,pklName+'.tmp')
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
