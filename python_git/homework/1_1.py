# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



for i in range(9,0,-1):
    for j in range(i,0,-1):
        print('{}*{}={}'.format(i,j,j*i),end='\t')
    print()
