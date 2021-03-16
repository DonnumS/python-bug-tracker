import mysql.connector

connected = False
con = mysql.connector.connect(user='root',
                              password='Liver1pool',
                              database='bug_tracker')
cursor = con.cursor()

# All the functions that helps the app communicate with the MySQL server that runs locally on my machine


def getHigh():
    # Get the count for bugs with priority 1
    query = "SELECT COUNT(*) FROM BugDetails WHERE Priority = 1"
    cursor.execute(query)

    stringNum = ""

    for num in cursor:
        stringNum = num[0]

    return int(stringNum)


def getMed():
    # Get the count for bugs with priority 2
    query = "SELECT COUNT(*) FROM BugDetails WHERE Priority = 2"
    cursor.execute(query)

    stringNum = ""

    for num in cursor:
        stringNum = num[0]

    return int(stringNum)


def getLow():
    # Get the count for bugs with priority 3
    query = "SELECT COUNT(*) FROM BugDetails WHERE Priority = 3"
    cursor.execute(query)

    stringNum = ""

    for num in cursor:
        stringNum = num[0]

    return int(stringNum)


def getComplete():
    # Get the count for bugs with priority 4
    query = "SELECT COUNT(*) FROM BugDetails WHERE Priority = 4"
    cursor.execute(query)

    stringNum = ""

    for num in cursor:
        stringNum = num[0]

    return int(stringNum)


def addNewUser(name, username, password, userId, email, role):
    idInt = int(userId)
    query = ("INSERT INTO loginCredentials (EmployeeId, Username, Password, UserRole, FullName, Email) VALUES ({}, '{}', '{}', '{}', '{}', '{}')".format(
        idInt, username, password, role, name, email))

    cursor.execute("INSERT INTO loginCredentials (EmployeeId, Username, Password, UserRole, FullName, Email) VALUES (%(idInt)s, %(username)s, %(password)s, %(role)s, %(name)s, %(email)s)", {
        'idInt': idInt,
        'username': username,
        'password': password,
        'role': role,
        'name': name,
        'email': email
    })
    # Commit the changes to the db
    con.commit()


def checkValidLogin(username, password):
    cursor.execute("SELECT Username, Password FROM loginCredentials WHERE Username = %(username)s AND Password = %(password)s", {
        'username': username,
        'password': password
    })

    # print("Query: {}\n".format(query))

    uName = ""
    pWord = ""

    # Used for debugging purposes
    for(Username, Password) in cursor:
        uName = Username
        pWord = Password

    # print(uName + " " + pWord)

    # Count if there is only 1 row
    rowCount = cursor.rowcount
    # print(rowCount)

    # If 1 then return True, else False
    if(rowCount == 1):
        return True
    return False


def removeUser(id):
    idInt = int(id)

    cursor.execute("DELETE FROM loginCredentials WHERE EmployeeId = %(idInt)s", {
        'idInt': idInt
    })

    # Commit the changes to the db
    con.commit()


def adminCheck(user):
    # Get the role of user
    cursor.execute("SELECT UserRole FROM loginCredentials WHERE Username = %(user)s", {
        'user': user,
    })

    result = ""

    for(UserRole) in cursor:
        result = UserRole

    if result[0] == "admin":
        return True
    return False


def moderatorCheck(user):
    # Get the role of the user
    cursor.execute("SELECT UserRole FROM loginCredentials WHERE Username = %(user)s", {
        'user': user,
    })

    result = ""

    # Get the role of the user
    for(UserRole) in cursor:
        result = UserRole

    # Check if role is admin or moderator
    if result[0] == "admin" or result[0] == "moderator":
        return True
    return False


def getUncompleteData():
    cursor.execute(
        "SELECT BugId, BugTitle, Application, AppVersion, Details, Steps, Priority, Assigned, CreatedBy, DayCreated FROM BugDetails WHERE Priority <> 4")

    # Construct the list of lists with data
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
    cursor.execute(
        "SELECT BugId, BugTitle, Application, AppVersion, Details, Steps, Priority, Assigned, CreatedBy, DayCreated FROM BugDetails WHERE Priority = 4")

    # Construct list of lists with the data
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
    # Change priority of bug with bugId to priority 4

    # Old query
    # query = "UPDATE BugDetails SET Priority = 4 WHERE BugId = {}".format(bugId)

    cursor.execute("UPDATE BugDetails SET Priority = 4 WHERE BugId = %(bugId)s", {
        'bugId': bugId
    })
    con.commit()


def deleteBug(bugId):
    # Delete bug with bugId

    # Old query
    # query = "DELETE FROM BugDetails WHERE BugId = {}".format(bugId)

    cursor.execute("DELETE FROM BugDetails WHERE BugId = %(bugId)s", {
        'bugId': bugId,
    })

    con.commit()


def addBug(title, appName, version, creator, assignedTo, details, priority, steps):
    # query = """INSERT INTO BugDetails (BugTitle, Application, AppVersion,
    #        Details, Steps, Priority, Assigned, CreatedBy, DayCreated)
    #        VALUES ('{}','{}','{}','{}','{}',{},'{}','{}', DATE(NOW()))""".format(title, appName, version, details, steps, priority, assignedTo, creator)
    # cursor.execute(query)

    # New query that should prevent SQL injection
    cursor.execute("INSERT INTO BugDetails (BugTitle, Application, AppVersion, Details, Steps, Priority, Assigned, CreatedBy, DayCreated) VALUES (%(title)s, %(appName)s, %(version)s, %(details)s, %(steps)s, %(priority)s, %(assignedTo)s, %(creator)s, DATE(NOW()));", {
        'title': title,
        'appName': appName,
        'version': version,
        'details': details,
        'steps': steps,
        'priority': priority,
        'assignedTo': assignedTo,
        'creator': creator
    })
    # Commit the change to db
    con.commit()
