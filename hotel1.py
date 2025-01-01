from tkinter import *
import random

wn = Tk()
wn.geometry("350x450")
wn.title("Roomeo")
wn.resizable(width=False, height=False)

name_label = Label(wn)
name_label.pack()
airplane_label = Label()
airplane_label.pack()


name = PhotoImage(file = r"images\namer.png")
name_label.config(image=name)
name_label.image = name

airplane= PhotoImage(file = r"images\airplane.png")
airplane_label.config(image=airplane)
airplane_label.image = airplane


btn_sign_in= Button(wn, text="sign in", bg="#B54D3D", width=10, height=3, font=("arial 12"))
btn_sign_in.place(x=60, y=360)

btn_create_account= Button(wn, text="create account", bg="#B54D3D", width=11, height=3, font=("arial 12"))
btn_create_account.place(x=200, y=360)









wn.mainloop()