#! /usr/local/bin/python3
# -*- coding：utf-8 -*-

'test python'

__atuhor__ = 'lx'


def find_max_and_min_in_array(arr):
    for i in range(len(arr) - 1):
        for j in range(i+1 , len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    li = []
    li.append((arr[0], arr[len(arr) - 1]))
    print(li)


if __name__ == "__main__":
    arr = [999, 123, 32, 4, 234, 324234, 234, 23, 423, 4, 234, 23, 423, 4, 234, 2, 312, 3, 132, 123]
    find_max_and_min_in_array(arr)
