#!
# -*- coding=utf-8 -*-

''

__author__ = ''


def find_max_in_str(s):
    if not s:
        return 0
    result = []
    current = 0
    for c in s:
        num = ord(c) - ord('0')
        if 9 >= num >= 0:
            current = current * 10 + num
            result.append(current)
        else:
            current = 0
    print(result)
    print(min(result))
    return max(result)


if __name__ == "__main__":
    s = "AF43F0DS5432FFG3FE9FNE2312100"
    number = find_max_in_str(s)
    print(number)