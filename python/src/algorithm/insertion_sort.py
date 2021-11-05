#! /user/bin/env python
# -*- coding:utf-8 -*-

""" """

__author__ = 'lx'


def insertion_sort(arr):
    if len(arr) <= 1:
        return
    for i in range(1, len(arr)):
        value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value
    return arr


if __name__ == '__main__':
    data = [1, 3, 5, 2, 4, 6, 0, 7]
    print(insertion_sort(data))
