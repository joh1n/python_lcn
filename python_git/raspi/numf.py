#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO
import time

# 定义单个数码管各段led对应的GPIO口
LED_A = 26
LED_B = 19
LED_C = 13
LED_D = 6
LED_E = 5
LED_F = 22
LED_G = 27
LED_DP = 17

# 定义1到4号数码管阳极对应的GPIO口
DIGIT1 = 12
DIGIT2 = 16
DIGIT3 = 20
DIGIT4 = 21

# 定义按钮输入的GPIO口
# btn = 27

RPi.GPIO.setmode(RPi.GPIO.BCM)

RPi.GPIO.setup(LED_A, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_B, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_C, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_D, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_E, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_F, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_G, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_DP, RPi.GPIO.OUT)
RPi.GPIO.setup(DIGIT1, RPi.GPIO.OUT)
RPi.GPIO.setup(DIGIT2, RPi.GPIO.OUT)
RPi.GPIO.setup(DIGIT3, RPi.GPIO.OUT)
RPi.GPIO.setup(DIGIT4, RPi.GPIO.OUT)

RPi.GPIO.output(DIGIT1, 1)
RPi.GPIO.output(DIGIT2, 1)
RPi.GPIO.output(DIGIT3, 1)
RPi.GPIO.output(DIGIT4, 1)

# RPi.GPIO.setup(btn, RPi.GPIO.IN, pull_up_down=RPi.GPIO.PUD_UP)

# 指定no(1-4)号数码管显示数字num(0-9)，第三个参数是显示不显示小数点（1/0）
def showDigit(no, num, showDotPoint):
    # 先将正极拉低，关掉显示
    RPi.GPIO.output(DIGIT1, 0)
    RPi.GPIO.output(DIGIT2, 0)
    RPi.GPIO.output(DIGIT3, 0)
    RPi.GPIO.output(DIGIT4, 0)
    
    if (num == 0) :
        RPi.GPIO.output(LED_A, 0)
        RPi.GPIO.output(LED_B, 0)
        RPi.GPIO.output(LED_C, 0)
        RPi.GPIO.output(LED_D, 0)
        RPi.GPIO.output(LED_E, 0)
        RPi.GPIO.output(LED_F, 0)
        RPi.GPIO.output(LED_G, 1)
        RPi.GPIO.output(LED_DP, not showDotPoint)
    elif (num == 1) :
        RPi.GPIO.output(LED_A, 1)
        RPi.GPIO.output(LED_B, 0)
        RPi.GPIO.output(LED_C, 0)
        RPi.GPIO.output(LED_D, 1)
        RPi.GPIO.output(LED_E, 1)
        RPi.GPIO.output(LED_F, 1)
        RPi.GPIO.output(LED_G, 1)
        RPi.GPIO.output(LED_DP, not showDotPoint)
    elif (num == 2) :
        RPi.GPIO.output(LED_A, 0)
        RPi.GPIO.output(LED_B, 0)
        RPi.GPIO.output(LED_C, 1)
        RPi.GPIO.output(LED_D, 0)
        RPi.GPIO.output(LED_E, 0)
        RPi.GPIO.output(LED_F, 1)
        RPi.GPIO.output(LED_G, 0)
        RPi.GPIO.output(LED_DP, not showDotPoint)
    elif (num == 3) :
        RPi.GPIO.output(LED_A, 0)
        RPi.GPIO.output(LED_B, 0)
        RPi.GPIO.output(LED_C, 0)
        RPi.GPIO.output(LED_D, 0)
        RPi.GPIO.output(LED_E, 1)
        RPi.GPIO.output(LED_F, 1)
        RPi.GPIO.output(LED_G, 0)
        RPi.GPIO.output(LED_DP, not showDotPoint)
    elif (num == 4) :
        RPi.GPIO.output(LED_A, 1)
        RPi.GPIO.output(LED_B, 0)
        RPi.GPIO.output(LED_C, 0)
        RPi.GPIO.output(LED_D, 1)
        RPi.GPIO.output(LED_E, 1)
        RPi.GPIO.output(LED_F, 0)
        RPi.GPIO.output(LED_G, 0)
        RPi.GPIO.output(LED_DP, not showDotPoint)
    elif (num == 5) :
        RPi.GPIO.output(LED_A, 0)
        RPi.GPIO.output(LED_B, 1)
        RPi.GPIO.output(LED_C, 0)
        RPi.GPIO.output(LED_D, 0)
        RPi.GPIO.output(LED_E, 1)
        RPi.GPIO.output(LED_F, 0)
        RPi.GPIO.output(LED_G, 0)
        RPi.GPIO.output(LED_DP, not showDotPoint)
    elif (num == 6) :
        RPi.GPIO.output(LED_A, 0)
        RPi.GPIO.output(LED_B, 1)
        RPi.GPIO.output(LED_C, 0)
        RPi.GPIO.output(LED_D, 0)
        RPi.GPIO.output(LED_E, 0)
        RPi.GPIO.output(LED_F, 0)
        RPi.GPIO.output(LED_G, 0)
        RPi.GPIO.output(LED_DP, not showDotPoint)
    elif (num == 7) :
        RPi.GPIO.output(LED_A, 0)
        RPi.GPIO.output(LED_B, 0)
        RPi.GPIO.output(LED_C, 0)
        RPi.GPIO.output(LED_D, 1)
        RPi.GPIO.output(LED_E, 1)
        RPi.GPIO.output(LED_F, 1)
        RPi.GPIO.output(LED_G, 1)
        RPi.GPIO.output(LED_DP, not showDotPoint)
    elif (num == 8) :
        RPi.GPIO.output(LED_A, 0)
        RPi.GPIO.output(LED_B, 0)
        RPi.GPIO.output(LED_C, 0)
        RPi.GPIO.output(LED_D, 0)
        RPi.GPIO.output(LED_E, 0)
        RPi.GPIO.output(LED_F, 0)
        RPi.GPIO.output(LED_G, 0)
        RPi.GPIO.output(LED_DP, not showDotPoint)
    elif (num == 9) :
        RPi.GPIO.output(LED_A, 0)
        RPi.GPIO.output(LED_B, 0)
        RPi.GPIO.output(LED_C, 0)
        RPi.GPIO.output(LED_D, 0)
        RPi.GPIO.output(LED_E, 1)
        RPi.GPIO.output(LED_F, 0)
        RPi.GPIO.output(LED_G, 0)
        RPi.GPIO.output(LED_DP, not showDotPoint)
    
    if (no == 1) :
        RPi.GPIO.output(DIGIT1, 1)
    elif (no == 2) :
        RPi.GPIO.output(DIGIT2, 1)
    elif (no == 3) :
        RPi.GPIO.output(DIGIT3, 1)
    elif (no == 4) :
        RPi.GPIO.output(DIGIT4, 1)


t=0.005
for j in range(0, 6):
    for i in range(0, 500):
        time.sleep(t)
        showDigit(1, int(int(time.strftime("%H",time.localtime(time.time()))) / 10), 0)
        time.sleep(t)
        showDigit(2, int(time.strftime("%H",time.localtime(time.time()))) % 10, 1)
        time.sleep(t)
        showDigit(3, int(int(time.strftime("%M",time.localtime(time.time()))) / 10), 0)
        time.sleep(t)
        showDigit(4, int(int(time.strftime("%M", time.localtime(time.time()))) % 10), 0)
    for i in range(0, 500):
        time.sleep(t)
        showDigit(1, int(int(time.strftime("%m",time.localtime(time.time()))) / 10), 0)
        time.sleep(t)
        showDigit(2, int(time.strftime("%m",time.localtime(time.time()))) % 10, 1)
        time.sleep(t)
        showDigit(3, int(int(time.strftime("%d",time.localtime(time.time()))) / 10), 0)
        time.sleep(t)
        showDigit(4, int(time.strftime("%d",time.localtime(time.time()))) % 10, 0)



# 最后清理GPIO口（不做也可以，建议每次程序结束时清理一下，好习惯）
RPi.GPIO.cleanup()

