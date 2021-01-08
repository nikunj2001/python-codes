import time
import pandas
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
        title="please look 20 feet away for 20 seconds",
        message=("The rule says that for every 20 minutes spent looking at ascreen  a person should look at something 20 feet away for 20 seconds. Following the rule is a great way to remember to take frequent breaks."),
        app_icon=(r"C:\Users\vnind\OneDrive\Desktop\python\icon.ico"),
        timeout=2
        )
        time.sleep(60*60)