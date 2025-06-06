class Movie:

    def __init__(self, movie_id:str, title:str, director:str, is_rented:bool):

        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = is_rented

    def rent(self):
        
        if self.is_rented:
            print(f"Il film {self.title} è già noleggiato")
        else:
            self.is_rented = True

    def return_movie(self):

        if self.is_rented:
            self.is_rented = False
        else:
            print(f"Il film '{self.title}' non è stato noleggiato da questo cliente.")


class Customer:

    def __init__(self, customer_id:str, name:str, rented_movies:list[Movie]):

        self.customer_id = customer_id
        self.name = name
        self.rented_movies = rented_movies

    def rent_movie(self, movie:Movie):

        if movie.is_rented:
            print(f"Il film {movie.title} è già noleggiato")
        else:
            self.rented_movies.append(movie)

    def return_movie(self, movie:Movie):
         
        if movie in self.rented_movies:
            self.rented_movies.remove(movie)
        else:
            print(f"Il film {movie.title} non è stato noleggiato da questo cliente")


class VideoRentalStore:

    def __init__(self, movies:dict[str,Movie], customers:dict[str,Customer]):

        self.movies = movies
        self.customers = customers

    def add_movie(self, movie_id:str, title:str, director:str):

        if movie_id not in self.movies:
            self.movies[movie_id] = Movie(movie_id, title, director, is_rented=False)
        else:
            print(f"Il film con ID {movie_id} esiste già.")
    
    def register_customer(self, customer_id:str, name:str):

        if customer_id not in self.customers:
            self.customers[customer_id] = Customer(customer_id, name)
        else:
            print(f"Il cliente con ID {customer_id} è già stato registrato")
    
    def rent_movie(self, customer_id:str, movie_id:str):

        if customer_id in self.customers and movie_id in self.movies:
            self.movies[movie_id].is_rented = True
        else:
            print(f"Cliente o film non trovato")

    def return_movie(self, customer_id:str, movie_id:str):

        if customer_id in self.customers and movie_id in self.movies:
            self.movies[movie_id].is_rented = False
        else:
            print(f"Cliente o film non trovato")

    def get_rented_movies(self, customer_id:str) -> list[Movie]:

        if customer_id in self.customers:
            return self.customers[customer_id].rented_movies
        else:
            print("Cliente non trovato")
            return []