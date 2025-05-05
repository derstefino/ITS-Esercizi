'''
Esercizio 5 – Funzione lambda con if

Crea una funzione lambda che prenda un numero e ritorni "pari" se è divisibile per 2, altrimenti "dispari".
'''

from typing import Callable

even_or_odd:Callable[[int], str] = lambda x: "pari" if x % 2 == 0 else "dispari"

print(even_or_odd(7))