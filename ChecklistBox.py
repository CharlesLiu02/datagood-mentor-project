import tkinter as tk
from tkinter import *
from entry_with_placeholder import EntryWithPlaceholder

class ChecklistBox(tk.Frame):
    def __init__(self, parent, isChildren, isKNN, choices, **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)

        self.vars = []
        bg = self.cget("background")
        self.checker = IntVar()
        self.age_checker = IntVar()
        self.charges_checker = IntVar()
        self.children_checker = IntVar()
        self.age_entry = EntryWithPlaceholder(self, "Enter age ")
        self.charges_entry = EntryWithPlaceholder(self, "Enter $ of charges")
        self.children_entry = EntryWithPlaceholder(self, "Enter # children")
        def activateCheck(KNN=False, checker = None, entry = None):
            if KNN:
                if checker_var.get() == 1:  # whenever checked
                    entry.config(state=NORMAL)
                elif checker_var.get() == 0:  # whenever unchecked
                    entry.config(state=DISABLED)
            else:
                if self.checker.get() == 1:  # whenever checked
                    self.entry.config(state=NORMAL)
                elif self.checker.get() == 0:  # whenever unchecked
                    self.entry.config(state=DISABLED)

        if isKNN:
            quantitative = [self.age_checker, self.charges_checker, self.children_checker]
            entries = [self.age_entry, self.charges_entry, self.children_entry]
            for choice in choices:
                var = tk.StringVar(value=choice)
                entry = entries.pop()
                checker_var= quantitative.pop()
                self.vars.append(var)
                cb = Checkbutton(self, variable=checker_var , command=activateCheck(True,checker_var,entry), text= choice + " : ",
                                       background=bg, relief="flat", highlightthickness=0)
                cb.pack(side="top", fill="x", anchor="w")
                entry.pack(side="top")
                entry.config(state=DISABLED)
                cb.deselect()

        else:
            for choice in choices:
                var = tk.StringVar(value=choice)
                self.vars.append(var)
                cb = tk.Checkbutton(self, var=var, text=choice,
                                    onvalue=choice, offvalue="",
                                    anchor="w", width=20, background=bg,
                                    relief="flat", highlightthickness=0)
                cb.deselect()
                cb.pack(side="top", fill="x", anchor="w")




            if isChildren:
                self.chk = Checkbutton(self, variable=self.checker, command=activateCheck, text="children: ",
                                       background=bg, relief="flat", highlightthickness=0)
                self.chk.pack(side="left")
                self.entry = EntryWithPlaceholder(self, "Enter # children")

                self.entry.pack(side="left")
                self.entry.config(state=DISABLED)


    def getCheckedItems(self):
        values = []
        for var in self.vars:
            value = var.get()
            if value:
                values.append(value)
        if self.checker.get() == 1:
            values.append("children: " + str(self.entry.get()))
        elif self.age_checker.get() == 1:
            values.append("age: " + str(self.age_entry.get()))
        elif self.charges_checker.get() == 1:
            values.append("charges: " + str(self.charges_entry.get()))
        elif self.children_checker.get() == 1:
            values.append("children: " + str(self.children_entry.get()))
        return values
