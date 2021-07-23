#!
# -*- coding:utf-8 -*-

""" """

__author__ = 'lx'


def merge_interval(arr):
    if len(arr) <= 1:
        return arr
    arr.sort(key=lambda x: x[0])
    result = [arr[0]]
    for i in range(1, len(arr)):
        if result[-1][0] < arr[i][0] < result[-1][1]:
            if arr[i][1] >= result[-1][1]:
                result[-1] = [result[-1][0], arr[i][1]]
            else:
                pass
        elif arr[i][0] >= result[-1][1]:
            result.append([arr[i][0], arr[i][1]])
    return result


if __name__ == '__main__':
    data = [[1, 3], [8, 10], [2, 6], [15, 18]]
    print(merge_interval(data))
