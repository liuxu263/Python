#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'学习使用按位异或 ^ 。'
"""
0^0=0; 0^1=1; 1^0=1; 1^1=0

"""

__author__='lx'

if __name__=='__main__':
    a=0o77
    b=a^3
    print("The a^3=%d"%b)
    b^=7
    print("The b^3=%d"%b)