def is_valid_ipv4(address:str) -> bool:

    parti = address.split(".")

    if len(parti) != 4:
        return False
    
    for parte in parti:

        if not parte.isdigit():
            return False
    
    valore = int(parte)
    if valore < 0 or valore > 255:
        return False
    
    return True