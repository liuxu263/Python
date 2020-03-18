#!
# -*- coding: utf-8 -*-

''

__author__ = "lx"


def selection_sort_min(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def selection_sort_max(arr):
    for i in range(len(arr) - 1, -1, -1):
        max_index = i
        for j in range(0, i):
            if arr[j] > arr[max_index]:
                max_index = j
        if i != max_index:
            arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr


if __name__ == "__main__":
    arr = [23, 123, 1, 5, 13, 123, 123131, 4124, 11, 1, 43242, 12313]
    # print(selection_sort_min(arr))
    print(selection_sort_max(arr))
