class Persona:

    def __init__(self, name:str, lastname:str, age:int):
        
        self.name=name
        self.lastname=lastname
        self.age=age

    def setName(self, name:str) -> None:
        self.name=name

    def setLastname(self, lastname:str) -> None:
        self.lastname=lastname

    def setAge(self, age:int) -> None:
        if age<0 or age>130:
            self.age=0
        else:
            self.age=age
        
    def getName(self) -> str:
        return self.name

    def getLastname(self) -> str:
        return self.lastname

    def getAge(self) -> int:
        return self.age
    
    def __str__(self):
        return f"Nome:{self.name}\nCognome:{self.lastname}\nEtà:{self.age}"
    

    def __call__(self):
            if self.età < 18:
                print(f"{self.name} {self.lastname} e' minorenne!")
            elif 18 <= self.age < 30:
                print(f"{self.name} {self.lastname} e' maggiorenne!")
            elif 30<= self.age < 80:
                print(f"{self.name} {self.lastname} e' una persona adulta!")
            else:
                print(f"{self.name} {self.lastname} e' una persona anziana!")

    

    