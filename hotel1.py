from tkinter import *
import random

wn = Tk()
wn.geometry("350x450")
wn.title("Roomeo")
wn.resizable(width=False, height=False)

# ---------------------------------------------------------------------------- #
def search_page():
    search_screen = Toplevel(wn)
    search_screen .geometry("350x450")
    search_screen .title("Roomeo_search")
    search_screen .resizable(width=False, height=False) 
    search_label = Label(search_screen)
    search_label.pack()
    search = PhotoImage(file = r"images\search.png")
    search_label.config(image=search)
    search_label.image = search
    btn1= Button(search_screen, text="search", bg="#6EA3CF", width=11, height=3,command=search_page)
    btn1.place(x=0, y=400)

    btn2= Button(search_screen, text="saved", bg="#6EA3CF", width=11, height=3,command=saved_page)
    btn2.place(x=80, y=400)

    btn3= Button(search_screen, text="booking", bg="#6EA3CF", width=11, height=3,command=booking_page)
    btn3.place(x=180, y=400)

    btn4= Button(search_screen, text="profile", bg="#6EA3CF", width=11, height=3,command=profile_page)
    btn4.place(x=265, y=400)

# ---------------------------------------------------------------------------- #
def saved_page():
    saved_screen = Toplevel(wn)
    saved_screen.geometry("350x450")
    saved_screen.title("Roomeo")
    saved_screen.resizable(width=False, height=False)
    saved_label = Label(saved_screen)
    saved_label.pack()
    saved = PhotoImage(file = r"images\saved.png")
    saved_label.config(image=saved)
    saved_label.image = saved

    btn1= Button(search_screen, text="search", bg="#6EA3CF", width=11, height=3,command=search_page)
    btn1.place(x=0, y=400)

    btn2= Button(search_screen, text="saved", bg="#6EA3CF", width=11, height=3,command=saved_page)
    btn2.place(x=80, y=400)

    btn3= Button(search_screen, text="booking", bg="#6EA3CF", width=11, height=3,command=booking_page)
    btn3.place(x=180, y=400)

    btn4= Button(search_screen, text="profile", bg="#6EA3CF", width=11, height=3,command=profile_page)
    btn4.place(x=265, y=400)
# ---------------------------------------------------------------------------- #
def booking_page():
    booking_screen = Toplevel(wn)
    booking.geometry("350x450")
    booking.title("Roomeo")
    booking.resizable(width=False, height=False)
    booking_label = Label(booking)
    booking_label.pack()
    booking = PhotoImage(file = r"images\booking.png")
    booking_label.config(image=booking)
    booking_label.image = booking

    btn1= Button(search_screen, text="search", bg="#6EA3CF", width=11, height=3,command=search_page)
    btn1.place(x=0, y=400)

    btn2= Button(search_screen, text="saved", bg="#6EA3CF", width=11, height=3,command=saved_page)
    btn2.place(x=80, y=400)

    btn3= Button(search_screen, text="booking", bg="#6EA3CF", width=11, height=3,command=booking_page)
    btn3.place(x=180, y=400)

    btn4= Button(search_screen, text="profile", bg="#6EA3CF", width=11, height=3,command=profile_page)
    btn4.place(x=265, y=400)
# ---------------------------------------------------------------------------- #
def profile_page():
    profile_screen = Toplevel(wn)
    profile_screen.geometry("350x450")
    profile_screen.title("Roomeo")
    profile_screen.resizable(width=False, height=False)

    profile_label = Label(profile_screen)
    profile_label.pack()



    profile = PhotoImage(file = r"images\profile.png")
    profile_label.config(image=profile)
    profile_label.image = profile


    btn_help= Button(wn, text="help", bg="grey", width=10, height=2)
    btn_help.place(x=20, y=250)


    name_label = Label(
        profile_screen,
        text="Name:",
        font = ("arial 15"),
        fg = "black"
    )
    name_label.pack()
    name_label.place(x=20,y=100)

    email_label = Label(
        profile_screen,
        text="E-Mail:",
        font = ("arial 15"),
        fg = "black"
    )
    email_label.pack()
    email_label.place(x=20,y=150)


    password_label = Label(
        profile_screen,
        text="Password:",
        font = ("arial 15"),
        fg = "black"
    )
    password_label.pack()
    password_label.place(x=20,y=200)

    btn1= Button(search_screen, text="search", bg="#6EA3CF", width=11, height=3,command=search_page)
    btn1.place(x=0, y=400)

    btn2= Button(search_screen, text="saved", bg="#6EA3CF", width=11, height=3,command=saved_page)
    btn2.place(x=80, y=400)

    btn3= Button(search_screen, text="booking", bg="#6EA3CF", width=11, height=3,command=booking_page)
    btn3.place(x=180, y=400)

    btn4= Button(search_screen, text="profile", bg="#6EA3CF", width=11, height=3,command=profile_page)
    btn4.place(x=265, y=400)
# ---------------------------------------------------------------------------- #
def sign_in():
    sign_in_screen = Toplevel(wn)
    sign_in_screen.geometry("350x450")
    sign_in_screen.title("Roomeo_sign_in")
    sign_in_screen.resizable(width=False, height=False)
    btn_devam= Button(sign_in_screen, text="ok", bg="grey", width=5, height=1, font=("arial 12"),command=search_page)
    btn_devam.place(x=150, y=300)

# ---------------------------------------------------------------------------- #
def create_account():
    create_account_screen = Toplevel(wn)
    create_account_screen.geometry("350x450")
    create_account_screen.title("Roomeo_sign_in")
    create_account_screen.resizable(width=False, height=False)
    btn_devam= Button(create_account_screen, text="ok", bg="grey", width=5, height=1, font=("arial 12"),command=search_page)
    btn_devam.place(x=150, y=300)

# ---------------------------------------------------------------------------- #


name_label = Label(wn)
name_label.pack()
airplane_label = Label(wn)
airplane_label.pack()



name = PhotoImage(file = r"images\namer.png")
name_label.config(image=name)
name_label.image = name

airplane= PhotoImage(file = r"images\airplane.png")
airplane_label.config(image=airplane)
airplane_label.image = airplane


btn_sign_in= Button(wn, text="sign in", bg="#B54D3D", width=10, height=3, font=("arial 12"), command=sign_in)
btn_sign_in.place(x=60, y=360)

btn_create_account= Button(wn, text="create account", bg="#B54D3D", width=11, height=3, font=("arial 12"), command=create_account)
btn_create_account.place(x=200, y=360)









wn.mainloop()