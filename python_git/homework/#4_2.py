# -*- coding: utf-8 -*-
import csv

with open('成绩单.csv') as f:
    f_csv=csv.reader(f)
    heads=next(f_csv)
    heads.append('加权成绩')
    rowlist=[]
    i=0
    for row in f_csv:
        rowlist.append(row)
        rowlist[i].append(0)
        rowlist[i][4]=0.22*int(rowlist[i][1])+0.18*int(rowlist[i][2])+0.6*int(rowlist[i][3])
        i+=1
    f.close()

with open('成绩单1.csv','w',newline='') as f:
    f_csv=csv.writer(f)
    f_csv.writerow(heads)
    f_csv.writerows(rowlist)
    f.close()


            

