from database import User



users = User.select()
#use forloop to display
for user in users:
    print(user.name, user.email, user.password)