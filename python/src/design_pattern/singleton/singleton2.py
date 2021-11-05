#! /user/bin/env python
# -*- coding:utf-8 -*-


# 类装饰器实现单例
class Singleton(object):
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]


@Singleton
class Test1(object):
    def __init__(self):
        pass


class Test2(object):
    def __init__(self):
        pass


if __name__ == '__main__':
    test1 = Test1()
    test2 = Test1()
    print(id(test1))
    print(id(test2))

    Test2 = Singleton(Test2)
    test3 = Test2()
    test4 = Test2()
    print(id(test3))
    print(id(test4))

