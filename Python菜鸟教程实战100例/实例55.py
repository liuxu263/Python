#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'学习使用按位取反~。'
"""
~0=1; ~1=0; 
取反码的方法，对于给定的数x
1 取反
2 判断正负 若正 取反的二进制数加1 若负取反的二进制数减1
3 取反
对于x  ~x=-x-1

"""

if __name__=='__main__':
    a=234
    b=~a
    print("The a \`s 1 complement is %d" % b)
    a=~b
    print("The a \`s 1 complement is %d" % a)