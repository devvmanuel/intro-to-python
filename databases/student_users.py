from database import User




try:
    jina = input("enter name\n")
    nambari = input("enter number\n")
    miaka = input("enter age\n")
    ukoo = input("gender?\n")
    kodi = input("student code\n")


    User.create(name=jina, nambari=phone, maika=age, ukoo=gender, kodi=studentcode)
    print("User Created Sucessfully")


except:
    print("failed to create users")
