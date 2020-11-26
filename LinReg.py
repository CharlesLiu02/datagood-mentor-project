from tkinter import *
from tkinter import font as tkFont

class LinRegWindow(object):
    def __init__(self, master, title, size):
        self.master = master
        self.title = title
        self.size = size
        self.master.title(self.title)
        self.master.geometry(self.size)
        self.content_frame = Frame(master, width=1000)
        self.sub_title_label = Label(self.content_frame, text="Linear Regression", font=helvetica(50, True))
        self.blurb_var = StringVar()
        self.blurb_var.set("Insert Blurb Here")
        self.blurb = Label(self.content_frame, textvariable=self.blurb_var, relief=RAISED,
                                    padx = 200, pady = 50, justify= CENTER, anchor = CENTER, font = helvetica(40))
        self.data = Label(self.content_frame, text="data", relief=RAISED,
                                    padx = 75, pady = 100, justify= CENTER, anchor = CENTER, font = helvetica(40))
        self.user_input = Label(self.content_frame, text="input", relief=RAISED,
                                    padx = 75, pady = 100, justify= CENTER, anchor = CENTER, font = helvetica(40))
        self.output = Label(self.content_frame, text="output", relief=RAISED,
                                    padx = 75, pady = 100, justify= CENTER, anchor = CENTER, font = helvetica(40))
        self.content_frame.grid(row=1,column=1)
        self.sub_title_label.grid(row=1,column=1)
        self.blurb.grid(row=2,column=1)
        self.data.grid(row=3,column=0)
        self.user_input.grid(row=3,column=1)
        self.output.grid(row=3,column=2)

def helvetica(x, bold=False):
    return tkFont.Font(family='Helvetica', size=x, weight=(lambda bold: tkFont.BOLD if bold else tkFont.NORMAL)(bold))
