#!/usr/bin/env python3 标准注释 可以让.py文件直接在Unix/Linux/Mac上运行
# -*- coding: utf-8 -*- 标准注释 表示.py文件本身使用标准UTF-8编码

'有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？'#注释

__author__='lx' #作者

#方法一
#d=[]
#for i in range(1,5):
#   for j in range(1,5):
#	    for k in range(1,5):
#		    if(i!=k) and (j!=i) and (j!=k):
#			    d.append([i,j,k])
#print("总数量:",len(d))
#print(d)

#方法二
from itertools import permutations

for i in permutations([1,2,3,4],3):
    print(i)