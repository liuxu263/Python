#!
# -*- coding=utf-8 -*-

''

__author__ = ''


def reverse_string(s):
    if not s:
        return 0
    result = s.split(" ")[::-1]
    print(result)
    # result = result[::-1]
    # print(result)
    return result


if __name__ == "__main__":
    s = "how are you? i am fine."
    print(reverse_string(s))
