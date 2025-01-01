from tkinter import *
import random

wn = Tk()
wn.geometry("350x450")
wn.title("Roomeo")
wn.resizable(width=False, height=False)

saved_label = Label(wn)
saved_label.pack()



saved = PhotoImage(file = r"images\saved.png")
saved_label.config(image=saved)
saved_label.image = saved











wn.mainloop()