

### DFA (Deterministic Finite Automaton)
- `laborator/dfa/DFA.py` - implementarea principală
- `laborator/dfa/dfa.json` - definirea automatului

**Ce face:** Simulează un automat finit determinist care acceptă stringuri binare cu un număr par de zerouri.

**Cum funcționează:**
- Citește definirea automatului din JSON
- Parcurge caracterele din string
- Verifică tranzițiile și acceptă/respinge stringul

### NFA (Nondeterministic Finite Automaton)  
- `laborator/nfa/NFA.py` - implementarea principală
- `laborator/nfa/NFA.json` - definirea automatului

**Ce face:** Simulează un automat finit nedeterminist cu tranzițiile epsilon.

**Funcționalități:**
- Calculează închiderea epsilon pentru stări
- Gestionează configurații multiple de stări
- Acceptă un string dacă există cel puțin un drum de acceptare

### PDA (Pushdown Automaton)
- `laborator/pda/PDA.py` - implementarea principală  
- `laborator/pda/pda.json` - definirea automatului

**Ce face:** Simulează un automat cu stivă care recunoaște limbajul {0^n 1^n | n ≥ 1}.

**Componente:**
- Stivă pentru memorarea simbolurilor
- Tranzițiile epsilon pentru inițializare și finalizare
- Verificare că stiva este goală la sfârșitul procesării

## Cum să rulezi

Pentru fiecare tip de automat:

```bash
cd laborator/dfa
python DFA.py

cd laborator/nfa  
python NFA.py

cd laborator/pda
python PDA.py
```

Introduci stringul de test când ești întrebat.

## Exemple de teste

**DFA:** 
- `1010` → Acceptat (2 zerouri - par)
- `101` → Respins (1 zero - impar)

**NFA:**
- `10` → Acceptat  
- `01` → Respins

**PDA:**
- `0011` → Acceptat (2 zerouri urmate de 2 unuri)
- `001` → Respins (numărul de zerouri ≠ numărul de unuri)

## Format JSON

Fiecare automat folosește o structură JSON standardizată cu:
- `states` - lista stărilor
- `sigma` - alfabetul de intrare  
- `routes` - tranzițiile
- `start` - starea inițială
- `final` - stările finale

Pentru PDA se adaugă și `stack_symbols` pentru simbolurile stivei.

