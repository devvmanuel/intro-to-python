from database import User

try:
    jina = input("Enter Name\n")
    arafa = input("Enter Email\n")
    siri = input("Enter Password\n")

    User.create(name=jina, email=arafa, password=siri)
    print("User Created Sucessfully")


except:
    print("Failed to create user")
