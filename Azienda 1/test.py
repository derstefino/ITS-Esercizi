from Azienda_1 import Impiegato, Progetto, Dipartimento

gino=Impiegato("gino", "b", "25/12/2020", 0)

gino_due=Impiegato("gino", "b", "25/12/2020", 0)

print(gino)

print(gino==gino_due)



primo_progetto=Progetto("Esperimento", 10000)

ultimo_progetto=Progetto("esercitazione", 0)

progetto=Progetto("Esperimento", 10000)

print(progetto)

print(progetto==primo_progetto)


progetto.aggiungi_impiegato(gino)
gino.assegna_progetto(primo_progetto)

gino_due.assegna_progetto(primo_progetto)



dipartimento=Dipartimento("Roma centro", 800000, gino)

dip=Dipartimento("Roma centro", 800000, gino_due)

print(dipartimento==dip)

lista = [dip, dipartimento]

print(set(lista))