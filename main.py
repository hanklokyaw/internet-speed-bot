from internet_speed_test import InternetSpeedBot
import datetime

PROMISED_DOWN_SPEED = 100.0
PROMISED_UP_SPEED = 10.0

app = InternetSpeedBot()
try:

    app.get_internet_speed()

    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    up_down_speed = f"Download: {app.down_speed} / Upload: {app.up_speed}"
    to_log = f"{time_now} - {up_down_speed}"

    if app.down_speed < PROMISED_DOWN_SPEED or app.up_speed < PROMISED_UP_SPEED:
        print(f"Low speed alerts! {to_log}")
        app.keep_log(to_log)
        app.driver.quit()
except:
    app.driver.quit()
    print("Oops! something went wrong. Check your code again.")
else:
    print("Speed test finished!")