#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# File:tkinterCheck.py
#---------------------------------------
#TO:
#---------------------------------------
#BY:
#---------------------------------------
# Date:2018-08-27
#---------------------------------------
import tkinter
root=tkinter.Tk()
r=tkinter.StringVar()#使用StringVar生成字符串变量，用于单选框
r.set('1')#初始化变量值
radio=tkinter.Radiobutton(root,#生成单选框组件
variable=r,#设置单选框关联的变量
value='1',#设置选中单选框时其所关联的变量的值
text='Radio1',#设置单选框显示的文本
indicatoron=0)#将单选框设置为按钮样式
radio.pack()
radio=tkinter.Radiobutton(root,variable=r,value='2',#当选中该单选框时r的值为2
text='Radio2',indicatoron=0)
radio.pack()
radio=tkinter.Radiobutton(root,variable=r,value='3',#当选中该单选框时r的值为3
text='Radio3',indicatoron=0)
radio.pack()
radio=tkinter.Radiobutton(root,variable=r,value='4',#当选中该单选框时r的值为4
text='Radio4',indicatoron=0)
radio.pack()
c=tkinter.IntVar()#使用IntVar生成整型变量，用于复选框
c.set(1)
check=tkinter.Checkbutton(root,text='Checkbutton',#设置复选框的文本
variable=c,#设置复选框关联的变量
onvalue=1,#当选中复选框时，c的值为1
offvalue=2,#当未选中复选框时，c的值为2
indicatoron=0)
check.pack()
root.mainloop()
print(r.get())#输出r的值
print(c.get())#输出c的值