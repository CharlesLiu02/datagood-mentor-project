import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font as tkFont
from ChecklistBox import ChecklistBox

class LinRegWindow(object):
    def __init__(self, master, title, size):
        self.master = master
        self.title = title
        self.size = size
        self.master.title(self.title)
        self.master.geometry(self.size)
        self.sub_title_label = Label(self.master, text="Linear Regression", font=helvetica(50, True))
        self.blurb_var = StringVar()
        self.blurb_var.set("Insert Blurb Here")
        self.blurb = Label(self.master, textvariable=self.blurb_var, relief=RAISED,
                                    padx = 200, pady = 50, justify= CENTER, anchor = CENTER, font = helvetica(10))
        self.data_frame = Frame(self.master)
        self.output = Label(self.master, text="output", relief=RAISED,
                                    padx = 75, pady = 100, justify= CENTER, anchor = CENTER, font = helvetica(40))
        # setting up data
        self.treeview = ttk.Treeview(self.data_frame)
        self.treeview.place(relheight=1, relwidth=1)
        treescrolly = tk.Scrollbar(self.data_frame, orient="vertical",
                                   command=self.treeview.yview)  # command means update the yaxis view of the widget
        treescrollx = tk.Scrollbar(self.data_frame, orient="horizontal",
                                   command=self.treeview.xview)  # command means update the xaxis view of the widget
        self.treeview.configure(xscrollcommand=treescrollx.set,
                                yscrollcommand=treescrolly.set)  # assign the scrollbars to the Treeview Widget
        treescrollx.pack(side="bottom", fill="x")  # make the scrollbar fill the x axis of the Treeview widget
        treescrolly.pack(side="right", fill="y")  # make the scrollbar fill the y axis of the Treeview widget
        self.load_data()

        self.sub_title_label.place(width=500, height=70, relx=0.25, rely=0.02)
        self.blurb.place(width=500, height=100, relx=0.25, rely=0.15)
        self.data_frame.place(width=500, height=250, relx=0.01, rely=0.4)
        self.checklist.place(width=200, height=150, relx=0.01, rely=0.78)
        self.output.place(width=400, height=250, relx=0.55, rely=0.4)
        self.treeview.place(relheight=1, relwidth=1)

    def load_data(self):
        file = './insurance.csv'
        df = pd.read_csv(file)
        self.clear_data()
        self.treeview["column"] = list(df.columns)
        self.treeview["show"] = "headings"
        for column in self.treeview["columns"]:
            self.treeview.heading(column, text=column)  # let the column heading = column name

        df_rows = df.to_numpy().tolist()  # turns the dataframe into a list of lists
        for row in df_rows:
            self.treeview.insert("", "end",
                       values=row)  # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
        choices = df.columns
        self.checklist = ChecklistBox(self.master, choices, bd=1, relief="sunken", background="white")
        return None

    def clear_data(self):
        self.treeview.delete(*self.treeview.get_children())
        return None


def helvetica(x, bold=False):
    return tkFont.Font(family='Helvetica', size=x, weight=(lambda bold: tkFont.BOLD if bold else tkFont.NORMAL)(bold))
