#! /usr/bin/env python3
# -*- coding:utf-8 -*-

"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""

__author__='lx'


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>=0:
            l=str(x)

            n=0
            for i in range (len(l)):
                n+=10**i*int(l[i])
            if n>2**31:
                n=0
            return n
        else:
            x=0-x
            l = str(x)

            n = 0
            for i in range(len(l)):
                n += 10 ** i * int(l[i])
            if n>2**31:
                n=0
            return -n




s=Solution()
n=s.reverse(-123)
print(n)