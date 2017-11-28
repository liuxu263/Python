#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。'

__author__='lx'

#方法1

#def output(s,l):
#    if l==0:
#        return
#    print(s[l-1])
#    output(s,l-1)

#s=input("Input a string:")
#l=len(s)
#output(s,l)


#方法2
s=input("Input a string:")
l=list(s)
l.reverse()
for i in range(len(l)):
    print(l[i])