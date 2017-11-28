#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。'

__author__='lx'

a=input("输入一串数字：")
b=a[::-1]
if a==b:
    print("%s是回文数"%a)
else:
    print("%s不是回文数"%a)
1