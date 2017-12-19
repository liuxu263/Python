#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'两个字符串连接程序。'

__author__ = 'lx'

if __name__ == "__main__":
    a = "qaweqwe"
    b = "dsfjskldfj"

    # 连接字符串
    c = a + b
    print(c)

    str = ''
    str = str.join([a, b, c])
    print(str)
