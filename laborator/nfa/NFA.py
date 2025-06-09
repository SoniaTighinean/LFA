import json

def calculeaza_tranzitii_epsilon(automat, starile_curente):
    configuratie_noua = set(starile_curente)
    gasit_modificare = True
    
    while gasit_modificare:
        gasit_modificare = False
        starile_de_verificat = list(configuratie_noua)
        
        for starea_curenta in starile_de_verificat:
            # Parcurgem toate tranzițiile din automat
            for conexiune in automat["routes"]:
                # Dacă găsim o tranziție epsilon din starea curentă
                if (conexiune["inc"] == starea_curenta and 
                    conexiune["state"] == "ε"):
                    
                    # Adăugăm toate stările destinație
                    for stare_destinatie in conexiune["fin"]:
                        if stare_destinatie not in configuratie_noua:
                            configuratie_noua.add(stare_destinatie)
                            gasit_modificare = True
    
    return configuratie_noua

def proceseaza_automat(automat, secventa_intrare):
    # Pornim cu stările inițiale și aplicăm închiderea epsilon
    configuratie_actuala = calculeaza_tranzitii_epsilon(automat, set(automat["start"]))
    
    # Procesăm fiecare caracter din secvența de intrare
    for caracter in secventa_intrare:
        configuratie_temporara = set()
        
        # Pentru fiecare stare activă în configurația curentă
        for stare_activa in configuratie_actuala:
            # Verificăm toate tranzițiile posibile
            for regula in automat["routes"]:
                # Dacă găsim o tranziție cu caracterul curent
                if (regula["inc"] == stare_activa and 
                    regula["state"] == caracter):
                    # Adăugăm stările destinație
                    configuratie_temporara.update(regula["fin"])
        
        # Aplicăm închiderea epsilon pe noua configurație
        configuratie_actuala = calculeaza_tranzitii_epsilon(automat, configuratie_temporara)
    
    # Verificăm dacă am ajuns într-o stare finală
    for stare_finala in automat["final"]:
        if stare_finala in configuratie_actuala:
            return True
    
    return False

def main():

    try:
        # Încărcăm definirea automatului din fișier
        with open("NFA.json", "r") as fisier:
            definitie_automat = json.load(fisier)
            
        secventa_test = input("Input: ")
        
        # Executăm simularea
        este_acceptata = proceseaza_automat(definitie_automat, secventa_test)
        
        # Afișăm rezultatul
        if este_acceptata:
            print("Acceptat")
        else:
            print("Respins")
            
    except FileNotFoundError:
        print("EROARE: Nu s-a găsit fișierul 'NFA.json'")
    except json.JSONDecodeError:
        print("EROARE: Formatul JSON din fișier este incorect")
    except KeyError as cheie_lipsa:
        print(f"EROARE: Lipsește cheia '{cheie_lipsa}' din structura JSON")
    except Exception as eroare_generala:
        print(f"EROARE: {str(eroare_generala)}")

main()
