from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QRadioButton, QButtonGroup
from ui_main import Ui_MainWindow
import helper
from db import get_db
from selection import SelectionWindow
import sys
import view

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.db = get_db()
        
        self.ui.loginBttn.clicked.connect(self.trylogin)
    
    def trylogin(self):
        username = self.ui.userText.text()
        password = self.ui.passText.text()
        
        result, id = self.db.verify_account(username, password)

        if result:
            self.selector_window = SelectionWindow(id)
            self.selector_window.show()
            self.close()
        else:
            print("Login failed")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())