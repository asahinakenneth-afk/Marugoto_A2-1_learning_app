import json
from datetime import datetime
from windows_toasts import (
    InteractableWindowsToaster, 
    Toast, 
    ToastImage,
    ToastImagePosition,
    ToastButton, 
    ToastActivatedEventArgs, 
    ToastDisplayImage)

'''
    I have noticed that, to fulfill the SRS method... You probably need to remind the users to study
    so this is what its for! Its even translatable too!
    You need to settle this at Windows Scheduler to run, though...
    you can check on this if you're unsure, but I swear I'm not inserting malicious code ;)
'''

def notification(notification_text):
    toaster = InteractableWindowsToaster('Marugoto A2-1', "1")

    notifier = Toast()

    notifier.text_fields = [notification_text]

    # notifier.AddImage(ToastImage("data/local/images/logo.ico"))

    notifier.AddAction(ToastButton('Alright', 'response=execute'))
    notifier.AddAction(ToastButton('Remind me later', 'response=setlater'))
    # notifier.AddImage(ToastDisplayImage.fromPath("data/local/images/notification.png"))

    toaster.show_toast(notifier)

def check():
    now = datetime.now()

    with open("data/local/config.json", 'r', encoding='utf-8') as archivo:
        config = json.load(archivo)
        language = config.get("language", "en")
        due_date = config.get("due_date", None) ## FORMAT YYYY-MM-DD
        due_time = config.get("due_time", None) ## FORMAT HH:MM

    due_datetime = datetime.strptime(f"{due_date} {due_time}", "%Y-%m-%d %H:%M")

    if now >= due_datetime:
        with open(f"data/local/languages/{language}.json", 'r', encoding='utf-8') as archivo:
            language = json.load(archivo)
            notification_text = language["text"]["notification"]
            title_text = language["text"]["title"]

            print("showing notification...")
            notification(notification_text)
    else:
        print("No notification needed at this time.")

print("SRS Notification background starting...")
check()  # Check immediately when the script starts :3