#!
# -*- coding=utf-8 -*-

''

__author__ = ''


def first_not_repeat_char1(s):
    if not s:
        return 0
    else:
        for i in s:
            if i not in s[s.index(i) + 1:]:
                print(s[s.index(i) + 1:])
                print(i)
                return i


def first_not_repeat_char2(s):
    if not s:
        return 0
    else:
        d = dict()
        for c in s:
            d[c] = d.get(c, 0)
        for c in s:
            if d[c] == 1:
                print(c)
                return c


if __name__ == "__main__":
    s = "abcdabc"
    print(first_not_repeat_char1(s))
    print(first_not_repeat_char2(s))
