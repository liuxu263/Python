#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'编写input()和output()函数输入，输出5个学生的数据记录。'

__author__ = 'lx'

student = []

for i in range(5):
    student.append(['', '', []])

# 代表学科的数量
N = 3


def input_stu(stu):
    for i in range(5):
        stu[i][0] = int(input('请输入学号：\n'))
        stu[i][1] = input('请输入姓名：\n')
        for j in range(N):
            stu[i][2].append(int(input('请输入成绩：\n')))


def output_stu(stu):
    for i in range(5):
        print("%-6d%-10s" % (stu[i][0], stu[i][1]))
        for j in range(N):
            print("%-8d" % stu[i][2][j])


if __name__ == '__main__':
    input_stu(student)
    print(student)
    output_stu(student)
