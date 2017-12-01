#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'求100之内的素数'

__author__='lx'

# 输出指定范围内的素数
# 用户输入数据

lower=int(input("输入区间最小值："))
upper=int(input("输入区间最大值："))

for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
#这个else的位置还是挺关键的，例如某一个num，应该是它循环完i的值从2到num-1之后再决定是否输出它
        else:
            print(num)

