#!
# -*- coding = utf-8 -*-

""" """

__author__ = 'lx'

file_path = "data.txt"


def func1():
    with open(file_path, "r") as file:
        lines = file.read()
    return lines


def func2():
    with open(file_path, "r") as file:
        line = file.readline()
        while line:
            print(line, end="")
            line = file.readline()


def func3():
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line, end="")


def func4():
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            print(file.read())
    except FileNotFoundError:
        print('无法打开指定的文件！')
    except LookupError:
        print('指定了未知的编码！')
    except UnicodeDecodeError:
        print('读文件时解码错误！')


if __name__ == '__main__':
    print(func1(), end="")
    (func2())
    (func3())
