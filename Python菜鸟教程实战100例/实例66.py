#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'输入3个数a,b,c，按大小顺序输出。'

__author__ = 'lx'

#解法1
"""
if __name__ == '__main__':
    a = int(input("请输入第一个数：\n"))
    b = int(input("请输入第二个数：\n"))
    c = int(input("请输入第三个数：\n"))


    def swap(n1, n2):
        return n2, n1


    if a > b: a, b = swap(a, b)
    if a > c: a, c = swap(a, c)
    if b > c: b, c = swap(b, c)

print("顺序为：%d，%d，%d"%(a,b,c))
"""

#解法2

l=[]
for i in  range (0,3):
    l.append(input("请输入一个数：\n"))
l.sort()
print("顺序为：")
print(l)