#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# File:tkinterSimpleDialog.py
#---------------------------------------
#TO:
#---------------------------------------
#BY:
#---------------------------------------
# Date:2018-08-27
#---------------------------------------
import tkinter,tkinter.simpledialog#导入tkinter模块、tkSimpleDialog模块
def InStr():#按钮事件处理函数
    r=tkinter.simpledialog.askstring('Python tkinter',#创建字符串输入对话框
    'Input String',#指定提示字符
    initialvalue='tkinter')#指定初始化文本
    print(r)#输出返回值 
def InInt():#按钮事件处理函数
    r=tkinter.simpledialog.askinteger('Python tkinter','Input Integer',initialvalue=55)#创建整数对话输入框
    print(r)
def InFlo():#按钮事件处理函数
    r=tkinter.simpledialog.askfloat('Python tkinter','Input Float',initialvalue=3.14)#创建浮点数输入对话框
    print(r)

root=tkinter.Tk()
button1=tkinter.Button(root,text='Input String',#创建按钮
command=InStr)#指定按钮事件处理函数
button1.pack(side='left')
button2=tkinter.Button(root,text='Input Integer',
command=InInt)#指定按钮事件处理函数
button2.pack(side='left')
button3=tkinter.Button(root,text='Input Float',
command=InFlo)#指定按钮事件处理函数
button3.pack(side='left')
root.mainloop()#进入消息循环