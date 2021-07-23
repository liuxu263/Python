#!
# -*- coding:utf-8 -*-

""" """

__author__ = 'lx'


def quick_sort(arr, low, high):
    if low < high:
        p = find_p(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)
    return arr


def find_p(arr, low, high):
    if low >= high:
        return
    p = arr[low]
    left = low
    right = high
    while left < right:
        while left < right and arr[right] >= p:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] < p:
            left += 1
        arr[right] = arr[left]
    arr[left] = p
    return left


if __name__ == '__main__':
    data = [1, 3, 5, 2, 4, 6, 0, 7]
    print(quick_sort(data, 0, len(data) - 1))
