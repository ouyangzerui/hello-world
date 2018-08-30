#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# File:tkinterEntry.py
#---------------------------------------
#TO:
#---------------------------------------
#BY:
#---------------------------------------
# Date:2018-08-27
#---------------------------------------

import tkinter#导入tkinter模块
root=tkinter.Tk()
entry1=tkinter.Entry(root,#生成单行文本框组件
show='*')#输入文本框中的内容被显示为“*”
entry1.pack()#将文本框添加到窗口中
entry2=tkinter.Entry(root,show='#',#输入文本框中的内容被显示为“#”
width=50)#将文本框的宽度设置为50个字符
entry2.pack()
entry3=tkinter.Entry(root,bg='red',#文本框的背景颜色设置为红色
fg='blue')#文本框的前景色设置为蓝色
entry3.pack()
entry4=tkinter.Entry(root,selectbackground='red',#将选中文本的背景颜色设置为红色
selectforeground='gray')#将选中文本的前景色设置为灰色
entry4.pack()
entry5=tkinter.Entry(root,state=tkinter.DISABLED)#将文本框设置为禁用
entry5.pack()
edit1=tkinter.Text(root,selectbackground='gray',#将选中文本的背景色设置为红色
selectforeground='red')#将选中文本的前景色设置为灰色
edit1.pack()
root.mainloop()#进入消息循环