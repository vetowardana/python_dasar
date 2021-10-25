import main
print("--------------------------------------------------")
print("aplikasi penghitung luas dan keliling bangun datar")
print("--------------------------------------------------")

ulang = "lanjut"
while(ulang == "lanjut"):
    print('Menu :')
    print("1. Persegi Panjang")
    print("2. Segitiga")
    print("3. Lingkaran")
    print("4. Exit")
    pilih = input("Pilih bangun datar : ")
    print('')
    
    if(pilih == "1"):
        print("------------------------")
        print("Hitung persegi panjang")
        print("------------------------")
        panjang = input("Masukkan panjang : ")
        lebar = input("Masukkan lebar : ")
        print('')
        a = float(panjang)
        b = float(lebar)

        hasil_lpp = main.luas_persegi(a, b)
        hasil_kpp = main.keliling_persegi(a, b)

        print("Luas persegi panjang :", hasil_lpp)
        print("keliling persegi panjang :", hasil_kpp)
        print('')
        ulang = "lanjut"
    elif(pilih == "2"):
        print("------------------------")
        print("Hitung segitiga")
        print("------------------------")
        alas = input("Masukkan alas : ")
        tinggi = input("Masukkan tinggi : ")
        print('')
        x = float(alas)
        y = float(tinggi)

        hasil_ls = main.luas_segitiga(x, y)
        hasil_ks = main.keliling_segitiga(x, y)

        print("Luas segitiga :", hasil_ls)
        print("keliling segitiga :", hasil_ks)
        print('')
        ulang = "lanjut"
    elif(pilih == "3"):
        print("------------------------")
        print("Hitung lingkaran")
        print("------------------------")
        radius = input("Masukkan jari-jari : ")
        print('')
        z = float(radius)

        hasil_ll = main.luas_lingkaran(z)
        hasil_kl = main.keliling_lingkaran(z)

        print("Luas lingkaran :", hasil_ll)
        print("keliling lingkaran :", hasil_kl)
        print('')
        ulang = "lanjut"
    elif(pilih == "4"):
        break
    else:
        print("Coba lagi")
        print('')
