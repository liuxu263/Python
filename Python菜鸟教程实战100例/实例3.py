#!/usr/bin/env python3 标准注释 可以让.py文件直接在Unix/Linux/Mac上运行
# -*- coding: utf-8 -*- 标准注释 表示.py文件本身使用标准UTF-8编码

'一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？'

__author__='lx' #作者

for i in range(1,85):
    if 168 % i == 0:
        j = 168 / i;
        if  i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0 :
            m = (i + j) / 2
            n = (i - j) / 2
            x = n * n - 100
            print(x)