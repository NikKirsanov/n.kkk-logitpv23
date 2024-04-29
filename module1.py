from tkinter import *
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def parooli_muutmine_aken():
    def muuda_parool():
        kasutajanimi = kasutajanimi_sisend.get()
        vana_parool = vana_parooli_sisend.get()
        uus_parool = uus_parooli_sisend.get()

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
                vana_parooli_sisend.delete(0, END)  
                uus_parooli_sisend.delete(0, END)   
                muuda_parooli_aken.destroy()
                send_email("Parooli muutmine", f"Parool muudetud kasutajale: {kasutajanimi}")
                return
        print("Vale kasutajanimi või parool!")

    muuda_parooli_aken = Toplevel()
    muuda_parooli_aken.title("Parooli muutmine")
    muuda_parooli_aken.geometry("300x200")

    kasutajanimi_silt = Label(muuda_parooli_aken, text="Kasutajanimi:")
    vana_parooli_silt = Label(muuda_parooli_aken, text="Vana parool:")
    uus_parooli_silt = Label(muuda_parooli_aken, text="Uus parool:")

    kasutajanimi_sisend = Entry(muuda_parooli_aken)
    vana_parooli_sisend = Entry(muuda_parooli_aken, show="*")
    uus_parooli_sisend = Entry(muuda_parooli_aken, show="*")

    muuda_nupp = Button(muuda_parooli_aken, text="Muuda", command=muuda_parool)

    kasutajanimi_silt.grid(row=0, column=0, padx=10, pady=5)
    kasutajanimi_sisend.grid(row=0, column=1, padx=10, pady=5)
    vana_parooli_silt.grid(row=1, column=0, padx=10, pady=5)
    vana_parooli_sisend.grid(row=1, column=1, padx=10, pady=5)
    uus_parooli_silt.grid(row=2, column=0, padx=10, pady=5)
    uus_parooli_sisend.grid(row=2, column=1, padx=10, pady=5)
    muuda_nupp.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

def send_email(subject, body):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "nik.kirsanov17@gmail.com"  # Замените на свою почту
    password = input("Введите пароль и нажмите Enter: ")
    receiver_email = "nik.kirsanov118@gmail.com"  # Замените на адрес получателя
    context = ssl.create_default_context()

    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            server.send_message(msg)
        print("Письмо успешно отправлено.")
    except Exception as e:
        print("Ошибка отправки письма:", e)

def registreerimine():
    kasutajanimi = kasutajanime_sisestus.get()
    parool = parooli_sisestus.get()

    if kasutajanimi and parool: 
        with open("kasutajad.txt", "a") as f:
            f.write(f"{kasutajanimi},{parool}\n")
        print("Kasutaja registreeritud!")
        aken.configure(bg="#FFFF00")
        send_email("Registreerimine", f"Uus kasutaja registreeritud: {kasutajanimi}")
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
                            command=parooli_muutmine_aken)  # Изменено на parooli_muutmine_aken

pealkiri.pack()
raam.pack()
kasutajanime_silt.grid(row=0,column=0)
kasutajanime_sisestus.grid(row=0,column=1)
parooli_silt.grid(row=1,column=0)
parooli_sisestus.grid(row=1,column=1)
registreeri_nupp.grid(row=2,column=0)
autoriseeri_nupp.grid(row=2,column=1)

muuda_parooli_nupp.grid(row=3,column=0,columnspan=2)

def close_window():
    aken.destroy()

close_button = Button(aken, text="Sulge", command=close_window)
close_button.pack()

aken.mainloop()
