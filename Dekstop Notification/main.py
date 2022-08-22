import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title = "ALERT!!!",
            message = "Take a break! Have a cup of coffee!",
            timeout = 4
        )
        time.sleep(20)