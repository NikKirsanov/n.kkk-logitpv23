from tkinter import*

def tehtudvalik(var):
    f=var.get()
    if f:
        texbox.configure(show="")
    else:
        texbox.configure(show="*")
def textpealkirjasse():
    t=texbox.get()
    pealkiri.configure(text=t)
    texbox.delete(0,END)
aken=Tk()
aken.geometry("500x500")
aken.title("Akna pealkiri")
aken.configure(bg="#5a63db")
aken.iconbitmap("mmm.ico")
pealkiri=Label(aken,
                text="Põhielemendid",
                bg="#d25adb",
                fg="#db1215",
                cursor="star",
                font="Times_New_Roman 16",
                justify=CENTER,
                height=3,width=26)
raam=Frame(aken)
texbox=Entry(raam,
             bg="#d25adb",
             fg="#db1215",
             font="Times_New_Roman 16",
             width=16,
             show="*")
pilt=PhotoImage(file="ll.png")
var=BooleanVar() #IntVar(), StringVar()
valik=Checkbutton(raam,
                  image=pilt, #text="Punkt1
                  variable=var,
                  onvalue=True,
                  offvalue=False,
                  command=lambda:tehtudvalik(var))
#valik.deselect()
nupp=Button(raam,
            text="Vajuta mind",
            bg="#d25adb",
            fg="#db1215",
            font="Times_New_Roman 16",
            width=16,
            command=textpealkirjasse)

pealkiri.pack()
raam.pack()
texbox.grid(row=0,column=0) #raami sees
valik.grid(row=0,column=1) #raami sees
nupp.grid(row=0,column=2) #raami sees
aken.mainloop()
