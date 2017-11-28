#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。'

__author__='lx'

num=list(input("输入一个最多5位的数字："))

l=len(num)
print("数字是%d位数"%l)
num.reverse()
for i in range(l):
    print(num[i],end='')