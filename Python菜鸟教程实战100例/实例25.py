#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'求1+2!+3!+...+20!的和。'

__author__='lx'

n=0
s=0
t=1
for n in range(1,21):
    t*=n
    s+=t
print("1! + 2! + 3! + ... + 20! = %d"%s)
