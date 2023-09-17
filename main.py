import time
import winsound

class Alarm:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        self.enabled = True

    def check(self):
        current_time = time.localtime()
        return self.enabled and current_time.tm_hour == self.hours and current_time.tm_min == self.minutes

def set_alarm():
    alarms = []
    
    while True:
        print("\nAlarm Clock Menu:")
        print("1. Set an alarm")
        print("2. List all alarms")
        print("3. Snooze an alarm")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            hours = int(input("Enter the hour (0-23): "))
            minutes = int(input("Enter the minute (0-59): "))
            
            alarm = Alarm(hours, minutes)
            alarms.append(alarm)
            
            print(f"Alarm set for {hours:02d}:{minutes:02d}")
        
        elif choice == "2":
            current_time = time.localtime()
            print("\nCurrent Time:", time.strftime("%H:%M:%S", current_time))
            
            for i, alarm in enumerate(alarms):
                alarm_time = f"{alarm.hours:02d}:{alarm.minutes:02d}"
                status = "Enabled" if alarm.check() else "Disabled"
                print(f"{i + 1}. Alarm at {alarm_time} - {status}")
        
        elif choice == "3":
            if not alarms:
                print("No alarms set.")
            else:
                print("\nSelect an alarm to snooze:")
                for i, alarm in enumerate(alarms):
                    alarm_time = f"{alarm.hours:02d}:{alarm.minutes:02d}"
                    print(f"{i + 1}. Alarm at {alarm_time}")
                
                try:
                    alarm_index = int(input("Enter the number of the alarm to snooze: ")) - 1
                    if 0 <= alarm_index < len(alarms):
                        snooze_duration = int(input("Enter snooze duration in minutes: "))
                        alarms[alarm_index].enabled = False
                        snooze_time = time.time() + snooze_duration * 60
                        print(f"Alarm snoozed for {snooze_duration} minutes.")
                        
                        while time.time() < snooze_time:
                            time.sleep(1)
                        alarms[alarm_index].enabled = True
                    else:
                        print("Invalid alarm number. Please enter a valid number.")
                except ValueError:
                    print("Invalid input. Please enter valid values.")
        
        elif choice == "4":
            print("Exiting Alarm Clock.")
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")

    while True:
        for alarm in alarms:
            if alarm.check():
                print(f"\nTime to wake up at {alarm.hours:02d}:{alarm.minutes:02d}!")
                winsound.Beep(1000, 1000)  # Play a sound (adjust as needed)
                alarm.enabled = False
        time.sleep(60)  # Check alarms every minute

if __name__ == "__main__":
    set_alarm()
