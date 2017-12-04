#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'使用lambda来创建匿名函数。'

__author__='lx'

MAXINUM =lambda x,y:(x>y)*x+(x<y)*y
MININUM =lambda x,y:(x>y)*y+(x<y)*x

if __name__=='__main__':
    a=10
    b=20
    print("最大的数为：%d" % MAXINUM(a, b))
    print("最小的数为：%d" % MININUM(a, b))