'''1-4. Si scriva un programma che dato un intero di quattro cifre,
per esempio 2024, utilizzando gli opportuni operatori, lo si visualizzi, una cifra per riga:

2
0
2
4'''

numero:int = int(input("inserisci un numero a 4 cifre: "))

numero_str = str(numero)

for cifra in numero_str:
    print(cifra)