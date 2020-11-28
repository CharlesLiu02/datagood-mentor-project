import tkinter as tk
from tkinter import *
from entry_with_placeholder import EntryWithPlaceholder

class ChecklistBox(tk.Frame):
    def __init__(self, parent, isChildren, choices, **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)

        self.vars = []
        bg = self.cget("background")
        for choice in choices:
            var = tk.StringVar(value=choice)
            self.vars.append(var)
            cb = tk.Checkbutton(self, var=var, text=choice,
                                onvalue=choice, offvalue="",
                                anchor="w", width=20, background=bg,
                                relief="flat", highlightthickness=0,
            )
            cb.deselect()
            cb.pack(side="top", fill="x", anchor="w")

        def activateCheck():
            if self.checker.get() == 1:  # whenever checked
                self.entry.config(state=NORMAL)
            elif self.checker.get() == 0:  # whenever unchecked
                self.entry.config(state=DISABLED)

        self.checker = IntVar()
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
        return values