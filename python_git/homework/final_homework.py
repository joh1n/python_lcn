#本人承诺本程序是自己编写的，没有抄袭。
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 19:00:07 2017

@author: 000
"""
#%%大作业第一题
#第二种方式爬虫抓取
import requests
from bs4 import BeautifulSoup as bs

head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

html = requests.get("http://lishi.tianqi.com/beijing/index.html", headers=head)  
bsObj = bs(html.content, 'lxml')

alink=bsObj.find('div',class_='tqtongji1').find_all("a")

web1=[]
for i in alink:
    web1.append(i.get('href'))

def getdata(web):
    html = requests.get(web, headers=head)  
    bsObj = bs(html.content, 'lxml')
    alink=bsObj.find('div',class_='tqtongji2').find_all("li")
    data=[]
    for i in alink:
        data.append(i.text)
    for j in [0,1,2,3,4,5]:
        del data[0]
    return(data)

bjwdata=[]
for i in web1:
    bjwdata=getdata(i)+bjwdata
    
#写入

import xlwt

book = xlwt.Workbook()
sheet1 = book.add_sheet('bjweather')

for i in range(0,int(len(bjwdata)/6)):
    for j in [0,1,2,3,4,5]:
        #print(i,j,bjwdata[i*6+j])
        sheet1.write(i,j,bjwdata[i*6+j])
       
book.save('beijing_weather.xls')


#第一种读取方式
import xlrd  
  
wb = xlrd.open_workbook('beijing_weather.xls')

sheet = wb.sheet_by_index(0)

bjweather=sheet.col_values(3)


import numpy as np
'''
vec=TfidfVectorizer()
a=vec.fit_transform(bjweather)
b=a.toarray()
print(a.toarray())
'''

xdata=np.zeros((len(bjweather),7))
ydata=np.zeros((len(bjweather),1))
#%%大作业第二题

for i in range(0,len(bjweather)):
    if bjweather[i].count('晴'):
        xdata[i,0]+=1
    if bjweather[i].count('雨'):
        xdata[i,1]+=1
        ydata[i]=1
    if bjweather[i].count('云'):
        xdata[i,2]+=1
    if bjweather[i].count('阴'):
        xdata[i,3]+=1
    if bjweather[i].count('雪'):
        xdata[i,4]+=1
        ydata[i]=1
    if bjweather[i].count('霾'):
        xdata[i,5]+=1
    if bjweather[i].count('尘'):
        xdata[i,6]+=1  

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='STSong'
labels='晴','雨','云','阴','雪','霾','尘'
plt.figure(figsize=(20,10))
plt.subplot(331)
sizes=sum(xdata[0:365,:])
plt.pie(sizes,labels=labels,autopct='%1.1f%%')
plt.title('2011年天气统计')
plt.subplot(332)
sizes=sum(xdata[365:365+366,:])
plt.pie(sizes,labels=labels,autopct='%1.1f%%')
plt.title('2012年天气统计')
plt.subplot(333)
sizes=sum(xdata[365+366:365*3+1,:])
plt.pie(sizes,labels=labels,autopct='%1.1f%%')
plt.title('2013年天气统计')
plt.subplot(334)
sizes=sum(xdata[365*3+1:365*4+1,:])
plt.pie(sizes,labels=labels,autopct='%1.1f%%')
plt.title('2014年天气统计')
plt.subplot(335)
sizes=sum(xdata[365*4+1:365*5+1,:])
plt.pie(sizes,labels=labels,autopct='%1.1f%%')
plt.title('2015年天气统计')
plt.subplot(336)
sizes=sum(xdata[365*5+1:365*6+2,:])
plt.pie(sizes,labels=labels,autopct='%1.1f%%')
plt.title('2016年天气统计')
plt.subplot(337)
sizes=sum(xdata[365*6+2:len(bjweather),:])
plt.pie(sizes,labels=labels,autopct='%1.1f%%')
plt.title('2017年天气统计')
plt.show()
#%%  大作业第三题
'''
smogdays=np.zeros((6,1))
j=0
for i in range(len(bjweather)):
    if xdata[i,5]:
        j+=1
    else:
        if j>0:
           smogdays[0]+=1
        if j>5:
           j=5
        smogdays[j]+=1
        j=0'''
def smogsta(xd):
    smogdays=np.zeros((6,1))
    j=0
    for i in range(len(xd)):
        if xd[i]:
            j+=1
        else:
            if j>0:
                smogdays[0]+=1
            if j>5:
                j=5
            smogdays[j]+=1
            j=0
    return(smogdays)
smog20=np.zeros((5,7))
smog20[:,0]=smogsta(xdata[0:365,5])[1:6].ravel()
smog20[:,1]=smogsta(xdata[365:365+366,5])[1:6].ravel()
smog20[:,2]=smogsta(xdata[365+366:365*3+1,5])[1:6].ravel()
smog20[:,3]=smogsta(xdata[365*3+1:365*4+1,5])[1:6].ravel()
smog20[:,4]=smogsta(xdata[365*4+1:365*5+1,5])[1:6].ravel()
smog20[:,5]=smogsta(xdata[365*5+1:365*6+2,5])[1:6].ravel()
smog20[:,6]=smogsta(xdata[365*6+2:len(bjweather),5])[1:6].ravel()
print('2011与2012年没有出现雾霾')

index=np.arange(7)
bar_width=0.15

plt.figure(figsize=(20,10))
plt.bar(index,smog20[0,:],bar_width,alpha=0.5,label='连续1天')
plt.bar(index+bar_width,smog20[1,:],bar_width,alpha=0.5,label='连续2天')
plt.bar(index+bar_width*2,smog20[2,:],bar_width,alpha=0.5,label='连续3天')
plt.bar(index+bar_width*3,smog20[3,:],bar_width,alpha=0.5,label='连续4天')
plt.bar(index+bar_width*4,smog20[4,:],bar_width,alpha=0.5,label='5天及以上')

plt.title('2011~2017年雾霾天数统计',color='k',fontproperties='SimHei',size=20,weight='bold')
plt.xlabel('年份',color='r',fontsize=20)
plt.ylabel('天数',color='r',fontsize=20)
plt.xticks(index+1.5*bar_width,[2011,2012,2013,2014,2015,2016,2017])
plt.legend()
plt.show()


#%%  大作业第四题
xxdata=np.zeros((len(bjweather)-1,7))
yydata=np.zeros((len(bjweather)-1,1))
for i in range(0,len(bjweather)-1):
    xxdata[i,:]=xdata[i,:]
    yydata[i]=ydata[i+1]
yydata=yydata.ravel()

from sklearn.cross_validation import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=5)
scoresknn=cross_val_score(knn,xxdata,yydata,cv=5,scoring='accuracy')
print('KNN得分：')
print(scoresknn.mean())

'''
from sklearn.linear_model import LogisticRegression
linlog=LogisticRegression()
linlog.fit(xxdata,yydata)
y_predict=linlog.predict([0,0,0,0,0,0,1])
'''
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
scoreslr=cross_val_score(lr,xxdata,yydata,cv=5,scoring='accuracy')
print('LR得分：')
print(scoreslr.mean())
#%%
print('LR为较优算法且没有参数')
print('如果说有的话，请运行下面注释的一段（需要想当长的时间）')
'''
from sklearn import preprocessing
X=preprocessing.scale(xxdata)
Y=preprocessing.scale(yydata)
from sklearn.svm import SVR
from sklearn.grid_search import GridSearchCV
svr=SVR(kernel='rbf')
param={'C':[1e0,1e1,1e2],'gamma':np.linspace(0.01,0.1,1)}
gs=GridSearchCV(svr,param,cv=5,scoring='mean_absolute_error',n_jobs=-1)
gs.fit(X,Y)
print(gs.best_score_)
print(gs.best_params_)
'''
#以下为KNN算法的最优参数确定，因为数量太多，故需要花费相当长时间
'''
from sklearn.neighbors import KNeighborsClassifier
from sklearn.grid_search import GridSearchCV
knn=KNeighborsClassifier()
param={'n_neighbors':np.arange(1,4),'weights':['uniform','distance']}
gs=GridSearchCV(knn,param,cv=5,n_jobs=-1,scoring='accuracy')
gs.fit(xxdata,yydata)
print(gs.best_score_)
print(gs.best_params_)
'''

