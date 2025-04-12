def car_info(manufacturer:str, model_name:str, **kwargs) -> dict:

    car_dict:dict[str] = {'manufact':manufacturer, 'model':model_name}

    for x in kwargs:
        car_dict[x]=kwargs[x]  
    
    print(car_dict)