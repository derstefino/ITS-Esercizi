'''

4. Verifica un CAP

Scrivi una funzione is_valid_cap(cap) che restituisce True se il CAP è valido (5 cifre), False altrimenti.

Esempio:

is_valid_cap("70124")   # True
is_valid_cap("A0123")   # False


'''

import re

def is_valid_cap(cap:str) -> bool:

    match = re.fullmatch("\d{5}", cap)

    if match:
        return True
    else:
        return False
    

print(is_valid_cap("dffff"))