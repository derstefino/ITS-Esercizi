'''

6. Verifica un codice prodotto

Scrivi una funzione check_product_code(code) che verifica se il codice è nel formato PROD-1234-AB.

Esempio:

check_product_code("PROD-9876-ZX")  # True
check_product_code("PROD-99-ZX")    # False


'''

import re

def check_product_code(code:str) -> bool:

    match = re.findall("[A-Z]{4}-[0-9]{4}-[A-Z]{2}", code)

    if match:
        return True
    else:
        return False
    
print(check_product_code("PROD-a-ZX"))

