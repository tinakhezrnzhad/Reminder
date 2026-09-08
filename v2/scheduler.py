# این فایل وظیفه اش اینه که به reminder  بگه برو هر چند ثانیه یک بار یاداوری ها را بررسی کن 
import time  # ماژول استاندارد پایتون
# ما به ابزار sleep ان یعنی صبر کردن نیاز داریم مثلا 
# sleep(10) یعنی صبر کردن برای 10 ثانیه

from reminder import CheckTime

# کلاس چک تایم را از فایل ریمایندر می اوریم

def start_scheduler():
# یک تابع برای شروع زمانبندی
    # print("🔥 1 - Scheduler function started")

    try:
        # print("🔥 2 - Creating CheckTime")
        
        checker = CheckTime()
        
        # print("🔥 3 - CheckTime created")
        # یک نمونه از کلاس چکتایم میسازیم تا خارج از کلاس اجرا بشه 
        
        # این خط میگه تا وقتی برنامه درحال اجرلست این کار را دائم تکرار کن/   
        while True:
            # print("🔥 4 - Checking reminders")
    
            checker.check_reminders()
            
            # print("🔥 5 - Check finished")
            
            time.sleep(10)
            # اینجا یعنی هر 10 ثانیه یکبار برو این تابع یا بررسی کردن دیتابیس که ایا یاداوری وجود دارد را چک کن 

    except KeyboardInterrupt:
        print("Scheduler stopped.")

    finally:
        checker.close()


if __name__ == "__main__":
    start_scheduler()
    # این برای اینه اگر از یک فایل دیگر خواستیم این تابع اجرا بشه 