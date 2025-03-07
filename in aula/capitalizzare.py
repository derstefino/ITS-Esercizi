'''l'utente inserisce una stringa contenente almeno uno spazio e 
dobbiamo stampare una stringa che è come la prima ma con lettere maiuscole a ogni parola'''




insert_string:str = str(input("inserisci una stringa con almeno uno spazio: "))

inverted:str = ""

print(insert_string.title())

insert_string.title()

'''stampare le ultime lettere maiuscole'''

for i in range(len(insert_string)):
    inverted = insert_string[i] + inverted

inverted = inverted.title()

reinverted:str = ""

for i in range(len(inverted)):
    reinverted = inverted[i] + reinverted

print(reinverted)

'''string into list'''

insert_string = insert_string.split()

cap_list:list = [] 

for word in insert_string:
    cap_list.append(word.capitalize())

print(*cap_list)

