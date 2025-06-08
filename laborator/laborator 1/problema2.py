import json

with open('stari.json', 'r') as f:
    automat = json.load(f)

cuvant = input("Input: ")

if not automat["start"]:
    print("Eroare: Nu există stare de start")
    exit()
stare = automat["start"][0]
print("Stare inițială:", stare)

for simbol in cuvant:
    gasit = False  
    for tranzitie in automat["routes"]:
        if tranzitie["inc"] == stare and tranzitie["state"] == simbol:
            stare = tranzitie["fin"]  
            print(f"Citit '{simbol}' → noua stare: {stare}")
            gasit = True
            break 

    if not gasit:
        print(f"Eroare: nu există tranziție din '{stare}' cu simbolul '{simbol}'")
        break

if stare in automat["final"]:
    print("Acceptat")
else:
    print("Respins")
