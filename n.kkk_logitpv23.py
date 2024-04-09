from tkinter import *
from tkinter import messagebox as mb
from string import *
from time import sleep
import random
import imghdr
from tkinter import simpledialog as sd
def autoriseerimine(kasutajad: list, paroolid: list):
    p = 0
    while True:
        kasutaja = input("Sisestage kasutajanimi: ")
        parool = input("Sisestage parool: ")
        if kasutaja in kasutajad and parool in paroolid:
            print("Sisselogimine õnnestus!")
            return kasutaja
        else:
            p += 1
            print("Vale nimi või salasõna!")
            if p == 5:
                print("Proovi uuesti 10 sekundi pärast")
                for i in range(10):
                    sleep(1)
                    print(f"On jäänud {10-i} sekundit")
            else:
                print("Kasutajat pole")
                break
def tehtudvalik(var):
    f=var.get()
    if f:
        texbox.configure(show="")
        valik.configure(image=pilt2)
    else:
        texbox.configure(show="*")
        valik.configure(image=pilt1)
def textpealkirjasse():
    vastus=mb.askquestion("Küsimus","Kas tõesti tahad info kopeerida?")
    if vastus=='yes':
        mb.showwarning("Tähelepanu","Kohe teiseldatakse info!")
        t=texbox.get()
        pealkiri.configure(text=t)
        texbox.delete(0,END)
    else:
        mb.showinfo("Valik oli tehtud","Info jääb omal kohal")
        nimi=sd.askstring("Saame tuttavaks!","Mis on sinu nimi?")
aken=Tk()
aken.geometry("500x500")
aken.title("Akna pealkiri")
aken.configure(bg="#13e0eb")
aken.iconbitmap("icon.ico")
pealkiri=Label(aken,
               text="Põhielemendid",
               bg="#9edb8f",
               fg="#18420d",
               cursor="star",
               font="Britannic_Bold 16",
               justify=CENTER,
               height=3,width=26)
raam=Frame(aken)
texbox=Entry(raam,
             bg="#18420d",
             fg="#9edb8f",
             font="Britannic_Bold 16",
             width=16,
             show="*")
pilt=PhotoImage(file="eye.png")
var=BooleanVar() #IntVar(), StringVar()
valik=Checkbutton(raam,
                  image=pilt, #text="Punkt1"
                  variable=var,
                  onvalue=True,
                  offvalue=False,
                  command=lambda:tehtudvalik(var))
#valik.deselect()
nupp=Button(raam,
            text="Vajuta mind",
            bg="#9edb8f",
            fg="#18420d",
            font="Britannic_Bold 16",
            width=16,
            command=textpealkirjasse)

pealkiri.pack()
raam.pack()
texbox.grid(row=0,column=0) #raami sees
valik.grid(row=0,column=1) #raami sees
nupp.grid(row=0,column=2) #raami sees
aken.mainloop()


from module1 import *
kasutajad = ["Nikita"]
paroolid = ["Nikita2006"]
kus_vas = loe("Ankeet.txt")
while True:
    print("1 - Soorita test\n2 - Logi administraatorina sisse\n3 - Lõpetamine")
    vastus = int(input("Sisestage arv: "))
    if vastus == 1:
        print("Soorita test")
        osaleja_nimi = input("Palun sisestage oma nimi: ")
        receiver_email = input("Sisesta oma email: ")
        N = int(input("Mitu küsimust soovite? "))
        punktid, correct_answers = küsimus_vastus(kus_vas, N)
        salvesta(osaleja_nimi, punktid, "Oiged.txt", "Valed.txt")
        hindamine = "Positiivne" if punktid > N/2 else "Negatiivne"
        tulemused_(osaleja_nimi, receiver_email, punktid, hindamine)
        print("\nEdukalt läbinud osalejad:")
        with open("Oiged.txt", 'r', encoding='utf-8') as oiged_fail:
            print(oiged_fail.read())
            print("\nEbaõnnestunud osalejad:")
        with open("Valed.txt", 'r', encoding='utf-8') as valed_fail:
            print(valed_fail.read())
    elif vastus == 2:
        print("Administraator")
        autoriseerimine(kasutajad, paroolid)
        uued = {}
        uute_arv = int(input("Sisesta mitu tahate teha uute küsimuset: "))
        for i in range(uute_arv):
            küsimus = input("Sisestage uus küsimus: ")
            vastus = input("Sisestage küsimusele vastus: ")
            uued[küsimus] = vastus
        lisa(uued, "Ankeet.txt")
    elif vastus == 3:
        print("Lõpetamine")
        break
    else:
        print("Tundmatu valik")