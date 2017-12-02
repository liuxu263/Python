#! /usr/bin/env python3
# -*- coding：utf-8 -*-

'模仿静态变量的用法'

__author__='lx'

def varfunc():
    var =0
    print("var=%d"%var)
    var+=1
if __name__=='__main__':
    for i in  range(3):
        varfunc()

#类的属性
#作为类的一个属性吧

class Static:
    StaticVar = 5
    def vaffunc(self):
        self.StaticVar +=1
        print(self.StaticVar)
print(Static.StaticVar)
a=Static()
for i in range(3):
    a.vaffunc()