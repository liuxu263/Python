#!
# -*- coding=utf-8 -*-

""" """

__author__ = ''


class Test:
    i = 1

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Study(Test):
    j = 2

    def __init__(self, name):
        Test.__init__(self, name)

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
