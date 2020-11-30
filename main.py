from tkinter import *
from StartupWindow import StartupWindow

if __name__ == '__main__':
    WIDTH = "800"
    HEIGHT = "600"
    root = Tk()
    root.resizable(False, False)

    startup_window = StartupWindow(root, "Health Insurance Prediction Tool", WIDTH + "x" + HEIGHT)
    root.mainloop()
