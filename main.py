from tkinter import *
import tkinter as tk
# Press the green button in the gutter to run the script.
from StartupWindow import StartupWindow
from LinReg import LinRegWindow

if __name__ == '__main__':
    WIDTH = "1000"
    HEIGHT = "500"
    root = Tk()

    startup_window = StartupWindow(root, "DataGood Mentored Project", WIDTH + "x" + HEIGHT)
    # linreg_window = LinRegWindow(root, "Linear Regression",  WIDTH + "x" + HEIGHT)
    root.mainloop()
