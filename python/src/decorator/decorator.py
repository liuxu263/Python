#!
# -*- coding:utf-8 -*-

""" """

__author__ = 'lx'

import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s()' % func.__name__)
        print('args = {}'.format(*args))
        return func(*args, **kwargs)
    return wrapper


@log
def test(p):
    print(test.__name__ + " param " + p)


def log_with_param(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('call %s():' % func.__name__)
            print('args = {}'.format(*args))
            print('log_param = {}'.format(text))
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log_with_param("param")
def test_with_param(p):
    print(test_with_param.__name__ + " param is " + p)


if __name__ == '__main__':
    test("I'm a param")
    # wrapper = log(test)
    # wrapper("I'm a param")

    test_with_param("lx")
