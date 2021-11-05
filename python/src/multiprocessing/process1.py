#! /user/bin/env python
# -*- coding:utf-8 -*-

""" """

__author__ = 'lx'


import os

if __name__ == '__main__':
    print('Process (%s) start...' % os.getpid())
    pid = os.fork()
    if pid == 0:
        print('I am child multiprocessing (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
    else:
        print('I (%s) just created a child multiprocessing (%s)' % (os.getpid(), pid))