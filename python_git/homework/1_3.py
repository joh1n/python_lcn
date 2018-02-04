# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 15:37:57 2017

@author: DELL
"""

for a in range(1000,10000):
    b1=0
    for i in range(1,a):
        if a%i==0:
            b1=b1+i
    b2=0
    for i in range(1,b1):
        if b1%i==0:
            b2=b2+i
    if (b2==a)&(b2<10000):
        print(a,b1)
print('END')
