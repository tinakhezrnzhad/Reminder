import os
# برای پیدا کردن مسیر

APP_DATA_PATH = os.getenv("FLET_APP_STORAGE_DATA")
# ببین ایا مسیر مخصوص ذخیره ی اطلاعات را داریم یا خیر 

if APP_DATA_PATH is None:
    APP_DATA_PATH = os.path.join(
        os.path.expanduser("~"),
        # این کد پوشه ی home کاربر فعلی را پیدا میکند
        "ReminderApp"
        # بعد با این اسم ترکیب می کنیم
    )

os.makedirs(APP_DATA_PATH, exist_ok=True)
# اگر قابل بالا وجود نداشت بسازش اگر هم وجود داشت خطا نده

DB_PATH = os.path.join(APP_DATA_PATH, "myReminder.db")

# print("مسیر دیتابیس:", DB_PATH)

# pyinstaller --clean --onefile --name Reminder --collect-data flet midator.py
# این دستور را زدیم تا قسمت رابط کاربری بسته بندی شود ویک فایلexe ساخته شود