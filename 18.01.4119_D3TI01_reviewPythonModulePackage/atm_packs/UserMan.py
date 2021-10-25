import json

def loadDataNasabah(filename):
    files = open(filename)

    dt = json.load(files)
    
    nasabah = []
    for i in dt['nasabah']:
        nasabah.append(i)

    files.close()    
    return nasabah

def UpdateDataNasabah(data_nasabah, filename):
    dt = {"nasabah" : data_nasabah}

    with open(filename, 'w') as f:
        json.dump(dt, f, indent=4)