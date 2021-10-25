from os import system, name

def appHeader():
    print('=====================================================')
    print('          B M I  M E A S U R E M E N T               ')
    print('=====================================================')
    print()

def menuku():
    print("Menu :")
    print("1. Lihat History")
    print("2. Hapus Data Berdasarkan Nama")
    print("3. Ukur BMI")
    print("4. Exit")
    print('---------------------------------')

def clearscreen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


