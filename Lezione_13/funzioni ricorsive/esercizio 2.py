'''Esercizio 2.

Si supponga di voler calcolare l'ammontare del denaro depositato su un conto bancario ad interesse composto.
Se m è la somma depositata sul conto, la somma disponibile alla fine del mese sarà 1.005 volte m.
Scrivere una funzione ricorsiva compoundInterest che calcoli la somma presente sul conto dopo t mesi data una somma di partenza m.
'''

def compoundInterest(m:float, mesi:int):

    if mesi==1:
        m = m * 1.005
        return m

    if mesi > 1:
        m += 1.005*compoundInterest(m, mesi -1) 
        return m

print(compoundInterest(1000, 12))

