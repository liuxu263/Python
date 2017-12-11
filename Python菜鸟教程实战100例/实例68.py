#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数'

__author__ = 'lx'

m = 3
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def rot(a, n):
    l = len(a)
    n = l - n
    return a[n:l] + a[0:n]


b = rot(a, m)
print(a)
print(b)
