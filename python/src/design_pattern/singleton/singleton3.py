#! /user/bin/env python
# -*- coding:utf-8 -*-


# 使用new关键字实现单例模式
class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        pass


if __name__ == '__main__':
    test1 = Singleton()
    test2 = Singleton()
    print(id(test1))
    print(id(test2))
