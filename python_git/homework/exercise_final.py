# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 18:04:12 2017

@author: DELL
"""
import math
def prime(m):
    k=int(math.sqrt(m))
    for i in range(2,k+1):
        if m%i==0:
            return False
    return True

def divisornum(num):
    l=[]
    if prime(num):
        l.append([num,1])
        return l
    else:
        for i in range(2,num):
            if prime(i):
                l.append([i,0])
        n=0
        for i in l:
            while(num%i[0]==0):
                l[n][1]+=1
                num=num/i[0]
            n+=1
        m=0
        for i in range(0,len(l)):
            if l[m][1]==0:
               del l[m]
            else:
               m+=1
  
        return l
       
def commondiv(a,b):
    l1=divisornum(a)
    l2=divisornum(b)
    l3=[]
    for i in l1:
        for j in l2:
            if i[0]==j[0]:
               l3.append([i[0],min(i[1],j[1])])
    return l3

def maxcommondiv(a,b):
    l1=divisornum(a)
    l2=divisornum(b)
    l3=[]
    for s in l2:
        aa=True
        for x in l1:
            if x[0]==s[0]:
               l3.append([s[0],max(s[1],x[1])])
               aa=False
               break
        if aa:
            l3.append(s)
    for s in l1:
        aa=True
        for x in l2:
            if x[0]==s[0]:
               aa=False
               break
        if aa:
            l3.append(s)
    return l3

def max_min(a,b):
    m=commondiv(a,b)
    n=maxcommondiv(a,b)
    print('%d,%d公因子及个数为'%(a,b))
    print(m)
    print('%d,%d所有因子及个数为'%(a,b))
    print(n)
    mindiv=1
    maxdiv=1
    for s in m:
        mindiv*=s[0]*s[1]
    for s in n:
        maxdiv*=s[0]*s[1]
    return mindiv,maxdiv

a=15
b=6
c,d=max_min(a,b)
print('%d和%d的最大公约数为%d,最小公倍数为%d'%(a,b,c,d))


a=24
b=60
c,d=max_min(a,b)
print('%d和%d的最大公约数为%d,最小公倍数为%d'%(a,b,c,d))


a=319
b=377
c,d=max_min(a,b)
print('%d和%d的最大公约数为%d,最小公倍数为%d'%(a,b,c,d))






