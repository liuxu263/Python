#! /usr/bitv python3
# -*- coding:utf-8 -*-

"""Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice."""

__author__ = 'lx'


class Solution:
    """

    def twoSum(self, nums, target):

        :type nums: List[int]
        :type target: int
        :rtype: List[int]


        l = [0,0]
        for i in range(0,len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    l[0]=i
                    l[1]=j
                    print("%d+%d=%d" % (int(nums[i]), int(nums[j]), int(target)))
                    return (l)
    """
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                print("%d+%d=%d" % (int(target - nums[i]), int(nums[i]), int(target)))
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i




nums = [2, 7, 11, 15]
target = 17
s = Solution()
s.twoSum(nums, target)

