#! /usr/local/bin/python3
# -*- coding：utf-8 -*-

''

__atuhor__ = 'lx'


def find_max_index(arr, k):
    for i in arr:
        if i >= k:
            return arr.index(i)
    if arr[0] >= k:
        return 0
    elif arr[len(arr) - 1] < k:
        return len(arr)


if __name__ == "__main__":
    arr = [1, 3, 5, 6]
    k = 0
    print(find_max_index(arr, k))
