#!
# -*- coding: utf-8 -*-

''

__author__ = "lx"

'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
示例 1:
输入: "()"
输出: true
示例 2:
输入: "()[]{}"
输出: true
示例 3:
输入: "(]"
输出: false
示例 4:
输入: "([)]"
输出: false
示例 5:
输入: "{[]}"
输出: true
'''


def function(s):
    b = True
    stack_for_left = []
    if len(s) % 2 != 0:
        b = False
    left = {"[": 0, "{": 1, "(": 2}
    right = {"]": 0, "}": 1, ")": 2}
    for i in s:
        if i in left:
            stack_for_left.append(left[i])
        else:
            if len(stack_for_left) != 0 and stack_for_left[-1] == right[i]:
                stack_for_left.pop()
            else:
                b = False
    if len(stack_for_left) != 0:
        b = False
    return b


if __name__ == "__main__":
    s = "{}[]()()()(["
    print(function(s))
