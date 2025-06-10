import string


def f(testo:str) -> dict:

    parole = testo.split()

    conteggio = {}

    for parola in parole:
        parola_minusc = parola.lower().strip(string.punctuation)

        if parola_minusc in conteggio:
            conteggio[parola_minusc] += 1
        else:
            conteggio[parola_minusc] = 1

    return conteggio


print(f("Hello, world! Hello... PYTHON? world."))