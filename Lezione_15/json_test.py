class Example:

    def __init__(self, name:str, version:str):

        self.name=name
        self.version=version
    

import json

with open("Lezione_15/config.json", "r") as file:

    my_config : dict = json.load(file)

    


file = open("Lezione_15/config.json", "w")

db : dict = {"uomo":{"nome":"stefano"}}


json.dump(db, file)



file.close()