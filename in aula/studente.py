from persona import Persona

class Studente(Persona):

    '''
    def inheritanceTest(self):
      # verificare che la classe studente erediti tutti gli attriburi della classe persona
        self.nome
        self.cognome
        self.età


   # verificare che la classe studente erediti tutti i metodi della classe persona
        self.getNome()
        self.getCognome
        self.getNome

'''



# inizializzare un oggetto della classe Studente
    
    def __init__(self, nome:str, cognome:str, età:int, matricola:str):
        
        super().__init__(nome, cognome, età)

        self.setMatricola(matricola)


    def setMatricola(self, matricola:str) -> None:

        if matricola:
            self.matricola = matricola
        else:
            print("Errore! La matricola non può essere una stringa vuota")

            
