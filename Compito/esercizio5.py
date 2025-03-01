'''Si supponga di poter acquistare barrette di cioccolato da un distributore automatico al costo di 1 euro ciascuna.
Ogni barretta acquistata contiene un buono sconto, e con 6 buoni sconto si ottiene una barretta gratuita.

Scrivere un programma che:

    Acquisisca in input un valore N (numero di euro disponibili).
    Calcoli e mostri in output il numero totale di barrette che si possono ottenere, considerando anche quelle ottenute con i buoni sconto.
    Mostri quanti buoni sconto avanzano al termine dell'acquisto.
'''

saldo_disponibile:int = int(input("quanti soldi hai? "))

if saldo_disponibile // 6 > 0:
    barrette_gratis:int = saldo_disponibile // 6

barrette_acquistabili:int = saldo_disponibile + barrette_gratis
buoni_avanzati:int = saldo_disponibile % 6

print("barrette acquistabili: ", barrette_acquistabili)
print("buoni rimasti: ", buoni_avanzati)

