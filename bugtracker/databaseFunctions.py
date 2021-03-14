import mysql.connector

connected = False
con = mysql.connector.connect(user='root',
                              password='Liver1pool',
                              database='bug_tracker')
cursor = con.cursor()

# All the functions that helps the app communicate with the MySQL server that runs locally on my machine


def getHigh():
    query = "SELECT COUNT(*) FROM BugDetails WHERE Priority = 1"
    cursor.execute(query)
    # print(cursor)

    stringNum = ""

    for num in cursor:
        stringNum = num[0]

    return int(stringNum)


def getMed():
    query = "SELECT COUNT(*) FROM BugDetails WHERE Priority = 2"
    cursor.execute(query)
    # print(cursor)

    stringNum = ""

    for num in cursor:
        stringNum = num[0]

    return int(stringNum)


def getLow():
    query = "SELECT COUNT(*) FROM BugDetails WHERE Priority = 3"
    cursor.execute(query)
    # print(cursor)

    stringNum = ""

    for num in cursor:
        stringNum = num[0]

    return int(stringNum)


def getComplete():
    query = "SELECT COUNT(*) FROM BugDetails WHERE Priority = 4"
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

    if result[0] == "admin" or result[0] == "moderator":
        return True
    return False


def getUncompleteData():
    query = "SELECT BugId, BugTitle, Application, AppVersion, Details, Steps, Priority, Assigned, CreatedBy, DayCreated FROM BugDetails WHERE Priority <> 4"
    cursor.execute(query)

    result = []
    for (BugId, BugTitle, Application, AppVersion, Details, Steps, Priority, Assigned, CreatedBy, DayCreated) in cursor:
        temp = []
        temp.extend((BugId, BugTitle, Application, AppVersion, Details,
                     Steps, Priority, Assigned, CreatedBy, DayCreated))
        result.append(temp)

    # Handles the case when query results in empty list
    if len(result) == 0:
        result = [["No bugs in db", "--", "--", "--", "--",
                   "--", "--", "--", "--", "--"]]
    return result


def getCompleteData():
    query = "SELECT BugId, BugTitle, Application, AppVersion, Details, Steps, Priority, Assigned, CreatedBy, DayCreated FROM BugDetails WHERE Priority = 4"
    cursor.execute(query)

    result = []
    for (BugId, BugTitle, Application, AppVersion, Details, Steps, Priority, Assigned, CreatedBy, DayCreated) in cursor:
        temp = []
        temp.extend((BugId, BugTitle, Application, AppVersion, Details,
                     Steps, Priority, Assigned, CreatedBy, DayCreated))
        result.append(temp)

    # Handles the case when query results in empty list
    if len(result) == 0:
        result = [["No bugs in db", "--", "--", "--", "--",
                   "--", "--", "--", "--", "--"]]

    return result


def setBugComplete(bugId):
    query = "UPDATE BugDetails SET Priority = 4 WHERE BugId = {}".format(bugId)
    cursor.execute(query)
    con.commit()


def deleteBug(bugId):
    query = "DELETE FROM BugDetails WHERE BugId = {}".format(bugId)
    cursor.execute(query)
    con.commit()


def addBug(title, appName, version, creator, assignedTo, details, priority, steps):
    print("Hei")
