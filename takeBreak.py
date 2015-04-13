import pynotify
from time import sleep

def sendmessage(title, message):
    pynotify.init("Break")
    notice = pynotify.Notification(title, message)
    notice.show()
    return

while True:
    news="Just 10 Seconds"
    sendmessage("Take A Break ", news)
    sleep(900)
