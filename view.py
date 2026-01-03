from PySide6.QtWidgets import QApplication, QMainWindow 
from PySide6.QtGui import QStandardItemModel, QStandardItem
from ui_view import Ui_MainWindow
import helper
from db import get_db
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.db = get_db()
        
        self.ui.accountBttn.clicked.connect(self.account)
        self.ui.documentBttn.clicked.connect(self.document)
        self.ui.classificationBttn.clicked.connect(self.classification)
        self.ui.logBttn.clicked.connect(self.log)
    
    def account(self):
        accounts = self.db.get_all_accounts()

         # Create model
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['ID', 'Username', 'Password Hash', 'Name', 'Position'])
        
        # Populate model with data
        for account in accounts:
            row = [
                QStandardItem(str(account['id'])),
                QStandardItem(account['username']),
                QStandardItem(account['password_hash']),
                QStandardItem(account['name']),
                QStandardItem(account['position'] or '')
            ]
            model.appendRow(row)
        
        # Set model to table view
        self.ui.tableView.setModel(model)
        self.ui.tableView.resizeColumnsToContents()

    def document(self):
        documents = self.db.get_all_documents()

         # Create model
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['ID', 'File Path', 'File Name', 'File Type', 'Document Type'])
        
        # Populate model with data
        for document in documents:
            row = [
                QStandardItem(str(document['id'])),
                QStandardItem(document['file_path']),
                QStandardItem(document['file_name']),
                QStandardItem(document['file_type']),
                QStandardItem(document['document_type'])
            ]
            model.appendRow(row)
        
        # Set model to table view
        self.ui.tableView.setModel(model)
        self.ui.tableView.resizeColumnsToContents()
    
    def classification(self):
        classifications = self.db.get_all_classifications()
        
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['ID', 'Document ID', 'Area Number', 'Parameter', 'Section', 'Node', 'Sub Key'])
        for classification in classifications:
            row = [
                QStandardItem(str(classification['id'])),
                QStandardItem(str(classification['document_id'])),
                QStandardItem(str(classification['area_num'])),
                QStandardItem(classification['parameter']),
                QStandardItem(classification['section']),
                QStandardItem(str(classification['node'])),
                QStandardItem(str(classification['sub_key']))
            ]
            model.appendRow(row)
        
        self.ui.tableView.setModel(model)
        self.ui.tableView.resizeColumnsToContents()
    
    def log(self):
        logs = self.db.get_all_logs()
        
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['ID', 'Classification ID', 'Account ID', 'Timestamp'])
        for log in logs:
            row = [
                QStandardItem(str(log['id'])),
                QStandardItem(str(log['classification_id'])),
                QStandardItem(str(log['accounts_id'])),
                QStandardItem(log['timestamp'])
            ]
            model.appendRow(row)
        
        self.ui.tableView.setModel(model)
        self.ui.tableView.resizeColumnsToContents()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())