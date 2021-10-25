import atm_packs

lokasi = './nasabah.json'
dn = atm_packs.loadDataNasabah(lokasi)

while(True):
    atm_packs.atmHeader()
    
    nr = input("Masukkan No Rekening : ")
    np = input("Masukkan Pin         : ")

    cl = atm_packs.checkLogin(nr, np, dn)
    [kondisi, data] = cl

    if(kondisi == True):
        while(True):
            print("Hello -", data['nama'])
            print('')
            print('1. Transfer')
            print('2. Tarik Tunai')
            print('3. Cek Saldo')
            print('4. Keluar')
            print('-----------------------------------------------------')
            pilih = input('Pilihan Menu : ')

            if(pilih == '1'):
                print("Sedang dibangun")
            elif(pilih == '2'):
                ambil_uang = input("Masukkan nominal pengambilan : ")
                ambil_uang2 = int(ambil_uang)

                if(ambil_uang2 >= data['saldo']):
                    print("Maaf, saldo anda tidak mencukupi")
                    input("Tekan enter untuk melanjutkan transaksi")
                else:
                    dn2 = atm_packs.loadDataNasabah(lokasi)
                    idn = data['id']
                    index_idn = next((index for(index, d) in enumerate(dn2) if d['id'] == idn), None)
                    sb = data['saldo'] - ambil_uang2
                    data['saldo'] = sb
                    print("Saldo anda saat ini :", data['saldo'])
                    dn2[index_idn] = data
                    input("Tekan enter untuk melanjutkan transaksi")
                    atm_packs.UpdateDataNasabah(dn2, lokasi)
            elif(pilih == '3'):
                print("Saldo anda saat ini :", data['saldo'])
                input("Tekan enter untuk melanjutkan transaksi")
            elif(pilih == '4'):
                break
            else:
                print('')
    else:
        print('failed')
