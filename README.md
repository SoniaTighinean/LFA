
## Laborator 1 - Introducere si DFA de baza
### Problema 1 - Lucru cu matrici
- **problema1.py** - Program care citeste o matrice dintr-un fisier text, o valideaza (verifica daca toate liniile au aceeasi lungime) si o scrie in alt fisier
- **matrice.txt** - fisierul de input cu matricea 3x3
- **iesire.txt** - fisierul de output
- Programul are error handling pentru fisiere inexistente si matrici invalide

### Problema 2 - DFA simplu  
- **problema2.py** - Primul meu automat finit determinist care accepta cuvinte
- **stari.json** - JSON cu definitia automatului (2 stari: q0, q1)
- Automatul accepta cuvinte care au un numar impar de simboluri (0 sau 1)
- Citeste caracter cu caracter si schimba starea, la final verifica daca e in stare finala

## Laborator 2 - NFA (Automate Nedeterministe)
- **NFA.py** - Implementare completa pentru automate nedeterministe cu tranzitii epsilon
- **NFA.json** - Definitia automatului cu 3 stari (q0, q1, q2)
- Am implementat functia pentru epsilon-closure care calculeaza toate starile accesibile prin tranzitii epsilon
- Algoritmul parcurge toate starile posibile in paralel si verifica la final daca macar una e finala

## Laborator 3 - PDA (Automate cu Stiva)
- **PDA.py** - Automat pushdown care recunoaste limbajul 0^n1^n (acelasi numar de 0-uri si 1-uri)
- **pda.json** - Definitia cu 4 stari si operatii pe stiva (push/pop)
- Algoritmul:
  1. Pune $ pe stiva la inceput (epsilon move)
  2. Pentru fiecare 0 citit, pune un 0 pe stiva  
  3. Pentru fiecare 1 citit, scoate un 0 de pe stiva
  4. La final scoate $ si ajunge in starea finala

## Laborator 4 - DFA (Automat Finit Determinist)
- **DFA.py** - Implementare clasica de DFA, mai simpla decat NFA
- **dfa.json** - Automat cu 2 stari care accepta cuvinte cu numar par de 0-uri
- Algoritmul e direct: citeste caracter, gaseste tranzitia corespunzatoare, schimba starea

## Cum rulez programele:

### Pentru matrici (Lab 1):
```bash
python problema1.py
# Citeste din matrice.txt si scrie in iesire.txt
```

### Pentru automate (Lab 1, 2, 3, 4):
```bash
python problema2.py
# Input: 101 (exemplu)
# Output: Acceptat/Respins

python NFA.py  
# Input: 01 (exemplu)
# Output: Acceptat/Respins

python PDA.py
# Input: 0011 (exemplu pentru 0^n1^n)
# Output: Acceptat/Respins

python DFA.py
# Input: 00 (exemplu pentru numar par de 0-uri)
# Output: Acceptat/Respins
```

## Structura fisierelor JSON:
Toate automatele sunt definite in JSON cu urmatoarele campuri:
- `states` - lista cu toate starile
- `sigma` - alfabetul (simbolurile acceptate)  
- `routes` - tranzitiile (inc=stare_initiala, fin=stare_finala)
- `start` - starea initiala
- `final` - lista cu starile finale

Pentru PDA mai am si:
- `stack_symbols` - simbolurile care pot fi pe stiva
- `read`, `pop`, `push` - operatii pentru fiecare tranzitie

## Note:
- Toate programele citesc input de la tastatura
- Fisierele JSON contin definitiile automatelor  
- Pentru PDA trebuie sa ai grija ca stiva sa fie goala la final
