'''6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways.
Use one of the example programs from this chapter,
and extend it by adding new keys and values, changing the context of the program, or improving the formatting of the output.
'''

cities:dict[str:dict] = {'Rome':{'country':'Italy', 'population':'3 milions', 'fact':'colosseo'},
                         'Pompei': {'country':'Italy', 'population':'uknown', 'fact':'vesuvio'}}


for key in cities:
    print(f"Here's some info on {key}: ")
    
    d = cities[key]
    
    for key in cities[key]:
        
        print(f"{key}: {d[key]}")