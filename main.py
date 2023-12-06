# IMPORT DEPENDICIES
import sys
import time
from PyQt6 import QtGui
from PyQt6.QtCore import QRunnable, QThreadPool, pyqtSignal, QObject, QSettings
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

# IMPORT GUI FILE
from ui_interface import *

# IMPORT DATABASE 
import database

# IMPORT SCRAPPER
import scrape


db = database.Database()
threadpool = QThreadPool.globalInstance()

doneBtnStyleSheet = (
    """
    QPushButton {
        background-color: #4CAF50;
        color: white;
    }
    QPushButton:hover {
        background-color: #0080bf;
    }
    """
)

class WorkerSignals(QObject):
    progress = pyqtSignal(int, int)
    finished = pyqtSignal(int)
    error = pyqtSignal(tuple)
    result = pyqtSignal(int)
    interrupt = pyqtSignal()

class UpdateWorker(QRunnable):

    def __init__(self, condition=None):
        super(UpdateWorker, self).__init__()
        self.condition = condition
        self.email = scrape.emtEmail()
        self.signals = WorkerSignals()

    def run(self):
        db.connect()
        self.email.connect()
        beforeEntryCount = len(db.fetch_all('received_emts'))

        emailCount = self.email.get_email_count(self.condition)
        for i in range(emailCount):
            # Retreive ['name', 'amt', 'memo', 'date', 'refID'] from Interac Confirmation Email
            emailData = self.email.fetch_email_content(i)
            #print(emailData)
            self.signals.progress.emit(i+1, emailCount)
            # Continue to next email if -1 (Email did not match Interac E-Transfer Format)
            if (emailData == -1): continue
            db.insert_record("received_emts", ['name', 'amt', 'memo', 'date', 'refID'], emailData)

        # Calculate how many new entries were added
        afterEntryCount = len(db.fetch_all('received_emts'))
        newEntryCount = afterEntryCount - beforeEntryCount

        self.email.disconnect()
        db.disconnect()
        self.signals.finished.emit(newEntryCount)


class ListenWorker(QRunnable):

    def __init__(self):
        super(ListenWorker, self).__init__()
        self.shouldStop = False
        self.email = scrape.emtEmail()
        self.signals = WorkerSignals()

    def stop(self):
        self.shouldStop = True

    def run(self):
        self.email.connect()
        while not self.shouldStop:
            result = self.email.check_for_new_emails()
            if self.shouldStop or result == -1: break
            self.signals.result.emit(result)
        self.email.disconnect()
        print("Listen Thread Complete")




## MAIN WINDOW CLASS
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # VARIABLES
        self.menuStatus = True
        self.selectedMenu = self.ui.homeBtn
        self.isSearching = False
        self.idleTriggerMail = scrape.emtEmail()

        # INITIALIZE UI
        self.initializeTableData()
        self.ui.stackedWidget.setCurrentWidget(self.ui.homePage)
        self.ui.newDataTable.horizontalHeader().setVisible(True)
        self.ui.allDataTable.horizontalHeader().setVisible(True)

        # INITIALIZE SETTINGS
        self.settings = QSettings('EMTManager', 'App1')
        try:
            self.resize(self.settings.value('window size'))
            self.move(self.settings.value('window position'))
        except:
            pass

        ## BUTTON CONNECTORS

        self.ui.menuBtn.clicked.connect(self.menuToggle)
        # SideMenu Buttons
        self.ui.homeBtn.clicked.connect(lambda:self.showPage(self.ui.homePage))
        self.ui.dataBtn.clicked.connect(lambda:self.showPage(self.ui.dataPage))
        self.ui.reportBtn.clicked.connect(lambda:self.showPage(self.ui.reportPage))
        self.ui.settingsBtn.clicked.connect(lambda:self.showPage(self.ui.settingPage))
        self.ui.infoBtn.clicked.connect(lambda:self.showPage(self.ui.infoPage))
        self.ui.helpBtn.clicked.connect(lambda:self.showPage(self.ui.helpPage))
        # Home Buttons
        self.ui.homeUpdateBtn.clicked.connect(self.updateDatabase)
        self.ui.autoUpdateCheckBox.toggled.connect(self.toggle_auto_update)
        self.ui.searchAllTableBtn.clicked.connect(lambda:self.search_table(self.ui.searchAllTableLine.text(), self.ui.allDataTable))



    ## WORKER SIGNAL FUNCTIONS
    def reportProgress(self, curValue, maxValue):
        self.ui.receivedEMTprogressBar.setMaximum(maxValue)
        self.ui.receivedEMTprogressBar.setValue(curValue)

    def updateComplete(self, count):
        if count > 0:
            self.ui.updateStatusLabel.setText(f"Successfully added ({count}) new entries!")
        else:
            self.ui.updateStatusLabel.setText(f"No new entries found.")

        self.initializeTableData()
        self.isSearching = False


    def handle_new_email(self, result):
        if result == 1:
            #print("Email Event")
            self.updateDatabase("UNSEEN")
        else:
            print("Timed out / Error")


    ## UI FUNCTIONS

    def menuToggle(self):
        if (self.menuStatus):
            self.menuStatus = False
            self.ui.homeBtn.setText("")
            self.ui.dataBtn.setText("")
            self.ui.reportBtn.setText("")
            self.ui.settingsBtn.setText("")
            self.ui.infoBtn.setText("")
            self.ui.helpBtn.setText("")
        else:
            self.menuStatus = True
            self.ui.homeBtn.setText("Home")
            self.ui.dataBtn.setText("Data Analysis")
            self.ui.reportBtn.setText("Reports")
            self.ui.settingsBtn.setText("Settings")
            self.ui.infoBtn.setText("Information")
            self.ui.helpBtn.setText("Help")


    def toggle_auto_update(self):
        if (self.sender().isChecked()):
            self.listenWorker = ListenWorker()
            self.listenWorker.signals.result.connect(self.handle_new_email)
            threadpool.start(self.listenWorker)
        else:
            self.listenWorker.stop()
            self.idleTriggerMail.break_idle_loop()


    def showPage(self, page):
        self.ui.stackedWidget.setCurrentWidget(page)
        self.selectedMenu.setStyleSheet('')
        self.sender().setStyleSheet('background-color: #1f232a;')
        self.selectedMenu = self.sender()


    def updateDatabase(self, condition=None):
        if self.isSearching: return 
        self.isSearching = True

        self.ui.updateStatusLabel.setText(f"Updating Database... Please Wait")

        self.ui.receivedEMTprogressBar.setMinimum(0)
        self.ui.receivedEMTprogressBar.setValue(0)

        self.updateWorker = UpdateWorker(condition)
        self.updateWorker.signals.progress.connect(self.reportProgress)
        self.updateWorker.signals.finished.connect(self.updateComplete)
        threadpool.start(self.updateWorker)


    def search_table(self, value, tableWidgit):
        db.connect()
        dataList = db.fetch_all_from_value('received_emts', value)
        db.disconnect()
        
        self.setTableItems(tableWidgit, dataList)


    def setTableItems(self, tableWidgit, dataList, buttonCSS=None, buttonConnection=None):
        colShift = 0
        tableWidgit.setRowCount(len(dataList))
        for row, data in enumerate(dataList):
            if buttonConnection:
                colShift = 1
                tableWidgit.setColumnWidth(0, 25)
                button = QPushButton("DONE")
                button.clicked.connect(buttonConnection)
                button.setStyleSheet(buttonCSS)
                tableWidgit.setCellWidget(row, 0, button)
            # Row Data ex. : ['2104673 ONTARIO INC', '2,500', 'N/A', datetime.datetime(2023, 10, 24, 17, 7), 'CAHfMDyz']
            tableWidgit.setItem(row, 0 + colShift, QtWidgets.QTableWidgetItem(data[0])) 
            tableWidgit.setItem(row, 1 + colShift, QtWidgets.QTableWidgetItem(data[1])) 
            tableWidgit.setItem(row, 2 + colShift, QtWidgets.QTableWidgetItem(data[2])) 
            tableWidgit.setItem(row, 3 + colShift, QtWidgets.QTableWidgetItem(str(data[3]))) 
            tableWidgit.setItem(row, 4 + colShift, QtWidgets.QTableWidgetItem(data[4]))


    def initializeTableData(self):
        db.connect()

        dataList = db.fetch_all("received_emts")
        self.setTableItems(self.ui.allDataTable, dataList)
        
        dataList = db.fetch_all_confirmed("received_emts")
        self.setTableItems(self.ui.newDataTable, dataList, doneBtnStyleSheet, self.button_clicked)

        db.disconnect()


    def button_clicked(self):
        button = self.sender()
        index = self.ui.newDataTable.indexAt(button.pos())

        if index.isValid():
            row = index.row()
            id = self.ui.newDataTable.item(row, 5).text()
            condition = f"refID = '{id}'"

            db.connect()
            db.update_column_bool("received_emts", "confirmed", True, condition)
            db.disconnect()

            self.ui.newDataTable.removeRow(row)


    def closeEvent(self, event):
        # Stop Email Listening Thread if Active
        if self.ui.autoUpdateCheckBox.isChecked(): 
            self.ui.autoUpdateCheckBox.toggle()

        threadpool.clear()

        self.settings.setValue('window size', self.size())
        self.settings.setValue('window position', self.pos())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print("Exiting")
        

