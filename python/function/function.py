#!
# -*- coding = utf-8 -*-

""" """

__author__ = 'lx'


def func1():
    print("hello world")


def func2(param1, param2):
    print(param1 + param2)


def func3(*args):
    print(args)
    print(args[0] + args[1])


def func4(**kwargs):
    print(kwargs)
    print(kwargs["a"] + kwargs["b"])


if __name__ == '__main__':
    func1()
    a = 1
    b = 2
    func2(a, b)
    func3(a, b)
    func4(a=a, b=b)
