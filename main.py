import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

def set_date_color(date, color):
    # Remove previous tags from the date
    tags = cal.tag_has('selected_date')
    for tag in tags:
        cal.tag_remove(tag, '1.0', 'end')

    # Add the new tag with the specified color to the date
    tag = f'selected_date_{color}'
    cal.calevent_create(date, 'Selected', 'selected_date', tag=tag)

def on_date_select(date):
    message_window = tk.Toplevel(root)
    message_window.geometry('300x150')
    message_window.title('Important message')

    message_label = tk.Label(message_window, text='Did you make today something important to you?')
    message_label.pack(pady=10)

    yes_button = ttk.Button(message_window, text='Yes', command=lambda: set_date_color(date, 'green'))
    yes_button.pack(pady=10)

    no_button = ttk.Button(message_window, text='No', command=lambda: set_date_color(date, 'red'))
    no_button.pack(pady=10)

root = tk.Tk()
root.geometry('800x600')
root.title('Calendar')

style = ttk.Style(root)
style.theme_use('default')

cal = Calendar(root, selectmode='day', year=2023, month=5, day=7)
cal.pack(pady=20)

cal.bind('<<CalendarSelected>>', lambda event: on_date_select(cal.selection_get()))

root.mainloop()