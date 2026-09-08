import sqlite3
from datetime import datetime
from notification import notify
import jdatetime
from storage import DB_PATH

class CheckTime:
    def __init__(self): 
        # اتصال به دیتابیس
        self.connection = sqlite3.connect(DB_PATH)

        # ساخت Cursor
        self.cursor =self.connection.cursor()
    
    def check_reminders(self):
        
        
        self.cursor.execute("SELECT * FROM remind WHERE is_done=0")
        reminders = self.cursor.fetchall()
        print(reminders)
        now = datetime.now()

        for reminder in reminders:
            date_next = reminder[2]
            time_next = reminder[3]
            reminde_text=reminder[1]
            reminder_id=reminder[0]
            
            date_time_text = date_next + " " + time_next
            # print("ذخیره شده تو دیتابیس:", date_time_text) 

            try:
                # این کد های پایین در واقع تاریخ را کاملا به میلادی تبدیل نمی کنند بلکه 
                # اگر کاربر تاریخ را به شمسی وارد کرد برنامه گیج نمی شه که ببینه اه این تاریخ کجائیه؟
                # بنابراین این کد ها زمان شمسی را به میلادی برای مقایسهبادتاریخ فعلی سیستم تغییر میدهند
                jalali_datetime = jdatetime.datetime.strptime(
                    date_time_text,
                    "%Y/%m/%d %H:%M"
                )
                reminder_datetime = jalali_datetime.togregorian()
            except ValueError as e:
                print("فرمت  تاریخ یا ساعت اشتباه است:", e)
                continue
            
            print("NOW:", now)
            print("REMINDER:", reminder_datetime)
            print("NOW TYPE:", type(now))
            print("REMINDER TYPE:", type(reminder_datetime))
            print("COMPARISON:", now >= reminder_datetime)

            if now >= reminder_datetime:
                # self.labelRemind.configure(text="Reminder is ready!")
                # self.labelComment.configure(text=f"comment: {reminde_text}")
                print("به شرط رسیدیم ")
                notify("یادآوری جدید!", reminde_text)
                print("اجرا شد اعلان ")
                # self.cursor.execute("DELETE FROM remind WHERE id=?" , (reminder[0],))
                # self.connection.commit()
                self.cursor.execute("UPDATE remind SET is_done = 1 WHERE id=?", (reminder_id,))
                self.connection.commit() 
                 
    def close(self):
        self.connection.close()
        # برای اینکه بعد از بررسی دیتابیس بسته بشه دیتابیس دیگر 
        
# Check_time = CheckTime()
# Check_time.check_reminders()
# دو خط بالا را حذف کردیم چون نمی خواهیم که تابع چک کردن دیتابیس هر وقت خواست بره دیتابیس را چک کند 
# بلکه می خواهیم تابع زمانبتدی این کار را کنترل کند 
