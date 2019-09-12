#!
# -*- coding: utf-8 -*-

''

__author__ = "lx"

'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
示例 1:
输入: 121
输出: true
示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
'''


def function(num):
    bool = False
    l = list(str(num))
    if num >= 0 and l[0:int((len(l) + 1) / 2)] == l[::-1][0:int((len(l) + 1) / 2):]:
        bool = True
    return bool


if __name__ == "__main__":
    num = 121
    bool = function(num)
    print(bool)
