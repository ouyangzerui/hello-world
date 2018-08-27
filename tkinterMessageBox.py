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
import tkinter,tkinter.messagebox

def cmd():
    global n
    global buttontext
    n=n+1
    if n==1:
        tkinter.messagebox.askokcancel('Python tkinter','askokcancel')
        buttontext.set('skquestion')
    elif n==2:
        tkinter.messagebox.askquestion('Python tkinter','skquestion')
        buttontext.set('askyesno')
    elif n==3:
        tkinter.messagebox.askyesno('Python tkinter','askyesno')
        buttontext.set('showerror')
    elif n==4:
        tkinter.messagebox.showerror('Python tkinter','showerror')
        buttontext.set('showinfo')
    elif n==5:
        tkinter.messagebox.showinfo('Python tkinter','showinfo')
        buttontext.set('showwarning')
    else:
        n=0
        tkinter.messagebox.showwarning('Python tkinter','showwarning')
        buttontext.set('askokcancel')
n=0
root=tkinter.Tk()
buttontext=tkinter.StringVar()
buttontext.set('askokcancel')
button=tkinter.Button(root,textvariable=buttontext,command=cmd)
button.pack()
root.mainloop()