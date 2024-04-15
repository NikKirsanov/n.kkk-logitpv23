from tkinter import *

def registreerimine():
    kasutajanimi = kasutajanime_sisestus.get()
    parool = parooli_sisestus.get()

    if kasutajanimi and parool: 
        with open("kasutajad.txt", "a") as f:
            f.write(f"{kasutajanimi},{parool}\n")
        print("Kasutaja registreeritud!")
        aken.configure(bg="#FFFF00")
    else:
        print("Kasutajanimi või parool puudub!")

def autoriseerimine():
    kasutajanimi = kasutajanime_sisestus.get()
    parool = parooli_sisestus.get()

    with open("kasutajad.txt", "r") as f:
        kasutajad = f.readlines()

    kasutajad = [kasutaja.strip().split(",") for kasutaja in kasutajad]
    if [kasutajanimi, parool] in kasutajad:
        print("Kasutaja autoriseeritud!")
    else:
        print("Vale kasutajanimi või parool!")

def parooli_muutmine():
    def muuda_parool():
        kasutajanimi = kasutajanime_sisestus.get()
        vana_parool = vana_parooli_sisestus.get()
        uus_parool = uus_parooli_sisestus.get()

        with open("kasutajad.txt", "r") as f:
            kasutajad = f.readlines()

        kasutajad = [kasutaja.strip().split(",") for kasutaja in kasutajad]
        for i, kasutaja in enumerate(kasutajad):
            if kasutaja[0] == kasutajanimi and kasutaja[1] == vana_parool:
                kasutajad[i][1] = uus_parool
                with open("kasutajad.txt", "w") as f:
                    for kasutaja in kasutajad:
                        f.write(f"{kasutaja[0]},{kasutaja[1]}\n")
                print("Parool muudetud!")
                vana_parooli_sisestus.delete(0, END)  
                uus_parooli_sisestus.delete(0, END)   
                top.destroy()
                return
        print("Vale kasutajanimi või parool!")

def close_window():
    aken.destroy()

aken = Tk()
aken.geometry("500x500")
aken.title("Akna pealkiri")
aken.configure(bg="#ec42f5")
aken.iconbitmap("mmm.ico")

pealkiri = Label(aken,
                 text="Nikita Logitpv23",
                 bg="#f54287",
                 fg="#111211",
                 cursor="star",
                 font="Times_New_Roman 16",
                 justify=CENTER,
                 height=3,width=26)

raam = Frame(aken)

kasutajanime_silt = Label(raam, text="Kasutajanimi:")
parooli_silt = Label(raam, text="Parool:")

kasutajanime_sisestus = Entry(raam,
                              bg="#f54287",
                              fg="#111211",
                              font="Times_New_Roman 16",
                              width=16)

parooli_sisestus = Entry(raam,
                         bg="#f54287",
                         fg="#111211",
                         font="Times_New_Roman 16",
                         width=16,
                         show="*")

registreeri_nupp = Button(raam,
                          text="Registreeri",
                          bg="#f54287",
                          fg="#111211",
                          font="Times_New_Roman 16",
                          width=16,
                          command=registreerimine)

autoriseeri_nupp = Button(raam,
                          text="Autoriseeri",
                          bg="#f54287",
                          fg="#111211",
                          font="Times_New_Roman 16",
                          width=16,
                          command=autoriseerimine)

muuda_parooli_nupp = Button(raam,
                            text="Muuda parool",
                            bg="#f54287",
                            fg="#111211",
                            font="Times_New_Roman 16",
                            width=16,
                            command=parooli_muutmine)

pealkiri.pack()
raam.pack()
kasutajanime_silt.grid(row=0,column=0)
kasutajanime_sisestus.grid(row=0,column=1)
parooli_silt.grid(row=1,column=0)
parooli_sisestus.grid(row=1,column=1)
registreeri_nupp.grid(row=2,column=0)
autoriseeri_nupp.grid(row=2,column=1)

muuda_parooli_nupp.grid(row=3,column=0,columnspan=2)

close_button = Button(aken, text="Close", command=close_window)
close_button.pack()

aken.mainloop()
