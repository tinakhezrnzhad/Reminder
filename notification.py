from winotify import Notification

def notify(title, message):
    toast = Notification(
        app_id="Reminder",
        title=title,
        msg=message
    )

    toast.show()
   
