from tkinter import *

def login():
    print("Вы нажали кнопку 'Вход'")

def register():
    print("Вы нажали кнопку 'Регистрация'")

tekst="Аутентификация"
aken=Tk()
aken.geometry("700x700")
aken.title(tekst)

pealkiri=Label(aken,
               text="Выберите действие:",
               bg="yellow",
               fg="#0d010b",
               font="Chiller 20",
               height=3,
               width=25)

login_button = Button(aken, 
                      text="Вход",
                      bg="purple",
                      fg="#0d010b",
                      font="Chiller 20",
                      activebackground="red",
                      activeforeground="white",
                      height=3,
                      width=20,
                      command=login)

register_button = Button(aken, 
                         text="Регистрация",
                         bg="green",
                         fg="#0d010b",
                         font="Chiller 20",
                         activebackground="blue",
                         activeforeground="white",
                         height=3,
                         width=20,
                         command=register)

pealkiri.pack()
login_button.pack(pady=10)
register_button.pack(pady=10)

aken.mainloop()
