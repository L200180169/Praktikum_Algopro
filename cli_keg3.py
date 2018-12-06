import socket

hostname = 'localhost'
pesan = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50001))
print "Menghitung luas prisma"
while pesan != 'keluar':
    pesan = raw_input('Pesan : ')
    s.send(pesan)
    if pesan.lower()=='keluar':
        response = s.recv(1024)
        print 'respon: -'
        s.close()
        break
    elif pesan.lower() != 'keluar':
        response = s.recv(1024)
        print 'respon:', response
s.close()
 
