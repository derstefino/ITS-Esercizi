'''9-3. Users: Make a class called User. Create two attributes called first_name and last_name,
and then create several other attributes that are typically stored in a user profile.
Make a method called describe_user() that prints a summary of the user’s information.
Make another method called greet_user() that prints a personalized greeting to the user.
Create several instances representing different users, and call both methods for each user.
'''

class User:

    def __init__(self, first_name, last_name, **kwargs):

        self.first_name = first_name
        self.last_name = last_name
        self.kwargs = kwargs

        pass

    def describe_user(self):

        print(f"User's first name is {self.first_name}, his last name is {self.last_name} and here's other info about this user:\n{self.kwargs}")

    def greet_user(self):

        print(f"Hi, {self.first_name} {self.last_name}")


Joker = User(first_name="Heath", last_name="Ledger", age=30)

Joker.describe_user()
Joker.greet_user()
    

