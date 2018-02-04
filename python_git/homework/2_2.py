# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 16:08:57 2017

@author: DELL
"""

str1='abcdeabcdeab'
str2='ab'

a=str1.index(str2)
print(a)
for i in range(1,str1.count(str2)):
    a=str1.index(str2,a+1)
    print(a)
