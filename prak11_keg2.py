from Tkinter import *
calc = Tk(className="Kalkulator Sederhana")

L1 = Label(calc, text='Angka 1', font="Times 14")
L1.place(x=10, y=10)

L2 = Label(calc, text='Angka 2', font="Times 14")
L2.place(x=10, y=60)

E1 = Entry(calc, justify=RIGHT, font="Times 14")
E1.place(x=90, y=10, height=35, width=180)

E2 = Entry(calc, justify=RIGHT, font="Times 14")
E2.place(x=90, y=60, height=35, width=180)

def tambah():
    "menjumlahkan dua bilangan"
    bil1 = float(E1.get())
    bil2 = float(E2.get())
    hasil = bil1 + bil2
    L4.config(text=hasil)

def kurang():
    "menjumlahkan dua bilangan"
    bil1 = float(E1.get())
    bil2 = float(E2.get())
    hasil = bil1 - bil2
    L4.config(text=hasil)

def kali():
    "menjumlahkan dua bilangan"
    bil1 = float(E1.get())
    bil2 = float(E2.get())
    hasil = bil1 * bil2
    L4.config(text=hasil)

def bagi():
    "menjumlahkan dua bilangan"
    bil1 = float(E1.get())
    bil2 = float(E2.get())
    hasil = bil1 / bil2
    L4.config(text=hasil)
    
B1 = Button(calc, text="+", command=tambah, font="Times 14")
B1.place(x=40, y=110, height=30, width=30)

B2 = Button(calc, text="-", command=kurang, font="Times 14")
B2.place(x=95, y=110, height=30, width=30)

B3 = Button(calc, text="x", command=kali, font="Times 14")
B3.place(x=150, y=110, height=30, width=30)

B4 = Button(calc, text=":", command=bagi, font="Times 14")
B4.place(x=205, y=110, height=30, width=30)

L3 = Label(calc, text='Hasil', font="Times 14")
L3.place(x=20, y=170)

L4 = Label(calc, font="Times 14", justify=CENTER, relief=RIDGE)
L4.place(x=90, y=165, height=35, width=180)

calc.mainloop()
