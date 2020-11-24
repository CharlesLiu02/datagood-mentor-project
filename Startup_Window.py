from tkinter import *

class Startup_Window(object):
    def __init__(self, master, title, size):
        #TODO: create and initialize widgets

        #TODO: create layout
        self.title_frame.grid()
        self.main_title_label.grid(row=0, columnspan=2)
        self.content_frame.grid(row=1)
        self.sub_title_label.grid(row=0)
        self.linear_regression_button.bind(row=1)
        self.random_forest.bind(row=2)
