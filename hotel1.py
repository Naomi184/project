from tkinter import *
# from tkinter import ttk
from tkinter import messagebox
import random
import sqlite3
from datetime import datetime



wn = Tk()
wn.geometry("350x450")
wn.title("Roomeo")
wn.resizable(width=False, height=False)


ID = 1

hotelVeritabani=sqlite3.connect("bilgiler.db")
curr=hotelVeritabani.cursor()

curr.execute('''CREATE TABLE IF NOT EXISTS Customer(
CustomerID INTEGER PRIMARY KEY,
email VARCHAR(50),
name VARCHAR(50),
password VARCHAR(50)
)''')

hotelVeritabani.commit()
hotelVeritabani.close()

#-------------------------------#

favorites=sqlite3.connect("favorites2.db")
curr=favorites.cursor()

curr.execute('''CREATE TABLE IF NOT EXISTS favorites2(
ID INTEGER PRIMARY KEY,
ad TEXT,
adres TEXT,
tel TEXT,
ucret TEXT
)''')
favorites.commit()
favorites.close()
#-------------------------------#

booked=sqlite3.connect("booked2.db")
curr=booked.cursor()

curr.execute('''CREATE TABLE IF NOT EXISTS booked2(
ID INTEGER PRIMARY KEY,
ad TEXT,
adres TEXT,
tel TEXT,
ucret TEXT
)''')
booked.commit()
booked.close()
#-------------------------------#











hotels=[
  {
    "id": 1,
    "ad": "Hotel Sunshine",
    "kapasite": 200,
    "adres": "USA",
    "tel": "+1-305-555-1234",
    "url": "https://www.sunshineholidayresort.com/",
    "fotograf": "https://gtr.oteldenrezerve.com/UserFiles/Media/HotelImages/large/12828_Sunshine_Holiday_Resort_107912.jpg",
    "ucret": "110"
  },
  {
    "id": 6,
    "ad": "Royal Palace Hotel",
    "kapasite": 500,
    "adres": "UK",
    "tel": "+44-20-555-1234",
    "url": "https://www.expedia.co.uk/Turin-Hotels-ROYAL-PALACE-HOTEL-SPA.h41521109.Hotel-Information",
    "fotograf": "https://images.trvl-media.com/lodging/42000000/41530000/41521200/41521109/1d112ee3.jpg?impolicy=resizecrop&rw=1200&ra=fit",
    "ucret": "110"
  },
  {
    "id": 7,
    "ad": "Safari Lodge",
    "kapasite": 120,
    "adres": "Kenya",
    "tel": "+254-20-555-6789",
    "url": "https://www.karibu-safaris.de/Kenia/?kw=safari%20kenya&cpn=18966741283&utm_term=safari%20kenya&utm_campaign=_+Kenia&utm_source=adwords&utm_medium=ppc&hsa_acc=4416216333&hsa_cam=18966741283&hsa_grp=144788092978&hsa_ad=636042758603&hsa_src=g&hsa_tgt=kwd-52380993&hsa_kw=safari%20kenya&hsa_mt=p&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=Cj0KCQiA4rK8BhD7ARIsAFe5LXKhx2Mq4-gdXrjs6XXZkQv03nVoCrfHYf1aSrK6DaXC-anRMYi2GcgaAtpuEALw_wcB",
    "fotograf": "https://www.choosethemoon.com/images/anuncios/mara-serena-safari-lodge-1-2268.jpg",
    "ucret": "110"
  },
  {
    "id": 8,
    "ad": "Aurora Borealis Inn",
    "kapasite": 100,
    "adres": "Norway",
    "tel": "+47-77-555-4321",
    "url": "https://aurora-borealis-observatory-silsand.hotel-mix.de/",
    "fotograf": "https://aurora-borealis-observatory-silsand.hotel-mix.de/data/Photos/450x450/15376/1537673/1537673914.JPEG",
    "ucret": "110"
  },
  {
    "id": 9,
    "ad": "Rainforest Resort",
    "kapasite": 200,
    "adres": "Brazil",
    "tel": "+55-92-555-9876",
    "url": "https://ruppertbrasil.de/katalog/brasilien-reisen/amazonas-reisen/anavilhanas-jungle-lodge/#",
    "fotograf": "https://ruppertbrasil.de/wp-content/uploads/2015/06/1320-br-mao-Anavilhanas-Bungalows.jpg",
    "ucret": "110"
  },
  {
    "id": 10,
    "ad": "Ocean View Suites",
    "kapasite": 220,
    "adres": "Australia",
    "tel": "+61-2-555-3456",
    "url": "https://ocean-views-resort.sunshine-coast-tophotels.com/de/",
    "fotograf": "https://ocean-views-resort.sunshine-coast-tophotels.com/data/Pics/OriginalPhoto/8471/847118/847118423/ocean-views-resort-caloundra-pic-1.JPEG",
    "ucret": "110"
  },
  {
    "id": 11,
    "ad": "Hotel Canoe and Suites",
    "kapasite": 150,
    "adres": "Canada",
    "tel": "+1-604-555-7890",
    "url": "https://www.skiresortlodge.com",
    "fotograf": "https://www.skiresortlodge.com/images/hotel11.jpg",
    "ucret": "110"
  },
  {
    "id": 12,
    "ad": "Luxury Yacht Hotel",
    "kapasite": 50,
    "adres": "Singapore",
    "tel": "+65-555-1234",
    "url": "https://hotelcanoeandsuites.com/superior-suite/",
    "fotograf": "https://hotelcanoeandsuites.com/wp-content/uploads/2024/07/Superior-Suite-800.jpg",
    "ucret": "110"
  },
  {
    "id": 13,
    "ad": "Forest Haven",
    "kapasite": 180,
    "adres": "India",
    "tel": "+41-31-555-6789",
    "url": "https://www.foresthavenresort.com/",
    "fotograf": "https://www.foresthavenresort.com/assets/img/foresthaven1.jpg",
    "ucret": "110"
  },
  {
    "id": 14,
    "ad": "Aqua Luxury Suites",
    "kapasite": 250,
    "adres": "Greece",
    "tel": "+30-22860-55555",
    "url": "https://aquasuites.gr/",
    "fotograf": "https://aquasuites.gr/wp-content/uploads/2024/04/deluxedoubleroom_9076-retouched.jpg",
    "ucret": "110"
  },
  {
    "id": 15,
    "ad": "ONE@Tokyo",
    "kapasite": 350,
    "adres": "Japan",
    "tel": "+81-3-555-9876",
    "url": "https://www.onetokyo.com/",
    "fotograf": "https://www.onetokyo.com/img/accommodation/atelier/img_atelier02.png",
    "ucret": "110"
  },
  {
    "id": 16,
    "ad": "Hôtel de France",
    "kapasite": 100,
    "adres": "France",
    "tel": "+33-5-555-6543",
    "url": "https://www.hoteldefrance-paris.fr/",
    "fotograf": "https://lh3.googleusercontent.com/gps-proxy/ALd4DhGRElDcscuq3zSzgJf8sfzHwZ3vkQYOJ7NWIQ-8d9-0CYXy_h80l8JnnFelrxeY76wz7W5frn6VKh3uQj3LUF5orw7Pqn4D8f6ojSYQcZ7k5aqz_3sA5J0-cLkOgXt490DqTEcq0jeJxaFotzEAS0myKdBfI8Dai0ulJX2o77JbXfUtM-IGNuzo3Q=s294-w294-h220-n-k-no",
    "ucret": "110"
  },
  {
    "id": 17,
    "ad": "Ayada Maldives",
    "kapasite": 200,
    "adres": "Maldives",
    "tel": "+960-555-1234",
    "url": "https://lh3.googleusercontent.com/p/AF1QipN8fPljIU1HNyu5BbU_dWKcdENxExrEI0BM-Aom=s294-w294-h220-n-k-no",
    "fotograf": "https://www.ayadamaldives.com/",
    "ucret": "110"
  }
]
    


    






# ---------------------------------------------------------------------------- #
def search_page():
  secili_hotel = ""
  search_screen = Toplevel(wn)
  search_screen .geometry("350x450")
  search_screen .title("Roomeo_search")
  search_screen .resizable(width=False, height=False) 
  search_label = Label(search_screen)
  search_label.pack()
  search = PhotoImage(file = r"images\search.png")
  search_label.config(image=search)
  search_label.image = search
    
  hotelListbox=Listbox(search_screen)
  hotelListbox.place(x=120,y=200)
  for hotel in hotels:
    hotelListbox.insert(END,hotel["adres"])


  def hotel_kaydet():
    hotel=[]
    secili_hotel = hotelListbox.curselection()
    print(secili_hotel)
    if secili_hotel:
      hotel_bilgisi = hotels[secili_hotel[0]]
      print(hotel_bilgisi )
      info = {'ad':hotel_bilgisi['ad'],'adres': hotel_bilgisi['adres'], 'tel': hotel_bilgisi['tel'],'ucret':hotel_bilgisi['ucret']}
      hotel.append(info)
      favorites(hotel)
      booked(hotel)
    


  btn1= Button(search_screen, text="search", bg="#6EA3CF", width=11, height=3,command=search_page)
  btn1.place(x=0, y=400)

  btn2= Button(search_screen, text="saved", bg="#6EA3CF", width=11, height=3,command=hotel_kaydet)
  btn2.place(x=80, y=400)

  btn3= Button(search_screen, text="booking", bg="#6EA3CF", width=11, height=3,command=hotel_kaydet)
  btn3.place(x=180, y=400)

  btn4= Button(search_screen, text="profile", bg="#6EA3CF", width=11, height=3,command=profile_page)
  btn4.place(x=265, y=400)

# ---------------------------------------------------------------------------- #
def saved_page():
    y=100
    saved_screen = Toplevel(wn)
    saved_screen.geometry("350x450")
    saved_screen.title("Roomeo")
    saved_screen.resizable(width=False, height=False)
    saved_label = Label(saved_screen)
    saved_label.pack()
    saved = PhotoImage(file = r"images\saved.png")
    saved_label.config(image=saved)
    saved_label.image = saved


    favorites=sqlite3.connect("favorites2.db")
    curr=favorites.cursor()

    curr.execute(''' SELECT * FROM  favorites2''')
      # fetch işlemi bir şeyi al getir anlamında. Burdada verileri çekmek için kullanılır.
    bilgiler=curr.fetchall()
  

    favorites.commit()
    favorites.close()
    listeKutusu=Listbox(saved_screen,height=20,width=40)
    listeKutusu.place(x=20,y=10)
    for bilgi in bilgiler:            
            listeKutusu.insert(END,bilgi)

    btn1= Button(saved_screen, text="search", bg="#6EA3CF", width=11, height=3,command=search_page)
    btn1.place(x=0, y=400)

    btn2= Button(saved_screen, text="saved", bg="#6EA3CF", width=11, height=3,command=saved_page)
    btn2.place(x=80, y=400)

    btn3= Button(saved_screen, text="booking", bg="#6EA3CF", width=11, height=3,command=booking_page)
    btn3.place(x=180, y=400)

    btn4= Button(saved_screen, text="profile", bg="#6EA3CF", width=11, height=3,command=profile_page)
    btn4.place(x=265, y=400)

# ---------------------------------------------------------------------------- #
def favorites(hotel):
  ID = int(datetime.now().timestamp())
  print(hotel)
  favorites=sqlite3.connect("favorites2.db")
  curr=favorites.cursor()

  curr.execute('''INSERT OR REPLACE INTO favorites2 (ID,ad,adres,tel,ucret) VALUES (?,?,?,?,?)
  ''',(ID,hotel[0]['ad'],hotel[0]['adres'],hotel[0]['tel'],hotel[0]['ucret']))

  favorites.commit()
  favorites.close()
  saved_page()
  



# ---------------------------------------------------------------------------- #
def booking_page():
  booking_screen = Toplevel(wn)
  booking_screen.geometry("350x450")
  booking_screen.title("Roomeo")
  booking_screen.resizable(width=False, height=False)
  booking_label = Label(booking_screen)
  booking_label.pack()
  booking = PhotoImage(file = r"images\booking.png")
  booking_label.config(image=booking)
  booking_label.image = booking
  #-----#
  booked=sqlite3.connect("booked2.db")
  curr=booked.cursor()

  curr.execute(''' SELECT * FROM  booked2''')
    # fetch işlemi bir şeyi al getir anlamında. Burdada verileri çekmek için kullanılır.
  bilgiler=curr.fetchall()
  

  booked.commit()
  booked.close()
  bKutusu=Listbox(booking_screen,height=20,width=40)
  bKutusu.place(x=20,y=10)
  for bilgi in bilgiler:            
    bKutusu.insert(END,bilgi)
  #-----#

  btn1= Button(booking_screen, text="search", bg="#6EA3CF", width=11, height=3,command=search_page)
  btn1.place(x=0, y=400)

  btn2= Button(booking_screen, text="saved", bg="#6EA3CF", width=11, height=3,command=saved_page)
  btn2.place(x=80, y=400)

  btn3= Button(booking_screen, text="booking", bg="#6EA3CF", width=11, height=3,command=booking_page)
  btn3.place(x=180, y=400)

  btn4= Button(booking_screen, text="profile", bg="#6EA3CF", width=11, height=3,command=profile_page)
  btn4.place(x=265, y=400)

  # ---------------------------------------------------------------------------- #
def booked(hotel):
  ID = int(datetime.now().timestamp())
  print(hotel)
  booked=sqlite3.connect("booked2.db")
  curr=booked.cursor()

  curr.execute('''INSERT OR REPLACE INTO booked2 (ID,ad,adres,tel,ucret) VALUES (?,?,?,?,?)
  ''',(ID,hotel[0]['ad'],hotel[0]['adres'],hotel[0]['tel'],hotel[0]['ucret']))

  booked.commit()
  booked.close()
  booking_page()


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


  btn_help= Button(profile_screen, text="help", bg="grey", width=10, height=2, command=help_page)
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

  btn1= Button(profile_screen, text="search", bg="#6EA3CF", width=11, height=3,command=search_page)
  btn1.place(x=0, y=400)

  btn2= Button(profile_screen, text="saved", bg="#6EA3CF", width=11, height=3,command=saved_page)
  btn2.place(x=80, y=400)

  btn3= Button(profile_screen, text="booking", bg="#6EA3CF", width=11, height=3,command=booking_page)
  btn3.place(x=180, y=400)

  btn4= Button(profile_screen, text="profile", bg="#6EA3CF", width=11, height=3,command=profile_page)
  btn4.place(x=265, y=400)
# ---------------------------------------------------------------------------- #
def help_page():
  help_screen = Toplevel(wn)
  help_screen.geometry("350x450")
  help_screen.title("Roomeo")
  help_screen.resizable(width=False, height=False)

  help_label = Label(help_screen)
  help_label.pack()

  help = PhotoImage(file = r"images\help.png")
  help_label.config(image=help)
  help_label.image = help


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
  
  iiinfo = f"Try it at sing in, maybe you have already a account."

    
    
  def Kaydet(email,name,password):
    global ID
    ID = int(datetime.now().timestamp())

    hotelVeritabani=sqlite3.connect("bilgiler.db")
    curr=hotelVeritabani.cursor()
    curr.execute('''
    INSERT INTO Customer (CustomerID, email, name, password)
    VALUES (?,?,?,?)
    ''', (ID, email, name, password))
    hotelVeritabani.commit()
    hotelVeritabani.close()
    print("Veri kaydedildi.")
    # if  :                                                                   #<----account war sa
    #   messagebox.showinfo(iiinfo)


  Label(create_account_screen, text="email:").place(x=90, y=80)
  email = Entry(create_account_screen)
  email.place(x=150, y=80)
    
  Label(create_account_screen, text="name:").place(x=90, y=120)
  name = Entry(create_account_screen)
  name.place(x=150, y=120)

  Label(create_account_screen, text="password:").place(x=90, y=160)
  password = Entry(create_account_screen)
  password.place(x=150, y=160)

  email = email.get()
  name = name.get()
  password = password.get()

  btn_devam= Button(create_account_screen, text="save", bg="grey", width=5, height=1, font=("arial 12"),command=lambda:Kaydet(email,name,password))
  btn_devam.place(x=80, y=300)

  btn_devam= Button(create_account_screen, text="go", bg="grey", width=5, height=1, font=("arial 12"),command=search_page)
  btn_devam.place(x=230, y=300)
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