def citeste_matrice(nume_fisier):
    try:
        with open(nume_fisier, 'r') as fisier:
            continut = fisier.readlines()
    except FileNotFoundError:
        print(f"[Eroare] Fișierul '{nume_fisier}' nu a fost găsit.")
        return None

    matrice = []
    for linie in continut:
        try:
            valori = list(map(int, linie.strip().split()))
            matrice.append(valori)
        except ValueError:
            print(f"[Eroare] Linia invalidă: '{linie.strip()}'")
            return None

    if len(matrice) == 0:
        print("[Eroare] Fișierul este gol sau nu conține date valide.")
        return None

    lungime_linie = len(matrice[0])
    for linie in matrice:
        if len(linie) != lungime_linie:
            print("[Eroare] Liniile nu au aceeași lungime. Nu este o matrice.")
            return None

    return matrice


def scrie_matrice(fisier_destinatie, matricea):
    if matricea is None:
        return

    try:
        with open(fisier_destinatie, 'w') as fout:
            for linie in matricea:
                fout.write(' '.join(map(str, linie)) + '\n')
    except IOError:

        print(f"[Eroare] Nu s-a putut scrie în fișierul '{fisier_destinatie}'.")


mat = citeste_matrice('matrice.txt')  
if mat:
    print("Matrice citită:")
    for linie in mat:
        print(linie)
    scrie_matrice('iesire.txt', mat)  
