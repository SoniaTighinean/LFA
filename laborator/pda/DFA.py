import json


with open('dfa.json', 'r') as f:
    dfa = json.load(f)

# Starea inițială
starea_curenta = dfa["start"]

sir = input("Input: ")

# Parcurgem fiecare caracter din șir
for caracter in sir:
    # Căutăm tranziția corespunzătoare
    tranzitie_gasita = False
    
    for ruta in dfa["routes"]:
        if ruta["inc"] == starea_curenta and ruta["read"] == caracter:
            starea_curenta = ruta["fin"]
            tranzitie_gasita = True
            break
    
    # Dacă nu găsim tranziția, șirul nu e acceptat
    if not tranzitie_gasita:
        print("Respins")
        exit()

# Verificăm dacă starea finală e în lista de stări finale
if starea_curenta in dfa["final"]:
    print("Acceptat")
else:
    print("Respins")
