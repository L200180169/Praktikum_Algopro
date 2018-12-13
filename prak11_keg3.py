from tkinter import *
bgeo = Tk(className="Bangun Geometri")

judul = Label(bgeo, text="Bangun Geometri", font="Times, 24", padx=10, pady=10)
judul.grid(row=0)

des = Label(bgeo, font="Times, 12", justify=CENTER, text="""Dalam geometri, prisma ada
ada banyak jenisnya, misalnyay prisma segitiga,segiempat,segilima,dll""", padx=10)
des.grid(row=1)

L1 = Label(bgeo, font="Times, 12", text="Luas Alas :", padx=10)
L1.place(x=85, y=170)

E1 = Entry(bgeo, font="Times, 12")
E1.place(x=175, y=170, height=30)

L2 = Label(bgeo, font="Times, 12", text="Total Luas Selimut :", padx=10)
L2.place(x=85, y=210)

E2 = Entry(bgeo, font="Times, 12")
E2.place(x=175, y=210, height=30)

def hitung():
    s1 = float(E1.get())
    s2 = float(E2.get())
    hasil = (2 * s1) + s2
    luas.config(text=hasil)
    
B = Button(bgeo, text="Hitung Luas", command=hitung, font="Times 14", justify=CENTER)
B.place(x=85, y=250)

L2 = Label(bgeo, text="Luas = ", font="Times 14 bold")
L2.place(x=200, y=255)

luas = Label(bgeo, font="Times 14 bold")
luas.place(x=265, y=255)

bgeo.mainloop()
