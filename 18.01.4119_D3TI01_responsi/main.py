import package
fileloc = "./history.json"

while(True):
    package.clearscreen()
    package.appHeader()
    package.menuku()
    pilihan = input("Pilih menu : ")
    print('')

    if(pilihan == '1'):
        data = package.loadDataHistory(fileloc)
        if(not data):
            print("Data history")
            print(96*"=")
            print("|{:<15}|{:<15}|{:<15}|{:<20}|{:<25}|".format('Nama', 'Tinggi Badan', 'Berat Badan', 'Besaran BMI', 'Status Berat'))
            print(96*"=")
            print("|No data history available                                                                     |")
            print(96*"=")
        else:
            print("Data history")
            print(96*"=")
            print("|{:<15}|{:<15}|{:<15}|{:<20}|{:<25}|".format('Nama', 'Tinggi Badan', 'Berat Badan', 'Besaran BMI', 'Status Berat'))
            print(96*"=")
            
            for i in range(len(data)) :
                print("|{:<15}|{:<7}cm      |{:<7}kg      |{:<20}|{:<25}|".format(data[i]['nama'], data[i]['tinggi'], data[i]['berat'], data[i]['bmi'], data[i]['status']))
            print(96*"=")
        input("Tekan enter untuk melanjutkan")
        package.clearscreen()
    elif(pilihan == '2'):
        print("Hapus data berdasarkan nama")
        print("---------------------------")
        datax = package.loadDataHistory(fileloc)
        namax = input("Masukkan nama : ")
        try:
            index = next((index for(index, b) in enumerate(datax) if b['nama'] == namax), None)
            del datax[index]
            package.UpdateDataHistory(datax, fileloc)
            print("Data berhasil dihapus")
            input("Tekan enter untuk melanjutkan")
        except TypeError:
            print('Data tidak ditemukan')
            input("Tekan enter untuk melanjutkan")
        package.clearscreen()
    elif(pilihan == '3'):
        ulang = True
        while(ulang == True):
            package.clearscreen()
            package.appHeader()
            data2 = package.loadDataHistory(fileloc)
            nama = input("Masukkan nama lengkap anda      = ")
            tb = input("Masukkan tinggi badan anda (cm) = ")
            bb = input("Masukkan berat badan anda (kg)  = ")
            print('')
            try:
                tb2 = float(tb)
                try:
                    berat = float(bb)
                    
                    tinggi = (tb2/100)**2
                    hasil = berat/tinggi
                    
                    if(hasil < 18.5):
                        status = "Kekurangan berat badan"
                        print("Hasilnya :")
                        print("Status Berat : ", status)
                        print("Besaran BMI  : ", hasil)
                        x = {'nama' : nama,
                             'tinggi' : tb2,
                             'berat' : berat,
                             'bmi' : hasil,
                             'status' : status}
                        data2.append(x)
                        package.UpdateDataHistory(data2, fileloc)
                    elif(hasil >= 18.5 and hasil <= 24.9):
                        status = "Normal (ideal)"
                        print("Hasilnya :")
                        print("Status Berat : ", status)
                        print("Besaran BMI  : ", hasil)
                        x = {'nama' : nama,
                             'tinggi' : tb2,
                             'berat' : berat,
                             'bmi' : hasil,
                             'status' : status}
                        data2.append(x)
                        package.UpdateDataHistory(data2, fileloc)
                    elif(hasil >= 25.0 and hasil <= 29.9):
                        status = "Kelebihan berat badan"
                        print("Hasilnya :")
                        print("Status Berat : ", status)
                        print("Besaran BMI  : ", hasil)
                        x = {'nama' : nama,
                             'tinggi' : tb2,
                             'berat' : berat,
                             'bmi' : hasil,
                             'status' : status}
                        data2.append(x)
                        package.UpdateDataHistory(data2, fileloc)
                    else:
                        status = "Kegemukan (obesitas)"
                        print("Hasilnya :")
                        print("Status Berat : ", status)
                        print("Besaran BMI  : ", hasil)
                        x = {'nama' : nama,
                             'tinggi' : tb2,
                             'berat' : berat,
                             'bmi' : hasil,
                             'status' : status}
                        data2.append(x)
                        package.UpdateDataHistory(data2, fileloc)
                except ValueError:
                    print('ValueError')
            except ValueError:
                print('ValueError')
            a = "b"
            while(a == "b"):
                ulangi = input("Apakah akan mengulang perhitungan (y/n)? : ")
                if(ulangi == 'n'):
                    ulang = False
                    break
                    package.clearscreen()
                elif(ulangi == 'y'):
                    ulang = True
                    break
                    package.clearscreen()
                else:
                    a = "b"
    elif(pilihan == '4'):
        break
    else:
        package.clearscreen()
