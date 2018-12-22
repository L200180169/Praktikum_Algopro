def hitung(luasa,luasb,sisi) :
    a=luasa
    b=luasb
    n=sisi
    luas=(2*a)+(n*b)
    return luas
luasa = 30
luasb = 100

print "<!DOCTYPE html>"
print
print """<html>
<head><title>Luas Bangun Geometri</title></head>
<body>"""
print """<table>
<tr>
    <th rowspan='8' width='150'> GAMBAR </th>
    <td><h3> Bangun Geometri <h3></td>
</tr>
<tr>
    <td>Nama Bangun</td>
    <td>:</td>
    <td>Prisma</td>
</tr>
<tr>
    <td>Dimensi (2D/3D)</td>
    <td>:</td>
    <td>3d</td>
</tr>
<tr>
    <td>Rumus Luas</td>
    <td>:</td>
    <td>(2*luas alas) + (luas bidang tegak)</td>
</tr>
<tr>
    <td>Luas Alas</td>
    <td>:</td>
    <td>{}</td>
</tr>
""".format(luasa)
print """<tr>
    <td>Luas bidang tegak</td>
    <td>:</td>
    <td>{}</td>
</tr>
""".format(luasb)
print """<tr>
    <td>banyak sisi bidang tegak prisma?</td>
    <td>:</td>
    <td>{}</td>
</tr>
""".format(n)
print """<tr>
    <td>Luas</td>
    <td>:</td>
    <td>{}</td>
</tr>
""".format(hitung(luasa,luasb,n))
print"""
</table>"""

print"</body></html>"
