from tkinter import *
import tkinter as tk
# Press the green button in the gutter to run the script.
from StartupWindow import StartupWindow

if __name__ == '__main__':
    WIDTH = "800"
    HEIGHT = "800"
    root = Tk()
    startup_window = StartupWindow(root, "DataGood Mentored Project", WIDTH + "x" + HEIGHT)
    root.mainloop()
