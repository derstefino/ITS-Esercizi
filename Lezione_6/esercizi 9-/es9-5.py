'''9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3.
Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts() several times.
Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts().
Print login_attempts again to make sure it was reset to 0.
'''

class User:

    def __init__(self, first_name, last_name, login_attempts=0, **kwargs):

        self.first_name = first_name
        self.last_name = last_name
        self.login_attemps = login_attempts
        self.kwargs = kwargs

    def increment_login_attempts(self, n:int):

        self.login_attemps += n

    def reset_login_attempts(self):

        self.login_attemps = 0

        pass

    def describe_user(self):

        print(f"User's first name is {self.first_name}, his last name is {self.last_name} and here's other info about this user:\n{self.kwargs}")

    def greet_user(self):

        print(f"Hi, {self.first_name} {self.last_name}")


user = User(first_name="user", last_name="user")

user.increment_login_attempts(10)

print(user.login_attemps)

user.reset_login_attempts()

print(user.login_attemps)