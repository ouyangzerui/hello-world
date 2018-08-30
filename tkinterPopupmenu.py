#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# File:tkinterPopupmenu.py
#---------------------------------------
#TO:
#---------------------------------------
#BY:
#---------------------------------------
# Date:2018-08-27
#---------------------------------------

import tkinter
root=tkinter.Tk()
menu=tkinter.Menu(root,tearoff=0)#创建菜单
menu.add_command(label='Copy')#向菜单添加Copy命令
menu.add_command(label='Paste')#向菜单添加Paste命令
menu.add_separator()#向菜单听分隔符
menu.add_command(label='Cut')#向菜单添加Cut命令
def popupmenu(event):#定义右键事件处理函数
    menu.post(event.x_root,event.y_root)#显示菜单
root.bind('<Button-3>',popupmenu)#在主窗口绑定右键事件
root.mainloop()