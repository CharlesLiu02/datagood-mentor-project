from tkinter import *
from tkinter import font as tkFont
from LinReg import LinRegWindow

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
        self.linear_button = Button(self.content_frame, text="Linear Regression", width=25, pady=50,
                                               font=helvetica(40))
        self.random_forest_button = Button(self.content_frame, text="Random Forest Regression", width=25, pady=50,
                                           font=helvetica(40))
        self.knn_button = Button(self.content_frame, text="K Nearest Neighbors", width=25, pady=50, font=helvetica(40))

        self.content_frame.grid(row=1)
        self.sub_title_label.grid(row=0)
        self.linear_button.grid(row=1)
        self.random_forest_button.grid(row=2)
        self.knn_button.grid(row=3)

        self.linear_button.bind("<Button-1>", self.create_linear)
        self.random_forest_button.bind("<Button-1>", self.create_random_forest)
        self.knn_button.bind("<Button-1>", self.create_knn)
        self.linear_window = None
        self.forest_window = None
        self.knn_window = None

    def create_linear(self, event):
        # TODO: create new window
        root = Tk()
        self.linear_window = LinRegWindow(root, "Linear Regression", "600x600")
        root.mainloop()

    def create_random_forest(self, event):
        # TODO: create new window
        root = Tk()
        # self.forest_window = ForestWindow(root, "Random Forest Regression", "600x600")
        root.mainloop()

    def create_knn(self):
        # TODO: create new window
        root = Tk()
        # self.knn_window = KNNWindow(root, "K Nearest Neighbors", "600x600")
        root.mainloop()


def helvetica(x, bold=False):
    return tkFont.Font(family='Helvetica', size=x, weight=(lambda bold: tkFont.BOLD if bold else tkFont.NORMAL)(bold))
