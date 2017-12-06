#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'学习使用按位或\ 。'
"""
0|0=0; 0|1=1; 1|0=1; 1|1=1

"""

__author__='lx'

if __name__=="__main__":
    a=0o77
    b=a|3
    print("a|3 is %d"%b)
    b|=7
    print("b|7 is %d"%b)