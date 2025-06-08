import json

def citeste_automat(nume_fisier):
    with open(nume_fisier, 'r', encoding='utf-8') as f:
        return json.load(f)

def cauta_tranzitie(automat, stare, caracter):
    for t in automat["routes"]:
        if t["inc"] == stare and t["read"] == caracter:
            return t
    return None

def aplica_tranzitie(tranzitie, stiva):
    # verific daca pot aplica tranzitia
    if tranzitie["pop"] == "ε":
        poate_aplica = True
    elif len(stiva) > 0 and stiva[-1] == tranzitie["pop"]:
        poate_aplica = True
    else:
        poate_aplica = False
    
    if poate_aplica:
        # scot din stiva
        if tranzitie["pop"] != "ε":
            stiva.pop()
        # adaug in stiva
        if tranzitie["push"] != "ε":
            stiva.append(tranzitie["push"])
        return True
    return False

# main
automat = citeste_automat('pda.json')
stare = automat["start"]
stiva = []

# epsilon move initial
tranzitie_epsilon = cauta_tranzitie(automat, stare, "ε")
if tranzitie_epsilon:
    if aplica_tranzitie(tranzitie_epsilon, stiva):
        stare = tranzitie_epsilon["fin"]

cuvant = input("Introduceti sirul: ")

# procesez cuvantul
i = 0
while i < len(cuvant):
    caracter = cuvant[i]
    tranzitie = cauta_tranzitie(automat, stare, caracter)
    
    if tranzitie and aplica_tranzitie(tranzitie, stiva):
        stare = tranzitie["fin"]
        i += 1
    else:
        print("Respins")
        exit()

# epsilon move final
tranzitie_epsilon = cauta_tranzitie(automat, stare, "ε")
if tranzitie_epsilon and len(stiva) > 0:
    if stiva[-1] == tranzitie_epsilon["pop"]:
        stiva.pop()
        stare = tranzitie_epsilon["fin"]

# verific acceptarea
acceptat = stare in automat["final"] and len(stiva) == 0
print("Acceptat" if acceptat else "Respins")
