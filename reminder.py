import sqlite3
from datetime import datetime
import tkinter as tk
from notification import notify

class checkTime:
    def __init__(self):
        
    # اتصال به دیتابیس
        self.connection = sqlite3.connect("myReminder.db")

        # ساخت Cursor
        self.cursor =self.connection.cursor()
    def check_reminders(self):
        
        self.cursor.execute("SELECT * FROM remind WHERE is_done=0")
        reminders = self.cursor.fetchall()
        now = datetime.now()

        for reminder in reminders:
            date_next = reminder[2]
            time_next = reminder[3]
            reminde_text=reminder[4]
            reminder_id=reminder[0]
            
            date_time_text = date_next + " " + time_next
            # print("ذخیره شده تو دیتابیس:", date_time_text) 

            try:
                reminder_datetime = datetime.strptime(date_time_text, "%m/%d/%y %H:%M")
            except ValueError as e:
                print("فرمت تاریخ اشتباهه:", e)
                continue

            if now >= reminder_datetime:
                self.labelRemind.configure(text="Reminder is ready!")
                self.labelComment.configure(text=f"comment: {reminde_text}")
                notify("یادآوری جدید!", reminde_text)
                # self.cursor.execute("DELETE FROM remind WHERE id=?" , (reminder[0],))
                # self.connection.commit()
                self.cursor.execute("UPDATE remind SET is_done = 1 WHERE id=?", (reminder_id,))
                self.connection.commit()

        self.win.after(5000, self.check_reminders)


    def tkinter(self):
        self.win=tk.Tk()
        self.win.title("Reminder")
        self.win.geometry("200x200")
        
        self.labelRemind=tk.Label(self.win , text="در حال بارگذاری یادآوری")
        self.labelRemind.pack()
        
        self.labelComment=tk.Label(self.win , text="در حال بارگذاری یادآوری")
        self.labelComment.pack()
        
        self.check_reminders()
        
        self.win.mainloop()
            
Check_time = checkTime()
Check_time.tkinter()
# Check_time.check_reminders()
         


# import time