from string import ascii_lowercase

def caesar_cypher_encrypt(s:str, key:int) -> str:
    encrypted:str = ""

    for char in s:
        if char==char.upper():
            if char.lower() in ascii_lowercase:
                encrypted += ascii_lowercase[(ascii_lowercase.index(char.lower()) + key) % len(ascii_lowercase)].upper()
        else:
            if char.lower() in ascii_lowercase:
                encrypted += ascii_lowercase[(ascii_lowercase.index(char.lower()) + key) % len(ascii_lowercase)]
    
    return encrypted


print(caesar_cypher_encrypt("ciao", 2))


def caesar_cypher_decrypt(s:str, key:int) -> str:
    decrypted = ""

    for char in s:
        if char==char.upper():
            if char.lower() in ascii_lowercase:
                decrypted += ascii_lowercase[(ascii_lowercase.index(char.lower()) - key) % len(ascii_lowercase)].upper()
        else:
            if char.lower() in ascii_lowercase:
                decrypted += ascii_lowercase[(ascii_lowercase.index(char.lower()) - key) % len(ascii_lowercase)]
    
    return decrypted


print(caesar_cypher_decrypt("ekcq", 2))