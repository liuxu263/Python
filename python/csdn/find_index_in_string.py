#!
# -*- coding=utf-8 -*-

''

__author__ = ''


def func(str1, str2):
    for i in range(len(str2) - len(str1) + 1):
        if str1 == str2[i:len(str1) + i ]:
            print(str2[i:len(str1) + i])
            return i


if __name__ == "__main__":
    str1 = "abc"
    str2 = "cvabcerdadad"
    print(func(str1, str2))
