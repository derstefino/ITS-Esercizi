'''
Esercizio 4 – Ordinamento con sorted()

Hai una lista di tuple studenti = [("Luca", 21), ("Anna", 19), ("Marco", 22)].
Ordina la lista in base all’età (secondo elemento) usando sorted() e lambda.
'''

students:list = [("Luca", 21), ("Anna", 19), ("Marco", 22)]

sorted_by_age:list = sorted(students, key=lambda x: x[1])

print(sorted_by_age)