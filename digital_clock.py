# Importing dependencies
from tkinter import *
import time

# Functionality
def times():
    current_time = time.strftime("%r")
    clock.config(text = current_time)
    clock.after(1000, times)

# Gui Calculator
digClock = Tk()
digClock.title("Digital Clock")
digClock.geometry("500x250")
digClock.resizable(0, 0)

# Label
digi = Label(digClock, text="Digital Clock", font=("times", 24, "bold"))
digi.grid(row=0, column=2)

# Actual Clock
clock= Label(digClock, font=("times", 50, "bold"), bg="white")
clock.grid(row=2, column= 2, pady=25, padx=80)
times()

# Notation
nota = Label(digClock, text="Hours    Minutes    Seconds ", font=("times", 15, "bold"))
nota.grid(row=3, column=2)


# For continuos looping
digClock.mainloop()