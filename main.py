import sys

# IMPORT GUI FILE
from ui_interface import *

from PyQt6.QtWidgets import QApplication, QMainWindow

## MAIN WINDOW CLASS
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.menuStatus = True
        self.ui.menuBtn.clicked.connect(self.menuToggle)

        

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
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print("Exiting")

