# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 16:46:56 2017

@author: DELL
"""

def myexpress(num,opr,value):
    import itertools
    numlist=list(itertools.permutations(num,len(num)))
    oprlist=list(itertools.permutations(opr,len(num)-1))
    r=[]
    for i in numlist:
        for j in oprlist:
            j=j+('',)
            express=''.join([a+b for a,b in zip(i,j)])
            value1=eval(express)
            if value1==value:
                r.append(express+'='+str(value))
    return r


num=['2','3','4','5']
opr=['+','-','*','/','**']

r=myexpress(num,opr,24)
for i in r:
    print(i)