class Persona:
    
    def __init__(self, name:str, lastname:str, age:int):
        
        self.name = name
        self.lastname = lastname
        self.age = age

        # funzione che mi mostri in output i dati relativi ad una persona

    def displayData(self) -> None:
        print(f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}")

    