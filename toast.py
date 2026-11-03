
from win10toast import ToastNotifier

toast = ToastNotifier()

toast.show_toast(
    "You have a new notification!",
    "Hello ReDi class!!",
    duration = 20,
    threaded = True,
)