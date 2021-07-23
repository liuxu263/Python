#!
# -*- coding:utf-8 -*-

""" """

__author__ = 'lx'

from abc import ABCMeta


class Pet(object, metaclass=ABCMeta):

    def __init__(self, nickname):
        self._nickname = nickname

    @classmethod
    def make_voice(cls):
        pass


class Dog(Pet):

    def make_voice(self):
        print(f'{self._nickname}汪汪汪的叫')


class Cat(Pet):

    def make_voice(self):
        print(f'{self._nickname}喵喵喵的叫')


if __name__ == '__main__':
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()
