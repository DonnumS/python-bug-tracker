import mysql.connector

connected = False
con = mysql.connector.connect(user='root',
                              password='Liver1pool',
                              database='bug_tracker')
cursor = con.cursor()


def getHigh():
    query = "SELECT COUNT(*) FROM BugDetails WHERE Priority = 1"
    cursor.execute(query)
    # print(cursor)

    stringNum = ""

    for num in cursor:
        stringNum = num[0]

    return int(stringNum)


def addNewUser(name, username, password, id, email, role):
    idInt = int(id)
    query = ("INSERT INTO loginCredentials (EmployeeId, Username, Password, UserRole, FullName, Email) VALUES ({}, '{}', '{}', '{}', '{}', '{}')".format(
        idInt, username, password, role, name, email))

    # print(query)
    cursor.execute(query)
    con.commit()
    #print("Added user to database")


def checkValidLogin(username, password):
    # Very simple and very unsafe login system that is only here for the functionality
    query = ("SELECT Username, Password FROM loginCredentials WHERE Username = '{}' AND Password = '{}'".format(
        username, password))
    cursor.execute(query)

    #print("Query: {}\n".format(query))

    uName = ""
    pWord = ""

    # Used for debugging purposes
    for(Username, Password) in cursor:
        uName = Username
        pWord = Password

    #print(uName + " " + pWord)

    # Count if there is only 1 row
    rowCount = cursor.rowcount
    # print(rowCount)

    # If 1 then return True, else False
    if(rowCount == 1):
        return True
    return False


def removeUser(id):
    iDint = int(id)
    query = "DELETE FROM loginCredentials WHERE EmployeeId = {}".format(iDint)
    cursor.execute(query)
    con.commit()
    #print("Deleted user from database")


def adminCheck(user):
    #print(user + " is the user to be checked")
    query = "SELECT UserRole FROM loginCredentials WHERE Username = '{}'".format(
        user)
    # print(query)
    cursor.execute(query)

    result = ""

    for(UserRole) in cursor:
        result = UserRole

    #print("The result from role query is:")
    # print(result[0])

    if result[0] == "admin":
        return True
    return False


def moderatorCheck(user):
    return False


def canAdministerBugs(user):
    # Check db if user has role "admin" or "moderator"
    if(user == "admin" or user == "moderator"):
        return True

    return False


getHigh()
