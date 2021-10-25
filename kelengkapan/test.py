import atm_packs

lokasi = './nasabah.json'
dn = atm_packs.loadDataNasabah(lokasi)

while(True):
    atm_packs.atmHeader()
    while(True):
        nr = input("Masukkan No Rekening : ")
        np = input("Masukkan Pin         : ")

        cl = atm_packs.checkLogin(nr, np, dn)
        [kondisi, data] = cl

        if(kondisi == True):
            while(True):
                atm_packs.clearscreen()
                atm_packs.atmHeader()
                print("Hello -", data['nama'])
                atm_packs.menuku()
                pilih = input('Pilihan Menu : ')
                if(pilih == '1'):
                    atm_packs.clearscreen()
                    atm_packs.atmHeader()
                    jt = input("Masukkan nominal transaksi  : Rp ")
                    try:
                        jt2 = int(jt)
                        if(jt2 <= 50000):
                            print("Transfer harus lebih dari Rp 50000")
                            input("Tekan enter untuk melanjutkan transaksi")
                        else:
                            if(jt2 >= data['saldo']):
                                print("Maaf, saldo anda tidak mencukupi")
                                input("Tekan enter untuk melanjutkan transaksi")
                            else:
                                nr2 = input("Masukkan No Rekening tujuan : ")
                                if(nr2 == data['no_rekening']):
                                    print("Transfer ke nomor rekening anda tidak diperbolehkan")
                                    input("Tekan enter untuk melanjutkan transaksi")
                                else:
                                    dn3 = atm_packs.loadDataNasabah(lokasi)
                                    cekDn = atm_packs.check_DataNasabah(nr2, dn3)
                                    [kondisi2, data2] = cekDn
                                        
                                    if(kondisi2 == True):
                                        if(data2['bank'] == 'mualamat'):
                                            atm_packs.clearscreen()
                                            atm_packs.atmHeader()
                                            dn4 = atm_packs.loadDataNasabah(lokasi)
                                            idn2 = data2['id']
                                            idn3 = data['id']
                                            index_idn2 = next((index for(index, x) in enumerate(dn4) if x['id'] == idn2), None)
                                            index_idn3 = next((index for(index, y) in enumerate(dn4) if y['id'] == idn3), None)
                                            dataB = dn4[index_idn2]
                                            dataC = dn4[index_idn3]
                                            dataB1 = dn4[index_idn2]['saldo']
                                            dataC1 = dn4[index_idn3]['saldo']
                                            admin = 0
                                            jml = jt2 + admin
                                            sb2 = dataB1 + jt2
                                            sb3 = dataC1 - jml
                                            
                                            print("    Transfer ATM    ")
                                            print("Data Tujuan Transfer")
                                            print("--------------------")
                                            print("Bank Tujuan      :", data2['bank'])
                                            print("No Rekening      :", data2['no_rekening'])
                                            print("Nama Pemilik     :", data2['nama'])
                                            print("Nominal Transfer : Rp", jt2)
                                            print("Biaya Admin      : Rp", admin)
                                            print("Jumlah           : Rp", jml)
                                            pinnnn = input("Masukkan pin untuk melanjutkan transaksi : ")
                                            
                                            if(pinnnn == data['pin']):
                                                dataB['saldo'] = sb2
                                                dataC['saldo'] = sb3
                                                dn4[index_idn2] = dataB
                                                dn4[index_idn3] = dataC
                                                #atm_packs.UpdateDataNasabah(dn4, lokasi)
                                                print(dn4)
                                                print("Saldo anda saat ini : Rp", dataC['saldo'])
                                                input("Tekan enter untuk melanjutkan transaksi")
                                            else:
                                                atm_packs.clearscreen()
                                                atm_packs.atmHeader()
                                                print("Pin salah")
                                                input("Tekan enter untuk melanjutkan transaksi")
                                        else:
                                            atm_packs.clearscreen()
                                            atm_packs.atmHeader()
                                            dn4 = atm_packs.loadDataNasabah(lokasi)
                                            idn2 = data2['id']
                                            idn3 = data['id']
                                            index_idn2 = next((index for(index, x) in enumerate(dn4) if x['id'] == idn2), None)
                                            index_idn3 = next((index for(index, y) in enumerate(dn4) if y['id'] == idn3), None)
                                            dataB = dn4[index_idn2]
                                            dataC = dn4[index_idn3]
                                            dataB1 = dn4[index_idn2]['saldo']
                                            dataC1 = dn4[index_idn3]['saldo']
                                            admin = 2500
                                            jml = jt2 + admin
                                            sb2 = dataB1 + jt2
                                            sb3 = dataC1 - jml
                                            
                                            print("    Transfer ATM    ")
                                            print("Data Tujuan Transfer")
                                            print("--------------------")
                                            print("Bank Tujuan      :", data2['bank'])
                                            print("No Rekening      :", data2['no_rekening'])
                                            print("Nama Pemilik     :", data2['nama'])
                                            print("Nominal Transfer : Rp", jt2)
                                            print("Biaya Admin      : Rp", admin)
                                            print("Jumlah           : Rp", jml)
                                            pinnnn = input("Masukkan pin untuk melanjutkan transaksi : ")
                                            
                                            if(pinnnn == data['pin']):
                                                dataB['saldo'] = sb2
                                                dataC['saldo'] = sb3
                                                dn4[index_idn2] = dataB
                                                dn4[index_idn3] = dataC
                                                #atm_packs.UpdateDataNasabah(dn4, lokasi)
                                                print(dn4)
                                                print("Saldo anda saat ini : Rp", dataC['saldo'])
                                                input("Tekan enter untuk melanjutkan transaksi")
                                            else:
                                                atm_packs.clearscreen()
                                                atm_packs.atmHeader()
                                                print("Pin salah")
                                                input("Tekan enter untuk melanjutkan transaksi")
                                    else:
                                        print("Rekening tujuan tidak ditemukan")
                                        input("Tekan enter untuk melanjutkan transaksi")
                    except ValueError:
                        print("ValueError")
                        input("Tekan enter untuk melanjutkan transaksi") 
                elif(pilih == '2'):
                    atm_packs.clearscreen()
                    atm_packs.atmHeader()
                    ambil_uang = input("Masukkan nominal pengambilan : Rp ")
                    try:
                        ambil_uang2 = int(ambil_uang)

                        if(ambil_uang2 <= 50000):
                            print("Pengambilan harus lebih dari Rp 50000")
                            input("Tekan enter untuk melanjutkan transaksi")
                        else:
                            if(ambil_uang2 >= data['saldo']):
                                print("Maaf, saldo anda tidak mencukupi")
                                input("Tekan enter untuk melanjutkan transaksi")
                            else:
                                dn2 = atm_packs.loadDataNasabah(lokasi)
                                idn = data['id']
                                index_idn = next((index for(index, d) in enumerate(dn2) if d['id'] == idn), None)
                                dataA = dn2[index_idn]
                                dataA1 = dn2[index_idn]['saldo']
                                sb = dataA1 - ambil_uang2
                                dataA['saldo'] = sb
                                dn2[index_idn] = dataA
                                #atm_packs.UpdateDataNasabah(dn2, lokasi)
                                print(dn2)
                                print("Saldo anda saat ini : Rp", dataA['saldo'])
                                input("Tekan enter untuk melanjutkan transaksi")
                    except ValueError:
                        print("ValueError")
                        input("Tekan enter untuk melanjutkan transaksi")
                elif(pilih == '3'):
                    dnx = atm_packs.loadDataNasabah(lokasi)
                    idnx = data['id']
                    index_idnx = next((index for(index, z) in enumerate(dnx) if z['id'] == idnx), None)
                    print("Saldo anda saat ini : Rp", dnx[index_idnx]['saldo'])
                    input("Tekan enter untuk melanjutkan transaksi")
                elif(pilih == '4'):
                    atm_packs.clearscreen()
                    atm_packs.atmHeader()
                    break
                else:
                    print('')
        else:
            atm_packs.clearscreen()
            atm_packs.atmHeader()
            print('No rekening atau password tidak cocok')
