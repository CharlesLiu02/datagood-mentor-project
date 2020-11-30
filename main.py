from tkinter import *
import tkinter as tk
# Press the green button in the gutter to run the script.
from StartupWindow import StartupWindow
from LinReg import LinRegWindow

if __name__ == '__main__':
    WIDTH = "800"
    HEIGHT = "600"
    root = Tk()
    root.resizable(False, False)

    startup_window = StartupWindow(root, "Health Insurance Prediction Tool", WIDTH + "x" + HEIGHT)
    root.mainloop()
