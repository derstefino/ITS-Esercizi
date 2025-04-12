class User:

    def __init__(self, first_name, last_name, username, email):

        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    
    def describe_user(self):

        print(f"User's first name: {self.first_name}\nUser's last name: {self.last_name}\nUser's username: {self.username}\nUser's email:{self.email}")

    def greet_user(self):

        print(f"Greetings, {self.first_name} {self.last_name}")

    
class Privileges:

    def __init__(self, list_of_privileges:list):

        self.list_of_privileges = list_of_privileges

    def show_privileges(self):

        print(*self.list_of_privileges, sep=", ")

user1 = User(first_name="user", last_name="user", username="user", email="user@user.user")

privileges_user1 = Privileges(["pranzo gratis", "caffè gratis"])

class Admin:

    def __init__(self, user=user1, privileges=privileges_user1):

        self.user = user
        self.privileges = privileges

    def describe_user(self):

        print(f"User's first name: {self.user.first_name}\nUser's last name: {self.user.last_name}\nUser's username: {self.user.username}\nUser's email:{self.user.email}")

    def greet_user(self):

        print(f"Greetings, {self.user.first_name} {self.user.last_name}")

    def show_privileges(self):

        print(*self.privileges.list_of_privileges, sep=", ")