'''
Esercizio 7 – Filtra parole corte

Hai una lista di parole parole = ["cane", "gatto", "elefante", "ratto", "orso"]
Estrai solo le parole con più di 4 lettere usando filter() e lambda.

'''

words:list = ["cane", "gatto", "elefante", "ratto", "orso"]

more_than_four_letters:list = list(filter(lambda x: len(x)>4, words))

print(more_than_four_letters)