from tkinter import *
import tkinter as tk
# Press the green button in the gutter to run the script.
from Startup_Window import Startup_Window

if __name__ == '__main__':
    WIDTH = "800"
    HEIGHT = "800"
    root = Tk()
    startup_window = Startup_Window(root, "DataGood Mentored Project", WIDTH + "x" + HEIGHT)
    root.mainloop()
