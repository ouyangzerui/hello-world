#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# File:tkinterDialog.py
#---------------------------------------
#TO:
#---------------------------------------
#BY:
#---------------------------------------
# Date:2018-08-27
#---------------------------------------

import tkinter,tkinter.messagebox#导入tkinter模、tkMessageBox模块
class MyDialog(object):#定义对话框类
    def __init__(self,root):#对话框初始化
        self.top=tkinter.Toplevel(root)#生成Toplevel组件
        label=tkinter.Label(self.top,text='Please Input')#生成标签组件
        label.pack()
        self.entry=tkinter.Entry(self.top)#生成文本框组件
        self.entry.pack()
        self.entry.focus()#让文本框获得焦点
        button=tkinter.Button(self.top,text='OK',#生成按钮
        command=self.Ok)#设置按钮事件处理函数
    def Ok(self):#定义按钮事件处理函数
        self.input=self.entry.get()#获得文本框中的内容
        self.top.destroy()#销毁对话框
    def get(self):#返回在文本框输入的内容
        return self.input

class MyButton(object):#定义按钮类
    def __init__(self,root,type):#按钮初始化
        self.root=root#保存父窗口引用
        if type==0:#根据类型创建不同按钮
            self.button=tkinter.Button(root,text='Create',command=self.Create)#设置Create按钮的事件处理函数
        else:
            self.button=tkinter.Button(root,text='Quit',command=self.Quit)#设置Quit按钮的事件处理函数
        self.button.pack()
    def Create(self):#Create按钮的事件处理函数
        d=MyDialog(self.root)#生成对话框
        self.button.wait_window(d.top)#等待对话框结束
        tkMessageBox.showinfo('Python','You input:\n'+d.get())#获得对话框中输入值，并输出
    def Quit(self):#Quit按钮的事件处理函数
        self.root.quit()#退出主窗口

root=tkinter.Tk()#生成主窗口
MyButton(root,0)#生成Create按钮
MyButton(root,1)#生成Quit按钮
root.mainloop()#进入消息循环