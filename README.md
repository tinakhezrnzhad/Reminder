
# Reminder

یک برنامه ساده برای مدیریت یادآوری‌ها در ویندوز.

با این برنامه می‌توانید یادآوری اضافه کنید، آن‌ها را ویرایش یا حذف کنید و بین یادآوری‌ها جستجو کنید. همچنین `ReminderWorker` در پس‌زمینه زمان یادآوری‌ها را بررسی می‌کند و در زمان مشخص، اعلان ویندوز را نمایش می‌دهد.

## با چه چیزهایی ساخته شده؟

این پروژه با استفاده از این ابزارها ساخته شده است:

* **Python** برای نوشتن برنامه
* **Flet** برای ساخت رابط کاربری
* **PyInstaller** برای تبدیل برنامه به فایل `.exe`
* **Windows Task Scheduler** برای اجرای خودکار Worker هنگام روشن شدن ویندوز
* **Windows Notifications** برای نمایش اعلان‌ها

## استفاده معمولی

برای استفاده معمولی فقط به دو فایل نیاز دارید:

```text
Reminder.exe
ReminderWorker.exe
```

بعد از قرار دادن فایل‌ها، باید `ReminderWorker.exe` را در **Windows Task Scheduler** تنظیم کنید تا هنگام روشن شدن ویندوز به صورت خودکار اجرا شود.

### تنظیم Task Scheduler

1. در ویندوز از طریق منوی Start، **Task Scheduler** را باز کنید.
2. از سمت راست روی **Create Task** کلیک کنید.

### General

در این قسمت:

* در قسمت **Name** یک نام برای Task انتخاب کنید، مثلاً:

```text
ReminderWorker
```

* در بخش **Security options** گزینه **Run whether user is logged on or not** را انتخاب کنید.
* گزینه **Run with highest privileges** معمولاً نیازی نیست و می‌توانید آن را فعال نکنید.

### Triggers

1. وارد تب **Triggers** شوید.
2. روی **New** کلیک کنید.
3. در قسمت **Begin the task** گزینه **At startup** را انتخاب کنید.
4. در صورت نیاز می‌توانید یک تأخیر کوتاه برای اجرای Worker قرار دهید، مثلاً **30 seconds**.
5. تنظیمات را تأیید کنید.

### Actions

1. وارد تب **Actions** شوید.
2. روی **New** کلیک کنید.
3. در قسمت **Action** گزینه **Start a program** را انتخاب کنید.
4. در قسمت **Program/script** مسیر کامل `ReminderWorker.exe` را وارد کنید.

مثلاً:

```text
D:\practice2\Reminder\dist\ReminderWorker.exe
```

5. در قسمت **Add arguments** چیزی وارد نکنید.
6. در قسمت **Start in** مسیر پوشه‌ای که `ReminderWorker.exe` داخل آن قرار دارد را وارد کنید:

```text
D:\practice2\Reminder\dist
```

### Conditions

در تب **Conditions** بهتر است گزینه‌ای که باعث شود Task فقط در شرایط خاصی اجرا شود فعال نباشد.

به‌خصوص اگر گزینه‌ای مربوط به **Start the task only if the computer is on AC power** فعال است، آن را بررسی کنید تا Worker روی لپ‌تاپ فقط به خاطر استفاده از باتری اجرا نشود.

### Settings

در این قسمت:

* گزینه **Allow task to be run on demand** را فعال کنید.
* گزینه **Run task as soon as possible after a scheduled start is missed** را فعال کنید.
* در صورت متوقف شدن Worker، می‌توانید گزینه **Restart the task every** را فعال کرده و مثلاً روی **1 minute** قرار دهید.
* تعداد تلاش برای اجرای مجدد را مثلاً روی **3 times** قرار دهید.
* اگر گزینه **If the task is already running** وجود داشت، آن را روی **Do not start a new instance** قرار دهید.

در آخر روی **OK** بزنید و اگر ویندوز برای ذخیره Task رمز حساب کاربری را خواست، آن را وارد کنید.

حالا بعد از روشن شدن ویندوز، `ReminderWorker` به صورت خودکار اجرا می‌شود و در پس‌زمینه زمان یادآوری‌ها را بررسی می‌کند.

بعد از انجام این تنظیمات، می‌توانید `Reminder.exe` را باز کنید و یادآوری‌های خود را مدیریت کنید.

## استفاده برای توسعه

اگر می‌خواهید کد پروژه را ببینید یا آن را تغییر دهید، می‌توانید سورس پروژه را دریافت کنید.

برای اجرای پروژه به **Python 3.x** و کتابخانه‌های مورد نیاز نیاز دارید.

```bash
pip install -r requirements.txt
```

سپس می‌توانید فایل‌های Python پروژه را اجرا و تغییر دهید.

این پروژه بیشتر برای یادگیری و ساخت یک برنامه کاربردی با Python ساخته شده است

اگر میخواهید بعدا ویرایشی در کد ها انجام دهید میتوانید در ترمینال مربوط به پروژه این کد ها را وارد نمایید 
برای رابط کاربری :
pyinstaller --clean --onefile --noconsole --name Reminder --collect-data flet midator.py
برای بک اند :
pyinstaller --clean --onefile --noconsole --name ReminderWorker scheduler.py
