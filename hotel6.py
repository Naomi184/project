from tkinter import *
import random

wn = Tk()
wn.geometry("350x450")
wn.title("Roomeo")
wn.resizable(width=False, height=False)

help_label = Label(wn)
help_label.pack()



help = PhotoImage(file = r"images\help.png")
help_label.config(image=help)
help_label.image = help











wn.mainloop()