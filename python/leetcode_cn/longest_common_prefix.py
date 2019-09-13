#!
# -*- coding: utf-8 -*-

''

__author__ = "lx"

'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
示例 1:
输入: ["flower","flow","flight"]
输出: "fl"
示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:
所有输入只包含小写字母 a-z 。
'''


def function(strs):
    s = ""
    if len(strs) == 0:
        return s
    check_str_list = list()
    for i in range(len(strs[0])):
        check_str_list.append(strs[0][0:(i + 1)])
    target_strs = strs[1:]
    for check_str in check_str_list:
        bool = False
        for target_str in target_strs:
            if not target_str.startswith(check_str):
                bool = True
                break
        if bool == True:
            break
        s = check_str
    return s


if __name__ == "__main__":
    strs = ["flower ,flow", "flight"]
    s = function(strs)
    print(s)
