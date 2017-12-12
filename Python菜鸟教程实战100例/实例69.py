#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。'

__author__ = 'lx'

n = int(input("输入人数：\n"))
list = []
for i in range(1, n + 1):
    list.append(i)

sum = 0
while 1:
    t = 0
    for i in range(1, len(list) + 1):
        sum += 1
        if sum % 3 == 0:
            list.pop(i - 1 - t)
            # 退出一个人后，list的结构就发生了改变！！！
            t = t + 1
    if len(list) == 1:
        print('最后留下的是原来第%d号的那位' % list[0])
        break
