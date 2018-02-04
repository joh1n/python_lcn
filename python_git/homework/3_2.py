# -*- coding: utf-8 -*-
"""
Created on Sun May  7 23:05:29 2017

@author: boboom
"""

import requests
import os
from PIL import Image,ImageDraw,ImageFont
from bs4 import BeautifulSoup


path=os.path.join(os.getcwd(),'teacters')
if not os.path.exists(path):
    os.mkdir(path)


def pict(clink):

    for i in clink:
        if str(i['href'])[1]!='.':
            html0name='http://physics.bnu.edu.cn/application/faculty'+str(i['href'])[1:len(i['href'])]
            html0 = requests.get(html0name, headers=head)
            bs=BeautifulSoup(html0.content, 'lxml')
            personname=bs.find('title').get_text()
            k=str.rstrip(personname[0:3])
            images=bs.find_all('img')
            for j in images:
                if str(j['src'])[1]!='.':
                   print(j['src'])
                   print(html0name[0:len(html0name)-10]+str(j['src'])[1:len(j['src'])])
                   hlm2=requests.get(html0name[0:len(html0name)-10]+str(j['src'])[1:len(j['src'])])
                   with open('{}\\{}.jpg'.format(path,k), 'wb') as f:
                       f.write(hlm2.content)
                   f.close()

head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
html = requests.get("http://physics.bnu.edu.cn/application/faculty/theoretical_physics.php", headers=head)
bsObj = BeautifulSoup(html.content, 'lxml')
clink=bsObj.find_all('a')
pict(clink)



    
Font1=ImageFont.truetype("simsun.ttc",36) 
im2=Image.new('RGB',(1750,1000),'white')
drawObject = ImageDraw.Draw(im2) 
drawObject.ink = 0 + 0 * 256 + 0 * 256 * 256 

i=0
for files in os.listdir(path):
    print(files)
    text=files[0:len(files)-4]
    im=Image.open(path+'\\'+files)
    im2.paste(im.resize((170,200)),(5+175*(i%10),250*(int(i/10))))
    drawObject.text((20+175*(i%10),200+250*(int(i/10))),text,font=Font1) 
    i+=1

im2.show()
