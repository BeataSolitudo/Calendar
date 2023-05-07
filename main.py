import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry


def on_date_select():
    date = cal.selection_get()
    message_window = tk.Toplevel(root)
    message_window.title('Important message')
    message_label = ttk.Label(message_window, text='Did you make today something important to you?')
    message_label.pack(padx=20, pady=20)
    yes_button = ttk.Button(message_window, text='Yes', command=lambda: on_yes_click(date, message_window))
    yes_button.pack(side=tk.LEFT, padx=20, pady=20)
    no_button = ttk.Button(message_window, text='No', command=message_window.destroy)
    no_button.pack(side=tk.RIGHT, padx=20, pady=20)


def on_yes_click(date, message_window):
    cal.tag_config('selected_date', background='green')
    cal.calevent_create(date, 'Selected', 'selected_date')
    message_window.destroy()


root = tk.Tk()
root.geometry('600x400')

cal = Calendar(root, selectmode='day', date_pattern='yyyy-mm-dd')
cal.pack(fill=tk.BOTH, expand=True)
cal.bind('<<CalendarSelected>>', lambda event: on_date_select())

root.mainloop()