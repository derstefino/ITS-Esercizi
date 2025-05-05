'''
Esercizio 6 – Uso con reduce()

Usa reduce() (dal modulo functools) e una lambda per calcolare il prodotto di tutti gli elementi di una lista numeri = [2, 3, 4].
'''

from functools import reduce

nums:list = [2, 3, 4]

def add(x, y):
    return x + y

print(reduce(add, nums))