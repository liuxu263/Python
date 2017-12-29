#! /usr/bin/env python3
# -*- coding：utf-8 -*-

"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

"""
__author__='lx'

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float

        """

        nums11=[]
        for i in range(len(nums1)):
            nums11.append(int(nums1[i]))
        nums21 = []
        for i in range(len(nums2)):
            nums21.append(int(nums2[i]))

        s=nums11+nums21
        s.sort()
        if len(s)==0:
            n=0
        elif len(s)==1:
            n=s[0]
        elif len(s)%2!=0:
            n=s[int((len(s)-1)/2)]
        else :
            n=(s[int(len(s)/2-1)]+s[int(len(s)/2)])/2

        n=float(n)
        return n



l1=[]
l2=[]

s=Solution()
n=s.findMedianSortedArrays(l1,l2)
print(n)