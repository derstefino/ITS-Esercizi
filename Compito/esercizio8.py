'''Un'applicazione interessante dei computer è la rappresentazione grafica di dati.
Scrivere un programma che acquisisca cinque numeri interi (ognuno compreso tra 1 e 30)
e visualizzi in output un grafico a barre testuale con asterischi *.

Per ogni numero letto, il programma deve stampare una riga contenente tanti asterischi quanti il valore del numero stesso.'''

list_five_integers:list = [int(input()), int(input()), int(input()), int(input()), int(input())]

star:int = "*"
stars0:str = ""
stars1:str = ""
stars2:str = ""
stars3:str = ""
stars4:str = ""

for i in range(list_five_integers[0]):
    stars0 += star

print(stars0)

for i in range(list_five_integers[1]):
    stars1 += star

print(stars1)

for i in range(list_five_integers[2]):
    stars2 += star

print(stars2)

for i in range(list_five_integers[3]):
    stars3 += star

print(stars3)

for i in range(list_five_integers[4]):
    stars4 += star

print(stars4)