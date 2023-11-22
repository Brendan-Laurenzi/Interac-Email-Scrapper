# IMPORT DEPENDICIES
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

# IMPORT GUI FILE
from ui_interface import *

# IMPORT DATABASE 
import database as db

# IMPORT SCRAPPER
import scrape

## MAIN WINDOW CLASS
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # VARIABLES
        self.menuStatus = True

        # INITIALIZE TABLE DATA
        self.loadData()

        # BUTTON CONNECTORS
        self.ui.menuBtn.clicked.connect(self.menuToggle)
        self.ui.updateButton.clicked.connect(self.loadData)

    ## UI FUNCTIONS

    def menuToggle(self):
        if (self.menuStatus):
            print("Max")
            self.menuStatus = False
            self.ui.homeBtn.setText("")
            self.ui.dataBtn.setText("")
            self.ui.reportBtn.setText("")
            self.ui.settingsBtn.setText("")
            self.ui.infoBtn.setText("")
            self.ui.helpBtn.setText("")
        else:
            print("Min")
            self.menuStatus = True
            self.ui.homeBtn.setText("Home")
            self.ui.dataBtn.setText("Data Analysis")
            self.ui.reportBtn.setText("Reports")
            self.ui.settingsBtn.setText("Settings")
            self.ui.infoBtn.setText("Information")
            self.ui.helpBtn.setText("Help")

    def loadData(self):
        dataList = db.Database.get_all_emt_data()
        self.ui.tableWidget.setRowCount(len(dataList))
        for row, data in enumerate(dataList):
            # Row Data ex. : ['2104673 ONTARIO INC', '2,500', 'N/A', datetime.datetime(2023, 10, 24, 17, 7), 'CAHfMDyz']
            self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(data[0])) 
            self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(data[1])) 
            self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(data[2])) 
            self.ui.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(data[3]))) 
            self.ui.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(data[4]))

            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print("Exiting")

