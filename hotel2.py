from tkinter import *
import random

wn = Tk()
wn.geometry("350x450")
wn.title("Roomeo")
wn.resizable(width=False, height=False)



btn1= Button(wn, text="sign in", bg="#6EA3CF", width=11, height=3)
btn1.place(x=0, y=400)

btn2= Button(wn, text="sign in", bg="#6EA3CF", width=11, height=3)
btn2.place(x=80, y=400)

btn3= Button(wn, text="sign in", bg="#6EA3CF", width=11, height=3)
btn3.place(x=180, y=400)

btn4= Button(wn, text="sign in", bg="#6EA3CF", width=11, height=3)
btn4.place(x=265, y=400)




wn.mainloop()