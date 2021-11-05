#! /user/bin/env python
# -*- coding:utf-8 -*-

""" """

__author__ = 'lx'


def merge_ordered_arrays(l1, l2):
    if len(l1) == 0:
        return l2
    elif len(l2) == 0:
        return l1
    result = []
    length1 = len(l1)
    length2 = len(l2)
    i = 0
    j = 0
    while i < length1 and j < length2:
        if l1[i] <= l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append((l2[j]))
            j += 1
    if i == length1:
        result.extend(l2[j:])
    if j == length2:
        result.extend(l1[i:])
    return result


if __name__ == '__main__':
    data1 = [1, 3, 5, 7]
    data2 = [6, 8, 10, 12]
    print(merge_ordered_arrays(data1, data2))
