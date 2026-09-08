# import tkinter as tk
# from tkinter import messagebox as msg
# from tkinter import ttk 
import sqlite3
# from tkcalendar import DateEntry
# from userInterFace import ui

# import jdatetime
# from datetime import datetime

# def get_shamsi_date(date):
#     jd=jdatetime.datetime.fromgregorian(datetime=date)
#     return jd.strftime("%Y/%m/%d")
 
class reminding:
    def __init__(self):
        self.connection = sqlite3.connect("myReminder.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS remind (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            comment TEXT,
            dateNext TEXT,
            timeNext TEXT,
            is_done INTEGER
        )
        """)
        self.connection.commit()
        
    def add(self ,comment, dateNext, timeNext, is_done):
        try:
            self.cursor.execute("""
            INSERT INTO remind(comment, dateNext, timeNext, is_done)
            VALUES (?, ?, ?, ?)
            """, (comment, dateNext, timeNext, is_done))
# برای متن یعنی برو از اول تا اخر اون متن را داخل دیتابیس ذخیره کن 
            self.connection.commit()

            print("یادآوری ها با موفقیت ثبت شدند")
        except Exception as e:
            print(e)
            # msg.showerror("error", "invalid input!")
    # def search_for_delete(self, id):
    #     self.cursor.execute("""
    #     SELECT * FROM remind WHERE id=?                   
    #     """, (id,))
    #     return self.cursor.fetchall()
        
    def delete(self, id):
        try:
            self.cursor.execute("""
            DELETE FROM remind WHERE id=?                    
            """ , (id,) )
            self.connection.commit()
            print("یادآوری هابا موفقیت حذف شدند")  
        except Exception as e:
            print(e)

            
    def search(self , id ):
        try:
            self.cursor.execute('SELECT * FROM remind WHERE id=?' , (id,))
            return self.cursor.fetchall()  
        except:
            print("نتونستین چیزی که براش میگشتی را پیدا کنیم")
            
            
    # def search_for_update(self , id):
    #     self.cursor.execute("""
    #     SELECT * FROM remind WHERE id=?                   
    #     """, (id,))
    #     return self.cursor.fetchall()
    
    def update(self, id, comment, dateNext, timeNext, is_done):
        try:
            self.cursor.execute("""
            UPDATE remind
            SET comment=?,
            dateNext=? ,
            timeNext=? ,
            is_done=? 
            WHERE id=?                   
                """ , (comment, dateNext, timeNext, is_done, id)) 
            self.connection.commit()

        except Exception as e:
            print(e)
            return False
        
    def get_all_reminders(self):
        self.cursor.execute("SELECT * FROM remind")
        return self.cursor.fetchall()
            
#     def show(self , parent):
#         # try:
#             dataWindow=tk.Toplevel(parent)
#             dataWindow.title('نمایش برنامه ')
#             # اماده کردن بستر خروجی برای مشاهده ی اطلاعات
#             table=ttk.Treeview(dataWindow,columns=("id", "dateToday", "dateNext", "timeNext", "comment" ,"is_done"), show="headings")
#             table.heading("id", text="آیدی")
#             table.heading("dateToday", text="اریخ الان ")
#             table.heading("dateNext", text="تاریخ یادآوری")
#             table.heading("timeNext", text="ساعت یاآوری")
#             table.heading("comment", text="یادداشت")
#             table.heading("is_done" , text="وضعیت یاداوری")
            
#             table.column("id", width=60)
#             table.column("dateToday", width=120)
#             table.column("dateNext", width=120)
#             table.column("timeNext", width=80)
#             table.column("comment", width=60)
#             table.column("is_done", width=60)
            
#             self.cursor.execute("SELECT * FROM remind")       
#             products = self.cursor.fetchall()
#             # به صورت تاپل انها را نمایش می دهد 
#             # تا بعدا بتواند انها را یکی کی از هم جدا و نمایش دهد 
#             for item in products:
#                 table.insert("", "end", values=(item[0], item[1], item[2], item[3], item[4] ,item[5]))

#             table.pack(padx=2, pady=10, fill=tk.BOTH, expand=True)
#         # except:
#         #     msg.showerror("error", "can not show u something!")
# def show_update(parent):
#     updatewin=tk.Toplevel(parent)
#     updatewin.title("به روز رسانی کردن ")
#     updatewin.geometry("300x300")
    
#     tk.Label( updatewin , text="آیدی مورد نظر را وارد کنید").grid(row=0, column=1)
#     idEntry= tk.Entry(updatewin)
#     idEntry.grid(row=0, column=0, padx=5, pady=5)
#     def do_update(parent):
#         id = idEntry.get()
#         result = remindingExample.search_for_update(id)
#         if len(result)!=0:
#             item=result[0]
#             updateWindow=tk.Toplevel(parent)
#             updateWindow.title('نتیجه ی جستجو برای آپدیت')
            
#             tk.Label(updateWindow, text="آیدی").grid(row=0, column=0)
#             idntry = tk.Entry(updateWindow)
#             idntry.grid(row=0, column=1)
#             # مقدار قبلی را نمایش می دهیم
#             idntry.insert(0, item[0])
            
#             tk.Label(updateWindow, text="تاریخ الان ").grid(row=1, column=0)
#             dayTodayEntry = tk.Entry(updateWindow)
#             dayTodayEntry.grid(row=1, column=1)
#             dayTodayEntry.insert(0, item[1])

#             tk.Label(updateWindow, text="تاریخ یادآوری ").grid(row=2, column=0)
#             dateNextEntry = tk.Entry(updateWindow)
#             dateNextEntry.grid(row=2, column=1)
#             dateNextEntry.insert(0, item[2])
            
#             tk.Label(updateWindow, text="ساعت یادآوری").grid(row=3, column=0)
#             timeNextEntry = tk.Entry(updateWindow)
#             timeNextEntry.grid(row=3, column=1)
#             timeNextEntry.insert(0, item[3])
            
#             tk.Label(updateWindow, text="یادداشت").grid(row=4, column=0)
#             commentEntry = tk.Entry(updateWindow)
#             commentEntry.grid(row=4, column=1)
#             commentEntry.insert(0, item[4])
            
#             tk.Label(updateWindow, text="وضعیت یادآوری").grid(row=5, column=0)
#             is_doneEntry = tk.Entry(updateWindow)
#             is_doneEntry.grid(row=5, column=1)
#             is_doneEntry.insert(0, item[4])
#             # این کد ها اطلاعاتی را نمایش می دهد که مال قبل است 
            
#             def save_changes():
#                 new_id = idntry.get()
#                 new_day = dayTodayEntry.get()
#                 new_date = dateNextEntry.get()
#                 new_list1 = timeNextEntry.get()
#                 new_list2 = commentEntry.get()
#                 new_list3 = is_doneEntry.get()
                
#                 remindingExample.update(
#                     new_id,
#                     new_day,
#                     new_date,
#                     new_list1,
#                     new_list2,
#                     new_list3
#                 )
#                 msg.showinfo("به روز رسانی انجام شد ", "با موفقیت تغییر کرد")
            
#             delete = tk.Button(updateWindow , text="به روز رسانی نهایی" , command=save_changes)
#             delete.grid(row=6 , column=1)
#     goUpdate = tk.Button(updatewin , text="رفتن بای دیدن اطلاعاتی که میخواهی آپدیت کنی " , command=lambda:do_update(parent))
#     goUpdate.grid(row=1 , column=1) 
    
            
# def show_delete(parent):
#     deletewind=tk.Toplevel(parent)
#     deletewind.title('حذف کردن ')
#     deletewind.geometry("300x300")

#     tk.Label( deletewind , text="آیدی مورد نظر را وارد کنید").grid(row=0, column=1)
#     idEntry= tk.Entry(deletewind)
#     idEntry.grid(row=0, column=0, padx=5, pady=5)
#     def do_delete(parent):
#         id = idEntry.get()
#         result = remindingExample.search_for_delete(id)
#         if len(result)!=0:
#             item=result[0]
#             deleteWindow=tk.Toplevel(parent)
#             deleteWindow.title('نتیجه ی جستجو برای حذف ')
            
#             tk.Label(deleteWindow, text="آیدی").grid(row=0, column=0)
#             idntry = tk.Entry(deleteWindow)
#             idntry.grid(row=0, column=1)
#             # مقدار قبلی را نمایش می دهیم
#             idntry.insert(0, item[0])
            
#             tk.Label(deleteWindow, text="تاریخ الان ").grid(row=1, column=0)
#             dayTodayEntry = DateEntry(deleteWindow)
#             dayTodayEntry.grid(row=1, column=1)
#             dayTodayEntry.insert(0, item[1])

#             tk.Label(deleteWindow, text="تاریخ یادآوری ").grid(row=2, column=0)
#             dateNextEntry = DateEntry(deleteWindow)
#             dateNextEntry.grid(row=2, column=1)
#             dateNextEntry.insert(0, item[2])
            
#             tk.Label(deleteWindow, text="ساعت یادآوری").grid(row=3, column=0)
#             timeNextEntry = tk.Entry(deleteWindow)
#             timeNextEntry.grid(row=3, column=1)
#             timeNextEntry.insert(0, item[3])
            
#             tk.Label(deleteWindow, text="یادداشت").grid(row=4, column=0)
#             commentEntry = tk.Entry(deleteWindow)
#             commentEntry.grid(row=4, column=1)
#             commentEntry.insert(0, item[4])
            
#             tk.Label(deleteWindow, text="وضعیت یادآوری").grid(row=5, column=0)
#             is_doneEntry = tk.Entry(deleteWindow)
#             is_doneEntry.grid(row=5, column=1)
#             is_doneEntry.insert(0, item[4])
            
#             delete = tk.Button(deleteWindow , text="حذف نهایی" , command=lambda:remindingExample.delete(id))
#             delete.grid(row=6 , column=1)
            
#         else:
#             msg.showinfo("error","ایدی مورد نظر پیدا نشد ") 
            
#     godelete = tk.Button(deletewind , text="رفتن بای دیدن اطلاعاتی که میخواهی حذف کنی " , command=lambda:do_delete(parent))
#     godelete.grid(row=1 , column=1)  

# def show_Search(parent):
#     wind2=tk.Toplevel(parent)
#     wind2.title('جستجو کردن ')
#     wind2.geometry("300x150")
    
#     tk.Label( wind2 , text="ایدی مورد نظر برای جستجو را وارد کنید").grid(row=0, column=0)
#     searchEntry= tk.Entry(wind2)
#     searchEntry.grid(row=0, column=1, padx=5, pady=5)
#     def do_search(parent):
#         id = searchEntry.get()
#         result = remindingExample.search(id)
#         if len(result)!=0:
#             dataWindow=tk.Toplevel(parent)
#             dataWindow.title('نتیجه ی جستجو ')
#             # اماده کردن بستر خروجی برای مشاهده ی اطلاعات
#             table=ttk.Treeview(dataWindow,columns=("id", "dateToday", "dateNext", "timeNext", "comment","is_done"), show="headings")
#             table.heading("id", text="آیدی")
#             table.heading("dateToday", text="اریخ الان ")
#             table.heading("dateNext", text="تاریخ یادآوری")
#             table.heading("timeNext", text="ساعت یاآوری")
#             table.heading("comment", text="یادداشت")
#             table.heading("is_done", text="یادداشت")
            
            
#             table.column("id", width=60)
#             table.column("dateToday", width=120)
#             table.column("dateNext", width=120)
#             table.column("timeNext", width=80)
#             table.column("comment", width=60)
#             table.column("is_done", width=60)
            
            
#             for item in result:
#                 table.insert("", "end", values=(item[0], item[1], item[2], item[3], item[4] ,item[5]))

#             table.grid(padx=2, pady=10)
#         else:
#             msg.showerror("Error", "Product not found")
#     btn = tk.Button(wind2 , text="show" , command=lambda:do_search(parent))
#     btn.grid(row=1, column=0)
remindingExample=reminding()  
# remindingExample.ui()       
        # مشکلات و تغییراتی که بعدا باید اعمال کنم :
        # 1- وقتی به روز رسانی می کنم در تکینتر تغییر می کند و لی در دیتابیس خیر 
        # 2- باید اندازه ی پنجره ها را استاندارد کنم 
        # 3- باید یک صفحه ی لاگ این اضافه کنم که هر کس دفترچهی خودش را داشته باشد 
        # که برای ان باید قسمت رابط کاربری را داخل یه کلاسیا تابع بزارم تابع بهتره 