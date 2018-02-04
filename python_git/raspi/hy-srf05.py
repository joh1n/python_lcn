#! /usr/bin/python
# -*- coding:utf-8 -*-

import RPi.GPIO as GPIO  # ( 导入模块 )
import sys
import time

# ( 引脚编号 )
Trig = 23  # 第3号针，GPIO2
Echo = 24 # 第5号针，GPIO3

# 初始化引脚
GPIO.setmode(GPIO.BCM)
# (设置通道)

GPIO.setup(Trig, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Echo, GPIO.IN)  # 输入的引脚.


time.sleep(1)

GPIO.output(Trig, GPIO.HIGH)  # gaodianpin
# 保持10us以上（我选择15us）
time.sleep(0.000015)
GPIO.output(Trig, GPIO.LOW)
while not GPIO.input(Echo):
    pass
# 发现高电平时开时计时
t1 = time.time()
while GPIO.input(Echo):
    pass
# 高电平结束停止计时
t2 = time.time()
# 返回距离，单位为米
print((t2 - t1) * 340 / 2)
GPIO.cleanup()


