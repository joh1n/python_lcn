# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 12:45:21 2017

@author: DELL
"""

import numpy as np
from scipy import linalg

adjclose=np.loadtxt('IBM.csv', delimiter=',', usecols=(6,), unpack=True)
year=np.loadtxt('IBM.csv', delimiter=',', dtype=bytes,usecols=(0,), unpack=True).astype(str)

def err(N):
    #print(N)
    x=adjclose.size-N

    ry=adjclose[N:]

    A=np.zeros((x, N))
    for i in range(x):
        A[i,]=adjclose[i:i+N]
    result=linalg.lstsq(A,ry)

    predict=np.dot(A, result[0])
    err1=ry-predict
    return(np.mean(np.abs(err1)))

minerr = float('inf')
minsn=0
for i in range(1,adjclose.size):
    tem=err(i)
    if minerr>tem:
        minerr=tem
        minsn=i
print('当N={}时误差最小，误差为{}'.format(minsn, minerr))


rx=np.arange(adjclose.size)
p2=np.polyfit(rx, adjclose, 15)
pred=np.polyval(p2,rx)
roots=np.roots(np.polyder(p2))
print('拐点为:{}'.format(roots))


import matplotlib.pyplot as plt
index=np.arange(np.size(adjclose))
plt.figure(figsize=(20,10))
plt.plot(index,adjclose,'o',marker='.')
plt.plot(index,pred)
for i in roots:
    if i.imag==0:
       #print(i) 
       plt.plot(i.real,np.polyval(p2,i.real),'go')
plt.xlabel('year')
plt.ylabel('adj close')
xticks = index[::50]
plt.xticks(xticks, year[xticks])
