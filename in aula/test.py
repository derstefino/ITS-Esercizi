from persona import Persona
from studente import Studente
#

# creare un oggetto p di classe persona

p: Persona = Persona("Federico", "March", 29)


print(p)


studente1: Studente = Studente("Mario", "Rossi", 33, "0123456")

if isinstance(studente1, Studente):
    print("L'oggetto studente1 è un oggetto della classe Studente")

print(studente1)



