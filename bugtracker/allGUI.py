import login
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication


class LoginPage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("\n"
                                 "#centralwidget{background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 purple, stop:1 orange);}\n"
                                 "\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)

        self.pushButton.setGeometry(QtCore.QRect(340, 470, 113, 32))
        self.pushButton.setObjectName("submitBtn")
        self.pushButton.clicked.connect(self.submitCredentials)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(340, 370, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 280, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 260, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 350, 60, 16))
        self.label_2.setObjectName("label_2")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(240, 70, 301, 81))
        self.title.setStyleSheet("#title{\n"
                                 "color: black;\n"
                                 "font-size: 53px; \n"
                                 "text-decoration: none;\n"
                                 "background-color: white; \n"
                                 "border: 3px solid black; \n"
                                 "border-radius: 10px;\n"
                                 "\n"
                                 "}")
        self.title.setObjectName("title")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Log In"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.title.setText(_translate("MainWindow", "Bug Tracker"))

    def submitCredentials(self):
        print("Username: " + self.lineEdit_2.text())
        print("Password: " + self.lineEdit.text())

        username = self.lineEdit_2.text()
        password = self.lineEdit_2.text()

        # Popup to alert of wrong username and password combo
        if(username != "admin"):
            self.wrongCredentials()
        else:
            if(login.checkValidLogin(username, password)):
                pass

    def wrongCredentials(self):
        # Simple popup message box to alert user when wrong login credentials is given
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Wrong Username and Password combination")

        x = msg.exec_()


class WelcomePage(object):
    # Main/Welcome page class
    # Shown when logged in successfully
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(783, 585)
        MainWindow.setMinimumSize(QtCore.QSize(783, 585))
        MainWindow.setMaximumSize(QtCore.QSize(783, 585))
        MainWindow.setStyleSheet(
            "#MainWindow {background-color: rgb(240, 243, 243);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sideBar = QtWidgets.QColumnView(self.centralwidget)
        self.sideBar.setGeometry(QtCore.QRect(0, 0, 111, 581))
        self.sideBar.setStyleSheet("background-color: rgb(235, 238, 238);\n"
                                   "color: black;")
        self.sideBar.setObjectName("sideBar")
        self.menuLabel = QtWidgets.QLabel(self.centralwidget)
        self.menuLabel.setGeometry(QtCore.QRect(10, 10, 91, 20))
        self.menuLabel.setStyleSheet("color: black;")
        self.menuLabel.setObjectName("menuLabel")
        self.dashBoardButton = QtWidgets.QPushButton(self.centralwidget)
        self.dashBoardButton.setGeometry(QtCore.QRect(10, 140, 91, 32))
        self.dashBoardButton.setStyleSheet("color: black;")
        self.dashBoardButton.setObjectName("dashBoardButton")
        self.viewBugsButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewBugsButton.setGeometry(QtCore.QRect(10, 180, 91, 32))
        self.viewBugsButton.setStyleSheet("color: black;")
        self.viewBugsButton.setObjectName("viewBugsButton")
        self.createBugButton = QtWidgets.QPushButton(self.centralwidget)
        self.createBugButton.setGeometry(QtCore.QRect(10, 220, 91, 32))
        self.createBugButton.setStyleSheet("color: black;")
        self.createBugButton.setObjectName("createBugButton")
        self.logOutButton = QtWidgets.QPushButton(self.centralwidget)
        self.logOutButton.setGeometry(QtCore.QRect(10, 470, 91, 32))
        self.logOutButton.setStyleSheet("color: black;\n"
                                        "")
        self.logOutButton.setObjectName("logOutButton")
        self.appDetailsTxt = QtWidgets.QLabel(self.centralwidget)
        self.appDetailsTxt.setGeometry(QtCore.QRect(140, 10, 611, 551))
        self.appDetailsTxt.setStyleSheet("color: rgb(0, 0, 0);")
        self.appDetailsTxt.setObjectName("appDetailsTxt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuLabel.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                          "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">MENU</span></p></body></html>"))
        self.dashBoardButton.setText(_translate("MainWindow", "Dashboard"))
        self.viewBugsButton.setText(_translate("MainWindow", "View Bugs"))
        self.createBugButton.setText(_translate("MainWindow", "Create Bug"))
        self.logOutButton.setText(_translate("MainWindow", "Log Out"))
        self.appDetailsTxt.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">Welcome to the Bug Tracker</span></p><p align=\"center\"><br/></p><p align=\"center\">Written using Python, data stored using MySQL and designed in QT Designer</p><p align=\"center\"><br/></p><p align=\"justify\"><br/></p><p align=\"justify\">This desktop app lets you track bugs. Different users have different access. Users can view bugs </p><p align=\"justify\">and mark them as completed. Moderators can aslo create, edit and delete bugs. And admins can </p><p align=\"justify\">aditionally create and delete users from the database. The data for all bugs is stored in a local </p><p align=\"justify\">MySQL database. </p><p align=\"justify\"><br/></p><p align=\"justify\">Use the sidebar on the left to navigate and get started. </p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = WelcomePage()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
