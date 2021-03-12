import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer

from main_ui import Ui_MainWindow

from login import checkValidLogin


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        # Start by showing the log in screen
        self.ui.stackedWidget.setCurrentWidget(self.ui.loginPage)

        # Log in when we press log in button
        self.ui.loginButton.clicked.connect(self.tryLoggin)

        # Log out when we press log out button
        self.ui.logoutButton.clicked.connect(self.logOut)
        self.ui.logoutButton_2.clicked.connect(self.logOut)

        # Buttons that navigate to dashboard
        self.ui.dashboardButton.clicked.connect(self.navigateDashboard)
        self.ui.dashboardButton_2.clicked.connect(self.navigateDashboard)

    def show(self):
        self.main_win.show()

    def tryLoggin(self):
        # Get input for login
        username = self.ui.userNameInput.text()
        password = self.ui.passwordInput.text()

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

    # Navigate to log in screen when we press logout
    def logOut(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.loginPage)

    def navigateDashboard(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.dashBoardPage)

    def navigateViewBugs(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.viewBugsPage)

    def addUser(self):
        pass

    def removeUser(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
