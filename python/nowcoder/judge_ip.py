#! /usr/local/bin/python3
# -*- coding：utf-8 -*-

''

__atuhor__ = 'lx'


def judge_ip(str):
    if len(str) == 0:
        return False
    elif '.' not in str:
        return False
    elif str.count('.') != 3:
        return False
    else:
        flag = True
        nums = str.split(".")
        for num in nums:
            try:
                num1 = int(num)
                if num1 >= 0 and num1 <= 255:
                    pass
                else:
                    flag = False
            except:
                flag = False
        return flag


if __name__ == "__main__":
    ip_list = ['', '172.31.137.251', '100.10.0.1000', '1.1.1.1', '12.23.13', 'aa.12.1.2', '12345678', '289043jdhjkbh']
    for i in ip_list:
        print(judge_ip(i))
