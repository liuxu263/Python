#!
# -*- coding: utf-8 -*-

''

__author__ = "lx"


def inpt_array(n):
    arr = []
    for i in range(int(n)):
        arr.append(int(input("请输入一个整数:\n")))

    return arr


def find_partion(arr, low, high):
    p = arr[low]
    while low < high:
        while low < high and p <= arr[high]:
            high -= 1
        arr[low] = arr[high]
        while low < high and p > arr[low]:
            low += 1
        arr[high] = arr[low]
    arr[low] = p
    return low


def quick_sort(arr, low, high):
    if low < high:
        p = find_partion(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)


def find_k(arr, low, high, k):
    p = find_partion(arr, low, high)
    if p == k:
        return arr[p]
    if p < k:
        return find_k(arr, p + 1, high, k)
    else:
        return find_k(arr, low, p - 1, k)


if __name__ == "__main__":
    n = int(input("请输入数组大小，并依次输入整数:\n"))
    arr = inpt_array(n)
    quick_sort(arr, 0, n - 1, )
    print("排序后的数组为:\n")
    print(arr)
    m = int(input("请输入想知道的第几大的数字:\n"))
    print(find_k(arr, 0, n - 1, m - 1))
