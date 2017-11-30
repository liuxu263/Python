#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'按逗号分隔列表。'

__author__='lx'

numbers=list(range(0,9))
for i in numbers:
    if i==numbers[-1]:
        print(i)
    else:
        print(i,end=',')