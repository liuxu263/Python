#!/usr/bin/env python3 标准注释 可以让.py文件直接在Unix/Linux/Mac上运行
# -*- coding: utf-8 -*- 标准注释 表示.py文件本身使用标准UTF-8编码

'模块的文档注释'

__author__='lx' #作者

year=int(input('year:\n'))
month=int(input('month:\n'))
day=int(input('day:\n'))
months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 < month <= 12:
    sum = months[month - 1]
else:
    print('data error')
sum=sum+day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
print('it is the',sum,'th day.')