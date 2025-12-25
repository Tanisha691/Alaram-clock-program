from tkinter import *
import datetime
import time
import threading
import winsound

def alarm_thread():
    while True:
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        if current_time == set_alarm_time:
            print("Alarm Ringing...")
            for i in range(5):  
                winsound.Beep(1000, 1000)   # (frequency, duration)
            break
        time.sleep(1)

def start_alarm():
    t = threading.Thread(target=alarm_thread)
    t.start()

root = Tk()
root.title("Alarm Clock")
root.geometry("350x200")
root.config(bg="lightblue")

Label(root, text="Set Alarm Time", font=("Helvetica", 18), bg="lightblue").pack(pady=10)

frame = Frame(root)
frame.pack()

hour = StringVar()
minute = StringVar()
second = StringVar()

Entry(frame, textvariable=hour, width=4, font=("Arial", 18)).grid(row=0, column=0)
Entry(frame, textvariable=minute, width=4, font=("Arial", 18)).grid(row=0, column=1)
Entry(frame, textvariable=second, width=4, font=("Arial", 18)).grid(row=0, column=2)

Button(root, text="Set Alarm", command=start_alarm, font=("Arial", 16), bg="green", fg="white").pack(pady=20)

root.mainloop()


