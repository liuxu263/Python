#! /usr/local/bin/python3
# -*- coding：utf-8 -*-

''

__atuhor__ = 'lx'


def drop_eggs(n, k):
    if n == 0 or k == 0:
        return 0
    if n == 1:
        return 1
    if k == 1:
        return n
    m = 100000
    for i in range(1, n + 1):
        m = min(m, max(drop_eggs(i-1, k - 1), drop_eggs(n - i, k))+1)
    return m


if __name__ == "__main__":
    n = 10
    k = 2
    print(drop_eggs(n, k))
