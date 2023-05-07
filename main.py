import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry


def set_date_color(date, color):
    cal.tag_config(color, background=color)
    cal.calevent_create(date, 'Selected', 'selected_date', tag=color)


def on_date_select():
    date = cal.selection_get()
    message_window = tk.Toplevel(root)
    message_window.title('Important message')

    def on_yes_click():
        set_date_color(date, 'green')
        message_window.destroy()

    def on_no_click():
        set_date_color(date, 'red')
        message_window.destroy()

    message_label = ttk.Label(message_window, text='Did you make today something important to you?')
    message_label.pack(padx=20, pady=20)
    yes_button = ttk.Button(message_window, text='Yes', command=on_yes_click)
    yes_button.pack(side=tk.LEFT, padx=20, pady=20)
    no_button = ttk.Button(message_window, text='No', command=on_no_click)
    no_button.pack(side=tk.RIGHT, padx=20, pady=20)


root = tk.Tk()
root.geometry('600x400')

cal = Calendar(root, selectmode='day', date_pattern='yyyy-mm-dd')
cal.pack(fill=tk.BOTH, expand=True)
cal.bind('<<CalendarSelected>>', lambda event: on_date_select())

root.mainloop()