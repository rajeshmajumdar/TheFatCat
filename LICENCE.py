# License for freakymonk

# Copyright 2017-18 by Rajesh Majumdar <@freakym0nk>

# Web : www.rajeshmajumdar.github.io
# Contact : @freakym0nk

# All Rights Reserved 

# Permission to use, copy, modify, and distribute this software and its 
# documentation for any purpose and without fee is hereby granted, 
# provided that the above copyright notice appear in all copies and that 
# both that copyright notice and this permission notice appear in 
# supporting documentation.

# Project Name : freakymonk
# Project Date : 17-12-2016
# Author : Rajesh Majumdar
# Contact : @freakym0nk

#!/usr/bin/env python
#-*- coding:utf-8-*-

from Tkinter import *
from tkMessageBox import *

MainWindow = Tk()
MainWindow.geometry("155x300+150+100")
MainWindow.title("License")

def Button1Click():
	print "Hello freakymonk "

Button1 = Button(text = "Click Me", command = Button1Click)
Button1 .place(relx = 0.5, rely = 0.5, relheight = 0.20)

mainloop()
