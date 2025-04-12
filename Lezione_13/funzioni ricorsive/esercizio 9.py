'''Esercizio 9.

Si scriva una funzione ricorsiva vowelRemover che elimini tutte le vocali da una stringa data
e restituisca sotto forma di una nuova stringa la stringa originale ma senza le vocali.

Suggerimento: utilizzare l'operatore + per realizzare la concatenazione di stringhe al fine di costruire la stringa da restituire.
'''

def vowlerRemover(s:str):

    if len(s)==0:
        return s
    elif s[0].lower() not in 'aeiou':
        return s[0]+vowlerRemover(s[1:])
    else:
        return vowlerRemover(s[1:])
    


print(vowlerRemover("gavrilo"))