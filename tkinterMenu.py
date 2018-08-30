#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# File:tkinterMenu.py
#---------------------------------------
#TO:
#---------------------------------------
#BY:
#---------------------------------------
# Date:2018-08-27
#---------------------------------------

import tkinter#导入tkinter模块
root=tkinter.Tk()
menu=tkinter.Menu(root)#生成菜单
submenu=tkinter.Menu(menu,tearoff=0)#生成下拉菜单
submenu.add_command(label='Open')#向下拉菜单中添加Open命令
submenu.add_command(label='Save')#向下拉菜单添加Save命令
submenu.add_command(label='Close')#向下拉菜单添加Close命令
menu.add_cascade(label='File',menu=submenu)#将下拉菜单添加到菜单中
submenu=tkinter.Menu(menu,tearoff=0)#生成下拉菜单
submenu.add_command(label='Copy')#向下拉菜单添加Copy命令
submenu.add_command(label='Paste')#向下拉菜单添加Paste命令
submenu.add_separator()#向下拉菜单添加分隔符
submenu.add_command(label='Cut')#向下拉菜单添加Cut命令
menu.add_cascade(label='Edit',menu=submenu)#将下拉菜单添加到菜单中
submenu=tkinter.Menu(menu,tearoff=0)#生成下拉菜单
submenu.add_command(label='About')#向下拉菜单添加About命令
menu.add_cascade(label='Help',menu=submenu)#将下拉菜单添加到菜单中
root.config(menu=menu)
root.mainloop()