# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 17:53:53 2017

@author: aaa
"""

import win32api
import win32con
import win32gui

wrHd=win32gui.FindWindow('Notepad.exe','1.txt - 记事本')
win32gui.ShowWindow(wrHd,win32con.SW_SHOWNORMAL)

win32api.keybd_event(17,0,0,0)  #ctrl键位码是17
win32api.keybd_event(86,0,0,0)  #v键位码是86
win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)

