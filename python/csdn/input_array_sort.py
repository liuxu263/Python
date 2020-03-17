#!
# -*- coding: utf-8 -*-

''

__author__ = "lx"


def input_array(n):
    array = []
    if n <= 1:
        return
    else:
        for i in range(int(n)):
            array.append(int(input("请输入一个数字：\n")))
    array.sort()
    print(array)
    return array


if __name__ == "__main__":
    n = input("请输入数组大小：\n")
    input_array(int(n))
