#!
# -*- coding:utf-8 -*-

""" """

__author__ = 'lx'

# Python 的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号，列表使用方括号。
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

tup1 = ()


# 元祖运算符
# +
# *
# in
# for x in tuple

# 元祖索引，截取

# 元祖内置函数
# len
# max
# min
# tuple

def func1():
    # 元祖生成式生成一个生成器对象
    temp = (x ** 2 for x in range(0, 10))
    print(type(temp))
    for t in temp:
        print(t)


def func2():
    f = fib(6)
    print(type(f))
    for i in f:
        print(i)


def func3():
    f = fib(6)
    while True:
        try:
            x = next(f)
            print(x)
        except StopIteration as e:
            print("Generator return value:", e.value)
            break


def fib(number):
    n = 0
    a = 0
    b = 1
    while n < number:
        yield b
        a, b = b, a + b
        n += 1
    return "done"


if __name__ == '__main__':
    func1()
    func2()
    func3()
