import random, time

percorso:list[str] = [
            "_", "_", "_", "_", "_", "_", "_", "_", "_", "_",
            "_", "_", "_", "_", "_", "_", "_", "_", "_", "_",
            "_", "_", "_", "_", "_", "_", "_", "_", "_", "_",
            "_", "_", "_", "_", "_", "_", "_", "_", "_", "_",
            "_", "_", "_", "_", "_", "_", "_", "_", "_", "_",
            "_", "_", "_", "_", "_", "_", "_", "_", "_", "_",
            "_", "_", "_", "_", "_", "_", "_", "_", "_", "_",
            "_", "_", "_", "_", "_", "_", "_", "_", "_", "_",
            "_", "_", "_", "_", "_", "_", "_", "_", "_", "_",
            "_", "_", "_", "_", "_", "_", "_", "_", "_", "_",
            ]

posizione_Tartaruga = 0

while percorso[-1]== "_" :
    mossa_tartaruga = random.randint(1,10)

    if 1 <= mossa_tartaruga <= 5:
        print("\nPasso veloce della tartaruga!\n")
        posizione_Tartaruga += 3
        percorso[posizione_Tartaruga] = "T"
        
        for element in percorso[range(0,posizione_Tartaruga)]:
            element = "_"

        
        print(percorso, "\n")

    time.sleep(2)
