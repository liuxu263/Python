#! /user/bin/env python
# -*- coding:utf-8 -*-


# 函数装饰器实现单例
def singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    return inner


@singleton
class Test(object):
    def __init__(self):
        pass


if __name__ == '__main__':
    test1 = Test()
    test2 = Test()
    print(id(test1))
    print(id(test2))
