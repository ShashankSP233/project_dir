import time

def set_reminder(reminder_time, message):
    current_time = time.time()
    time_difference = reminder_time - current_time

    if time_difference > 0:
        print(f"Reminder set! I'll remind you in {time_difference:.1f} seconds.")
        time.sleep(time_difference)
        print(f"Reminder: {message}")
    else:
        print("Invalid time. The reminder time should be in the future.")

try:
    reminder_time = float(input("Enter the time in seconds for the reminder: "))
    reminder_message = input("Enter the reminder message: ")

    set_reminder(time.time() + reminder_time, reminder_message)
except ValueError:
    print("Invalid input. Please enter a valid time in seconds.")
