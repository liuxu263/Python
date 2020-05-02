#! /usr/local/bin/python3
# -*- coding：utf-8 -*-

''

__atuhor__ = 'lx'


def min_cut(s):
    if not s:
        return 0
    s_len = len(s)
    men = [i for i in range(-1, s_len)]
    for i in range(1, s_len + 1):
        for j in range(i):
            if s[j:i] == s[j:i][::-1]:
                men[i] = min(men[i], men[j] + 1)
    return men[-1]


if __name__ == "__main__":
    s = "a"
    print(min_cut(s))
