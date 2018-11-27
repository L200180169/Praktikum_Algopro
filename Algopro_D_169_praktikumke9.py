#/usr/bin/python
# menulis data ke dalam berkas
#kegiatan 1 dan 2
berkas = open("L200180169", "w")
berkas.write(" NIM = L200180169 \n")
berkas.write(" TL = 09/18/2000 \n")
berkas.write(" Nama = Yusuf Ade Putra Perdana \n")
berkas.write("Kotalahir = Boyolali ")
berkas.close()
z = open ("L200180169", "r")
NIM = z.readline()
TL = z.readline()
Nama = z.readline()
Kotalhr = z.readline()
print Nama
print Kotalhr, TL
print NIM

#kegitan 3
import shelve
a = open ("L200180169", "r")
NIM = a.readline()
TL = a.readline()
Nama = a.readline()
a.close()

a=shelve.open("yusuf")
a['b'] = [NIM, TL, Nama]
a.close()

#kegiatan 4
a=shelve.open("yusuf")
print a['b']
print a['b'][0]
print a['b'][1]
print a['b'][2]
