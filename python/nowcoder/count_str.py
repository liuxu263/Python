#! /usr/local/bin/python3
# -*- coding：utf-8 -*-

''

__atuhor__ = 'lx'


def count_str(str1, str2):
    l = []
    for i in range(len(str1) - 1):
        if str2 == str1[i:len(str2) + i]:
            l.append(i)
    print(len(l))


if __name__ == "__main__":
    str1 = "abcdfabcasdaabcasadjhkabca"
    str2 = "abc"
    count_str(str1, str2)
