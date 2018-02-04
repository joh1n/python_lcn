# -*- coding: utf-8 -*-
"""
Created on Sun May  7 10:00:27 2017

@author: boboom
"""

import requests
#伪装成浏览器
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}



def apr_news(html):
    
    from bs4 import BeautifulSoup
    bsObj = BeautifulSoup(html.content, 'lxml')

    clink=bsObj.find_all('span',class_="pull-right")

    with open('Apr-News.txt','a+') as f:
    
        for i in clink:

            if i.string[0:7]=="2017-04":
                clink0=i.parent.find('a',class_="").string
                f.write(str(i.string[0:10]))
                f.write(str.rstrip(str(clink0)))
                f.write('\n')
        f.close()
'''
html = requests.get("http://www.bnu.edu.cn/bsdkx/index1.html", headers=head)
apr_news(html)
'''
html = requests.get("http://www.bnu.edu.cn/bsdkx/index.html", headers=head)
apr_news(html)
html = requests.get("http://www.bnu.edu.cn/bsdkx/index2.html", headers=head)
apr_news(html)
html = requests.get("http://www.bnu.edu.cn/bsdkx/index3.html", headers=head)
apr_news(html)
