#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
    >>> python test.py test.mp3
'''

import os, sys
from acrcloud.recognizer import ACRCloudRecognizer
from acrcloud.recognizer import ACRCloudRecognizeType
import json
import ast
import song

def recognize(file_name):
    config = {
        'host':'identify-cn-north-1.acrcloud.com',
        'access_key':'a2027bf3a7998a47874e361ad626409e',
        'access_secret':'n8u8aoLWvqqM5v3Gg6wDPxya8VpnwIpYreq7JrMx',
        'recognize_type': ACRCloudRecognizeType.ACR_OPT_REC_AUDIO,
        'debug':False,
        'timeout':10 # seconds
    }
    
    print('config ok')
    '''This module can recognize ACRCloud by most of audio/video file. 
        Audio: mp3, wav, m4a, flac, aac, amr, ape, ogg ...
        Video: mp4, mkv, wmv, flv, ts, avi ...'''
    re = ACRCloudRecognizer(config)
    
    print('read config ok')
    
    res=json.loads(re.recognize_by_file(file_name))
    
    number=len(res['metadata']['music'])
    songList=[]
    for i in range(number):
        song={}
        song["name"]=res['metadata']['music'][i]['title']
        song["singer"]=res['metadata']['music'][i]['artists'][0]['name']
        songList.append(song)
    
    result={}
    result["songlist"]=songList

    #result=json.loads(result)
    result=str(result)
    
    return result.replace('u\'', '\'')

#song.download(res['metadata']['music'][0]['title'])
