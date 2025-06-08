import json

with open('stari.json', 'r') as f:
    automat = json.load(f)

cuvant = input("Input: ")

stare = automat["start"][0]  # presupunem că avem o singură stare de start
print("Stare inițială:", stare)

for simbol in cuvant:
    gasit = False  # presupunem inițial că nu avem nicio tranziție validă

    for tranzitie in automat["routes"]:
        # Căutăm o tranziție valabilă din starea curentă cu simbolul curent
        if tranzitie["inc"] == stare and tranzitie["read"] == simbol:
            stare = tranzitie["fin"]  # trecem în starea următoare
            print(f"Citit '{simbol}' → noua stare: {stare}")
            gasit = True
            break  # ieșim din bucla de căutare, am găsit tranziția

    if not gasit:
        # Dacă nu există nicio tranziție valabilă, automatul nu poate continua
        print(f"Eroare: nu există tranziție din '{stare}' cu simbolul '{simbol}'")
        break

# Verificăm dacă am ajuns într-o stare finală
if stare in automat["final"]:
    print("Cuvânt acceptat de automat.")
else:
    print("Cuvânt respins de automat.")
