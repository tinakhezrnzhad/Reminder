import flet as ft

from main import reminding
from flet_ui import initialize_ui

db=reminding()

def main(page:ft.Page):
    my_ui = initialize_ui(page) # تابع رو صدا می‌زنیم و آبجکت UI رو می‌گیریم
    reminders = db.get_all_reminders() #اینجا میگیم یادیاوری را فراخوانی کن
    my_ui.show_reminders(reminders)  
    # اینجا می گیم که چیز هایی که در flet_ui.pyپیدا کردی را نمایش بده یا اجرا کن 


    def handle_add_click(e):
        comment, date, time= my_ui.get_inputs()
        
        if not comment or not date or not time:
            my_ui.set_message("لطفاً همه فیلدها رو پر کن!",ft.Colors.RED)
        else:
            try:
                db.add(comment, date, time , 0)
                # چون به طور پیش فرش یاداوری وضعیتش صفر یا اضافه نشده است 
                my_ui.set_message("یادآوری با موفقیت ذخیره شد ",ft.Colors.GREEN)
                my_ui.clear_inputs() # پاک کردن فیلدها
            except Exception as err:
                my_ui.set_message(f"خطایی رخ داد {err}",ft.Colors.RED)
        reminders = db.get_all_reminders()
        my_ui.refresh_reminders(reminders)
        page.update() # آپدیت صفحه

    my_ui.set_add_button_handler(handle_add_click)
    # یعنی وقتی دکمه ی اضافه کردن کلیک شد تابع داخل پرانتز را اجرا کن
    # که یعنی برو و اطلاعات را داخل دیتا بیس ذخیره کن 

    page.update() # آپدیت نهایی صفحه
    
    
    def handle_delete(id):
        db.delete(id)

        reminders = db.get_all_reminders()

        my_ui.refresh_reminders(reminders)

        page.update()
     
    my_ui.set_delete_handler(handle_delete)  
    
    page.update() 
    
    def handle_edit(id):
        reminder = db.search(id)
        my_ui.show_edit_dialog(reminder[0])
        # یعنی اولین چیزی که با این ایدی پیدا کردی را داخل فیلد ها نمایش بده 
    my_ui.set_edit_handler(handle_edit)
    
    def handle_save_edit(id, comment, date, time, dialog):
        reminder = db.search(id)

        if reminder:
            is_done = reminder[0][4]
            # یعنی وضعیت یاداوری را تغییر نده و همان را قرار بده 
            db.update(id, comment, date, time, is_done)
            dialog.open = False  # برای بستن پنجره ی دایالوگ
        reminders = db.get_all_reminders()
        my_ui.refresh_reminders(reminders)
    
        page.update()
    
    my_ui.set_save_edit_handler(handle_save_edit)
    
    page.update()
    
    def handle_search_click(e):
        my_ui.show_search_dialog()

    my_ui.set_search_button_handler(handle_search_click)
    
    def handle_search(reminder_id, dialog ,result_view):
        reminder = db.search(reminder_id)
        my_ui.show_search_result(
        reminder,
        result_view
        )
    my_ui.set_search_handler(handle_search)
    
if __name__ == "__main__":
    ft.run(main)
    
    
    # مراحل بعدی :
    # 1: باید اگر حذف را زدیم از جدول هم حذف بشه 
    # 2: باید اپدیت و جستجو هم کامل کنم 
    
    # و ساختن یک رابط کاربری برای صفحه ی ساین این سایت فروشگاه
    
    
    # مشکل جدید چرا در رابط کاربری اپدیت صورت نمی گیرد ؟؟؟؟؟؟؟؟؟؟