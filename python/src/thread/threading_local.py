#! /user/bin/env python
# -*- coding:utf-8 -*-

""" """

__author__ = 'lx'


import threading
import time

local_school = threading.local()


def process_student():
    std = local_school.student
    print('Hello,%s(in %s)' % (std, threading.current_thread().name))
    time.sleep(2)


def process_thread(name):
    local_school.student = name
    process_student()


if __name__ == '__main__':
    t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
    t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
