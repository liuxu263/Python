#! /user/bin/env python
# -*- coding: utf-8 -*-


def bubble_sort(arr):
    if len(arr) <= 1:
        return
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


if __name__ == '__main__':
    data = [1, 3, 5, 2, 4, 6, 0, 7]
    print(bubble_sort(data))
