from tkinter import *
from tkinter import font as tkFont

class Startup_Window(object):
    def __init__(self, master, title, size):
        #TODO: create and initialize widgets
        self.master = master
        self.title = title
        self.size = size
        self.master.title(self.title)
        self.master.geometry(self.size)
        self.name = Label(self.master, text="Predictive Smoking Algorithm", font = helvetica(50, True))
        self.name.pack()
        self.items = ["Linear Regression", "Random Forest Regression", "KNN"] #KNN Optional
        for item in self.items:
            button = Button(self.master, text=item, width=25, pady = 50, font = helvetica(40)) #command not implented yet
            button.pack()

        #TODO: create layout
def helvetica(x, bold=False):
    return tkFont.Font(family='Helvetica', size=x, weight=(lambda bold: tkFont.BOLD if bold else tkFont.NORMAL) (bold) )
