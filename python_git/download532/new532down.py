# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 20:01:37 2018

@author: aaa
"""

import threading
import requests
import time
import os

path = 'F:\\532dw'
for i in os.listdir(path):
   path_file = os.path.join(path,i)  # 取文件路径
   os.remove(path_file)



copyurl='http://172.16.215.66:6081/uploads/video6/hls/f/c/b/5/fcb50b1725614470669426a8270aa298/wl_0000810.ts'


nnnn=int(copyurl[-10:-3])
url0=copyurl[0:-13]

head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}


# 新线程执行的代码:
def loop(n0,n1):
    for i in range(n0,n1):
        if i%200==0:
            time.sleep(0.3)
        filmnum=str(i).zfill(5)
        filmname='wl_00'+filmnum+'.ts'
        url1=url0+filmname
        html = requests.get(url1,headers=head)
        with open("F:\\532dw\\"+filmname, 'wb') as file:
            file.write(html.content)
    print('thread %s ended.' % threading.current_thread().name)



print('thread %s is running...' % threading.current_thread().name)
t0 = threading.Thread(target=loop,args=(0,int(nnnn/4),), name='LoopThread0')
t1 = threading.Thread(target=loop,args=(int(nnnn/4)*1,2*int(nnnn/4),), name='LoopThread1')
t2 = threading.Thread(target=loop,args=(int(nnnn/4)*2,3*int(nnnn/4),), name='LoopThread2')
t3 = threading.Thread(target=loop,args=(int(nnnn/4)*3,nnnn+1,), name='LoopThread3')
t0.start()
t1.start()
t2.start()
t3.start()
t0.join()
t1.join()
t2.join()
t3.join()
print('thread %s ended.' % threading.current_thread().name)


with open(r'F:\wl.ts', 'ab') as file:
    for i in range(0,nnnn+1):
        filmnum=str(i).zfill(5)
        filmname='wl_00'+filmnum+'.ts'
        with open("F:\\532dw\\"+filmname, 'rb') as f:
            s=f.read()
        file.write(s)
print('Done')
