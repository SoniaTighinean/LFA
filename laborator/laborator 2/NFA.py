import json  # pentru a încărca fișierul NFA.json

# Funcție care calculează închiderea epsilon pentru un set de stări
def inchidere_epsilon(nfa, stari):
    rezultat = set(stari)  # inițial, închidem doar stările primite
    schimbat = True

    # Repetăm cât timp mai adăugăm stări noi în închidere
    while schimbat:
        schimbat = False
        for stare in list(rezultat):
            for tranzitie in nfa["routes"]:
                # Dacă există o tranziție ε din starea curentă
                if tranzitie["inc"] == stare and tranzitie["state"] == "ε":
                    # CORECTARE: Gestionăm corect array-ul din "fin"
                    for destinatie in tranzitie["fin"]:
                        if destinatie not in rezultat:
                            rezultat.add(destinatie)
                            schimbat = True  # reluăm ciclul cu noile stări

    return rezultat

# Simulează rularea unui cuvânt pe automatul nedeterminist cu epsilon
def simuleaza_nfa(nfa, cuvant):
    # Începem cu închiderea epsilon a stărilor de start
    stari = inchidere_epsilon(nfa, set(nfa["start"]))
    print("Stări inițiale cu închidere ε:", stari)

    # Parcurgem fiecare simbol din cuvânt
    for simbol in cuvant:
        urmatoare = set()
        print(f"Simbol citit: '{simbol}'")

        for stare in stari:
            for tranzitie in nfa["routes"]:
                # Dacă există o tranziție validă cu simbolul curent
                if tranzitie["inc"] == stare and tranzitie["state"] == simbol:
                    print(f"  Din {stare} cu '{simbol}' → {tranzitie['fin']}")
                    # CORECTARE: Gestionăm corect array-ul din "fin"
                    urmatoare.update(tranzitie["fin"])  # adăugăm toate destinațiile

        # Aplicăm închiderea epsilon din nou pe stările obținute
        stari = inchidere_epsilon(nfa, urmatoare)
        print("Stări active după închidere ε:", stari)

    # Verificăm dacă am ajuns într-o stare finală
    return any(stare in nfa["final"] for stare in stari)

# Funcție auxiliară pentru debugging - afișează structura automatului
def afiseaza_automat(nfa):
    print("=== Structura automatului ===")
    print(f"Stări: {nfa['states']}")
    print(f"Alfabet: {nfa['sigma']}")
    print(f"Stări de start: {nfa['start']}")
    print(f"Stări finale: {nfa['final']}")
    print("Tranziții:")
    for tranzitie in nfa["routes"]:
        print(f"  {tranzitie['inc']} --{tranzitie['state']}--> {tranzitie['fin']}")
    print("=" * 30)

# Citim automatul din fișierul JSON
try:
    with open("nfa.json", "r", encoding='utf-8') as f:
        nfa = json.load(f)
    
    # Afișăm structura pentru debugging
    afiseaza_automat(nfa)
    
    # Cerem utilizatorului să introducă un cuvânt
    cuvant = input("Introdu cuvântul: ")
    
    # Apelăm funcția de simulare și afișăm rezultatul
    rezultat = simuleaza_nfa(nfa, cuvant)
    print("\n" + "="*20)
    print("ACCEPTAT" if rezultat else "RESPINS")
    print("="*20)

except FileNotFoundError:
    print("Eroare: Fișierul 'NFA.json' nu a fost găsit!")
except json.JSONDecodeError:
    print("Eroare: Fișierul JSON nu este valid!")
except KeyError as e:
    print(f"Eroare: Cheia {e} lipsește din structura JSON!")
except Exception as e:
    print(f"Eroare neașteptată: {e}")
