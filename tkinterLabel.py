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
import tkinter
root=tkinter.Tk()
label1=tkinter.Label(root,anchor=tkinter.E,bg='blue',fg='red',text='Python',width=30,height=5)
label1.pack()
label2=tkinter.Label(root,text='Python GUI\nthinkter',justify=tkinter.LEFT,width=30,height=5)
label2.pack()
label3=tkinter.Label(root,text='Python GUI\nthinkter',justify=tkinter.RIGHT,width=30,height=5)
label3.pack()
label4=tkinter.Label(root,text='Python GUI\nthinkter',justify=tkinter.CENTER,width=30,height=5)
label4.pack()
root.mainloop()