




def login():

    username=input("Username: ")
    password=input("Password: ")

    if (username == "admin" and password == "123"):
        print("Successfully logged in as admin")
    else:
        print("Wrong username and password combination")
        
login()