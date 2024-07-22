from tkinter import *
from datetime import datetime 
import time

def count_down(t):
    while t > 0: 
        min, secs = divmod(t, 60)
        hours, min = divmod(min, 60)
        time_format = '{:02d}:{:02d}:{:02d}'.format(hours, min, secs)
        lbl_time.config(text=time_format)
        root.update()
        time.sleep(1)
        t -= 1
    lbl_time.config(text="Time-Up")

def start_countdown():
    try:
        t = int(Entry_Hour.get())*3600 + int(Entry_Min.get())*60 + int(Entry_Sec.get())
        count_down(t)
    except ValueError:
        print("Enter right value")

root = Tk()
root.title("Count Down Timer")
root.geometry("500x500")

lbl1 = Label(root, text="Hours")
lbl2 = Label(root, text="Minutes")
lbl3 = Label(root, text="Second")
Entry_Hour = Entry(root)
Entry_Min = Entry(root)
Entry_Sec = Entry(root)

Entry_Hour.grid(row=0, column=1)
Entry_Min.grid(row=1, column=1)
Entry_Sec.grid(row=2, column=1)

lbl1.grid(row=0, column=0)  
lbl2.grid(row=1, column=0)
lbl3.grid(row=2, column=0)

button = Button(root, text="Set countdown", command=start_countdown)
button.grid(row=4, column=1)

lbl_time = Label(root, text="", font=('Helvetica', 24))
lbl_time.grid(row=5, column=1)

root.mainloop()