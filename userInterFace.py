import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from tkcalendar import DateEntry
from main import reminding
database = reminding()
import main

class ui:
    def __init__(self):
        self.win=tk.Tk()
        self.win.title("Reminder")
        self.win.geometry("1000x1000")

        tk.Label(self.win , text="برنامه ی یادآوری ").grid(row=1, column=1)

        tk.Label(self.win , text="امروز چه تاریخی است ؟").grid(row=2, column=1)
        self.dateToday = DateEntry(self.win )
        self.dateToday.grid(row=2, column=0, padx=5, pady=5)

        tk.Label(self.win, text="چه تاریخی یادآوری کنم ؟").grid(row=3, column=1)
        self.dateNext = DateEntry(self.win)
        self.dateNext.grid(row=3, column=0, padx=5, pady=5)

        tk.Label(self.win , text="چه ساعتی یادآوری کنم ؟").grid(row=4, column=1)
        self.timeNext =tk.Entry(self.win)
        self.timeNext.grid(row=4, column=0, padx=5, pady=5)
    
        tk.Label(self.win , text="چه چیزی را یادآوری کنم ؟").grid(row=5, column=1)
        self.comment = tk.Text(self.win , width=60 , height=7)
        self.comment.grid(row=5, column=0, padx=5, pady=5)
        
        states= ["انجام شده" , "انجام نشده"]
        states_var = tk.StringVar(self.win) #?
        states_var.set(states)
        ttk.Label(self.win , text="یادآوری در چه وضعیتی است ؟").grid(row=6 , column=1)
        self.state_combobox = ttk.Combobox(self.win, textvariable=states_var, values=states, state="readonly")
        self.state_combobox.grid(row=6, column=0, padx=5, pady=5)

        # tk.Label(win , text="چه کار هایی بایدانجام بدم ؟").grid(row=7, column=1)

        # tk.Label(win , text="-2").grid(row=10, column=1)
        # list2 = tk.Text(win , width=60 , height=7)
        # list2.grid(row=11, column=1, padx=5, pady=5 )

        # tk.Label(win , text=": یادداشت های امروز").grid(row=12, column=1)

        # note = tk.Text(win , width=60 , height=12)
        # note.grid(row=13, column=1, padx=5, pady=5 )
        def add_reminder():
            dateToday = self.dateToday.get()
            dateNext = self.dateNext.get()
            timeNext = self.timeNext.get()
            comment = self.comment.get("1.0", "end-1c")
            # تبدیل متن به عدد برای دیتابیس
            status_text = self.state_combobox.get()
            is_done = 1 if status_text == "انجام شده" else 0
            # حالا is_done که عدد شده رو می‌فرستیم
            database.add(dateToday, dateNext, timeNext, comment, is_done)
            
        self.btnAdd = tk.Button(self.win , text="اضافه کردن" , command=add_reminder)
        self.btnAdd.grid(row=14 , column=0)

        self.btnDelete = tk.Button(self.win , text="حذف کردن" , command=lambda:main.show_delete(self.win))
        self.btnDelete.grid(row=14 , column=1)

        self.btnSearch = tk.Button(self.win , text="جستجو کردن" , command=lambda:main.show_Search(self.win))
        self.btnSearch.grid(row=14 , column=2)

        self.btnUpdate = tk.Button(self.win , text="به روز رسانی کردن" , command=lambda:main.show_update(self.win))
        self.btnUpdate.grid(row=14 , column=3)

        self.btnShow = tk.Button(self.win , text="نمایش دادن", command=lambda:database.show(self.win))
        self.btnShow.grid(row=14 , column=4)

        self.win.mainloop()
UIpatern=ui()
