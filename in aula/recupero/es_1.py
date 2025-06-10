def f(x,y,z) -> str:

    if x and (y or z):
        return "Azione permessa"
    else:
        return "Azione negata"