import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font as tkFont
from ChecklistBox import ChecklistBox

class RandomForestWindow(object):
    def __init__(self, master, title, size):
        self.master = master
        self.title = title
        self.size = size
        self.master.title(self.title)
        self.master.geometry(self.size)
        self.sub_title_label = Label(self.master, text="Random Forest Regression", font=helvetica(30, True))
        self.blurb_var = StringVar()
        self.blurb_var.set( "Random forest is a Supervised Learning algorithm which uses ensemble learning method for classification."
                            " Shown below is a data set of insurance charges for different "
                            "individuals with different characteristics. You can select certain parameters you want "
                            "to use for your random forest regression model and the program will display the predicted charges "
                            "based on your model and its error compared to the actual charges. For each category,"
                            "please only select on parameter (ex: only selecting northwest). You must select at least "
                            "one quantitative measurement.")
        self.blurb = Label(self.master, textvariable=self.blurb_var, relief=RAISED,
                                    padx = 200, pady = 50, justify= CENTER, anchor = CENTER, font = helvetica(10), wraplength=500)
        self.input_label = Label(self.master, text="Input Data", font=helvetica(20))
        self.output_label = Label(self.master, text="Output Data", font=helvetica(20))
        self.error_label = Label(self.master, text="", font=helvetica(15), justify=LEFT, wraplength=400)
        self.data_frame = Frame(self.master)
        self.output_frame = Frame(self.master)
        self.submit_button = Button(self.master, text="Click for random forest regression", width=20, font=helvetica(8))
        # setting up data
        self.input_treeview = ttk.Treeview(self.data_frame)
        self.input_treeview.place(relheight=1, relwidth=1)
        input_treescrolly = tk.Scrollbar(self.data_frame, orient="vertical",
                                   command=self.input_treeview.yview)  # command means update the yaxis view of the widget
        input_treescrollx = tk.Scrollbar(self.data_frame, orient="horizontal",
                                   command=self.input_treeview.xview)  # command means update the xaxis view of the widget
        self.input_treeview.configure(xscrollcommand=input_treescrollx.set,
                                      yscrollcommand=input_treescrolly.set)  # assign the scrollbars to the Treeview Widget
        input_treescrollx.pack(side="bottom", fill="x")  # make the scrollbar fill the x axis of the Treeview widget
        input_treescrolly.pack(side="right", fill="y")  # make the scrollbar fill the y axis of the Treeview widget
        file = './insurance.csv'
        self.df = pd.read_csv(file).sort_values(by=['age', 'sex', 'bmi'], ascending=True)
        self.load_data(self.input_treeview, self.df,[])

        choices1 = ["age", "sex: male", "sex: female", "bmi", "smoker: no", "smoker: yes", ]
        self.checklist1 = ChecklistBox(self.master, True, False, choices1, bd=1, relief="sunken", background="white")
        choices2 = ["region: northwest", "region: northeast", "region: southwest", "region: southeast"]
        self.checklist2 = ChecklistBox(self.master, False, False, choices2, bd=1, relief="sunken", background="white")

        self.output_treeview = ttk.Treeview(self.output_frame)
        self.output_treeview.place(relheight=1, relwidth=1)
        output_treescrolly = tk.Scrollbar(self.output_frame, orient="vertical",
                                         command=self.output_treeview.yview)  # command means update the yaxis view of the widget
        output_treescrollx = tk.Scrollbar(self.output_frame, orient="horizontal",
                                         command=self.output_treeview.xview)  # command means update the xaxis view of the widget
        self.output_treeview.configure(xscrollcommand=output_treescrollx.set,
                                      yscrollcommand=output_treescrolly.set)  # assign the scrollbars to the Treeview Widget
        output_treescrollx.pack(side="bottom", fill="x")  # make the scrollbar fill the x axis of the Treeview widget
        output_treescrolly.pack(side="right", fill="y")  # make the scrollbar fill the y axis of the Treeview widget

        self.sub_title_label.place(width=500, height=70, relx=0.25, rely=0.02)
        self.input_label.place(width=100, height=40, relx=0.18, rely=0.36)
        self.output_label.place(width=120, height=40, relx=0.67, rely=0.36)
        self.error_label.place(width=400, height=100, relx=0.5, rely=0.78)
        self.blurb.place(width=500, height=100, relx=0.25, rely=0.15)
        self.data_frame.place(width=450, height=250, relx=0.01, rely=0.4)
        self.checklist1.place(width=200, height=150, relx=0.01, rely=0.78)
        self.checklist2.place(width=200, height=150, relx=0.25, rely=0.78)
        self.output_frame.place(width=450, height=250, relx=0.5, rely=0.4)
        self.submit_button.place(width=150, height=30, relx=0.5, rely=0.78)

        self.submit_button.bind("<Button-1>", self.random_forest_regression)

    def load_data(self, treeview, data, columns):
        data = data.drop(columns, axis=1)
        self.clear_data(treeview)
        treeview["column"] = list(data.columns)
        treeview["show"] = "headings"
        for column in treeview["columns"]:
            treeview.heading(column, text=column)  # let the column heading = column name

        df_rows = data.to_numpy().tolist()  # turns the dataframe into a list of lists
        for row in df_rows:
            treeview.insert("", "end", values=row)  # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
        return None

    def clear_data(self, treeview):
        treeview.delete(*treeview.get_children())
        return None

    def random_forest_regression(self, event):
        checked1 = self.checklist1.getCheckedItems()
        checked2 = self.checklist2.getCheckedItems()
        checked = checked1 + checked2
        quantitative = []
        qualitative = []
        for choice in checked:
            if ":" in choice:
                qualitative.append(choice)
            else:
                quantitative.append(choice)

        data = self.df
        for choice in qualitative:
            category = choice.split(":")[0]
            answer = choice.split(":")[1][1:]
            if category == "children":
                boolean_index = data[category] == int(answer)
            else:
                boolean_index = data[category] == answer
            data = data[boolean_index]

        train, test = train_test_split(data, test_size=0.2, random_state=83)
        X_train = train.loc[:, quantitative]
        y_train = train["charges"]
        X_test = test.loc[:, quantitative]
        y_test = test["charges"]

        for i in range(len(checked)):
            if ":" in checked[i]:
                checked[i] = checked[i].split(":")[0]
        checked.append("charges")
        model = RandomForestRegressor(n_estimators = 200, n_jobs = -1)
        try:
            model.fit(X_train, y_train)
        except:
            self.error_label['text'] = "An error has occurred. You most likely did not select age or bmi."
        y_pred_train = model.predict(X_train)
        y_pred_test = model.predict(X_test)
        training_error = root_mean_squared_error(y_train, y_pred_train)
        test_error = root_mean_squared_error(y_test, y_pred_test)
        test = test.rename({'charges': 'real charges'}, axis=1)
        test['predicted charges'] = pd.Series(self.find_predicted(model, X_test), index=test.index)
        self.load_data(self.output_treeview, test.sort_values(by=['age', 'sex', 'bmi'], ascending=True),
                       [x for x in self.df.columns if x not in checked])
        self.error_label['text'] = "The training error is " + str(training_error) + " and the test error is " + str(test_error)

    def find_predicted(self, model, x_test):
        result = []
        for i in range(len(x_test)):
            result.append(model.predict(x_test)[i])
        return result


def root_mean_squared_error(actual, predicted):
    return np.mean((actual - predicted) ** 2) ** 0.5

def helvetica(x, bold=False):
    return tkFont.Font(family='Helvetica', size=x, weight=(lambda bold: tkFont.BOLD if bold else tkFont.NORMAL)(bold))
