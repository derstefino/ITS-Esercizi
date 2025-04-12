class Persona:

    def __init__(self, nome:str, cognome:str, età:int):
        
        self.nome=nome
        self.cognome=cognome
        self.età=età

    def setNome(self, nome:str) -> None:
        self.nome=nome

    def setCognome(self, cognome:str) -> None:
        self.cognome=cognome

    def setEtà(self, età:int) -> None:
        if età<0 or età>130:
            self.età=0
        else:
            self.età=età
        
    def getNome(self) -> str:
        return self.nome

    def getCognome(self) -> str:
        return self.cognome

    def getEtà(self) -> int:
        return self.età
    
    def __str__(self):
        return f"Nome:{self.nome}\nCognome:{self.cognome}\nEtà:{self.età}"
    

    def __call__(self):
            if self.età < 18:
                print(f"{self.nome} {self.cognome} e' minorenne!")
            elif 18 <= self.age < 30:
                print(f"{self.nome} {self.cognome} e' maggiorenne!")
            elif 30<= self.age < 80:
                print(f"{self.nome} {self.cognome} e' una persona adulta!")
            else:
                print(f"{self} {self.cognome} e' una persona anziana!")

    

    