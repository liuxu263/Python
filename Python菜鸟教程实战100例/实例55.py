#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'学习使用按位取反~。'
"""
~0=1; ~1=0; 

"""

if __name__=='__main__':
    a=234
    b=~a
    print("The a \`s 1 complement is %d" % b)
    a=~b
    print("The a \`s 1 complement is %d" % a)