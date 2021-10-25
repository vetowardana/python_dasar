import math

#Fungsi luas & keliling persegi panjang
def luas_persegi(panjang, lebar):
    return panjang * lebar
def keliling_persegi(panjang, lebar):
    return 2 * (panjang + lebar)

#Fungsi luas & keliling segitiga
def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi
def keliling_segitiga(alas, tinggi):
    sisi_x = math.sqrt((alas**2) + (tinggi**2))
    return alas + tinggi + sisi_x

#Fungsi luas & keliling lingkaran
def luas_lingkaran(radius):
    return math.pi * (radius ** 2)
def keliling_lingkaran(radius):
    return 2 * math.pi * radius
