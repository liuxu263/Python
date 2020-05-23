#! /usr/local/bin/python3
# -*- coding：utf-8 -*-

''

__atuhor__ = 'lx'


def cut_rope1(length):
    if length == 0:
        return 0
    if length == 1:
        return 1
    if length == 2:
        return 2
    if length ==3:
        return 3
    if length == 4:
        return 4
    result = [0, 1, 2, 3]
    for i in range(4, length + 1):
        max = 0
        for j in range(1, i // 2 + 1):
            temp = result[j] * result[i - j]
            if int(temp) > max:
                max = temp
        result.append(max)
    return result[length]


def cut_rope2(length):
    if length <= 4:
        return length
    time_of_three = length // 3
    if length - time_of_three * 3 == 1:
        time_of_three -= 1
    time_of_two = (length - time_of_three * 3) // 2
    return pow(3, time_of_three) * pow(2, time_of_two)


if __name__ == "__main__":
    print(cut_rope1(2))
    print(cut_rope2(2))
