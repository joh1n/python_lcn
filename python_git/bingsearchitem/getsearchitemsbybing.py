# -*- coding: utf-8 -*-
"""
Created on Sat May 17 20:58:00 2017

@author: 000
"""

import re,urllib.parse,urllib.request,urllib.error
from bs4 import BeautifulSoup as BS

word='大学生、村官、吐槽、不满、不适应'
searchpages=2



def getpages(word,searchpages):
    searchpages=str(searchpages)
    weblist1=set()
    baseUrl = 'http://search.tianya.cn/bbs?'
    word = word.encode(encoding='utf-8', errors='strict')
#print(word)

    data = {'q':word}
    data = urllib.parse.urlencode(data)
#print(data)
    url = baseUrl+data+'&pn='+searchpages
    
    try:
        html = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        print(e.code)
    except urllib.error.URLError as e:
        print(e.reason)

    soup = BS(html,"html.parser")
    td = soup.findAll("h3")

    for t in td:
        #print(t.get_text())
        pattern = re.compile(r'href="([^"]*)"')
        h = re.search(pattern,str(t))
        if h:
            for x in h.groups():
                #print(x)
                weblist1.add(x)
    return weblist1

def searchweb(x):
    urlt=x;
    try:
        htmlt = urllib.request.urlopen(urlt)
    except urllib.error.HTTPError as e:
        print(e.code)
    except urllib.error.URLError as e:
        print(e.reason)
    print(x)
    soup = BS(htmlt,"html.parser")
    tdt = soup.findAll("body")
    h = re.findall(r'吐槽',str(tdt))
    return len(h)

   
wordstimes=0
weblist=set()
for i in range(1,searchpages+1):
    print('search '+str(i)+' pages')
    weblist.update(getpages(word,i))
    for j in range(0,len(weblist)):
        pagetimes=0
        try:
            pagetimes=searchweb(weblist.pop())
            wordstimes+=pagetimes
            print('this page appears '+str(pagetimes)+' times')
        except:
            print('wrongpage')
print('total times:')
print(wordstimes)
