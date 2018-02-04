# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 15:55:09 2017

@author: DELL
"""

a='this is  a test. 123  45678~ end?'

print('字符的总数为：',len(a))
aa=0
a1=0
ass=0
aleft=0
for s in a:
    if s.isalpha():
        aa+=1
    elif s.isnumeric():
        a1+=1
    elif s.isspace():
        ass+=1
    else:
        aleft+=1

print('字母出现的次数为：',aa)
print('数字出现的次数为：',a1)
print('空格出现的次数为：',ass)
print('其它出现的次数为：',aleft)

            