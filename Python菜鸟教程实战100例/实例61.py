#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'打印出杨辉三角形'

__author__='lx'


def lst(i,j):
    if i==j or j==1:
        return 1
    else:
        return lst(i-1,j-1)+lst(i-1,j)
if __name__=='__main__':
    n=10
    for i in range(1,n+1):
        for j in  range(1,i+1):
            print(lst(i,j),end=' ')
        print()

