#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度。'

__author__ = 'lx'


def f(str):
    print("字符串%s的长度为%d" % (str, len(str)))


if __name__ == '__main__':
    str = input('输入一个字符串：\n')
    f(str)
