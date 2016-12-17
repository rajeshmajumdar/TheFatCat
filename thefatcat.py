#!/usr/bin/env python
__author__ = 'Rajesh Majumdar'

from tkinter import *

import os

top = Tk()

def execute():
    if os.name=='nt':
        if (wordlistchecked.get()==1):
            final_cmd = 'core.py -w '+wordlist.get()+' '+url.get()
            os.system(final_cmd)
        else:
            final_cmd = 'core.py '+url.get()
            os.system(final_cmd)
        top.iconbitmap('icon.ico')
    else:
        if (wordlistchecked.get()==1):
            final_cmd = 'python core.py -w '+wordlist.get()+' '+url.get()
            os.system(final_cmd)
        else:
            final_cmd = 'python core.py '+url.get()
            os.system(final_cmd)
    

top.geometry("437x450+501+127")
top.title("TheFatCat - Subdomain Takeover Finder")
top.configure(background="#d9d9d9")
top.configure(highlightbackground="#d9d9d9")
top.configure(highlightcolor="black")


# URL Entry

url = Entry(top)
url.place(relx=0.18, rely=0.07, relheight=0.04, relwidth=0.54)
url.configure(background="white")
url.configure(disabledforeground="#a3a3a3")
url.configure(font="TkFixedFont")
url.configure(foreground="#000000")
url.configure(highlightbackground="#d9d9d9")
url.configure(highlightcolor="black")
url.configure(insertbackground="black")
url.configure(selectbackground="#c4c4c4")
url.configure(selectforeground="black")

# Submit Button

submit = Button(top, command=execute)
submit.place(relx=0.78, rely=0.09, height=34, width=67)
submit.configure(activebackground="#d9d9d9")
submit.configure(activeforeground="#000000")
submit.configure(background="#d9d9d9")
submit.configure(disabledforeground="#a3a3a3")
submit.configure(foreground="#000000")
submit.configure(highlightbackground="#d9d9d9")
submit.configure(highlightcolor="black")
submit.configure(pady="0")
submit.configure(text='''Submit''')

# Label

Label1 = Label(top)
Label1.place(relx=0.02, rely=0.07, height=21, width=64)
Label1.configure(activebackground="#f9f9f9")
Label1.configure(activeforeground="black")
Label1.configure(background="#d9d9d9")
Label1.configure(disabledforeground="#a3a3a3")
Label1.configure(foreground="#000000")
Label1.configure(highlightbackground="#d9d9d9")
Label1.configure(highlightcolor="black")
Label1.configure(text='''Enter URL:''')

# Wordlist Checkbox

wordlistchecked = IntVar()
wordlistcheck = Checkbutton(top, variable=wordlistchecked, command=execute)
wordlistcheck.place(relx=0.05, rely=0.16, relheight=0.06
                , relwidth=0.26)
wordlistcheck.configure(activebackground="#d9d9d9")
wordlistcheck.configure(activeforeground="#000000")
wordlistcheck.configure(background="#d9d9d9")
wordlistcheck.configure(disabledforeground="#a3a3a3")
wordlistcheck.configure(foreground="#000000")
wordlistcheck.configure(highlightbackground="#d9d9d9")
wordlistcheck.configure(highlightcolor="black")
wordlistcheck.configure(justify=LEFT)
wordlistcheck.configure(text='''Custom wordlist''')


# Wordlist Path

wordlist = Entry(top)
wordlist.place(relx=0.34, rely=0.16, relheight=0.04, relwidth=0.38)
wordlist.configure(background="white")
wordlist.configure(disabledforeground="#a3a3a3")
wordlist.configure(font="TkFixedFont")
wordlist.configure(foreground="#000000")
wordlist.configure(highlightbackground="#d9d9d9")
wordlist.configure(highlightcolor="black")
wordlist.configure(insertbackground="black")
wordlist.configure(selectbackground="#c4c4c4")
wordlist.configure(selectforeground="black")

# Output Box

output = Text(top)
output.place(relx=0.05, rely=0.33, relheight=0.63, relwidth=0.9)
output.insert(END, "This part is currently under development.\n\n\tAuthor: Rajesh Majumdar (@freakym0nk)\n\tWebsite: https://rajeshmajumdar.github.io/\n\tContact: @freakym0nk\n\nSorry! but the results would be in the terminal.\nI'm working on it.")

top.mainloop()
