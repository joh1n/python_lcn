# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 14:40:55 2017

@author: DELL
"""

import math
print('solve:ax^2+bx+c=0')
a=float(input('Value a:'))
b=float(input('Value b:'))
c=float(input('Value c:'))
m=b*b-4*a*c
if m>0:
    print('there are two roots:{},{}'.format((math.sqrt(m)-b)/(2*a),(-math.sqrt(m)-b)/(2*a)))
elif m==0:
    print('there are two equal roots:{}'.format((-math.sqrt(m)-b)/(2*a)))
elif m<0:
    print('there are two conjugate complex roots:{0}+{1}i,{0}-{1}i'.format(-b/(2*a),(math.sqrt(-m)/(2*a))))
else:
    print('error')
