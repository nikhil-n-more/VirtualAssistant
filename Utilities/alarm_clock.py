import datetime
import time
import winsound

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake up!")
            # Play sound
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break
        time.sleep(1)

# Set multiple alarms
alarms = ["08:00:00", "12:30:00", "18:45:00"]
alarms.sort()  # Sort the alarms array

for alarm in alarms:
    set_alarm(alarm)