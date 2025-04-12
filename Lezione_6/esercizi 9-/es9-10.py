'''9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module.
Make a separate file that imports Restaurant.
Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.
'''

from moduleRestaurant import Restaurant

ristorante = Restaurant(restaurant_name="Giorno", cuisine_type="Italiano")

print(ristorante.restaurant_name)

ristorante.set_number_served(10)

print(ristorante.number_served)