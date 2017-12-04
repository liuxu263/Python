#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'数字比较。'

__author__='lx'

def compare(num1,num2):
    if num1>num2:
        print("%d大于%d"%(num1,num2))
    elif num2>num1:
        print("%d大于%d"%(num2,num1))
    else:
        print("%d等于%d"%(num1,num2))

if __name__ =='__main__':
    num1=int(input('第一个数为：\n'))
    num2=int(input('第二个数为：\n'))
    compare(num1,num2)
