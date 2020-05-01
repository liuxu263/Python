#! /usr/local/bin/python3
# -*- coding：utf-8 -*-

''

__atuhor__ = 'lx'


def find_max(str):
    d = {}
    l = []
    for i in range(len(str) - 1):
        if str[i] not in d.keys():
            d[str[i]] = 0
        else:
            d[str[i]] += 1
    max_value = 0
    for key, value in d.items():
        if max_value < d[key]:
            max_value = d[key]
            l.append([key, value])
    print(l[-1])
    print(max_value)
    print(d)


if __name__ == "__main__":
    str = "dasda,sdasdasddasdasdasdasd"
    find_max(str)
