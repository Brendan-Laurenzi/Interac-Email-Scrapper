# Form implementation generated from reading ui file '.\interface.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import resources_re

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1036, 621)
        MainWindow.setStyleSheet("*{\n"
"    border: none;\n"
"    background-color: #transparent;\n"
"    background: none;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    color: #fff;\n"
"}\n"
"\n"
"#centralwidget{\n"
"    background-color: #1f232a;\n"
"}\n"
"\n"
"#tableWidget{\n"
"    background-color: #1f232a;\n"
"}\n"
"\n"
"#leftMenuSubContainer{\n"
"    background-color: #16191d;\n"
"}\n"
"\n"
"#leftMenuSubContainer QPushButton{\n"
"    text-align: left;\n"
"    padding: 2px 10px;\n"
"    border-top-left-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"#updateButton{\n"
"    background-color: #1f232a;\n"
"    border-top-right-radius: 10px;\n"
"}\n"
"\n"
"#searchBarContainer QFrame{\n"
"    background-color: rgb(98, 98, 98);\n"
"    padding: 2px 2px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftMenuContainer = QtWidgets.QWidget(parent=self.centralwidget)
        self.leftMenuContainer.setObjectName("leftMenuContainer")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.leftMenuSubContainer = QtWidgets.QWidget(parent=self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName("leftMenuSubContainer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setContentsMargins(5, 5, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(parent=self.leftMenuSubContainer)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.menuBtn = QtWidgets.QPushButton(parent=self.frame)
        self.menuBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons_light/icons_light/align-justify.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QtCore.QSize(24, 24))
        self.menuBtn.setObjectName("menuBtn")
        self.horizontalLayout_2.addWidget(self.menuBtn)
        self.verticalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.frame_2 = QtWidgets.QFrame(parent=self.leftMenuSubContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.homeBtn = QtWidgets.QPushButton(parent=self.frame_2)
        self.homeBtn.setStyleSheet("background-color: #1f232a;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons_light/icons_light/home.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QtCore.QSize(24, 24))
        self.homeBtn.setObjectName("homeBtn")
        self.verticalLayout_3.addWidget(self.homeBtn)
        self.dataBtn = QtWidgets.QPushButton(parent=self.frame_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons_light/icons_light/list.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.dataBtn.setIcon(icon2)
        self.dataBtn.setIconSize(QtCore.QSize(24, 24))
        self.dataBtn.setObjectName("dataBtn")
        self.verticalLayout_3.addWidget(self.dataBtn)
        self.reportBtn = QtWidgets.QPushButton(parent=self.frame_2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons_light/icons_light/printer.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.reportBtn.setIcon(icon3)
        self.reportBtn.setIconSize(QtCore.QSize(24, 24))
        self.reportBtn.setObjectName("reportBtn")
        self.verticalLayout_3.addWidget(self.reportBtn)
        self.verticalLayout_2.addWidget(self.frame_2, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.frame_3 = QtWidgets.QFrame(parent=self.leftMenuSubContainer)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.settingsBtn = QtWidgets.QPushButton(parent=self.frame_3)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons_light/icons_light/settings.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.settingsBtn.setIcon(icon4)
        self.settingsBtn.setIconSize(QtCore.QSize(24, 24))
        self.settingsBtn.setObjectName("settingsBtn")
        self.verticalLayout_4.addWidget(self.settingsBtn)
        self.infoBtn = QtWidgets.QPushButton(parent=self.frame_3)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons_light/icons_light/info.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.infoBtn.setIcon(icon5)
        self.infoBtn.setIconSize(QtCore.QSize(24, 24))
        self.infoBtn.setObjectName("infoBtn")
        self.verticalLayout_4.addWidget(self.infoBtn)
        self.helpBtn = QtWidgets.QPushButton(parent=self.frame_3)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons_light/icons_light/help-circle.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.helpBtn.setIcon(icon6)
        self.helpBtn.setIconSize(QtCore.QSize(24, 24))
        self.helpBtn.setObjectName("helpBtn")
        self.verticalLayout_4.addWidget(self.helpBtn)
        self.verticalLayout_2.addWidget(self.frame_3, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        self.verticalLayout.addWidget(self.leftMenuSubContainer, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout.addWidget(self.leftMenuContainer)
        self.mainBodyContainer = QtWidgets.QWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy)
        self.mainBodyContainer.setObjectName("mainBodyContainer")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.mainBodyContainer)
        self.stackedWidget.setObjectName("stackedWidget")
        self.homePage = QtWidgets.QWidget()
        self.homePage.setObjectName("homePage")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.homePage)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.homeHeaderContainer = QtWidgets.QWidget(parent=self.homePage)
        self.homeHeaderContainer.setStyleSheet("background-color: #1f232a;")
        self.homeHeaderContainer.setObjectName("homeHeaderContainer")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.homeHeaderContainer)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.homeHeaderLabelContainer = QtWidgets.QWidget(parent=self.homeHeaderContainer)
        self.homeHeaderLabelContainer.setObjectName("homeHeaderLabelContainer")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.homeHeaderLabelContainer)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.homeLabelFrame = QtWidgets.QFrame(parent=self.homeHeaderLabelContainer)
        self.homeLabelFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.homeLabelFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.homeLabelFrame.setObjectName("homeLabelFrame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.homeLabelFrame)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.homeLabel = QtWidgets.QLabel(parent=self.homeLabelFrame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.homeLabel.setFont(font)
        self.homeLabel.setObjectName("homeLabel")
        self.verticalLayout_9.addWidget(self.homeLabel)
        self.horizontalLayout_3.addWidget(self.homeLabelFrame)
        self.homeUpdateFrame = QtWidgets.QFrame(parent=self.homeHeaderLabelContainer)
        self.homeUpdateFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.homeUpdateFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.homeUpdateFrame.setObjectName("homeUpdateFrame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.homeUpdateFrame)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.updateButton = QtWidgets.QPushButton(parent=self.homeUpdateFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.updateButton.setFont(font)
        self.updateButton.setObjectName("updateButton")
        self.verticalLayout_8.addWidget(self.updateButton, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.horizontalLayout_3.addWidget(self.homeUpdateFrame)
        self.verticalLayout_7.addWidget(self.homeHeaderLabelContainer, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.homeSearchContainer = QtWidgets.QWidget(parent=self.homeHeaderContainer)
        self.homeSearchContainer.setObjectName("homeSearchContainer")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.homeSearchContainer)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.searchBarContainer = QtWidgets.QWidget(parent=self.homeSearchContainer)
        self.searchBarContainer.setObjectName("searchBarContainer")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.searchBarContainer)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.searchLineFrame = QtWidgets.QFrame(parent=self.searchBarContainer)
        self.searchLineFrame.setStyleSheet("")
        self.searchLineFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.searchLineFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.searchLineFrame.setObjectName("searchLineFrame")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.searchLineFrame)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.searchLineFrame)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(57, 57, 57);")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_11.addWidget(self.lineEdit)
        self.horizontalLayout_5.addWidget(self.searchLineFrame)
        self.searchButtonFrame = QtWidgets.QFrame(parent=self.searchBarContainer)
        self.searchButtonFrame.setStyleSheet("border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.searchButtonFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.searchButtonFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.searchButtonFrame.setLineWidth(1)
        self.searchButtonFrame.setObjectName("searchButtonFrame")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.searchButtonFrame)
        self.verticalLayout_10.setContentsMargins(0, 0, 3, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pushButton = QtWidgets.QPushButton(parent=self.searchButtonFrame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons_light/icons_light/search.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon7)
        self.pushButton.setIconSize(QtCore.QSize(24, 24))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_10.addWidget(self.pushButton)
        self.horizontalLayout_5.addWidget(self.searchButtonFrame)
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.horizontalLayout_4.addWidget(self.searchBarContainer)
        self.verticalLayout_7.addWidget(self.homeSearchContainer)
        self.verticalLayout_6.addWidget(self.homeHeaderContainer)
        self.homeBodyContainer = QtWidgets.QWidget(parent=self.homePage)
        self.homeBodyContainer.setObjectName("homeBodyContainer")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.homeBodyContainer)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.homeBodyContainer)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 900, 519))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.scrollAreaWidgetContents)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.horizontalLayout_7.addWidget(self.tableWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_6.addWidget(self.scrollArea)
        self.verticalLayout_6.addWidget(self.homeBodyContainer)
        self.homeBodyContainer.raise_()
        self.homeHeaderContainer.raise_()
        self.stackedWidget.addWidget(self.homePage)
        self.dataPage = QtWidgets.QWidget()
        self.dataPage.setObjectName("dataPage")
        self.stackedWidget.addWidget(self.dataPage)
        self.reportPage = QtWidgets.QWidget()
        self.reportPage.setObjectName("reportPage")
        self.stackedWidget.addWidget(self.reportPage)
        self.settingPage = QtWidgets.QWidget()
        self.settingPage.setObjectName("settingPage")
        self.stackedWidget.addWidget(self.settingPage)
        self.infoPage = QtWidgets.QWidget()
        self.infoPage.setObjectName("infoPage")
        self.stackedWidget.addWidget(self.infoPage)
        self.helpPage = QtWidgets.QWidget()
        self.helpPage.setObjectName("helpPage")
        self.stackedWidget.addWidget(self.helpPage)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.mainBodyContainer)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuBtn.setToolTip(_translate("MainWindow", "Menu"))
        self.homeBtn.setToolTip(_translate("MainWindow", "Home"))
        self.homeBtn.setText(_translate("MainWindow", "Home"))
        self.dataBtn.setToolTip(_translate("MainWindow", "Data Analysis"))
        self.dataBtn.setText(_translate("MainWindow", "Data Analysis"))
        self.reportBtn.setToolTip(_translate("MainWindow", "View Reports"))
        self.reportBtn.setText(_translate("MainWindow", "Reports"))
        self.settingsBtn.setToolTip(_translate("MainWindow", "Go to settings"))
        self.settingsBtn.setText(_translate("MainWindow", "Settings"))
        self.infoBtn.setToolTip(_translate("MainWindow", "Info about the app"))
        self.infoBtn.setText(_translate("MainWindow", "Information"))
        self.helpBtn.setToolTip(_translate("MainWindow", "Get more help"))
        self.helpBtn.setText(_translate("MainWindow", "Help"))
        self.homeLabel.setText(_translate("MainWindow", "Interact E-Transfer List"))
        self.updateButton.setText(_translate("MainWindow", "Update"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Amount"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Memo"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Ref_ID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())