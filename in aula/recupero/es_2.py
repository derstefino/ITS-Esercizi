def f(lista:list[int], treshold:int) -> int:
    result = 1
    for num in lista:
        if num < treshold:
            result*=num
    return result