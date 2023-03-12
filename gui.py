# It creates a GUI for taking input from user or it can be automated.
# After collecting the input, it sends the data to the saved joblib model.
# The model analyses whether trnsaction is fraudulent or genuine using ML algorithms and returns the result.
from tkinter import *
import joblib
import pandas as pd

window = Tk()
window.title("Credit Card Fraud Detection")
canvas = Canvas(height=400, width=300, bg="grey")
canvas.pack()


def predict():
    e = entry.get()
    e2 = entry2.get()
    e3 = entry3.get()
    e4 = entry4.get()
    e5 = entry5.get()
    e6 = entry6.get()
    e7 = entry7.get()
    e8 = entry8.get()
    new_data = pd.DataFrame({
        'Time': e3,
        'V1': e4,
        'V2': e5,
        'V14': e6,
        'V28': e7,
        'Amount': e8, }, index=[0])
    print(new_data)


Label(text="Enter the following data :").place(x=70, y=12)
entry = Entry(font=("Arial", 12, "bold"), width=15, borderwidth=3, )
entry.place(x=110, y=40)
Label(text="Name:").place(x=20, y=45)
entry2 = Entry(font=("Arial", 12, "bold"), width=15, borderwidth=3)
entry2.place(x=110, y=75)
Label(text="Credit-Card No:").place(x=20, y=80)
entry3 = Entry(font=("Arial", 12, "bold"), width=15, borderwidth=3)
entry3.place(x=110, y=110)
Label(text="Time:").place(x=20, y=115)
entry4 = Entry(font=("Arial", 12, "bold"), width=15, borderwidth=3)
entry4.place(x=110, y=145)
Label(text="V1:").place(x=20, y=150)
entry5 = Entry(font=("Arial", 12, "bold"), width=15, borderwidth=3)
entry5.place(x=110, y=180)
Label(text="V2:").place(x=20, y=185)
entry6 = Entry(font=("Arial", 12, "bold"), width=15, borderwidth=3)
entry6.place(x=110, y=215)
Label(text="V14:").place(x=20, y=220)
entry7 = Entry(font=("Arial", 12, "bold"), width=13, borderwidth=3)
entry7.place(x=130, y=250)
Label(text="V28:").place(x=20, y=255)
entry8 = Entry(font=("Arial", 12, "bold"), width=13, borderwidth=3)
entry8.place(x=130, y=285)
Label(text="Amount:").place(x=20, y=290)
Predict_button = Button(text=" Predict ", highlightthickness=0, bd=5, height=1, width=7, font="bold", command=predict)
Predict_button.place(x=110, y=330)
window.mainloop()
