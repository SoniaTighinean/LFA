import json
import sys

# Funcția care aplică toate tranzițiile ε (epsilon) posibile începând dintr-o stare dată
# Ne folosim de acest mecanism pentru a simula comportamentul nedeterminist al PDA-ului
def aplica_tranzitii_epsilon(automat, stare, stiva):
    while True:
        gasit = False  # Ne oprim doar când nu mai putem aplica nicio tranziție ε
        for tranzitie in automat["routes"]:
            if tranzitie["inc"] == stare and tranzitie["read"] == "ε":
                # Verificăm dacă trebuie să scoatem ceva din stivă (sau nu)
                if tranzitie["pop"] == "ε" or (stiva and stiva[-1] == tranzitie["pop"]):
                    # Scoatem de pe stivă dacă e cazul
                    if tranzitie["pop"] != "ε":
                        stiva.pop()
                    # Punem pe stivă dacă e cazul
                    if tranzitie["push"] != "ε":
                        stiva.append(tranzitie["push"])
                    # Ne mutăm în noua stare
                    stare = tranzitie["fin"]
                    gasit = True
                    break
        if not gasit:
            break  # Ne oprim dacă nu mai există tranziții epsilon aplicabile
    return stare, stiva

# Citim configurația automatului PDA din fișierul pda.json
with open('pda.json', 'r', encoding='utf-8') as fisier:
    automat = json.load(fisier)

# Unele fișiere folosesc "start": "q0", altele "start": ["q0"]
# Codul de mai jos gestionează ambele variante
stare = automat["start"] if isinstance(automat["start"], str) else automat["start"][0]
stiva = []  # Inițial, stiva este goală

# Aplicăm toate tranzițiile ε posibile din starea inițială (ex: punem simbolul $ pe stivă)
stare, stiva = aplica_tranzitii_epsilon(automat, stare, stiva)

# Citim șirul de intrare de la utilizator
sir_intrare = input("Introduceți șirul: ")

# Parcurgem fiecare simbol din șirul de intrare
for simbol in sir_intrare:
    potrivit = False  # Ne ajută să știm dacă am găsit o tranziție validă
    for tranzitie in automat["routes"]:
        # Găsim o tranziție care se potrivește cu simbolul curent și stiva
        if tranzitie["inc"] == stare and tranzitie["read"] == simbol:
            if tranzitie["pop"] == "ε" or (stiva and stiva[-1] == tranzitie["pop"]):
                # Gestionăm scoaterea din stivă (dacă e cazul)
                if tranzitie["pop"] != "ε":
                    stiva.pop()
                # Gestionăm adăugarea pe stivă (dacă e cazul)
                if tranzitie["push"] != "ε":
                    stiva.append(tranzitie["push"])
                # Ne mutăm în noua stare
                stare = tranzitie["fin"]
                # Aplicăm și eventualele tranziții epsilon care decurg din asta
                stare, stiva = aplica_tranzitii_epsilon(automat, stare, stiva)
                potrivit = True
                break  # Nu mai căutăm altă tranziție pentru acest simbol
    if not potrivit:
        # Dacă niciuna dintre tranziții nu s-a putut aplica, automatul respinge cuvântul
        print("Respins")
        sys.exit()

# După ce am parcurs tot șirul, mai verificăm o dată dacă putem aplica tranziții ε
stare, stiva = aplica_tranzitii_epsilon(automat, stare, stiva)

# Automat acceptă dacă ajunge într-o stare finală și stiva este complet goală
if stare in automat["final"] and not stiva:
    print("Acceptat")
else:
    print("Respins")
