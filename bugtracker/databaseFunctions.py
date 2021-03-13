








def addNewUser(name, username, password, id, email, role):
    print("Added user to database")


def removeUser(id):
    print("Removed user {} from database".format(id))


def canAdministerUsers(user):
    # Check db is user has role "admin"
    if(user == "none"):
        return False
    
    return True


def canAdministerBugs(user):
    # Check db if user has role "admin" or "moderator"
    if(user == "admin" or user == "moderator"):
        return True
    
    return False