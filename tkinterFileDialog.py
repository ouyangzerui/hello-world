#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# File:tkinterFileDialog.py
#---------------------------------------
#TO:
#---------------------------------------
#BY:
#---------------------------------------
# Date:2018-08-27
#---------------------------------------

import tkinter,tkinter.filedialog,os#导入tkinter模块、tkFieldDialog模块
def FileOpen():#按钮事件处理函数
    r=tkinter.filedialog.askopenfilename(title='Python tkinter',#创建打开文件对话框
    filetypes=[('Python','*.py *.pyw'),('All files','*')])#指定文本类型为Python脚本
    print(r)#输出返回值
def FileSave():#按钮事件处理函数
    r=tkinter.filedialog.asksaveasfilename(title='Python tkinter',#创建保存文件对话框
    initialdir=os.path.abspath('.'),#指定初始化目录
    initialfile='test.py')#指定初始化文件
    print(r)

root=tkinter.Tk()
button1=tkinter.Button(root,text='File Open',#创建按钮
command=FileOpen)#指定按钮事件处理函数
button1.pack(side='left')
button2=tkinter.Button(root,text='File Save',command=FileSave)#指定按钮事件处理函数
button2.pack(side='left')
root.mainloop()#进入消息循环