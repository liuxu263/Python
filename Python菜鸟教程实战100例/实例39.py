#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中'

__author__='lx'

list=[1,2,3,4,5,6,7,8,10,11]
print("插入数字前的列表为：")
print(list)
n=int(input("输入要插入的数字：\n"))
for i in range(0,10):
    if list[i]<n<list[i+1]:
        list.insert(i+1,n)
print("插入数字后的列表为：")
print(list)