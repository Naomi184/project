from tkinter import *
import random

wn = Tk()
wn.geometry("350x450")
wn.title("Roomeo")
wn.resizable(width=False, height=False)

profile_label = Label(wn)
profile_label.pack()



profile = PhotoImage(file = r"images\profile.png")
profile_label.config(image=profile)
profile_label.image = profile


btn_help= Button(wn, text="help", bg="grey", width=10, height=2)
btn_help.place(x=20, y=250)


name_label = Label(
    wn,
    text="Name:",
    font = ("arial 15"),
    fg = "black"
)
name_label.pack()
name_label.place(x=20,y=100)

email_label = Label(
    wn,
    text="E-Mail:",
    font = ("arial 15"),
    fg = "black"
)
email_label.pack()
email_label.place(x=20,y=150)


password_label = Label(
    wn,
    text="Password:",
    font = ("arial 15"),
    fg = "black"
)
password_label.pack()
password_label.place(x=20,y=200)




wn.mainloop()