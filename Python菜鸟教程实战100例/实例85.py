#! /usr/bin/env python3
#  -*- coding：utf-8 -*-

'输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。'

__author__ = 'lx'

b = int(input("请输入一个奇数：\n"))
a = 9
n = 1
while (1):
    if (a % b == 0):
        break
    else:
        a = a * 10 + 9
        n += 1
print("共需要%s个9可以整除%s" % (n, b))
