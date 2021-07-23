#!
# -*- coding:utf-8 -*-

""" """

__author__ = 'lx'


from multiprocessing import Process
import os
import time


def run_process(name):
    print('Run child multiprocessing %s (%s)...' % (name, os.getpid()))
    time.sleep(3)
    print('Child multiprocessing end.')


if __name__ == '__main__':
    print('Parent multiprocessing %s.' % os.getpid())
    p = Process(target=run_process, args=('test',))
    print('Child multiprocessing will start.')
    p.start()
    time.sleep(1)
    p.join()
    print('Parend multiprocessing end.')
