#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。'

__author__='lx'

a=2.0
b=1.0
s=0.0
for n in range(1,21):
    s+=a/b
    b,a=a,a+b
print(s)