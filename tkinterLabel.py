#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# File:tkinterLabel.py
#---------------------------------------
#TO:
#---------------------------------------
#BY:
#---------------------------------------
# Date:2018-08-27
#---------------------------------------
import tkinter#导入tkinter模块
root=tkinter.Tk()
label1=tkinter.Label(root,anchor=tkinter.E,#设置文本的位置
bg='blue',#设置标签背景色
fg='red',#设置标签前景色
text='Python',#设置标签中的文本
width=30,#设置标签的宽度为30
height=5)#设置标签的高度为5
label1.pack()
label2=tkinter.Label(root,text='Python GUI\nthinkter',#设置标签中的文本
justify=tkinter.LEFT,#设置多行文本为左对齐
width=30,height=5)
label2.pack()
label3=tkinter.Label(root,text='Python GUI\nthinkter',
justify=tkinter.RIGHT,#设置多行文本为右对齐
width=30,height=5)
label3.pack()
label4=tkinter.Label(root,text='Python GUI\nthinkter',
justify=tkinter.CENTER,#设置多行文本为居中对齐
width=30,height=5)
label4.pack()
root.mainloop()