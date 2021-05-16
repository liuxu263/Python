#! /user/bin/env python
# -*- coding: utf-8 -*-


def count_ele_in_list(arr):
    if len(arr) == 0:
        return
    d = dict()
    for i in range(len(arr)):
        if arr[i] in d.keys():
            d[arr[i]] += 1
        else:
            d[arr[i]] = 1

    # for k, v in d.items():
    #     if v == max(d.values()):
    #         max_key = k
    #         # return max_key, d[max_key]
    result = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return result[0]


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 2, 3, 3, 1, 1, 3, 1, 4, 1, 1, 1, 1, 1, 2, 2]
    print(count_ele_in_list(data))
