#! /user/bin/env python
# -*- coding:utf-8 -*-


# 使用metaclass实现单例模式
class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class Test(metaclass=Singleton):
    pass


if __name__ == '__main__':
    test1 = Test()
    test2 = Test()
    print(id(test1))
    print(id(test2))
