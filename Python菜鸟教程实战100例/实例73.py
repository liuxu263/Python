#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'反向输出一个链表'

__author__ = 'lx'


if __name__ == '__main__':
    ptr = []
    for i in range(5):
        ptr.append(int(input('请输入一个数:\n')))
    print(ptr)
    ptr.reverse()
    print(ptr)