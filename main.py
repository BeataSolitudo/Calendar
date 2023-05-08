import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import csv
import datetime


def on_date_select():
    date = cal.selection_get()
    message_window = tk.Toplevel(root)
    message_window.title('Important message')
    message_label = ttk.Label(message_window, text='Did you make today something important to you?')
    message_label.pack(padx=20, pady=20)
    yes_button = ttk.Button(message_window, text='Yes', command=lambda: on_yes_click(date, message_window))
    yes_button.pack(side=tk.LEFT, padx=20, pady=20)
    no_button = ttk.Button(message_window, text='No', command=lambda: on_no_click(date, message_window))
    no_button.pack(side=tk.RIGHT, padx=20, pady=20)


def on_yes_click(date, message_window):
    cal.calevent_create(date, 'Selected', 'selected_date_green')
    message_window.destroy()
    with open("Calendar.csv", "a", newline="") as csvwrite:
        writer = csv.writer(csvwrite)
        writer.writerow([date, "1"])


def on_no_click(date, message_window):
    cal.calevent_create(date, 'Selected', 'selected_date_red')
    message_window.destroy()
    with open("Calendar.csv", "a", newline="") as csvwrite:
        writer = csv.writer(csvwrite)
        writer.writerow([date, "0"])


root = tk.Tk()
root.geometry('600x400')

cal = Calendar(root, selectmode='day', date_pattern='yyyy-mm-dd')
cal.pack(fill=tk.BOTH, expand=True)
cal.tag_config('selected_date_green', background='green')
cal.tag_config('selected_date_red', background='red')
cal.bind('<<CalendarSelected>>', lambda event: on_date_select())

with open("Calendar.csv", "r", newline="") as csvread:
    reader = csv.reader(csvread)
    for row in reader:
        date1 = datetime.datetime.strptime(row[0], '%Y-%m-%d')
        if row[1] == "1":
            cal.calevent_create(date1, 'Selected', 'selected_date_green')
        else:
            cal.calevent_create(date1, 'Selected', 'selected_date_red')
root.mainloop()
