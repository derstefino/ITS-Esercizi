'''
Sviluppa un sistema per la gestione dei contatti in Python che permetta agli utenti di
creare, modificare, e cercare contatti basati sui numeri di telefono. Il sistema dovrà
essere capace di gestire una collezione (dizionario) di contatti e i loro numeri di telefono.
'''

class ContactManager:

    def __init__(self, contacts:dict[str,list[str]]):

        self.contacts = contacts
    
    def create_contact(self, name:str, phone_numbers:list[str]):

        if name not in self.contacts:
            self.contacts[name] = phone_numbers
            return dict(name, self.contacts[name])
        else:
            return "Errore: il contatto esiste già."

    def add_phone_number(self, contact_name:str, phone_number:str):

        if contact_name in self.contacts and phone_number not in self.contacts[contact_name]:
            self.contacts[contact_name].append(phone_number)
            return dict(contact_name, self.contacts[contact_name])
        
        elif contact_name not in self.contacts:
            return "Errore: il contatto non esiste."
        elif phone_number in self.contacts[contact_name]:
            return "Errore: il numero di telefono esiste già."
        
    def remove_phone_number(self, contact_name:str, phone_number:str):

        if contact_name in self.contacts:
            if phone_number not in self.contacts[contact_name]:
                return "Errore: il numero di telefono non è presente."
            else:
                self.contacts[contact_name].append(phone_number)
                return dict(contact_name, self.contacts[contact_name])
        else:
            return "Errore: il contatto non esiste."
        
    def update_phone_numbers(self, contact_name:str, old_phone_number:str, new_phone_number:str):

        if contact_name in self.contacts:
            if old_phone_number not in self.contacts[contact_name]:
                return "Errore: il numero di telefono non è presente."
            else:
                self.contacts[contact_name].insert(self.contacts[contact_name].index(old_phone_number), new_phone_number)
                return dict(contact_name, self.contacts[contact_name])
        else:
            return "Errore: il contatto non esiste."
    
    def list_contacts(self):
        return list(self.contacts.keys())
    
    def list_phone_numbers(self, contact_name:str):
        if contact_name in self.contacts:
            return self.contacts[contact_name]
        else:
            return "Errore: il contatto non esiste."
        
    def search_contact_by_phone_number(self, phone_number:str):
        contacts:list = [] 
        for key in self.contacts:
            if phone_number in self.contacts[key]:
              contacts.append(key)
        if not contacts:
            return "Nessun contatto trovato conquesto numero di telefono."
        return contacts