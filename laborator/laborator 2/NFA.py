import json

def inchidere_epsilon(nfa, stari):
    rezultat = set(stari)
    schimbat = True

    while schimbat:
        schimbat = False
        # Iterează peste o copie a setului pentru a permite modificarea lui în timpul iterației
        for stare in list(rezultat):
            for tranzitie in nfa["routes"]:
                # Verifică dacă tranziția este o tranziție epsilon dintr-o stare activă
                if tranzitie["inc"] == stare and tranzitie["state"] == "ε":
                    for destinatie in tranzitie["fin"]:
                        if destinatie not in rezultat:
                            rezultat.add(destinatie)
                            schimbat = True # Setează la True dacă s-au adăugat stări noi, pentru a continua bucla
    return rezultat

def simuleaza_nfa(nfa, cuvant):
    # Inițializează setul de stări active cu închiderea epsilon a stărilor de start
    stari_active = inchidere_epsilon(nfa, set(nfa["start"]))

    # Procesează fiecare simbol din cuvântul de intrare
    for simbol_curent in cuvant:
        stari_urmatoare = set()
        for stare_din_set in stari_active:
            for regula_tranzitie in nfa["routes"]:
                # Caută toate tranzițiile posibile din stările active pentru simbolul curent
                if regula_tranzitie["inc"] == stare_din_set and regula_tranzitie["state"] == simbol_curent:
                    stari_urmatoare.update(regula_tranzitie["fin"])
        
        # Aplică închiderea epsilon pe noile stări obținute, pentru a include și tranzițiile spontane
        stari_active = inchidere_epsilon(nfa, stari_urmatoare)
    
    # Cuvântul este acceptat dacă cel puțin o stare finală este atinsă după procesarea întregului cuvânt
    return any(stare_finala in nfa["final"] for stare_finala in stari_active)


try:
    with open("NFA.json", "r", encoding='utf-8') as f:
        automat_nfa = json.load(f)
    
    cuvant_intrare = input("Input: ")
    
    rezultat_simulare = simuleaza_nfa(automat_nfa, cuvant_intrare)
    
    print("ACCEPTAT" if rezultat_simulare else "RESPINS")

except FileNotFoundError:
    print("Eroare: Fișierul 'NFA.json' nu a fost găsit!")
except json.JSONDecodeError:
    print("Eroare: Fișierul JSON nu este valid!")
except KeyError as e:
    print(f"Eroare: Cheia {e} lipsește din structura JSON!")
except Exception as e:
    print(f"Eroare neașteptată: {e}")
