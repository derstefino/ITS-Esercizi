'''Scrivere un programma che acquisisca in input due numeri interi, n1 e n2,
e calcoli il prodotto di tutti i numeri compresi tra n1 e n2, inclusi gli estremi.

Il programma deve gestire anche il caso in cui n1 > n2, calcolando comunque il prodotto correttamente.'''

number1:int = int(input("inserisci un numero: "))

number2:int = int(input("inserisci un secondo numero: "))

prodotto:int = 1

if number1 < number2:
    for i in range(number1, number2 + 1):
        prodotto *= i
        
    print("il prodotto dei numeri compresi tra il primo e il secondo numero è: ", prodotto)

if number2 < number1:
    for i in range(number2, number1 + 1):
        prodotto *= i

    print("il prodotto dei numeri compresi tra il primo e il secondo numero è: ", prodotto)

if number1 == number2:
    prodotto *= number1

    print("il prodotto dei numeri compresi tra il primo e il secondo numero è: ", prodotto)
    
        

