#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'利用递归方法求5!。'

__author__='lx'

def f(j):
    sum=0
    if j==0:
        sum=1
    else:
        sum=j*f(j-1)
    return sum
for i in range(0,6):
    print("%d!=%d"%(i,f(i)))
