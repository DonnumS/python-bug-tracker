


# Temporary function that is used to check that invalid login goves error correctly
# Gonna be subbed out for a SQL query
def checkValidLogin(username, password):
    print(username)
    print(password)
    if(username == "admin" and password == "123"):
        return True
    
    return False