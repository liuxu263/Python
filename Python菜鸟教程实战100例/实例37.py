#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'对10个数进行排序'

__author__='lx'

print("请输入10个数字")
a=list()
for n in range(10):
    a.append(input('输入一个数字:\n'))
a.sort()
print(a)