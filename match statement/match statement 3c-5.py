'''
Esercizio 3C-5. Scrivere un programma in Python che memorizzi il nome, il ruolo e l'età di un utente in un dizionario.
Il nome, il ruolo e l'età devono essere inseriti in input dall'utente stesso.
Il programma deve determinare il livello di accesso ai servizi in base al ruolo e all'età dell'utente secondo questo schema:

- Admin → "Accesso completo a tutte le funzionalità."
- Moderatore → "Può gestire i contenuti ma non modificare le impostazioni."
- Utente adulto (età ≥ 18) → "Accesso standard a tutti i servizi."
- Utente minorenne (età < 18) → "Accesso limitato! Alcune funzionalità sono bloccate."
- Ospite → "Accesso ristretto! Solo visualizzazione dei contenuti."
- Ruolo non riconosciuto → "Attenzione! Ruolo non riconsciuto! Accesso Negato!"

Expected Output:

Digitare nome dell'utente: Mario Rossi
Digitare ruolo dell'utente: admin
Digitare l'età dell'utente: 30
Output: Accesso completo a tutte le funzionalità.

- - - - - - - - - - - - - - - - - - - - - - - - - - -

Digitare nome dell'utente: Giulia Bianchi
Digitare ruolo dell'utente: utente
Digitare l'età dell'utente: 16
Output: Accesso limitato! Alcune funzionalità sono limitate!

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digitare nome dell'utente: Sara Neri
Digitare ruolo dell'utente: vip
Digitare l'età dell'utente: 22
Output: Attenzione! Ruolo non riconosciuto! Accesso Negato!

 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digitare nome dell'utente: Luca Verdi
Digitare ruolo dell'utente: moderatore
Digitare l'età dell'utente: 25
Output: Salve Luca Verdi! Può gestire i contenuti ma non modificare le impostazioni.
'''

utenti:dict = {'Nome':[], 'Ruolo':[], 'Età':[], 'Admin':[], 'Moderatore':[], 'Ospite':[]}

while True:

    risposta = str(input("Vuoi inserire un nuovo utente?(sì per confermare, avanti per andare avanti): "))
    
    if risposta == "sì":
        
    

            inserimento_nome:str = str(input("Inserire il nome dell'utente: "))
            utenti['Nome'].append(inserimento_nome)
        
            inserimento_ruolo:str = str(input("Inserire il ruolo: "))
        
            if inserimento_ruolo == "Admin" or inserimento_ruolo == "admin":
                utenti['Admin'].append(inserimento_ruolo)
            if inserimento_ruolo == "Moderatore" or inserimento_ruolo == "moderatore":
                utenti['Moderatore'].append(inserimento_ruolo)
            if inserimento_ruolo == "Ospite" or inserimento_ruolo == "ospite":
                utenti['Ospite'].append(inserimento_ruolo)
        
            utenti['Ruolo'].append(inserimento_ruolo)
            inserimento_età:int = int(input("Inserire l'età: "))
            utenti['Età'].append(inserimento_età)

            risposta = str(input("Vuoi inserire un nuovo utente?(sì per confermare, avanti per andare avanti): "))
    
    if risposta == "avanti":

            ricerca_nome:str = str(input("Digitare nome dell'utente: "))
        
            ricerca_ruolo:str = str(input("Digitare ruolo dell'utente: "))

            ricerca_età:int = int(input("Digitare l'età dell'utente: "))


            if ricerca_età < 18:
                print("Accesso limitato! Alcune funzionalità sono bloccate.")
            if ricerca_età >= 18:
                print("Accesso standard a tutti i servizi.")

    match ricerca_ruolo:
            
            
            
            case ricerca_ruolo if ricerca_ruolo in utenti['Admin']:
                print("Accesso completo a tutte le funzionalità.")
            case ricerca_ruolo if ricerca_ruolo in utenti['Moderatore']:
                print(f" Salve {ricerca_nome}! Può gestire i contenuti ma non modificare le impostazioni.")
            case ricerca_ruolo if ricerca_ruolo in utenti['Ospite']:
                print("Accesso ristretto! Solo visualizzazione dei contenuti.")
            case _:
                print("Attenzione! Ruolo non riconosciuto! Accesso Negato!")
