from windows_toasts import InteractableWindowsToaster, Toast, ToastButton, ToastActivatedEventArgs, ToastDisplayImage

def activated_callback(activatedEventArgs: ToastActivatedEventArgs):
    print(activatedEventArgs.arguments) # response=decent/response=bad


toaster = InteractableWindowsToaster('Marugoto A2-1')

newToast = Toast()

newToast.text_fields = ["It's time to review your lesson! :)"]

newToast.AddAction(ToastButton('Alright', 'response=execute'))
newToast.AddAction(ToastButton('Remind me later', 'response=setlater'))
newToast.AddImage(ToastDisplayImage.fromPath("data/local/images/logo.ico"))

toaster.show_toast(newToast)

newToast.on_activated = activated_callback

'''
    I have noticed that, to fulfill the SRS method... You probably need to remind the users to study

'''