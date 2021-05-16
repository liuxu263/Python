#! /user/bin/env python
# -*- coding: utf-8 -*-


def divide_array(arr):
    flag = False
    if len(arr) <= 1:
        return flag
    arr.sort()
    for i in range(1, len(arr)):
        if sum(arr[0:i]) == sum(arr[i:]):
            flag = True
            print(i)
    return flag


if __name__ == '__main__':
    data = [1, 2, 3, 5]
    print(divide_array(data))
