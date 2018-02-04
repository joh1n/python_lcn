# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 10:23:03 2017

@author: DELL
"""

import numpy as np

data = np.loadtxt('populations.txt')
year=data[:,0].astype('int')
hare=data[:,1]
lynx=data[:,2]
carrot=data[:,3]

print('NAME','MEAN','STD')
print('hare',hare.mean(),hare.std())
print('lynx',lynx.mean(),lynx.std())
print('carrot',carrot.mean(),carrot.std())

print('max num year:')
print(year[hare.argmax()],year[lynx.argmax()],year[carrot.argmax()])

print('mix num 2 years:')
print(year[hare.argsort()[:2]],year[lynx.argsort()[:2]],year[carrot.argsort()[:2]])

x=0
for i in year:
    if (hare[x]>lynx[x])&(hare[x]>carrot[x]):
       print('In',i,'hare is most')
    elif (lynx[x]>hare[x])&(lynx[x]>carrot[x]):
         print('In',i,'hlynx is most')
    elif (carrot[x]>hare[x])&(carrot[x]>lynx[x]):
         print('In',i,'carrot is most')
    x=x+1

x=0
for i in year:
    if (hare[x]>50000)|(hare[x]>50000)|(carrot[x]>50000):
       print('In',i,'any kind of animals is over 50000')
    x=x+1


import matplotlib.pyplot as plt

index=np.arange(np.size(year))
plt.figure(figsize=(20,10))
barwidth=0.2
#for i in year:
harep=plt.bar(index,hare,barwidth,alpha=0.5,color='b',label='hare')
lynxp=plt.bar(index+barwidth,lynx,barwidth,alpha=0.5,color='y',label='lynx')
carrotp=plt.bar(index+barwidth+barwidth,carrot,barwidth,alpha=0.5,color='r',label='carrot')

plt.xlabel('populations')
plt.ylabel('number')
plt.xticks(index+barwidth+barwidth,year)
#plt.annotate('hare is the most',xy=(index[hare.argmax()]+(i+0.5)*barwidth-0.1,hare.max()))

plt.annotate('hare is the most',color='r',xy=(index[hare.argmax()],hare.max()),xytext=(index[hare.argmax()]+0.3,hare.max()),fontsize=12,arrowprops={'arrowstyle':'->','color':'m'})
plt.annotate('lynx is the most',color='r',xy=(index[lynx.argmax()]+barwidth,lynx.max()),xytext=(index[lynx.argmax()]+0.3+barwidth,lynx.max()),fontsize=12,arrowprops={'arrowstyle':'->','color':'m'})
plt.annotate('carrot is the most',color='r',xy=(index[carrot.argmax()]+barwidth+barwidth,carrot.max()),xytext=(index[carrot.argmax()]+barwidth+barwidth+0.3,carrot.max()),fontsize=12,arrowprops={'arrowstyle':'->','color':'m'})
plt.show()
