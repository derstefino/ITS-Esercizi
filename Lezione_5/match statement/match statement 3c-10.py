'''
Esercizio 3C-10. Scrivere un programma in Python che permetta all'utente di inserire una data (giorno e mese espressi in forma numerica),
salvi la data in una tupla e utilizzi un match statement per verificare se la data corrisponde a una festività o a un evento speciale:

- Capodanno → 1 Gennaio → "Capodanno"
- San Valentino → 14 Febbraio → "San Valentino"
- Festa della Repubblica Italiana → " Giugno → "Festa della Repubblica Italiana"
- Ferragosto → 15 Agosto → "Ferragosto"
- Halloween → 31 Ottobre → "Halloween"
- Natale → 25 Dicembre → "Natale"
- Altro caso → "Nessuna festività importante in questa data."

Expected Output:

Inserisci il giorno: 25
Inserisci il mese: 12
Output: Il 25/12 è Natale!

- - - - - - - - - - - - - - -

Inserisci il giorno: 5
Inserisci il mese: 3
Output: Nessuna festività importante in questa data.
'''



date_tuple: tuple[int, int] = (int(input("Inserisci il giorno: ")), int(input("Inserisci il mese: ")))

g,m = date_tuple

while not(g>=1 and g<32 and m>=1 and m <13):
         print("Inserisci una data valida")
         date_tuple: tuple[int, int] = (int(input("Inserisci il giorno: ")), int(input("Inserisci il mese: ")))
         g,m = date_tuple
         
         

match date_tuple:
                case 1,1:
                    print(f"Il {g}/{m} è Capodanno")
                case 14,2:
                    print(f"Il {g}/{m} è San Valentino")
                case 2,6:
                    print(f"Il {g}/{m} è la Festa della Repubblica Italiana")
                case 15,8:
                    print(f"Il {g}/{m} è Ferragosto")
                case 31,10:
                    print(f"Il {g}/{m} è Halloween")
                case 25,12:
                    print(f"Il {g}/{m} è Natale")
                case _:
                    print("Nessuna festività importante in questa data.")






