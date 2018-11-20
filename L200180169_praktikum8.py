##Yusuf Ade Putra Perdana
##L200180169

##kegiatan 1
a = {'NIM':'L200180169','Nama':'Yusuf Ade Putra Perdana','Alamat':'Karanganyar','Panggilan':'Yusuf / Ade / Khalid','PT':'UMS','Fak':'FKI','Prodi':'Informatika'}

print "Pilihan yang tersedia:"
print "N menampilkan Nama"
print "n menampilkan NIM"
print "l menampilkan Alamat"
print "p menampilkan Panggilan"
print "t menampilkan PT"
print "f menampilkan Fakultas"
print "i menampilkan Prodi"


def Nama():
    "menampilkan data diri masing-masing 1 setiap data"
    print 'Nama:' + a['Nama']
    

def NIM():
    "menampilkan data diri masing-masing 1 setiap data"
    print 'NIM:' + a['NIM']
    
def Alamat():
    "menampilkan data diri masing-masing 1 setiap data"
    print 'Alamat:' + a['Alamat']
    
def Panggilan():
    "menampilkan data diri masing-masing 1 setiap data"
    print 'Panggilan:' + a['Panggilan']

def PT():
    "menampilkan data diri masing-masing 1 setiap data"
    print 'PT:' + a['PT']
    
def Fak():
    "menampilkan data diri masing-masing 1 setiap data"
    print 'Fakultas:' + a['Fak']
    
def Prodi():
    "menampilkan data diri masing-masing 1 setiap data"
    print 'Prodi:' + a['Prodi']


repeat = True

while repeat :
    x = raw_input("Pilihan Saudara :")
    if x == "N" :
        Nama()
    elif x == "n" :
        NIM()
    elif x == "l" :
        Alamat()
    elif x == "p" :
        Panggilan()
    elif x == "t" :
        PT()
    elif x == "f" :
        Fak()
    elif x == "i" :
        Prodi()
    elif x == "k" :
        print "Terima Kasih."
        repeat = False


## kegiatan 2
def konversiSuhu (C = 0 , F = 0) :
    if C != 0 :
        x = (( 9 * C / 5 ) + 32)
        print ("Suhu", C , "Celcius setara dengan", x ,"Fahrenheit")
    elif F != 0 :
        y = (( F - 32) * 5 / 9 )
        print ("Suhu", F ,"Fahrenheit setara dengan", y ,"Celcius")
    else :
        print ("Suhu 0 Celcius setara dengan 32 Fahrenheit")
    return;
