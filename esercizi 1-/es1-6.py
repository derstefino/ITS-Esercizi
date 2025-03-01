'''1-6. Inserire all'interno di un dizionario il menu' di un ristorante,
che viene specificato alla fine della traccia di questo esercizio.

Aggiungere in un nuovo dizionario chiamato ordine, un primo, un secondo, un contorno, una bevanda ed un dolce preso dal menu'. 

Stampare a schermo il conto totale che il cliente dovrà pagare. 

ITS Bakery Menu':

Pizza: 9.00 euro Pasta: 10.50 euro

Zuppa : 7.00 euro

Hamburger: 15.50 euro

Cotoletta: 10.00 euro

Salmone: 20.20 euro

Patatine Fritte: 5.50 euro

Patate al forno: 5.50 euro

Verdura del giorno: 7.00 euro

Cheesecake: 6.00 euro

Tiramisu': 6.00 euro

Focaccia con Nutella: 6.00 euro

Coca Cola: 3.50 euro

Acqua: 1.50 euro

Vino: 5.00 euro'''

menu:dict = {'Pizza':'9.00 euro', 'Pasta':'10.50 euro', 'Zuppa':'7.00 euro','Hamburger':'15.50 euro', 
             
             'Cotoletta':'10.00 euro', 'Salmone':'20.20 euro', 
             
             'Patatine Fritte': '5.50 euro', 'Patate al forno':'5.50 euro', 'Verdura del giorno':'7.00 euro', 
             
             'Cheesecake':'6.00 euro', 'Tiramisù': '6.00 euro', 'Focaccia con Nutella': '6.00 euro', 
             
             'Coca Cola':'3.50 euro', 'Acqua':'1.50 euro', 'Vino':'5.00 euro'}

ordine:dict = {'Pizza':9.00, 'Cotoletta':10.00, 'Patatine Fritte':5.50, 'Tiramisù':6.00, 'Acqua':1.50}

totale:float = 0

for value in ordine.values():
    totale += value

print(f"Il totale del conto da pagare è: {totale:.2f}")