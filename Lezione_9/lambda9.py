'''
Esercizio 9 – Ritorna una lambda

Scrivi una funzione moltiplicatore(n

) che ritorni una lambda che moltiplica un valore per n.

Esempio d'uso:

per_due = moltiplicatore(2)
print(per_due(10))  # Output: 20
'''

from typing import Callable

def moltiplicatore(n:int) -> Callable:

    result:Callable[[int], int] = lambda x: x*n

    return result


per_due = moltiplicatore(2)

print(per_due(10))


