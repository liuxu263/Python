#! /user/bin/env python
# -*- coding:utf-8 -*-

""" """

__author__ = 'lx'


class Person(object):
    # 限定Person对象只能绑定 _name,_age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age


if __name__ == '__main__':
    person = Person('lx', 18)
    person._gender = "男"
    print(person._gender)
