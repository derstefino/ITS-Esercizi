def f(lista:list[tuple]) -> dict:

    d1:dict = {}

    for key, value in lista:

        if key in d1:
            d1[key] += value

        else:

            d1[key] = value

    return d1


