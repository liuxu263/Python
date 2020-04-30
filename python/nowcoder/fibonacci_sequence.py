#! /usr/local/bin/python3
# -*- coding：utf-8 -*-

''

__atuhor__ = 'lx'


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return (fib(n - 1) + fib(n - 2))


if __name__ == "__main__":
    l = []
    n = 5
    for i in range(1, n + 1):
        l.append(fib(i))
    print(l)
