from tkinter import *
# Press the green button in the gutter to run the script.
from Startup_Window import Startup_Window

if __name__ == '__main__':
    WIDTH = "600"
    HEIGHT = "600"
    root = Tk()
    startup_window = Startup_Window(root, "DataGood Mentored Project", WIDTH + "x" + HEIGHT)
    root.mainloop()
