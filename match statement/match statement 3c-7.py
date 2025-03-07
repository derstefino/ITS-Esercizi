'''
Esercizio 3C-7. Si scriva un programma in python che computi la statistica di otto lanci di una moneta.
Per ciascuno dei lanci effettuati, l'utente inserisce "t" o "T" se è uscito "testa", mentre inserisce "c" o "C" se è uscito "croce".
Il programma deve mostrare in output il numero totale e la percentuale dei risultati "testa" e "croce".

NOTA.
Le percentuali devono essere mostrate in output obbligatoriamente con 2 cifre decimali.
Usare il match statement.

Expected Output:

Per ciascun lancio della moneta inserisci "t" o "T" se e' uscito "testa" mentre inserisci "c" o "C" se e' uscito "croce".

Lancio 1: t
Lancio 2: c
Lancio 3: t
Lancio 4: t
Lancio 5: c
Lancio 6: c
Lancio 7: t
Lancio 8: t

Totale "testa": 5
Percentaule "testa": 62.50%

Totale "croce": 3
Percentuale "croce": 37.50%
'''

count:int = 0

teste:list[str] = []

croci:list[str] = []

while count < 8:


    lancio:str = str(input("Per ciascun lancio della moneta inserisci 't' o 'T' se è uscito 'testa' mentre inserisci 'c' o 'C' se e' uscito 'croce':" ))


    match lancio:
        case "t" | "T":
            teste.extend(lancio)
            count += 1

        case "c"|"C":
           croci.extend(lancio)
           count += 1
        case _:
            print("per favore inserisci T oppure C")      

        


    
numeroTeste:int = len(teste)
numeroCroci:int = len(croci)
print(f"Totale 'testa': {len(teste)}")
print(f"Percentuale 'testa': {((len(teste)/8)*100):.2f}%")

print(f"Totale 'croce': {len(croci)}")
print(f"Percentuale 'croce': {((len(croci)/8)*100):.2f}%")



