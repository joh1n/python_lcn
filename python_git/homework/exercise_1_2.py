# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 15:42:56 2017

@author: DELL
"""
def Euclidean_algorithm(m,n):
    r=m%n
    m=n
    n=r
    if r==0:
        return m
    else:
        return Euclidean_algorithm(m,n)
    
    

a=319
b=377
c=Euclidean_algorithm(a,b)
d=a*b/c
print('%d和%d的最大公约数为%d,最小公倍数为%d'%(a,b,c,d))


def myadd(a,b):
    c=[0,0]
    c[0]=a[0]*b[1]+a[1]*b[0]
    c[1]=a[1]*b[1]
    r=Euclidean_algorithm(c[1],c[0])
    c[1]=c[1]/r
    c[0]=c[0]/r
    return c
     
def mymultiply(a,b):
    c=[0,0]
    c[0]=a[0]*b[0]
    c[1]=a[1]*b[1]
    r=Euclidean_algorithm(c[1],c[0])
    c[1]=c[1]/r
    c[0]=c[0]/r
    return c  
  
   
a=(1,2)
b=(3,4)
c=myadd(a,b)
d=mymultiply(a,b)
print('%d/%d与%d/%d的和等于%d/%d,乘积等于%d/%d'%(a[0],a[1],b[0],b[1],c[0],c[1],d[0],d[1]))