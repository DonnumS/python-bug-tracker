import sys
from datetime import datetime
import datetime
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import QTimer
from main_ui import Ui_MainWindow


from databaseFunctions import addNewUser, removeUser, checkValidLogin, adminCheck, moderatorCheck, getHigh, getMed, getLow, getComplete, getUncompleteData, getCompleteData, setBugComplete, deleteBug


class MainWindow:

    def __init__(self):
        # Store the username of logged in user
        self.currentLoggedIn = ""

        # Used to build table from sql data
        self.tableData = []
        self.rows = 0
        self.columns = 0

        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        # Start by showing the log in screen
        self.ui.stackedWidget.setCurrentWidget(self.ui.loginPage)

        # NAVIGATION BUTTONS:

        # Log in when we press log in button
        self.ui.loginButton.clicked.connect(self.tryLoggin)

        # Log out when we press log out button
        self.ui.logoutButton.clicked.connect(self.logOut)
        self.ui.logoutButton_2.clicked.connect(self.logOut)

        # Buttons that navigate to dashboard
        self.ui.dashboardButton.clicked.connect(self.navigateDashboard)
        self.ui.dashboardButton_2.clicked.connect(self.navigateDashboard)
        self.ui.backButton.clicked.connect(self.navigateDashboard)
        self.ui.createBugBack.clicked.connect(self.navigateDashboard)
        self.ui.returnFromUserToDashboard.clicked.connect(
            self.navigateDashboard)
        self.ui.returnToDashboard.clicked.connect(self.navigateDashboard)

        # Buttons that navigate to viewBugsPage
        self.ui.viewBugsButton.clicked.connect(self.navigateViewBugs)
        self.ui.viewBugsButton_2.clicked.connect(self.navigateViewBugs)

        # Buttons that navigate to createBug page
        self.ui.createBugButton.clicked.connect(self.navigateCreateBugs)
        self.ui.createBugButton_2.clicked.connect(self.navigateCreateBugs)
        self.ui.addBugButton.clicked.connect(self.navigateCreateBugs)

        # Buttons that navigate to editBugStatus page
        self.ui.editBugStatus.clicked.connect(self.navigateEditStatusPage)

        # Buttons that navigate to User page
        self.ui.userButton.clicked.connect(self.navigateUserPage)
        self.ui.userButton_2.clicked.connect(self.navigateUserPage)

        # ACTION BUTTONS:

        # Buttons that loads data from sql database (uncompleted or completed bugs)
        self.ui.loadTableButton.clicked.connect(self.loadUncomplete)
        self.ui.loadCompleteTable.clicked.connect(self.loadComplete)

        # Buttons that submits/creates new bug

        # Buttons that marks bug as complete
        self.ui.markBugAsComplete.clicked.connect(self.bugCompleted)

        # Buttons that deletes bug from database
        self.ui.deleteBugFromDatabase.clicked.connect(self.bugDelete)

        # Buttons that adds new user to database
        self.ui.submitNewUser.clicked.connect(self.addUserToDb)
        self.ui.submitNewUser.clicked.connect(self.navigateDashboard)

        # Buttons that removes user from database
        self.ui.deleteUserButton.clicked.connect(self.removeUserFromDb)
        self.ui.deleteUserButton.clicked.connect(self.navigateDashboard)

    def show(self):
        self.main_win.show()

    def tryLoggin(self):
        # Get input for login
        username = self.ui.userNameInput.text()
        password = self.ui.passwordInput.text()

        # Set the username of the currently logged in
        self.currentLoggedIn = username

        # Either login provided correct credentials, or display error
        if(checkValidLogin(username, password)):
            # Clear password from line edit
            self.ui.passwordInput.clear()
            self.ui.stackedWidget.setCurrentWidget(self.ui.welcomePage)
        else:
            # Clear password from line edit
            self.ui.passwordInput.clear()
            self.wrongCredentials()

    def wrongCredentials(self):
        # Simple popup message box to alert user when wrong login credentials is given
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Wrong Username and Password combination")

        x = msg.exec_()

    def notAccess(self):
        # Simple popup message box to alert that user does not have access to certain parts of the app
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("You do not have correct privileges")

        x = msg.exec_()

    # Navigate to log in screen when we press logout
    def logOut(self):
        # Simply navigate to the loginPage after setting currentLoggedIn to an empty string
        self.currentLoggedIn = ""
        self.ui.stackedWidget.setCurrentWidget(self.ui.loginPage)

    def navigateDashboard(self):
        # First we update the dashboard bug counters
        self.ui.highCount.setText(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">{highCount}</span></p></body></html>".format(highCount=getHigh()))
        self.ui.medCount.setText(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">{medCount}</span></p></body></html>".format(medCount=getMed()))
        self.ui.lowCount.setText(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">{lowCount}</span></p></body></html>".format(lowCount=getLow()))
        self.ui.completeCount.setText(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">{completeCount}</span></p></body></html>".format(completeCount=getComplete()))
        # No restrictions when navigating to the dashboard
        self.ui.stackedWidget.setCurrentWidget(self.ui.dashBoardPage)

    def navigateViewBugs(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.viewBugsPage)

    def navigateCreateBugs(self):
        # Check if user has role admin or moderator

        if(adminCheck(self.currentLoggedIn) or moderatorCheck(self.currentLoggedIn)):
            # Navigate to page is user has correct roles
            self.ui.stackedWidget.setCurrentWidget(self.ui.createBugsPage)
        else:
            # Display error message if user does not have access
            self.notAccess()

    def navigateUserPage(self):
        # Check if user has role admin
        if(adminCheck(self.currentLoggedIn)):
            # Navigate to user page if user is admin
            self.ui.stackedWidget.setCurrentWidget(self.ui.userPage)
        else:
            # Display error message if user does not have access
            self.notAccess()

    def navigateEditStatusPage(self):
        # Check if user has role admin or moderator
        if(adminCheck(self.currentLoggedIn) or moderatorCheck(self.currentLoggedIn)):
            # Navigate to edit status page
            self.ui.stackedWidget.setCurrentWidget(self.ui.editBugStatusPage)
        else:
            # Display error message if user does not have access
            self.notAccess()

    def loadUncomplete(self):
        # Retrieve data from sql query and get columns and rows length
        self.tableData = getUncompleteData()
        self.rows = len(self.tableData)
        self.columns = len(self.tableData[0])

        # Clear table incase it hase been filled with data earlier
        self.ui.bugTable.clear()

        # Set the row and column count of the table to display
        self.ui.bugTable.setRowCount = self.rows
        self.ui.bugTable.setColumnCOunt = self.columns

        # Add correct labels to each of the columns and hide the vertical labels
        self.ui.bugTable.setHorizontalHeaderLabels(
            "BugId;Title;Application;Version;Details;Steps;Priority;AssignedTo;CreatedBy;DayCreated".split(";"))

        # Resize rows so all information can be viewed
        for i in range(100):
            self.ui.bugTable.setRowHeight(i, 100)

        # Insert data in table
        for row in range(self.rows):
            for column in range(self.columns):
                # Check if value datatime, if True convert to string
                if isinstance(self.tableData[row][column], datetime.date):
                    self.ui.bugTable.setItem(row, column, QTableWidgetItem(
                        (self.tableData[row][column].strftime('%d/%m/%Y'))))
                else:
                    self.ui.bugTable.setItem(
                        row, column, QTableWidgetItem(str(self.tableData[row][column])))

    def loadComplete(self):
        # Retrieve data from sql query and get columns and rows length
        self.tableData = getCompleteData()
        self.rows = len(self.tableData)
        self.columns = len(self.tableData[0])

        # Clear table incase it hase been filled with data earlier
        self.ui.bugTable.clear()

        # Set the row and column count of the table to display
        self.ui.bugTable.setRowCount = self.rows
        self.ui.bugTable.setColumnCOunt = self.columns

        # Add correct labels to each of the columns
        self.ui.bugTable.setHorizontalHeaderLabels(
            "BugId;Title;Application;Version;Details;Steps;Priority;AssignedTo;CreatedBy;DayCreated".split(";"))

        # Resize rows so all information can be viewed
        for i in range(100):
            self.ui.bugTable.setRowHeight(i, 100)

        # Insert data in table
        for row in range(self.rows):
            for column in range(self.columns):
                # Check if value datatime, if True convert to string
                if isinstance(self.tableData[row][column], datetime.date):
                    self.ui.bugTable.setItem(row, column, QTableWidgetItem(
                        (self.tableData[row][column].strftime('%d/%m/%Y'))))
                else:
                    self.ui.bugTable.setItem(
                        row, column, QTableWidgetItem(str(self.tableData[row][column])))

    def bugCompleted(self):
        bugId = int(self.ui.editStatusBugId.text())
        self.ui.editStatusBugId.clear()
        setBugComplete(bugId)

    def bugDelete(self):
        bugId = int(self.ui.editStatusBugId.text())
        self.ui.editStatusBugId.clear()
        deleteBug(bugId)

    def addUserToDb(self):

        # Get the different inputs
        name = self.ui.addNameInput.text()
        username = self.ui.addUsernameInput.text()
        password = self.ui.addPasswordInput.text()
        iD = self.ui.addIDInput.text()
        email = self.ui.addEmailInput.text()
        if(email == ""):
            email = "Not Specified"

        role = ""
        # Get role selected
        if(self.ui.radioAdmin.isChecked()):
            role = "admin"
        elif(self.ui.radioModerator.isChecked()):
            role = "moderator"
        else:
            role = "user"

        # For debugging purposes
        # print("Added new user with this info\nName: {}\nUsername: {}\nPassword: {}\nID: {}\nEmail: {}\nRole: {}".format(
        #   name, username, password, iD, email, role))

        # Add user to database with login information
        addNewUser(name, username, password, iD, email, role)
        self.ui.addNameInput.clear()
        self.ui.addUsernameInput.clear()
        self.ui.addPasswordInput.clear()
        self.ui.addIDInput.clear()
        self.ui.addEmailInput.clear()

    def removeUserFromDb(self):
        iD = self.ui.deleteUserId.text()

        # For debuggin purposes
        # print("Deleted user with employee id {} from database".format(iD))

        # Pass iD to database functions that removes employee with employee id = iD
        removeUser(iD)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
