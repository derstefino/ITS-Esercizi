'''Esercizio 1. 

Scrivere in Python una funzione recursivePower che calcola la potenza di un numero utilizzando la ricorsione.
La funzione deve ricevere due parametri in input:

    base: il numero da elevare a potenza.
    exponent: l’esponente a cui elevare la base.

Utilizzare, poi, la funzione per calcolare:

    3⁴, ovvero 3 elevato alla potenza di 4. 
    4^3 , ovvero 4 elevato alla potenza di 3.
    2^5, ovvero 2 elevato alla potenza di 5. 
    5^2, ovvero 5 elevato alla potenza di 2.
'''

def recursivePower(base:int, exp:int):

    if base==0:
        return 0
    if exp==0:
        return 1
    if exp==1:
        return base
    if exp > 1:
        return base*recursivePower(base, exp - 1)
    

print(recursivePower(5,2))