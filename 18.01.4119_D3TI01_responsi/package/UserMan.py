import json

def loadDataHistory(filename):
    files = open(filename)

    dt = json.load(files)
    
    history = []
    for i in dt['history']:
        history.append(i)

    files.close()    
    return history

def UpdateDataHistory(data_history, filename):
    dt = {"history" : data_history}

    with open(filename, 'w') as f:
        json.dump(dt, f, indent=4)