#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

'判断101-200之间有多少个素数，并输出所有素数。'

__author__='lx'

l=[]
for i in range(101,200):
    l.append(i)
    for j in  range(2,i-1):
        if i%j==0:
            l.pop()
            break


print(l)
print("总数为：%d"%len(l))