#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'打印出如下图案（菱形）:'
#   *
#  ***
# *****
#*******
# *****
#  ***
#   *

__author__='lx'

for i in range(1,5):
    print(' '*(4-i),end="")
    for j in range(1,2*i):
        print('*',end="")
    print()
for i in  range(3,0,-1):
    print(' '*(4-i),end="")
    for j in range(1,2*i):
        print('*',end="")
    print()