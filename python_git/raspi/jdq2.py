#! /usr/bin/python
# -*- coding:utf-8 -*-

import RPi.GPIO as GPIO  # ( 导入模块 )
import time


jdq1 = 4  # 第3号针，GPIO2
jdq2 = 17 # 第5号针，GPIO3

GPIO.setmode(GPIO.BCM)  # 以BCM编码格式

GPIO.setup(jdq1, GPIO.OUT)
GPIO.output(jdq1, 0)

GPIO.setup(jdq2, GPIO.OUT)
GPIO.output(jdq2, 0)


time.sleep(5)

GPIO.setup(jdq2, GPIO.OUT)
GPIO.output(jdq2, 1)

time.sleep(2)

GPIO.setup(jdq2, GPIO.OUT)
GPIO.output(jdq2, 0)


time.sleep(5)

GPIO.cleanup()
a1=time.time()
a2=time.time()
print(a1)
print(a2)
