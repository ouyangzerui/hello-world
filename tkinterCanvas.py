#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# File:tkinterCanvas.py
#---------------------------------------
#TO:
#---------------------------------------
#BY:
#---------------------------------------
# Date:2018-08-27
#---------------------------------------

import tkinter#导入tkinter模块
root=tkinter.Tk()
canvas=tkinter.Canvas(root,width=600,#指定Canvas组件的宽度
height=480,#指定Canvas组件的高度
bg='white')#指定Canvas组件的背景色
im=tkinter.PhotoImage(file='python.gif')#使用PhotoImage打开图片
canvas=create_image(300,50,image=im)#使用create_image将图片添加到Canvas组件中
canvas.create_text(302,77,#使用create_text方法绘文字
text='Use Canvas',#所绘制的文字内容
fill='gray')#所绘制的文字颜色为灰色
canvas.create_text(300,75,text='Use Canvas',fill='blue')
canvas.create_polygon(290,114,316,114,330,130,310,146,284,146,270,130)#使用create_polygon方法绘制六边形
canvas.create_oval(280,120,320,140,#使用create_oval方法绘制椭圆
fill='white')#设置椭圆的填充为白色
canvas.create_line(250,130,350,130)#使用create_line绘制直线
canvas.create_line(300,100,300,160)
canvas.create_rectangle(90,190,510,410,width=5)#使用create_rectangle绘制矩形，矩形线宽为5像素
canvas.create_arc(100,200,500,400,#使用create_arc绘制弧形
start=0,extent=240,#设置弧形的起止角度
fill='pink')#设置圆弧的填充颜色
canvas.create_arc(103,203,500,400,start=241,extent=118,fill='red')
canvas.pack()#将Canvas添加到主窗口
root.mainloop()