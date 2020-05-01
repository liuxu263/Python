#!
# -*- coding: utf-8 -*-

''

__author__ = "lx"


def find_longest(arr):
    longest = 0
    for num in arr:
        if num - 1 not in arr:
            end = num + 1
            while end in arr:
                end += 1
            longest = max(longest, end - num)
    print(longest)


if __name__ == "__main__":
    arr = [200, 1, 100, 2, 3, 4, 8, 6, 7]
    find_longest(arr)
