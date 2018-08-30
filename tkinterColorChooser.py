#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# File:tkinterColorChooser.py
#---------------------------------------
#TO:
#---------------------------------------
#BY:
#---------------------------------------
# Date:2018-08-27
#---------------------------------------

import tkinter,tkinter.colorchooser#导入tkinter模块、tkColorChooser模块
def ChooseColor():#按钮事件处理函数
    r=tkinter.colorchooser.askcolor(title='Python tkinter')#创建颜色选择对话框
    print(r)#输出返回值
root=tkinter.Tk()
button=tkinter.Button(root,text='Choose Color',#创建按钮
command=ChooseColor)#指定按钮事件处理函数
button.pack()
root.mainloop()#进入消息循环