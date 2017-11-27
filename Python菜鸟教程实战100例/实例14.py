#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

'将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5'

__author__='lx'

n=input("请输入要分解的正整数：")
n=int(n)
print("%d="%n,end=' ')
i=2
while i<=n:
    if n%i==0:
        if n==i:
            print('%d'%i,end=' ')
            break
        else:
            n=n/i
            print("%d*"%i,end=' ')
    else:
        i=i+1