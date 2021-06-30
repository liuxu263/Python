#!
# -*- coding = utf-8 -*-

""" """

__author__ = 'lx'


# 创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。

# 列表脚本操作符
# +
# *
# in
# for x in list

# 列表截取与拼接

# 嵌套列表

# 列表函数&方法
# len
# max
# min
# list
# append
# count
# extend
# index
# insert
# pop
# remove
# reverse
# sort
# clear
# copy

def func1(li):
    # 升序
    print(sorted(li))
    # 降序
    print(sorted(li, reverse=True))
    print(sorted(li, key=len))


def func2():
    # 列表生成式生成一个列表对象
    temp = [x ** 2 for x in range(0, 10)]
    print(type(temp))
    print(temp)
    for i in range(len(temp)):
        print(temp[i])


if __name__ == '__main__':
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    print(list1)
    func1(list1)
    print(list1)
    list1.sort(reverse=False)
    print(list1)
    func2()
