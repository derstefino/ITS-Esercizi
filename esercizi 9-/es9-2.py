'''9-2. Three Restaurants: Start with your class from Exercise 9-1.
Create three different instances from the class, and call describe_restaurant() for each instance.
'''

class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
        pass

        

    def describe_restaurant(self):
        
        print(self.restaurant_name, self.cuisine_type)





Sushi = Restaurant(restaurant_name="Domò", cuisine_type="Giapponese")
Cinese = Restaurant(restaurant_name="Vento dell'Est", cuisine_type="Asiatico")
Indiano = Restaurant(restaurant_name="India", cuisine_type="Orientale")

Sushi.describe_restaurant()
Cinese.describe_restaurant()
Indiano.describe_restaurant()




