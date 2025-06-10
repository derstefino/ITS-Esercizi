def binary_search(n:int, num_list:list[int]) -> bool:
    
    inizio = 0
    fine = len(num_list) - 1
    

    while inizio <= fine:

        incontro = (inizio + fine)//2
        valore = num_list[incontro]


        if n == valore:
            return True
        elif n < valore:
            fine = incontro -1
        elif n > valore:
            fine = incontro + 1
    

    return False
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return True

    
    
    
    
    
    
    return False