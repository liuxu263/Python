#!
# -*- coding = utf-8 -*-

""" """

__author__ = 'lx'


class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}')


if __name__ == "__main__":
    s = Student("lx", "18")
    s.study("Python")
