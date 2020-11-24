from tkinter import *
from tkinter import font as tkFont


class StartupWindow(object):
    def __init__(self, master, title, size):
        self.master = master
        self.title = title
        self.size = size
        self.master.title(self.title)
        self.master.geometry(self.size)
        self.content_frame = Frame(master)
        self.sub_title_label = Label(self.content_frame, text="Predictive Smoking Algorithm", font=helvetica(50, True))
        self.sub_title_label.pack()
        self.linear_regression_button = Button(self.content_frame, text="Linear Regression", width=25, pady=50,
                                               font=helvetica(40))
        self.random_forest_button = Button(self.content_frame, text="Random Forest Regression", width=25, pady=50,
                                           font=helvetica(40))
        self.knn_button = Button(self.content_frame, text="K Nearest Neighbors", width=25, pady=50, font=helvetica(40))

        self.content_frame.grid(row=1)
        self.sub_title_label.grid(row=0)
        self.linear_regression_button.grid(row=1)
        self.random_forest_button.grid(row=2)
        self.knn_button.grid(row=3)


def helvetica(x, bold=False):
    return tkFont.Font(family='Helvetica', size=x, weight=(lambda bold: tkFont.BOLD if bold else tkFont.NORMAL)(bold))
