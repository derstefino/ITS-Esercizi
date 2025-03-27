'''
# dal file persona.py importa la classe Persona
from persona import Persona

# creo una persona
fm:Persona = Persona("Federico", "March", 29)

print(fm)

print(fm.name, fm.lastname, fm.age)

# richiamare la funzione displayData della classe Persona per mostrare in out put i dati relativi alla persona fm
fm.displayData()

print("---------------")
'''

# dal file persona2 importa la classe Persona
from persona2 import Persona

fm:Persona = Persona()

# richiamo la funzione displayData della classe PErsona per mostrare in output le informazioni relative all'oggetto fm
fm.displayData()

# modificare il nome della persona fm
fm.setName("Doraemon")

print("---------------")

fm.displayData()

fm.setLastname("Il gatto spaziale")

print("---------------")

fm.displayData()

fm.setAge(129)

print("---------------")

fm.displayData()

print("---------------")

print(fm.getName(), fm.getLastname(), fm.getAge())