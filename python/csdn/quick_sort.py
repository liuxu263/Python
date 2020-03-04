#!
# -*- coding: utf-8 -*-

''

__author__ = "lx"


def partion(arr, low, high):
    q = arr[low]
    while low < high:
        while low < high and arr[high] >= q:
            high -= 1
        arr[low] = arr[high]
        while low < high and arr[low] < q:
            low += 1
        arr[high] = arr[low]
    arr[low] = q
    print(low)
    return low


def quick_sort(arr, low, high):
    if low < high:
        q = partion(arr, low, high)
        quick_sort(arr, low, q - 1)
        quick_sort(arr, q + 1, high)


if __name__ == "__main__":
    arr = [2, 9, 46, 46, 4, 3, 17, 7, 9, 12]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
