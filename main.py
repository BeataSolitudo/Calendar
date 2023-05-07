import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry


def set_date_color(date, color):
    try:
        tags = cal.tag_has('selected_date')
        for tag in tags:
            cal.tag_remove(tag, '1.0', 'end')
    except:
        pass
    cal.calevent_create(date, 'Selected', 'selected_date', background=color)


def show_message(date):
    message_window = tk.Toplevel(root)
    message_window.title('Message')
    message_window.geometry('300x150')

    message = tk.Label(
        message_window,
        text="Did you make today something important to you?"
    )
    message.pack(pady=10)

    yes_button = ttk.Button(
        message_window,
        text='Yes',
        command=lambda: set_date_color(date, 'green')
    )
    yes_button.pack(pady=10)

    no_button = ttk.Button(
        message_window,
        text='No',
        command=lambda: set_date_color(date, 'red')
    )
    no_button.pack(pady=10)


def on_date_click(date):
    show_message(date.strftime('%m/%d/%Y'))


root = tk.Tk()
root.title('Calendar')

cal = Calendar(
    root,
    font=('Arial', 14),
    selectmode='day',
    cursor="hand1",
    year=2023,
    month=5,
    day=1,
)
cal.pack(fill='both', expand=True)

cal.bind('<<CalendarSelected>>', lambda e: on_date_click(cal.selection_get()))

root.mainloop()
