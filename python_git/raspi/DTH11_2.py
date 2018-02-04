#! /usr/bin/python
# -*- coding:utf-8 -*-

import RPi.GPIO as GPIO #( 导入模块 )
import time

dht11_rpi_pin=4 #湿度温度连接的引脚号 GPIO4


GPIO.setmode(GPIO.BCM)
#(设置通道)
# 输出模式 初始状态给高电平 (dht11_rpi_pin)
GPIO.setup(dht11_rpi_pin, GPIO.OUT)
GPIO.output(dht11_rpi_pin, 1)
buff1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0]  # 定义一个长度为40的整型数组

GPIO.output(dht11_rpi_pin, 0)  # 输出低电平

time.sleep(0.02)  # 拉低20ms（延迟）

GPIO.output(dht11_rpi_pin, 1)  # 输出高电平

GPIO.setup(dht11_rpi_pin, GPIO.IN)  # 这里需要拉高20-40us,但更改模式需要50us,因此不调用延时

while not GPIO.input(dht11_rpi_pin):  # 检测返回信号 检测到启示信号的高电平结束
    pass

while GPIO.input(dht11_rpi_pin):  # 检测到启示信号的高电平则循环
    pass

i = 40

while i:
    start = time.time() * 1000000  # 为了严格时序 循环开始便计时
    i -= 1
    while not GPIO.input(dht11_rpi_pin):
        pass
    while GPIO.input(dht11_rpi_pin):
        pass
    buff1[i] = time.time() * 1000000 - start  # 为了严格时序 每次测得数据后都不马上处理 先存储

GPIO.setup(dht11_rpi_pin, GPIO.OUT)  # 读取结束 复位引脚
GPIO.output(dht11_rpi_pin, 1)
# print "buff1 - ",buff1

# 开始处理数据
for i in range(len(buff1)):  # 将时间转换为 0 1
    if buff1[i] > 100:  # 上方测试时是测试整个位的时间
        # 因此是与100比较 大于100为1(位周期中 低电平50us)
        buff1[i] = 1
    else:
        buff1[i] = 0
# print "After - ",buff1

humidity_bit = buff1[0:8]  # 分组
humidity_point_bit = buff1[8:16]
temperature_bit = buff1[16:24]
temperature_point_bit = buff1[24:32]
check_bit = buff1[32:40]

humidity = 0
humidity_point = 0
temperature = 0
temperature_point = 0
check = 0

for i in range(8):
    humidity += humidity_bit[i] * 2 ** (7 - i)  # 转换成十进制数据
    humidity_point += humidity_point_bit[i] * 2 ** (7 - i)
    temperature += temperature_bit[i] * 2 ** (7 - i)
    temperature_point += temperature_point_bit[i] * 2 ** (7 - i)
    check += check_bit[i] * 2 ** (7 - i)

tmp = humidity + humidity_point + temperature + temperature_point  # 十进制的数据相加

if check == tmp:  # 数据校验，相等则输出
    print("temperature : ", temperature, ", humidity : ", humidity)
else:  # 错误输出错误信息，和校验数据
    print("wrong")
    print("temperature : ", temperature, ", humidity : ", humidity, " check : ", check, " tmp : ", tmp)


GPIO.cleanup()

