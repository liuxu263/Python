#! /user/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Pool
import multiprocessing
import os
import time
import random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start_time = time.time()
    time.sleep(random.random() * 3)
    end_time = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end_time - start_time)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(8)
    for i in range(9):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all sub_processes done.')
    p.close()
    p.join()
    print('All sub_processed done.')
