#!
# -*- coding:utf-8 -*-

""" """

__author__ = 'lx'


class Person(object):

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
    print(person.age)
    person.age = 22
    print(person.age)
