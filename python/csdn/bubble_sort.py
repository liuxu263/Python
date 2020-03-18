#!
# -*- coding: utf-8 -*-

''

__author__ = "lx"


def bubble_sort_max(arr):
    for i in range(len(arr) - 1):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def bubble_sort_min(arr):
    for i in range(len(arr) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


if __name__ == "__main__":
    arr = [13, 34, 13, 1231, 23, 123, 123, 123, 12, 31, 231, 23, 124, 1, 2412, 5, 1251]
    # print(bubble_sort_max(arr))
    print(bubble_sort_min(arr))
