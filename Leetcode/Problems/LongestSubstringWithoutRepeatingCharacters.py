#! /usr/bin/env python3
# -*- coding：utf-8 -*-

"""Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.'
"""
__author__ = 'lx'


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int

        """
        l = []
        s=list(s)
        r = []
        if len(s)==0 or len(s)==1:
            return len(s)
        else:
            l.append(s[0])
            print(l)
            for i in range(1,len(s)):
                if s[i] in l:
                    t=l.index(s[i])
                    if t==0:
                        del l[0]
                        l.append(s[i])
                        r.append(len(l))
                    elif t==len(l)-1:
                        l=[]

                        l.append(s[i])
                        r.append(len(l))

                    else:
                        l=l[t+1:]
                        l.append(s[i])
                        r.append(len(l))

                else:
                    l.append(s[i])
                    r.append(len(l))
                    print(l)
            print(l)
            print(len(l))
            r.sort()
            return (max(r))


s = Solution()
str = "fertoeqnmcovigfbfesviallcaelwbrcfkxvoojbsxyaffbkluftuteztkmslfwqqtmgjxhbwhecphmaduuapazillaw"
print(s.lengthOfLongestSubstring(str))
