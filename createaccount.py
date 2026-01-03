from PySide6.QtWidgets import QApplication, QMainWindow
from ui_createaccount import Ui_MainWindow
import helper
from db import get_db

class CreateAccountWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.db = get_db()

        self.ui.createBttn.clicked.connect(self.create_account)
        self.ui.cancelBttn.clicked.connect(self.back)

    def back(self):
        self.close()

    def create_account(self):
        username = self.ui.usernameLine.text().strip()
        password = self.ui.passwordLine.text().strip()
        cpassword = self.ui.confirmPassLine.text().strip()
        name = self.ui.nameLine.text().strip()
        position = self.ui.positionLine.text().strip()

        if not username or not password or not name or not cpassword or not position:
            helper.show_invalid_file_dialog(self, "Input Error", "Some fields are empty.")
            return
        
        if password != cpassword:
            helper.show_invalid_file_dialog(self, "Input Error", "Passwords do not match.")
            return

        existing_account = self.db.get_account_by_username(username)
        if existing_account:
            helper.show_invalid_file_dialog(self, "Input Error", "Username already exists. Please choose another.")
            return

        acc_id = self.db.add_account(username, password, name, position)
        helper.show_info_dialog(self, "Success", f"Account Created Successfully. ID: {acc_id}")
        self.ui.usernameLine.clear()
        self.ui.passwordLine.clear()
        self.ui.nameLine.clear()
        self.ui.positionLine.clear()
        self.ui.confirmPassLine.clear()