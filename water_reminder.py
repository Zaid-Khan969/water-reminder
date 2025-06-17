import time
from plyer import notification
import platform

# Function to send a desktop notification
def send_notification():
    notification.notify(
        title="Drink Water Reminder",
        message="It's time to drink water! Stay hydrated for better health.",
        timeout=10  # Notification stays for 10 seconds
    )

# Function to beep (Windows only)
def beep():
    if platform.system() == 'Windows':
        import winsound
        winsound.Beep(1000, 1000)  # Frequency 1000 Hz, Duration 1000 ms
    else:
        print('\a')  # ASCII Bell character (Unix-based systems)

# Main reminder function
def reminder():
    while True:
        send_notification()  # Send a desktop notification
        beep()  # Optional: make a beep sound
        time.sleep(60* 60)  # Wait for 1 hour (3600 seconds)

# Start the reminder function
if __name__ == '__main__':
   reminder()
