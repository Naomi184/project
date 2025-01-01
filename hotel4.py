from tkinter import *
import random

wn = Tk()
wn.geometry("350x450")
wn.title("Roomeo")
wn.resizable(width=False, height=False)

booking_label = Label(wn)
booking_label.pack()



booking = PhotoImage(file = r"images\booking.png")
booking_label.config(image=booking)
booking_label.image = booking











wn.mainloop()