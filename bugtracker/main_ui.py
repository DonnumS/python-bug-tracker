# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stackedUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from databaseFunctions import getHigh


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 550)
        MainWindow.setMinimumSize(QtCore.QSize(800, 550))
        MainWindow.setMaximumSize(QtCore.QSize(800, 550))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-1, -1, 801, 551))
        self.stackedWidget.setStyleSheet("#dashBoardPage{background-color: rgb(239, 242, 242); }\n"
                                         "#welcomePage{background-color: rgb(239, 242, 242); }\n"
                                         "#viewBugsPage{background-color: rgb(239, 242, 242);}\n"
                                         "#editBugStatusPage{background-color: rgb(239, 242, 242);}\n"
                                         "#createBugsPage{background-color: rgb(239, 242, 242);}\n"
                                         "#userPage{background-color: rgb(239, 242, 242);}\n"
                                         "\n"
                                         "")
        self.stackedWidget.setObjectName("stackedWidget")
        self.loginPage = QtWidgets.QWidget()
        self.loginPage.setStyleSheet(
            "#loginPage{background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 purple, stop:1 orange);}")
        self.loginPage.setObjectName("loginPage")
        self.userNameInput = QtWidgets.QLineEdit(self.loginPage)
        self.userNameInput.setGeometry(QtCore.QRect(320, 280, 171, 21))
        self.userNameInput.setObjectName("userNameInput")
        self.passwordInput = QtWidgets.QLineEdit(self.loginPage)
        self.passwordInput.setGeometry(QtCore.QRect(320, 370, 171, 21))
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setObjectName("passwordInput")
        self.userNameLabel = QtWidgets.QLabel(self.loginPage)
        self.userNameLabel.setGeometry(QtCore.QRect(320, 250, 171, 20))
        self.userNameLabel.setStyleSheet("color: white;\n"
                                         "")
        self.userNameLabel.setObjectName("userNameLabel")
        self.passwordLabel = QtWidgets.QLabel(self.loginPage)
        self.passwordLabel.setGeometry(QtCore.QRect(320, 340, 171, 20))
        self.passwordLabel.setStyleSheet("color: white;")
        self.passwordLabel.setOpenExternalLinks(False)
        self.passwordLabel.setObjectName("passwordLabel")
        self.loginButton = QtWidgets.QPushButton(self.loginPage)
        self.loginButton.setGeometry(QtCore.QRect(350, 430, 113, 32))
        self.loginButton.setStyleSheet("color: black;")
        self.loginButton.setObjectName("loginButton")
        self.loginTitle = QtWidgets.QFrame(self.loginPage)
        self.loginTitle.setGeometry(QtCore.QRect(260, 120, 291, 80))
        self.loginTitle.setStyleSheet("#loginTitle{background-color: white;\n"
                                      "border: 2px solid black;\n"
                                      "border-radius: 25px;}")
        self.loginTitle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loginTitle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loginTitle.setObjectName("loginTitle")
        self.label = QtWidgets.QLabel(self.loginTitle)
        self.label.setGeometry(QtCore.QRect(9, 10, 271, 61))
        self.label.setStyleSheet("color: black;")
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.loginPage)
        self.welcomePage = QtWidgets.QWidget()
        self.welcomePage.setStyleSheet("")
        self.welcomePage.setObjectName("welcomePage")
        self.sideBar = QtWidgets.QWidget(self.welcomePage)
        self.sideBar.setGeometry(QtCore.QRect(-1, -11, 101, 571))
        self.sideBar.setStyleSheet(
            "#sideBar{background-color: rgb(221, 223, 223); border: 1px solid black;}")
        self.sideBar.setObjectName("sideBar")
        self.menuLabel = QtWidgets.QLabel(self.sideBar)
        self.menuLabel.setGeometry(QtCore.QRect(0, 40, 101, 20))
        self.menuLabel.setStyleSheet("color: black;")
        self.menuLabel.setObjectName("menuLabel")
        self.dashboardButton = QtWidgets.QPushButton(self.sideBar)
        self.dashboardButton.setGeometry(QtCore.QRect(0, 120, 101, 32))
        self.dashboardButton.setStyleSheet("color: black;")
        self.dashboardButton.setObjectName("dashboardButton")
        self.viewBugsButton = QtWidgets.QPushButton(self.sideBar)
        self.viewBugsButton.setGeometry(QtCore.QRect(0, 160, 101, 32))
        self.viewBugsButton.setStyleSheet("color: black;")
        self.viewBugsButton.setObjectName("viewBugsButton")
        self.createBugButton = QtWidgets.QPushButton(self.sideBar)
        self.createBugButton.setGeometry(QtCore.QRect(0, 200, 101, 32))
        self.createBugButton.setStyleSheet("color: black;")
        self.createBugButton.setObjectName("createBugButton")
        self.userButton = QtWidgets.QPushButton(self.sideBar)
        self.userButton.setGeometry(QtCore.QRect(0, 240, 101, 32))
        self.userButton.setStyleSheet("color: black;")
        self.userButton.setObjectName("userButton")
        self.logoutButton = QtWidgets.QPushButton(self.sideBar)
        self.logoutButton.setGeometry(QtCore.QRect(0, 480, 101, 32))
        self.logoutButton.setStyleSheet("color: black;")
        self.logoutButton.setObjectName("logoutButton")
        self.label_2 = QtWidgets.QLabel(self.welcomePage)
        self.label_2.setGeometry(QtCore.QRect(119, 25, 661, 511))
        self.label_2.setStyleSheet("#label_2{color: black;}")
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.welcomePage)
        self.dashBoardPage = QtWidgets.QWidget()
        self.dashBoardPage.setObjectName("dashBoardPage")
        self.sideBar_2 = QtWidgets.QWidget(self.dashBoardPage)
        self.sideBar_2.setGeometry(QtCore.QRect(0, -10, 101, 571))
        self.sideBar_2.setStyleSheet(
            "#sideBar_2{background-color: rgb(221, 223, 223); border: 1px solid black;}")
        self.sideBar_2.setObjectName("sideBar_2")
        self.menuLabel_2 = QtWidgets.QLabel(self.sideBar_2)
        self.menuLabel_2.setGeometry(QtCore.QRect(0, 40, 101, 20))
        self.menuLabel_2.setStyleSheet("color: black;")
        self.menuLabel_2.setObjectName("menuLabel_2")
        self.dashboardButton_2 = QtWidgets.QPushButton(self.sideBar_2)
        self.dashboardButton_2.setGeometry(QtCore.QRect(0, 120, 101, 32))
        self.dashboardButton_2.setStyleSheet("color: black;")
        self.dashboardButton_2.setObjectName("dashboardButton_2")
        self.viewBugsButton_2 = QtWidgets.QPushButton(self.sideBar_2)
        self.viewBugsButton_2.setGeometry(QtCore.QRect(0, 160, 101, 32))
        self.viewBugsButton_2.setStyleSheet("color: black;")
        self.viewBugsButton_2.setObjectName("viewBugsButton_2")
        self.createBugButton_2 = QtWidgets.QPushButton(self.sideBar_2)
        self.createBugButton_2.setGeometry(QtCore.QRect(0, 200, 101, 32))
        self.createBugButton_2.setStyleSheet("color: black;")
        self.createBugButton_2.setObjectName("createBugButton_2")
        self.userButton_2 = QtWidgets.QPushButton(self.sideBar_2)
        self.userButton_2.setGeometry(QtCore.QRect(0, 240, 101, 32))
        self.userButton_2.setStyleSheet("color: black;")
        self.userButton_2.setObjectName("userButton_2")
        self.logoutButton_2 = QtWidgets.QPushButton(self.sideBar_2)
        self.logoutButton_2.setGeometry(QtCore.QRect(0, 480, 101, 32))
        self.logoutButton_2.setStyleSheet("color: black;")
        self.logoutButton_2.setObjectName("logoutButton_2")
        self.highCard = QtWidgets.QWidget(self.dashBoardPage)
        self.highCard.setGeometry(QtCore.QRect(150, 40, 271, 191))
        self.highCard.setStyleSheet("#highCard{background-color: rgb(227, 230, 229);\n"
                                    "color: black;\n"
                                    "border: 1px solid balck;\n"
                                    "border-radius: 5px;}")
        self.highCard.setObjectName("highCard")
        self.highLabel = QtWidgets.QLabel(self.highCard)
        self.highLabel.setGeometry(QtCore.QRect(-1, 10, 271, 51))
        self.highLabel.setStyleSheet("color: black;")
        self.highLabel.setObjectName("highLabel")
        self.highCount = QtWidgets.QLabel(self.highCard)
        self.highCount.setGeometry(QtCore.QRect(0, 70, 271, 91))
        self.highCount.setStyleSheet("color: red;")
        self.highCount.setObjectName("highCount")
        self.medCard = QtWidgets.QWidget(self.dashBoardPage)
        self.medCard.setGeometry(QtCore.QRect(480, 40, 271, 191))
        self.medCard.setStyleSheet("#medCard{background-color: rgb(227, 230, 229);\n"
                                   "color: black;\n"
                                   "border: 1px solid balck;\n"
                                   "border-radius: 5px;}")
        self.medCard.setObjectName("medCard")
        self.medLabel = QtWidgets.QLabel(self.medCard)
        self.medLabel.setGeometry(QtCore.QRect(0, 10, 271, 61))
        self.medLabel.setStyleSheet("color: black;\n"
                                    "")
        self.medLabel.setObjectName("medLabel")
        self.medCount = QtWidgets.QLabel(self.medCard)
        self.medCount.setGeometry(QtCore.QRect(0, 70, 271, 91))
        self.medCount.setStyleSheet("color: yellow;")
        self.medCount.setObjectName("medCount")
        self.lowCard = QtWidgets.QWidget(self.dashBoardPage)
        self.lowCard.setGeometry(QtCore.QRect(150, 290, 271, 191))
        self.lowCard.setStyleSheet("#lowCard{background-color: rgb(227, 230, 229);\n"
                                   "color: black;\n"
                                   "border: 1px solid balck;\n"
                                   "border-radius: 5px;\n"
                                   "}")
        self.lowCard.setObjectName("lowCard")
        self.lowLabel = QtWidgets.QLabel(self.lowCard)
        self.lowLabel.setGeometry(QtCore.QRect(0, 10, 271, 61))
        self.lowLabel.setStyleSheet("color: black;")
        self.lowLabel.setObjectName("lowLabel")
        self.lowCount = QtWidgets.QLabel(self.lowCard)
        self.lowCount.setGeometry(QtCore.QRect(0, 70, 271, 91))
        self.lowCount.setStyleSheet("color: green;")
        self.lowCount.setObjectName("lowCount")
        self.completeCard = QtWidgets.QWidget(self.dashBoardPage)
        self.completeCard.setGeometry(QtCore.QRect(480, 290, 271, 191))
        self.completeCard.setStyleSheet("#completeCard{background-color: rgb(227, 230, 229);\n"
                                        "color: black;\n"
                                        "border: 1px solid balck;\n"
                                        "border-radius: 5px;\n"
                                        "}")
        self.completeCard.setObjectName("completeCard")
        self.completeLabel = QtWidgets.QLabel(self.completeCard)
        self.completeLabel.setGeometry(QtCore.QRect(0, 10, 271, 61))
        self.completeLabel.setStyleSheet("color: black;")
        self.completeLabel.setObjectName("completeLabel")
        self.completeCount = QtWidgets.QLabel(self.completeCard)
        self.completeCount.setGeometry(QtCore.QRect(0, 70, 271, 91))
        self.completeCount.setStyleSheet("color: rgb(67, 169, 255);")
        self.completeCount.setObjectName("completeCount")
        self.stackedWidget.addWidget(self.dashBoardPage)
        self.viewBugsPage = QtWidgets.QWidget()
        self.viewBugsPage.setStyleSheet("")
        self.viewBugsPage.setObjectName("viewBugsPage")
        self.bugTable = QtWidgets.QTableWidget(self.viewBugsPage)
        self.bugTable.setGeometry(QtCore.QRect(40, 40, 721, 371))
        self.bugTable.setStyleSheet("")
        self.bugTable.setRowCount(100)
        self.bugTable.setColumnCount(10)
        self.bugTable.setObjectName("bugTable")
        self.loadTableButton = QtWidgets.QPushButton(self.viewBugsPage)
        self.loadTableButton.setGeometry(QtCore.QRect(40, 420, 113, 32))
        self.loadTableButton.setStyleSheet("color: black;")
        self.loadTableButton.setObjectName("loadTableButton")
        self.backButton = QtWidgets.QPushButton(self.viewBugsPage)
        self.backButton.setGeometry(QtCore.QRect(160, 500, 151, 32))
        self.backButton.setStyleSheet("color: black;")
        self.backButton.setObjectName("backButton")
        self.bugTableTip = QtWidgets.QLabel(self.viewBugsPage)
        self.bugTableTip.setGeometry(QtCore.QRect(330, 430, 391, 91))
        self.bugTableTip.setStyleSheet("color: black;")
        self.bugTableTip.setObjectName("bugTableTip")
        self.editBugStatus = QtWidgets.QPushButton(self.viewBugsPage)
        self.editBugStatus.setGeometry(QtCore.QRect(160, 460, 151, 32))
        self.editBugStatus.setStyleSheet("color: black;")
        self.editBugStatus.setObjectName("editBugStatus")
        self.loadCompleteTable = QtWidgets.QPushButton(self.viewBugsPage)
        self.loadCompleteTable.setGeometry(QtCore.QRect(160, 420, 151, 32))
        self.loadCompleteTable.setStyleSheet("color: black;")
        self.loadCompleteTable.setObjectName("loadCompleteTable")
        self.addBugButton = QtWidgets.QPushButton(self.viewBugsPage)
        self.addBugButton.setGeometry(QtCore.QRect(40, 460, 111, 32))
        self.addBugButton.setStyleSheet("color: black;")
        self.addBugButton.setObjectName("addBugButton")
        self.tableTitle = QtWidgets.QLabel(self.viewBugsPage)
        self.tableTitle.setGeometry(QtCore.QRect(259, 10, 281, 20))
        self.tableTitle.setStyleSheet("color: black;")
        self.tableTitle.setObjectName("tableTitle")
        self.stackedWidget.addWidget(self.viewBugsPage)
        self.editBugStatusPage = QtWidgets.QWidget()
        self.editBugStatusPage.setObjectName("editBugStatusPage")
        self.label_17 = QtWidgets.QLabel(self.editBugStatusPage)
        self.label_17.setGeometry(QtCore.QRect(0, 20, 801, 61))
        self.label_17.setStyleSheet("color: black;")
        self.label_17.setObjectName("label_17")
        self.editStatusBugId = QtWidgets.QLineEdit(self.editBugStatusPage)
        self.editStatusBugId.setGeometry(QtCore.QRect(190, 100, 71, 21))
        self.editStatusBugId.setStyleSheet("background-color: white;\n"
                                           "color: black;")
        self.editStatusBugId.setObjectName("editStatusBugId")
        self.label_18 = QtWidgets.QLabel(self.editBugStatusPage)
        self.label_18.setGeometry(QtCore.QRect(40, 100, 141, 20))
        self.label_18.setStyleSheet("color: black;")
        self.label_18.setObjectName("label_18")
        self.markBugAsComplete = QtWidgets.QPushButton(self.editBugStatusPage)
        self.markBugAsComplete.setGeometry(QtCore.QRect(130, 160, 201, 32))
        self.markBugAsComplete.setStyleSheet("color: black;")
        self.markBugAsComplete.setObjectName("markBugAsComplete")
        self.deleteBugFromDatabase = QtWidgets.QPushButton(
            self.editBugStatusPage)
        self.deleteBugFromDatabase.setGeometry(QtCore.QRect(130, 200, 201, 32))
        self.deleteBugFromDatabase.setStyleSheet("color: black;")
        self.deleteBugFromDatabase.setObjectName("deleteBugFromDatabase")
        self.returnToDashboard = QtWidgets.QPushButton(self.editBugStatusPage)
        self.returnToDashboard.setGeometry(QtCore.QRect(130, 240, 201, 32))
        self.returnToDashboard.setStyleSheet("color: black;")
        self.returnToDashboard.setObjectName("returnToDashboard")
        self.editStatusToolTip = QtWidgets.QLabel(self.editBugStatusPage)
        self.editStatusToolTip.setGeometry(QtCore.QRect(370, 70, 351, 201))
        self.editStatusToolTip.setStyleSheet("color: black;")
        self.editStatusToolTip.setObjectName("editStatusToolTip")
        self.stackedWidget.addWidget(self.editBugStatusPage)
        self.createBugsPage = QtWidgets.QWidget()
        self.createBugsPage.setObjectName("createBugsPage")
        self.inputBugTitle = QtWidgets.QLineEdit(self.createBugsPage)
        self.inputBugTitle.setGeometry(QtCore.QRect(130, 60, 241, 21))
        self.inputBugTitle.setStyleSheet("background-color: white;\n"
                                         "color: black;")
        self.inputBugTitle.setText("")
        self.inputBugTitle.setObjectName("inputBugTitle")
        self.inputAppName = QtWidgets.QLineEdit(self.createBugsPage)
        self.inputAppName.setGeometry(QtCore.QRect(130, 120, 241, 21))
        self.inputAppName.setStyleSheet("background-color: white;\n"
                                        "color: black;")
        self.inputAppName.setText("")
        self.inputAppName.setObjectName("inputAppName")
        self.createBugBack = QtWidgets.QPushButton(self.createBugsPage)
        self.createBugBack.setGeometry(QtCore.QRect(460, 470, 121, 31))
        self.createBugBack.setStyleSheet("color: black;")
        self.createBugBack.setObjectName("createBugBack")
        self.createBugSubmit = QtWidgets.QPushButton(self.createBugsPage)
        self.createBugSubmit.setGeometry(QtCore.QRect(230, 470, 121, 31))
        self.createBugSubmit.setStyleSheet("color: black;")
        self.createBugSubmit.setObjectName("createBugSubmit")
        self.inputSteps = QtWidgets.QTextEdit(self.createBugsPage)
        self.inputSteps.setGeometry(QtCore.QRect(130, 310, 541, 131))
        self.inputSteps.setStyleSheet("background-color: white;\n"
                                      "color: black;")
        self.inputSteps.setObjectName("inputSteps")
        self.inputVersion = QtWidgets.QLineEdit(self.createBugsPage)
        self.inputVersion.setGeometry(QtCore.QRect(130, 180, 241, 21))
        self.inputVersion.setStyleSheet("background-color: white;\n"
                                        "color: black;")
        self.inputVersion.setText("")
        self.inputVersion.setObjectName("inputVersion")
        self.inputCreatedBy = QtWidgets.QLineEdit(self.createBugsPage)
        self.inputCreatedBy.setGeometry(QtCore.QRect(430, 60, 241, 21))
        self.inputCreatedBy.setStyleSheet("background-color: white;\n"
                                          "color: black;")
        self.inputCreatedBy.setText("")
        self.inputCreatedBy.setObjectName("inputCreatedBy")
        self.inputAssignedTo = QtWidgets.QLineEdit(self.createBugsPage)
        self.inputAssignedTo.setGeometry(QtCore.QRect(430, 120, 241, 21))
        self.inputAssignedTo.setStyleSheet("background-color: white;\n"
                                           "color: black;")
        self.inputAssignedTo.setText("")
        self.inputAssignedTo.setObjectName("inputAssignedTo")
        self.inputDetails = QtWidgets.QLineEdit(self.createBugsPage)
        self.inputDetails.setGeometry(QtCore.QRect(430, 180, 241, 21))
        self.inputDetails.setStyleSheet("background-color: white;\n"
                                        "color: black;")
        self.inputDetails.setText("")
        self.inputDetails.setObjectName("inputDetails")
        self.inputPriority = QtWidgets.QSpinBox(self.createBugsPage)
        self.inputPriority.setGeometry(QtCore.QRect(130, 240, 48, 24))
        self.inputPriority.setStyleSheet("background-color: white;\n"
                                         "color: black;")
        self.inputPriority.setMinimum(1)
        self.inputPriority.setMaximum(3)
        self.inputPriority.setObjectName("inputPriority")
        self.label_3 = QtWidgets.QLabel(self.createBugsPage)
        self.label_3.setGeometry(QtCore.QRect(130, 40, 60, 16))
        self.label_3.setStyleSheet("color: black;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.createBugsPage)
        self.label_4.setGeometry(QtCore.QRect(130, 100, 111, 16))
        self.label_4.setStyleSheet("color: black;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.createBugsPage)
        self.label_5.setGeometry(QtCore.QRect(130, 160, 60, 16))
        self.label_5.setStyleSheet("color: black;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.createBugsPage)
        self.label_6.setGeometry(QtCore.QRect(130, 220, 81, 16))
        self.label_6.setStyleSheet("color: black;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.createBugsPage)
        self.label_7.setGeometry(QtCore.QRect(130, 290, 131, 16))
        self.label_7.setStyleSheet("color: black;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.createBugsPage)
        self.label_8.setGeometry(QtCore.QRect(430, 160, 161, 16))
        self.label_8.setStyleSheet("color: black;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.createBugsPage)
        self.label_9.setGeometry(QtCore.QRect(430, 100, 81, 16))
        self.label_9.setStyleSheet("color: black;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.createBugsPage)
        self.label_10.setGeometry(QtCore.QRect(430, 40, 71, 16))
        self.label_10.setStyleSheet("color: black;")
        self.label_10.setObjectName("label_10")
        self.stackedWidget.addWidget(self.createBugsPage)
        self.userPage = QtWidgets.QWidget()
        self.userPage.setObjectName("userPage")
        self.dividerBox = QtWidgets.QWidget(self.userPage)
        self.dividerBox.setGeometry(QtCore.QRect(-40, -20, 441, 611))
        self.dividerBox.setStyleSheet("#dividerBox{border: 2px solid black;}")
        self.dividerBox.setObjectName("dividerBox")
        self.addTitle = QtWidgets.QLabel(self.dividerBox)
        self.addTitle.setGeometry(QtCore.QRect(40, 30, 401, 71))
        self.addTitle.setStyleSheet("color: black;")
        self.addTitle.setObjectName("addTitle")
        self.addNameInput = QtWidgets.QLineEdit(self.dividerBox)
        self.addNameInput.setGeometry(QtCore.QRect(180, 130, 113, 21))
        self.addNameInput.setStyleSheet("background-color: white;\n"
                                        "color: black;")
        self.addNameInput.setObjectName("addNameInput")
        self.addUsernameInput = QtWidgets.QLineEdit(self.dividerBox)
        self.addUsernameInput.setGeometry(QtCore.QRect(180, 170, 113, 21))
        self.addUsernameInput.setStyleSheet("background-color: white;\n"
                                            "color: black;")
        self.addUsernameInput.setObjectName("addUsernameInput")
        self.addPasswordInput = QtWidgets.QLineEdit(self.dividerBox)
        self.addPasswordInput.setGeometry(QtCore.QRect(180, 210, 113, 21))
        self.addPasswordInput.setStyleSheet("background-color: white;\n"
                                            "color: black;")
        self.addPasswordInput.setObjectName("addPasswordInput")
        self.addIDInput = QtWidgets.QLineEdit(self.dividerBox)
        self.addIDInput.setGeometry(QtCore.QRect(180, 250, 113, 21))
        self.addIDInput.setStyleSheet("background-color: white;\n"
                                      "color: black;")
        self.addIDInput.setObjectName("addIDInput")
        self.addEmailInput = QtWidgets.QLineEdit(self.dividerBox)
        self.addEmailInput.setGeometry(QtCore.QRect(180, 290, 113, 21))
        self.addEmailInput.setStyleSheet("background-color: white;\n"
                                         "color: black;")
        self.addEmailInput.setObjectName("addEmailInput")
        self.label_11 = QtWidgets.QLabel(self.dividerBox)
        self.label_11.setGeometry(QtCore.QRect(39, 130, 131, 20))
        self.label_11.setStyleSheet("color: black;")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.dividerBox)
        self.label_12.setGeometry(QtCore.QRect(39, 170, 131, 20))
        self.label_12.setStyleSheet("color: black;")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.dividerBox)
        self.label_13.setGeometry(QtCore.QRect(39, 210, 131, 20))
        self.label_13.setStyleSheet("color: black;")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.dividerBox)
        self.label_14.setGeometry(QtCore.QRect(39, 250, 131, 20))
        self.label_14.setStyleSheet("color: black;")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.dividerBox)
        self.label_15.setGeometry(QtCore.QRect(39, 290, 131, 20))
        self.label_15.setStyleSheet("color: black;")
        self.label_15.setObjectName("label_15")
        self.radioAdmin = QtWidgets.QRadioButton(self.dividerBox)
        self.radioAdmin.setGeometry(QtCore.QRect(80, 350, 100, 20))
        self.radioAdmin.setStyleSheet("color: black;")
        self.radioAdmin.setObjectName("radioAdmin")
        self.radioModerator = QtWidgets.QRadioButton(self.dividerBox)
        self.radioModerator.setGeometry(QtCore.QRect(80, 380, 100, 20))
        self.radioModerator.setStyleSheet("color: black;")
        self.radioModerator.setObjectName("radioModerator")
        self.radioNormal = QtWidgets.QRadioButton(self.dividerBox)
        self.radioNormal.setGeometry(QtCore.QRect(80, 410, 100, 20))
        self.radioNormal.setStyleSheet("color: black;")
        self.radioNormal.setObjectName("radioNormal")
        self.submitNewUser = QtWidgets.QPushButton(self.dividerBox)
        self.submitNewUser.setGeometry(QtCore.QRect(80, 460, 113, 32))
        self.submitNewUser.setStyleSheet("color: black;")
        self.submitNewUser.setObjectName("submitNewUser")
        self.returnFromUserToDashboard = QtWidgets.QPushButton(self.dividerBox)
        self.returnFromUserToDashboard.setGeometry(
            QtCore.QRect(290, 460, 113, 32))
        self.returnFromUserToDashboard.setStyleSheet("color: black;")
        self.returnFromUserToDashboard.setObjectName(
            "returnFromUserToDashboard")
        self.deleteUserTitle = QtWidgets.QLabel(self.userPage)
        self.deleteUserTitle.setGeometry(QtCore.QRect(400, 10, 401, 71))
        self.deleteUserTitle.setStyleSheet("color: black;")
        self.deleteUserTitle.setObjectName("deleteUserTitle")
        self.deleteUserButton = QtWidgets.QPushButton(self.userPage)
        self.deleteUserButton.setGeometry(QtCore.QRect(540, 160, 113, 32))
        self.deleteUserButton.setStyleSheet("color: black;")
        self.deleteUserButton.setObjectName("deleteUserButton")
        self.deleteUserId = QtWidgets.QLineEdit(self.userPage)
        self.deleteUserId.setGeometry(QtCore.QRect(540, 110, 113, 21))
        self.deleteUserId.setStyleSheet("background-color: white;\n"
                                        "color: black;")
        self.deleteUserId.setObjectName("deleteUserId")
        self.label_16 = QtWidgets.QLabel(self.userPage)
        self.label_16.setGeometry(QtCore.QRect(390, 110, 141, 20))
        self.label_16.setStyleSheet("color: black;")
        self.label_16.setObjectName("label_16")
        self.stackedWidget.addWidget(self.userPage)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.userNameLabel.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\">USERNAME</p></body></html>"))
        self.passwordLabel.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\">PASSWORD</p><p align=\"center\"><br/></p></body></html>"))
        self.loginButton.setText(_translate("MainWindow", "Log In"))
        self.label.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">BUG TRACKER</span></p></body></html>"))
        self.menuLabel.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">MENU</span></p></body></html>"))
        self.dashboardButton.setText(_translate("MainWindow", "Dashboard"))
        self.viewBugsButton.setText(_translate("MainWindow", "View Bugs"))
        self.createBugButton.setText(_translate("MainWindow", "Create Bug"))
        self.userButton.setText(_translate("MainWindow", "Users"))
        self.logoutButton.setText(_translate("MainWindow", "Log Out"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Welcome to Bug Tracker</span></p><p align=\"center\"><span style=\" font-size:14pt;\">Made using Python, MySQL and PyQt5</span></p><p align=\"center\"><br/></p><p align=\"justify\"><span style=\" font-size:14pt;\">This desktop app is a simple bug tracker. It works by storing bug data in a local database and </span></p><p align=\"justify\"><span style=\" font-size:14pt;\">displaying the data to the users. Bugs vary in priority from low to high. Users can mark bugs as </span></p><p align=\"justify\"><span style=\" font-size:14pt;\">complete when they have been fixed. </span></p><p align=\"justify\"><br/></p><p align=\"justify\">The app has 3 different user levels:</p><p align=\"justify\">Admin: No limitation</p><p align=\"justify\">Moderator: Can not create and add users.</p><p align=\"justify\">User: Cannot create bugs or delete them</p><p align=\"justify\"><br/></p><p align=\"justify\">Use the menu on the left to navigate</p><p align=\"center\"><br/></p></body></html>"))
        self.menuLabel_2.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">MENU</span></p></body></html>"))
        self.dashboardButton_2.setText(_translate("MainWindow", "Dashboard"))
        self.viewBugsButton_2.setText(_translate("MainWindow", "View Bugs"))
        self.createBugButton_2.setText(_translate("MainWindow", "Create Bug"))
        self.userButton_2.setText(_translate("MainWindow", "Users"))
        self.logoutButton_2.setText(_translate("MainWindow", "Log Out"))
        self.highLabel.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Total high:</span></p></body></html>"))
        self.highCount.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">0</span></p></body></html>"))
        self.medLabel.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Total medium:</span></p></body></html>"))
        self.medCount.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">0</span></p></body></html>"))
        self.lowLabel.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Total low:</span></p></body></html>"))
        self.lowCount.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">0</span></p></body></html>"))
        self.completeLabel.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Total complete:</span></p></body></html>"))
        self.completeCount.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">0</span></p></body></html>"))
        self.loadTableButton.setText(_translate("MainWindow", "Load Bugs"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.bugTableTip.setText(_translate(
            "MainWindow", "<html><head/><body><p>Tip: Scroll either horizontally or vertically to view all data in table</p></body></html>"))
        self.editBugStatus.setText(_translate("MainWindow", "Edit Bug Status"))
        self.loadCompleteTable.setText(
            _translate("MainWindow", "Load Completed"))
        self.addBugButton.setText(_translate("MainWindow", "Create Bug"))
        self.tableTitle.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Bug Data Table</span></p></body></html>"))
        self.label_17.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">EDIT BUG STATUS</span></p></body></html>"))
        self.label_18.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"right\">Bug Id</p></body></html>"))
        self.markBugAsComplete.setText(_translate(
            "MainWindow", "Mark Bug As Complete"))
        self.deleteBugFromDatabase.setText(_translate(
            "MainWindow", "Delete Bug From Database"))
        self.returnToDashboard.setText(
            _translate("MainWindow", "Back To Dashboard"))
        self.editStatusToolTip.setText(_translate(
            "MainWindow", "<html><head/><body><p>Enter the ID of the bug you want to either delete or mark</p><p>as complete</p><p><br/></p><p>Then simply press the button corresponding to your</p><p>wanted action.</p></body></html>"))
        self.createBugBack.setText(_translate("MainWindow", "Back"))
        self.createBugSubmit.setText(_translate("MainWindow", "Submit"))
        self.inputSteps.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Title"))
        self.label_4.setText(_translate("MainWindow", "Application Name"))
        self.label_5.setText(_translate("MainWindow", "Version"))
        self.label_6.setText(_translate("MainWindow", "Priority Level"))
        self.label_7.setText(_translate("MainWindow", "Steps To Reproduce"))
        self.label_8.setText(_translate(
            "MainWindow", "Short Problem Description"))
        self.label_9.setText(_translate("MainWindow", "Assigned To"))
        self.label_10.setText(_translate("MainWindow", "Created By"))
        self.addTitle.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Add User</span></p></body></html>"))
        self.label_11.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"right\">Name</p></body></html>"))
        self.label_12.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"right\">Username</p></body></html>"))
        self.label_13.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"right\">Password</p></body></html>"))
        self.label_14.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"right\">Employee ID</p></body></html>"))
        self.label_15.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"right\">Optional: Email</p></body></html>"))
        self.radioAdmin.setText(_translate("MainWindow", "Admin"))
        self.radioModerator.setText(_translate("MainWindow", "Moderator"))
        self.radioNormal.setText(_translate("MainWindow", "Normal User"))
        self.submitNewUser.setText(_translate("MainWindow", "Submit"))
        self.returnFromUserToDashboard.setText(
            _translate("MainWindow", "Back"))
        self.deleteUserTitle.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Delete User</span></p></body></html>"))
        self.deleteUserButton.setText(_translate("MainWindow", "Delete User"))
        self.label_16.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"right\">Employee ID</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
