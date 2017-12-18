#! /usr/bin/env python3
#  -*- coding：utf-8 -*-

'八进制转换为十进制'

__author__ = 'lx'


def f8to10(num):
    print("8进制数：%s" % num)
    l = str(num)
    length = len(l)
    sum = 0
    for i in range(length):
        sum += 8 ** (length - i - 1) * int(l[i])
    print("转换为10进制数为：%s" % sum)


f8to10(122)
f8to10(1111)
