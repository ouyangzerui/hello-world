#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# File:tkinterButton.py
#---------------------------------------
#TO:
#---------------------------------------
#BY:
#---------------------------------------
# Date:2018-08-27
#---------------------------------------

import tkinter#导入tkinter模块
root=tkinter.Tk()
button1=tkinter.Button(root,
anchor=tkinter.E,#指定文本对其方式
text='Button1',#指定按钮上的文本
width=40,#指定按钮宽度，相当于40个字符
height=5)#指定按钮的高度，相当于5个字符
button1.pack()#将按钮添加达到窗口中
button2=tkinter.Button(root,text='Button2',
bg='blue')#指定按钮的颜色
button2.pack()
button3=tkinter.Button(root,text='Button3',width=14,height=1)
button3.pack()
button4=tkinter.Button(root,text='Button4',width=60,height=5,
state=tkinter.DISABLED)#指定按钮为禁用状态
button4.pack()
root.mainloop()#进入消息循环