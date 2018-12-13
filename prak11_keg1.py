from Tkinter import *
my_app = Tk(className='Kegiatan 1')

L1 = Label(my_app, text='DATA DIRI', font=('Arial',24))
L1.grid(row=0, column=0)


L2 = Label(my_app, text='Nama')
L2.grid(row=1, column=0, sticky=W)

L3 = Label(my_app, text='Yusuf Ade Putra Perdana')
L3.grid(row=1, column=1, sticky=W)

L4 = Label(my_app, text='NIM')
L4.grid(row=2, column=0, sticky=W)

L5 = Label(my_app, text='L200180169')
L5.grid(row=2, column=1, sticky=W)

L6 = Label(my_app, text='Buku Favorit')
L6.grid(row=3, column=0, sticky=W)

L7 = Label(my_app, text='Daun Yang Terjatuh Tidak Pernah Membenci Angin')
L7.grid(row=3, column=1, sticky=W)

L8 = Label(my_app, text='Idola di kalangan sahabat')
L8.grid(row=4, column=0, sticky=W)

L9 = Label(my_app, text='Umar bin Khattab')
L9.grid(row=4, column=1, sticky=W)

L10 = Label(my_app, text='Motto')
L10.grid(row=5, column=0, sticky=W)

L2 = Label(my_app, text='Do what you love, love what you do')
L2.grid(row=5, column=1, sticky=W)

def tutup():
    my_app.destroy()

B = Button(my_app, text="Tutup", command=tutup)
B.grid(row=6, column=1, sticky=W)

my_app.mainloop()
