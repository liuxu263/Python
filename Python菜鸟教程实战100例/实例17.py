#！ /usr/bin/env python 3
# -*- coding：UTF-8 -*-

'输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。'

__autoor__='lx'

import string
s=input('请输入一行字符：')
letters=0
space=0
diget=0
others=0
for c in s:
    if c.isalpha():
        letters+=1
    elif c.isspace():
        space+=1
    elif c.isdigit():
        diget+=1
    else:
        others+=1
print("char=%d，space=%d，digit=%d，others=%d"%(letters,space,diget,others))