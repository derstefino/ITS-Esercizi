from datetime import date


class Progetto:

    _nome:str
    _budget:float

    def __init__(self, nome:str, budget:float):

        self.nome=nome
        self.budget=budget
        self.impiegati=[]

    def aggiungi_impiegato(self, impiegato) -> None:
        if impiegato not in self.impiegati:
            self.impiegati.append(impiegato)
    
    def __str__(self):

        return f"Progetto {self.nome}\nBudget: {self.budget:.2f}\nImpiegati: {self.impiegati}"

    def __hash__(self):
        return hash((self.nome, self.budget))
    
    def __eq__(self, other) -> bool:
        if other is None or not isinstance(other, type(self)) or hash(self)!=hash(other):

            return False
        return ((self.nome, self.budget)==(other.nome, other.budget))


class Impiegato:

    _nome:str
    _cognome:str
    _data_nascita:date
    _stipendio:float

    def __init__(self, nome:str, cognome:str, data_nascita:date, stipendio:float):

        self.nome=nome
        self.cognome=cognome
        self.data_nascita=data_nascita
        self.stipendio=stipendio
        self.dip=None
        self.progetti=[]  

    def assegna_progetto(self, progetto) -> None:
        if progetto not in self.progetti:
            self.progetti.append(progetto)

    def __str__(self):

        return f"Impiegato: {self.nome} {self.cognome}, nato il {self.data_nascita}\nStipendio: {self.stipendio:.2f}\nDipartimento: {self.dip}\nProgetti: {self.progetti}"

    def __hash__(self):
        return hash((self.nome, self.cognome, self.data_nascita, *self.progetti, self.dip))
    
    def __eq__(self, other) -> bool:
        if other is None or not isinstance(other, type(self)) or hash(self)!=hash(other):

            return False
        return ((self.nome, self.cognome, self.data_nascita, self.progetti, self.dip)==(other.nome, other.cognome, other.data_nascita, other.progetti, other.dip))
    

class Dipartimento:

    _nome:str
    _budget:float

    def __init__(self, nome:str, budget:float, direttore:Impiegato):

        self.nome=nome
        self.budget=budget
        self.direttore=direttore

    def __str__(self):

        return f"Dipartimento {self.nome}\nBudget:{self.budget:.2f}\nDirettore: {self.direttore}"

    def __hash__(self):
        return hash((self.nome, self.budget, self.direttore))
    
    def __eq__(self, other) -> bool:
        if other is None or not isinstance(other, type(self)) or hash(self)!=hash(other):

            return False
        return ((self.nome, self.budget, self.direttore)==(other.nome, other.budget, self.direttore))
    