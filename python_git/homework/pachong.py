# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 16:05:02 2017

@author: Deng Qiong qiong
"""
#爬虫快速入门

import requests
#伪装成浏览器
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}

#设置请求头
html = requests.get("http://www.bnu.edu.cn/", headers=head)  


#响应对象的一些属性
print(html.url)
print(html.content)  #二进制
print(html.status_code)
print(html.text)   #文本
print(html.encoding)
html.encoding='UTF-8'
print(html.text)

print(html.request.headers)  #请求头
print(html.headers)   #响应头



'''利用BeautifulSoup从html中根据标签查找东西，
标签有一些属性：name,attrs等'''

from bs4 import BeautifulSoup
bsObj = BeautifulSoup(html.content, 'lxml')
print(type(bsObj))


#找到html中第一个出现的标签
print(bsObj.title) 
print(bsObj.img)
print(bsObj.a)
print(bsObj.a.get_text())
print(bsObj.a.attrs)
print(bsObj.a['href'])

print(type(bsObj.a))  #标签对象

'''借助BeautifulSoup在html中利用find函数
查找满足条件的东西，
条件可以是标签和属性'''

alink=bsObj.find('a')
print(alink)

blink=bsObj.find('a',text='师大新闻')
print(blink)

clink=bsObj.find('img', alt='北京师范大学')
print(clink['src'])

#保存此图像到电脑上
image = requests.get("http://www.bnu.edu.cn/"+clink['src'])
with open('BNU-logo.png', 'wb') as f: 
    f.write(image.content)

#class 是关键词，不能直接使用，已注释掉
#dlink=bsObj.find('span', class="col-md-10")

#需要这样使用
dlink=bsObj.find('span', class_="col-md-10")
print(dlink)
dlink=bsObj.find('span', {'class':'col-md-10'})
print(dlink.get_text())


'''借助BeautifulSoup在html中利用find_all函数查找所有满足条件的东西，
条件是标签及属性，也可以是正则表达式'''

alink=bsObj.find_all('a')
print(alink)

blink=bsObj.find_all("a", limit=2)
print(blink)


clink=bsObj.find('li', class_="dropdown").find_all('a')
print(clink)

import re
imglist = bsObj.find_all('img', {"src":re.compile(".+\.jpg")})
print(imglist)


#其他常用函数
clink=bsObj.find('li', class_="dropdown")
print(clink)

print(clink.parent)

for child in clink.children:
    print(child)

for child in clink.descendants:
    print(child)
    
for child in clink.findChildren('li'):
    print(child)
    
for sibling in clink.next_siblings:
    print(sibling)

#%%
'''一个例子，从百度贴吧上把象棋的图像下下来，保存在电脑上。'''

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}
import requests
from bs4 import BeautifulSoup
url='https://tieba.baidu.com/p/3772710132?see_lz=1'
hlm=requests.get(url, headers=head)
bs=BeautifulSoup(hlm.content, 'lxml')
images=bs.find_all('img', class_='BDE_Image')

#通过os模块创建路径
import os
path=os.path.join(os.getcwd(),'象棋')
if not os.path.exists(path):
    os.mkdir(path)

j=1
for i in images:
    hlm2=requests.get(i['src'])
    with open('{}\\{}.jpg'.format(path,j), 'wb') as f:
        f.write(hlm2.content)
    j+=1