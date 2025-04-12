class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type,  number_served=0):
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def set_number_served(self, n:int):

        self.number_served = n

    def increment_number_served(self, n:int):

        self.number_served += n
