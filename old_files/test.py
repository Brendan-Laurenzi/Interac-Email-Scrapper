import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt6.QtCore import Qt
from PyQt6 import uic

scipt_dir = os.path.dirname(__file__)
ui_path = os.path.join("UI/interface.UI")

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_path, self)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    
    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print("Exiting")