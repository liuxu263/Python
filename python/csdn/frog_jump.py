#!
# -*- coding=utf-8 -*-

''

__author__ = ''


def frog_jump_time(n):
    if n <= 0:
        time = 0
    elif n == 1:
        time = 1
    elif n == 2:
        time = 2
    else:
        time = frog_jump_time(n - 1) + frog_jump_time(n - 2)
    return time


if __name__ == "__main__":
    n = 5
    print(frog_jump_time(n))
