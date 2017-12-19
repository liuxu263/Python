#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'列表转换为字典。'

__author__ = 'lx'

keys = ['a', 'b']
values = [1, 2]
print({keys[i]: values[i] for i in range(len(keys))})