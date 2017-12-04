#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'求输入数字的平方，如果平方运算后小于 50 则退出。'

__author__='lx'


while(1):
    n = int(input('请输入一个数字：'))

    if n**2<50:
        print("平方运算后小于50")
        quit()
    else:
        print("运算结果为：%d" % (n ** 2))
        print('请继续输入')