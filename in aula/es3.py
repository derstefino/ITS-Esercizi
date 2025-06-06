def f(d1:dict) -> dict:

    d2 = {}

    for key, value in d1.items():

         if value < 50:
              value += value/10
              d2[key] = round(value,2)
    
    return d2




print(f({"pane":4.90}))