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

import tkinter,tkinter.colorchooser
def ChooseColor():
    r=tkinter.colorchooser.askcolor(title='Python tkinter')
    print(r)
root=tkinter.Tk()
button=tkinter.Button(root,text='Choose Color',command=ChooseColor)
button.pack()
root.mainloop()