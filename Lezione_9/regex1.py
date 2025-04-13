'''
1. Verifica se una stringa è un numero intero

Scrivi una funzione is_integer(s) che
restituisce True se la stringa è un numero intero (positivo o negativo), False altrimenti.

Esempio:

is_integer("123")      # True
is_integer("-456")     # True
is_integer("12.3")     # False

'''

import re

def is_integer(s:str) -> bool:

    match = re.fullmatch("\d+", s)

    if match:
        return True
    else:
        return False
    

print(is_integer("2.2"))
