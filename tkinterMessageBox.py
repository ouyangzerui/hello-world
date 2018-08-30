#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# File:tkinterMessageBox.py
#---------------------------------------
#TO:
#---------------------------------------
#BY:
#---------------------------------------
# Date:2018-08-27
#---------------------------------------
import tkinter,tkinter.messagebox#导入tkinter模块、tkMessagebox模块

def cmd():#按钮消息处理函数
    global n#使用全局变量n
    global buttontext #使用全局变量buttontext
    n=n+1
    if n==1:#判断n的值，显示不同的消息框
        tkinter.messagebox.askokcancel('Python tkinter','askokcancel')#使用askokcancel函数
        buttontext.set('skquestion')#更改按钮上的文字
    elif n==2:
        tkinter.messagebox.askquestion('Python tkinter','skquestion')#使用askquestion函数
        buttontext.set('askyesno')
    elif n==3:
        tkinter.messagebox.askyesno('Python tkinter','askyesno')#使用askyesno函数
        buttontext.set('showerror')
    elif n==4:
        tkinter.messagebox.showerror('Python tkinter','showerror')#使用showerror函数
        buttontext.set('showinfo')
    elif n==5:
        tkinter.messagebox.showinfo('Python tkinter','showinfo')#使用showinfo函数
        buttontext.set('showwarning')
    else:
        n=0#将n赋值为0重新开始循环
        tkinter.messagebox.showwarning('Python tkinter','showwarning')#使用showwarning函数
        buttontext.set('askokcancel')
n=0#为n赋初始值
root=tkinter.Tk()
buttontext=tkinter.StringVar()#生成关联按钮文字的变量
buttontext.set('askokcancel')#设置buttontext的值
button=tkinter.Button(root,#生成按钮
textvariable=buttontext,#设置关联变量
command=cmd)#设置时间处理函数
button.pack()
root.mainloop()#进入消息循环