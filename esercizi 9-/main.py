from users import User, Privileges, Admin

user2 = User(first_name="user2", last_name="user2", username="user2", email="user2@user2.user2")

privileges_user2 = Privileges(["2 pranzi gratis", "2 caffè gratis"])

adminU = Admin(user2, privileges_user2)

adminU.describe_user()
adminU.show_privileges()




