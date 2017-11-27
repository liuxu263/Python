#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

'学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。'

__author__='lx'

score=int(input('输入分数：'))
if score >= 90:
    grade = 'A'
elif score >=60:
    grade = 'B'
else:
    grade = 'C'
print("%d属于%s"%(score,grade))
