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
        self.bmi_checker = IntVar()
        self.age_entry = EntryWithPlaceholder(self, "Enter age ")
        self.charges_entry = EntryWithPlaceholder(self, "Enter $ of charges")
        self.children_entry = EntryWithPlaceholder(self, "Enter # children")
        self.bmi_entry = EntryWithPlaceholder(self, "Enter BMI")
        def activateCheck():
            if self.checker.get() == 1:  # whenever checked
                self.entry.config(state=NORMAL)
                self.age.config(state=NORMAL)
            elif self.checker.get() == 0:  # whenever unchecked
                self.entry.config(state=DISABLED)
                self.age.config(state=DISABLED)
        def activateAgeCheck():
            if self.age_checker.get() == 1:  # whenever checked
                self.age_entry.config(state=NORMAL)
            elif self.age_checker.get() == 0:  # whenever unchecked
                self.age_entry.config(state=DISABLED)
        def activateChargesCheck():
            if self.charges_checker.get() == 1:  # whenever checked
                self.charges_entry.config(state=NORMAL)
            elif self.charges_checker.get() == 0:  # whenever unchecked
                self.charges_entry.config(state=DISABLED)
        def activateChildrenCheck():
            if self.children_checker.get() == 1:  # whenever checked
                self.children_entry.config(state=NORMAL)
            elif self.children_checker.get() == 0:  # whenever unchecked
                self.children_entry.config(state=DISABLED)
        def activateBMICheck():
            if self.bmi_checker.get() == 1:  # whenever checked
                self.bmi_entry.config(state=NORMAL)
            elif self.bmi_checker.get() == 0:  # whenever unchecked
                self.bmi_entry.config(state=DISABLED)

        if isKNN:
            checker_vars = [self.age_checker, self.charges_checker, self.children_checker, self.bmi_checker]
            entries = [self.age_entry, self.charges_entry, self.children_entry, self.bmi_entry]
            checker_funcs = [activateAgeCheck, activateChargesCheck, activateChildrenCheck, activateBMICheck]
            for i in range(len(choices)):
                cb = Checkbutton(self, variable=checker_vars[i], command=checker_funcs[i], text= choices[i],
                                       background=bg, relief="flat", highlightthickness=0)
                cb.pack(side="top", fill="x", anchor="w")
                entries[i].pack(side="top")
                entries[i].config(state=DISABLED)
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
        if self.age_checker.get() == 1:
            values.append("age " + str(self.age_entry.get()))
        if self.charges_checker.get() == 1:
            values.append("charges " + str(self.charges_entry.get()))
        if self.children_checker.get() == 1:
            values.append("children " + str(self.children_entry.get()))
        if self.bmi_checker.get() == 1:
            values.append("bmi: " + str(self.children_entry.get()))
        return values
