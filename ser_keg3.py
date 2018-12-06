import socket
def prisma(lp=0, ls=0):
    L = (2 * ls) + (2 * lp) 
    return L
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50001))
s.listen(5)
print "Server sudah siap"
data = ''

while 1:
    komm, addr = s.accept()
    while data.lower() !='keluar':
        data = komm.recv(1024)
        print 'Pesan:', data
        if data.find("parameter") != -1:
            param, value = data.split("=")
            if param == "parameter1":
                ls = float(value)
                lp = float(value)
                x = value
                komm.send("Parameter dicatat")
        elif data=='hitung':
            komm.send('luas prisma dengan ls{}dan lp{} adalah {}'.format(x, prisma(ls, lp)))
        else:
            komm.send('Tidak ada')
