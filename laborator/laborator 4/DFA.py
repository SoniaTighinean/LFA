import json
import sys

# Deschidem fișierul dfa.json și încărcăm configurația automatului
with open('dfa.json', 'r', encoding='utf-8') as fisier:
    dfa = json.load(fisier)

# Inițializăm starea curentă. Automat acceptă fie "start": "q0", fie "start": ["q0"]
# Aici verificăm tipul și extragem corect valoarea
stare = dfa["start"] if isinstance(dfa["start"], str) else dfa["start"][0]

# Citim șirul de intrare de la utilizator
sir_intrare = input("Introduceți șirul: ")

# Parcurgem caracter cu caracter
for simbol in sir_intrare:
    gasit = False  # Presupunem că nu există tranziție pentru simbolul curent
    for tranzitie in dfa["routes"]:
        # Căutăm o tranziție validă din starea curentă pentru simbolul actual
        if tranzitie["inc"] == stare and tranzitie["read"] == simbol:
            # Trecem în starea următoare conform tranziției
            stare = tranzitie["fin"]
            gasit = True
            break
    if not gasit:
        # Dacă nu am găsit nicio tranziție validă, automatul respinge cuvântul
        print("Respins — simbol necunoscut sau fără tranziție validă.")
        sys.exit()

# La final, verificăm dacă starea curentă este o stare finală
if stare in dfa["final"]:
    print("Acceptat")
else:
    print("Respins")
