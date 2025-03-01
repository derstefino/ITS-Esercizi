'''Scrivere un programma che consenta all'utente di inserire una sequenza di numeri reali non negativi (sia interi che decimali).
L'inserimento termina quando viene fornito un numero negativo, che funge da sentinella e non deve essere considerato nei calcoli.

Il programma deve:

    Calcolare la media dei soli numeri interi inseriti. Utilizzate la funzione is_integer() per verificare se il numero inserito è un intero.
    Determinare e visualizzare il numero più grande e il numero più piccolo tra tutti quelli inseriti (sia interi che decimali).
'''


number:float = float(input("inserisci un numero: "))

sum_int:int = 0
count_int:int = 0

if number < 0:
        number:float = float(input("inserisci un numero positivo: "))

max:int = number
min:int = number

while number >=0:

    if number.is_integer:
        sum_int += number
        count_int += 1

    if number < min:
         min = number
    if number > max:
         max = number

    number:float = float(input("inserisci un altro numero: "))

print("il numero più grande è: ", max)
print("il numero più piccolo è: ", min)
media = sum_int / count_int
print("la media tra gli interi è: ", media)