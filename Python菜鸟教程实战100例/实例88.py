#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。'

__author__ = 'lx'

def f(n):
    for i in  range(n):
        print("*",end='')
    print()

if __name__=="__main__":
    for i in range(7):
        a=int(input("请输入一个数：\n"))
        if a>0 and a<50:
            f(a)
        else:
            print("输入有误！！！")
            i-=1
