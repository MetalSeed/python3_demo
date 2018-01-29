#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-01-29 19:21:52
# @Author  : MetalSeed (mc.gaofei@gmail.com)
# @Link    : ------------------
# @Version : $Id$


from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='This is a bullshit slogan!')
        self.helloLabel.pack()

        self.nameInput = Entry(self)
        self.nameInput.pack()

        self.alertButton = Button(self, text = 'Okay', command = self.hello)
        self.alertButton.pack()

        self.quitButton = Button(self, text='fuck off!', command = self.quit)
        self.quitButton.pack()

    def hello(self):
    	name = self.nameInput.get() or 'None'
    	messagebox.showinfo('Message', 'xx is %s' % name)


app = Application()
# 设置窗口标题:
app.master.title('Red')
# 主消息循环:
app.mainloop()     