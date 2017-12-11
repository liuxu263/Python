#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'列表排序及连接'

__author__ = 'lx'

# 排序可使用 sort() 方法，连接可以使用 + 号或 extend() 方法。

if __name__ == '__main__':
    a = [1, 3, 2]
    b = [4, 5, 6]
    a.sort()
    print(a)
    print(a + b)
    a.extend(b)
    print(a)
