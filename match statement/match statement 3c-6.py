'''
Esercizio 3C-6. Modificare il codice dell'esercizio 3C-4,
affinchè si possa scrivere un codice python che consenta all'utente di inserire il nome di un animale ed un habitat.
Quando il codice dell'esercizo 3C-4 classifica l'animale inserito in una delle categorie tra mammiferi, rettili, uccelli o pesci,
oltre a mostrare un messaggio a schermo, deve salvare tale categoria in una variabile animal_type.
Se l'animale inserito non è classificabile in una delle quattro categorie proposte, il valore di animal_type sarà ' "unknown".

Inserire, poi, in un dizionario il nome dell'animale, la categoria a cui esso appartiene (animal_type) e l'habitat.

Verificare con un match statement se l'animale e la categoria a cui esso appartiene possano vivere nell'habitat inserito; dunque, verificare:
- se l'animale può vivere nell'habitat specificato, stampare un messaggio appropriato.
- se l'habitat non è compatibile con l'habitat specificato, stampare un avviso.
- Se l'animale o l'habitat non sono riconosciuti, stampare un messaggio di errore.

Le categorie di classificazione devono essere:
- Mammiferi: cane, gatto, cavallo, elefante, leone, balena, delfino.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco, cigno, anatra, gallina, tacchino.
- Pesci: squalo, trota, salmone, carpa.

Categorie di habitat:
- acqua
- aria
- terra

NOTA.
Il codice deve produrre un risultato sensato, ovvero che l'animale inserito possa effettivamente vivere nell'habitat specificato.
Tenere in considerazione il fatto che alcuni animali tra quelli specificati possono vivere in più di un habitat, mentre altri solo in uno.

Suggeirmento: può essere utile per coprire tutti i possibili casi implementare istruzioni match annidate.

Expected Output:

Digita il nome di un animale: leone
Digita l'habitat in cui vive l'animale leone: terra
Output:
Leone appartiene alla categoria dei Mammiferi!
L'animale leone è uno dei mammiferi che può vivere sulla terra!

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: balena
Digita l'habitat in cui vive l'animale balena: acqua
Output:
Balena appartiene alla categoria dei Mammiferi!
L'animale balena è uno dei mammiferi che può vivere in acqua!

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: delfino
Digita l'habitat in cui vive l'animale delfino: terra
Output:
Delfino appartiene alla categoria dei Mammiferi!
Non ho mai visto l'animale delfino vivere nell'habitat terra.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: drago
Digita l'habitat in cui vive l'animale drago: aria
Output:
Non so dire in quale categoria classificare l'animale drago!
Non sono in grado di fornire informazioni sull'habitat aria.
'''

Mammiferi:list[str] = ["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"]

Rettili:list[str] = ["serpente", "lucertola", "tartaruga", "coccodrillo"]

Uccelli:list[str] = ["aquila", "pappagallo", "gufo", "falco"]

Pesci:list[str] = ["squalo", "trota", "salmone", "carpa"]



animale:str = str(input("Digita il nome di un animale: "))


habitat:str = str(input(f"Digita l'habitat in cui vive l'animale {animale}: "))



dict:dict  = {}


match animale:
    
    case animale if animale in Mammiferi:
        print(f"{animale} appartiene alla categoria dei Mammiferi")
        animal_type = "mammiferi" 

        
    
    case animale if animale in Rettili:
        print(f"{animale} appartiene alla categoria dei Rettili")
        animal_type = "rettili"
        dict[animale] = animal_type, habitat

        
    
    case animale if animale in Uccelli:
        print(f"{animale} appartiene alla categoria degli Uccelli")
        animal_type = "uccelli"
        dict[animale] = animal_type, habitat

        
    
    case animale if animale in Pesci:
        print(f"{animale} appartiene alla categoria dei Pesci")
        animal_type = "pesci"
        dict[animale] = animal_type, habitat



    case _:
        animal_type = "uknown"
        dict[animale] = animal_type, habitat

        print(f"Non so dire in quale categoria classificare l'animale {animale}!")
        print(f"Non sono in grado di fornire informazioni sull'habitat {habitat}.")





print(f"Non ho mai visto l'animale {animale} vivere nell'habitat {habitat}.")
print(f"L'animale {animale} è uno dei mammiferi che può vivere sulla terra")