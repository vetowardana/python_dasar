from os import system, name

def atmHeader():
    print('=====================================================')
    print('             A T M  M U A L A M A T                  ')
    print('=====================================================')
    print()

def clearscreen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def checkLogin(user_norek, user_pin, dataset):
    loginuser = False
    dt = dataset
    for i in range (len(dt)):
        if(dt[i]['no_rekening'] == user_norek and dt[i]['pin'] == user_pin):
            loginuser =  True
            data = dt[i]
            break
        else:
            loginuser =  False
            data = ''
    
    return loginuser, data #tuple pack and unpack concept

def check_DataNasabah(no_rek, dataset):
    nasabah_tujuan = False
    dt_tujuan = ''
    dt = dataset
    for i in range (len(dt)):
        if dt[i]['no_rekening'] == no_rek:
            nasabah_tujuan = True
            dt_tujuan = dt[i]
            break
    
    return nasabah_tujuan, dt_tujuan #tuple pack and unpack concept
