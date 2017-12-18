#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'字符串排序。按首字母排序，如果相同就依次向后比较'

__author__ = 'lx'

l=[]

for i in range(3):
    l.append(input("请输入一个字符串:\n"))
l.sort()
print(l)