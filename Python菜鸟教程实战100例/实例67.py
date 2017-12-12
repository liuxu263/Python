#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。'

__author__ = 'lx'

a = [43, 2, 3, 1, 4543, 3, 543, 3, 44, 55]
for i in range(0, len(a) - 1):
    if a[i] == min(a):
        a[0], a[i] = a[i], a[0]
for i in range(0, len(a) - 1):
    if a[i] == max(a):
        a[len(a) - 1], a[i] = a[i], a[len(a) - 1]
print("调整顺序后为：")
print(a)
