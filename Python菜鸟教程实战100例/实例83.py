#! /usr/bin/env python3
#  -*- coding：utf-8 -*-

'求0—7所能组成的奇数个数。'

__author__ = 'lx'


def f(n):
    sum = 0
    if n == 1:
        sum = 4
    else:
        sum = 7 * 8 ** (n - 2) * 4
    return sum


if __name__ == '__main__':
    for i in range(1, 9):
        print("组成%s位数是%s个" % (i, f(i)))
