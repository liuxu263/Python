#! /usr/local/bin/python3
# -*- coding：utf-8 -*-

''

__atuhor__ = 'lx'


def find_two_numbers(arr, k):
    l = []
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == k:
                l.append((i, j))
    print(l)


if __name__ == "__main__":
    arr = [1, 12, 13, 123, 312, 3, 123, 2, 12, 3, 5, 342, 5456, 6575, 7]
    # arr = list(set(arr))
    find_two_numbers(arr, 14)
