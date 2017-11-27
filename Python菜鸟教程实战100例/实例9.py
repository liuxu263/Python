#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

'暂停一秒输出'

__author__='lx'

import time
dict ={'1':'a','2':'b'}
for key,value in dict.items():
    print( key,value)
    time.sleep(1)#暂停1秒