from datetime import datetime

import tkinter as tk

window = tk.Tk()
days_calculated = tk.StringVar()
days_calculated.set("")

first_date_label = tk.Label(text="Input first date:")
first_date_label.pack()

first_date = tk.Entry(fg="black", bg="white", width=50)
first_date.pack()

second_date_label = tk.Label(text="Input second date:")
second_date_label.pack()



second_date = tk.Entry(fg="black", bg="white", width=50)
second_date.pack()

def on_submit():
    first_date_value = first_date.get()
    second_date_value = second_date.get()
    d1 = datetime.strptime(first_date_value, "%d/%m/%Y")
    d2 = datetime.strptime(second_date_value, "%d/%m/%Y")
    delta = d2 - d1
    days_calculated.set(delta)


button = tk.Button(
    text="Submit",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=on_submit
)

button.pack()

result_label = tk.Label(textvariable=days_calculated)
result_label.pack()

window.mainloop()

#wib



