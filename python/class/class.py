#!
# -*- coding=utf-8 -*-

"""
class
"""

__author__ = ''


class Test(object):
    i = 1

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Study(Test):
    j = 2

    def __init__(self, name):
        super().__init__(name)

    def return_name(self):
        return self.name


if __name__ == "__main__":
    t = Test("lx")
    print(t.i)
    print(t.get_name())
    s = Study("kobe")
    print(s.i)
    print(s.j)
    print(s.get_name())
    print(s.return_name())
