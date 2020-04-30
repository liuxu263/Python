#! /usr/local/bin/python3
# -*- coding：utf-8 -*-

''

__atuhor__ = 'lx'


def drop_str1(str1, str2):
    str = " "
    for i in range(len(str1) - 1):
        if str1[i] not in str2:
            str += str1[i]
    print(str)


def drop_str2(str1, str2):
    for i in str1:
        if i in str2:
            str1 = str1.replace(i, '')
    print(str1)


if __name__ == "__main__":
    str1 = "asdasdasdasd"
    str2 = "ad"
    drop_str1(str1, str2)
