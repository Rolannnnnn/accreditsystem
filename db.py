import sqlite3
import os
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from datetime import datetime
import hashlib

class DatabaseManager:
    def __init__(self, db_path="accreditation.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize SQLite database and create tables"""
        # Create Qt SQL connection
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(self.db_path)
        
        if not self.db.open():
            print(f"Error opening database: {self.db.lastError().text()}")
            return False
        
        # Check if all required tables exist
        required_tables = ['accounts', 'documents', 'classifications', 'logs']
        existing_tables = self.db.tables()
        
        missing_tables = [table for table in required_tables if table not in existing_tables]
        
        if missing_tables:
            print(f"Missing tables: {missing_tables}. Creating tables...")
            self.create_tables()
            self.add_account("tempuser", "temppass", "Main Admin", "Administrator")
        else:
            print("All required tables already exist.")
    
        return True
    
    def create_tables(self):
        """Create necessary tables for the accreditation system"""
        query = QSqlQuery()
        
        account_table = """
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            name TEXT NOT NULL,
            position TEXT
        )
        """

        documents_table = """
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_path TEXT NOT NULL,
            file_name TEXT NOT NULL,
            file_type TEXT NOT NULL,
            document_type TEXT NOT NULL
        )
        """
        
        # Document classifications table (fixed: DOUBLE -> REAL)
        classifications_table = """
        CREATE TABLE IF NOT EXISTS classifications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            document_id INTEGER,
            area_num INTEGER NOT NULL,
            parameter TEXT NOT NULL,
            section TEXT NOT NULL,
            node INTEGER NOT NULL,
            sub_key REAL NOT NULL,
            FOREIGN KEY (document_id) REFERENCES documents (id)
        )
        """
        
        # Logs table
        logs_table = """
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            classification_id INTEGER,
            accounts_id INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (classification_id) REFERENCES classifications (id),
            FOREIGN KEY (accounts_id) REFERENCES accounts (id)
        )
        """
        
        # Execute table creation in correct order (accounts first)
        tables = [account_table, documents_table, classifications_table, logs_table]
        for table_sql in tables:
            if not query.exec(table_sql):
                print(f"Error creating table: {query.lastError().text()}")
    
    def add_document(self, file_path, document_type):
        """Add a new document to the database - matches schema"""
        query = QSqlQuery()
        query.prepare("""
            INSERT INTO documents (file_path, file_name, file_type, document_type)
            VALUES (?, ?, ?, ?)
        """)
        
        file_name = os.path.basename(file_path)
        file_ext = os.path.splitext(file_path)[1].lower()
        
        query.addBindValue(file_path)
        query.addBindValue(file_name)
        query.addBindValue(file_ext)
        query.addBindValue(document_type)
        
        if query.exec():
            return query.lastInsertId()
        else:
            print(f"Error inserting document: {query.lastError().text()}")
            return None
    
    def add_classification(self, document_id, area_num, parameter, section, node, sub_key=0):
        """Add a classification for a document - matches schema"""
        query = QSqlQuery()
        query.prepare("""
            INSERT INTO classifications (document_id, area_num, parameter, section, node, sub_key)
            VALUES (?, ?, ?, ?, ?, ?)
        """)
        
        query.addBindValue(document_id)
        query.addBindValue(area_num)
        query.addBindValue(parameter)
        query.addBindValue(section)
        query.addBindValue(node)
        query.addBindValue(float(sub_key))
        
        if query.exec():
            return query.lastInsertId()
        else:
            print(f"Error inserting classification: {query.lastError().text()}")
            return None
    
    def add_account(self, username, password, name, position=""):
        query = QSqlQuery()
        query.prepare("""
            INSERT INTO accounts (username, password_hash, name, position)
            VALUES (?, ?, ?, ?)
        """)
        
        # Hash the password
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        query.addBindValue(username)
        query.addBindValue(password_hash)
        query.addBindValue(name)
        query.addBindValue(position)
        
        if query.exec():
            return query.lastInsertId()
        else:
            print(f"Error inserting account: {query.lastError().text()}")
            return None
    
    def add_log(self, classification_id, accounts_id):
        """Add a log entry - matches schema"""
        query = QSqlQuery()
        query.prepare("""
            INSERT INTO logs (classification_id, accounts_id)
            VALUES (?, ?)
        """)
        
        query.addBindValue(classification_id)
        query.addBindValue(accounts_id)
        
        if query.exec():
            return query.lastInsertId()
        else:
            print(f"Error inserting log: {query.lastError().text()}")
            return None
    
    def get_document_by_id(self, doc_id):
        """Retrieve document by ID - matches schema"""
        query = QSqlQuery()
        query.prepare("SELECT * FROM documents WHERE id = ?")
        query.addBindValue(doc_id)
        
        if query.exec() and query.next():
            return {
                'id': query.value(0),
                'file_path': query.value(1),
                'file_name': query.value(2),
                'file_type': query.value(3),
                'document_type': query.value(4)
            }
        return None
    
    def get_classification_by_id(self, classification_id):
        """Retrieve classification by ID - matches schema"""
        query = QSqlQuery()
        query.prepare("SELECT * FROM classifications WHERE id = ?")
        query.addBindValue(classification_id)
        
        if query.exec() and query.next():
            return {
                'id': query.value(0),
                'document_id': query.value(1),
                'area_num': query.value(2),
                'parameter': query.value(3),
                'section': query.value(4),
                'node': query.value(5),
                'sub_key': query.value(6)
            }
        return None
    
    def get_account_by_id(self, account_id):
        """Retrieve account by ID - matches schema"""
        query = QSqlQuery()
        query.prepare("SELECT * FROM accounts WHERE id = ?")
        query.addBindValue(account_id)
        
        if query.exec() and query.next():
            return {
                'id': query.value(0),
                'username': query.value(1),
                'password_hash': query.value(2),
                'name': query.value(3),
                'position': query.value(4)
            }
        return None
    
    def get_account_by_username(self, username):
        """Retrieve account by username - matches schema"""
        query = QSqlQuery()
        query.prepare("SELECT * FROM accounts WHERE username = ?")
        query.addBindValue(username)
        
        if query.exec() and query.next():
            return {
                'id': query.value(0),
                'username': query.value(1),
                'password_hash': query.value(2),
                'name': query.value(3),
                'position': query.value(4)
            }
        return None
    
    def get_log_by_id(self, log_id):
        """Retrieve log by ID - matches schema"""
        query = QSqlQuery()
        query.prepare("SELECT * FROM logs WHERE id = ?")
        query.addBindValue(log_id)
        
        if query.exec() and query.next():
            return {
                'id': query.value(0),
                'classification_id': query.value(1),
                'accounts_id': query.value(2),
                'timestamp': query.value(3)
            }
        return None
    
    def get_all_accounts(self):
        query = QSqlQuery("SELECT * FROM accounts ORDER BY id ASC")
        accounts = []
        
        while query.next():
            accounts.append({
                'id': query.value(0),
                'username': query.value(1),
                'password_hash': query.value(2),
                'name': query.value(3),
                'position': query.value(4)
            })
        
        return accounts
    
    def get_all_documents(self):
        query = QSqlQuery("SELECT * FROM documents ORDER BY id DESC")
        documents = []
        
        while query.next():
            documents.append({
                'id': query.value(0),
                'file_path': query.value(1),
                'file_name': query.value(2),
                'file_type': query.value(3),
                'document_type': query.value(4)
            })
        
        return documents
    
    def get_all_classifications(self):
        query = QSqlQuery("SELECT * FROM classifications ORDER BY id DESC")
        classifications = []
        
        while query.next():
            classifications.append({
                'id': query.value(0),
                'document_id': query.value(1),
                'area_num': query.value(2),
                'parameter': query.value(3),
                'section': query.value(4),
                'node': query.value(5),
                'sub_key': query.value(6)
            })
        
        return classifications
    
    def get_all_logs(self):
        query = QSqlQuery("SELECT * FROM logs ORDER BY id DESC")
        logs = []
        
        while query.next():
            logs.append({
                'id': query.value(0),
                'classification_id': query.value(1),
                'accounts_id': query.value(2),
                'timestamp': query.value(3)
            })
        
        return logs
    
    def get_classifications_by_document_id(self, document_id):
        """Get all classifications for a specific document"""
        query = QSqlQuery()
        query.prepare("SELECT * FROM classifications WHERE document_id = ?")
        query.addBindValue(document_id)
        
        classifications = []
        if query.exec():
            while query.next():
                classifications.append({
                    'id': query.value(0),
                    'document_id': query.value(1),
                    'area_num': query.value(2),
                    'parameter': query.value(3),
                    'section': query.value(4),
                    'node': query.value(5),
                    'sub_key': query.value(6)
                })
        
        return classifications
    
    def get_logs_by_classification_id(self, classification_id):
        """Get all logs for a specific classification with account info"""
        query = QSqlQuery()
        query.prepare("""
            SELECT l.*, a.username, a.name 
            FROM logs l 
            JOIN accounts a ON l.accounts_id = a.id 
            WHERE l.classification_id = ?
            ORDER BY l.timestamp DESC
        """)
        query.addBindValue(classification_id)
        
        logs = []
        if query.exec():
            while query.next():
                logs.append({
                    'id': query.value(0),
                    'classification_id': query.value(1),
                    'accounts_id': query.value(2),
                    'timestamp': query.value(3),
                    'username': query.value(4),
                    'name': query.value(5)
                })
        
        return logs
    
    def verify_account(self, username, password):
        account = self.get_account_by_username(username)
        if account:
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            result = password_hash == account['password_hash']
            return result, account['id']
        return False, None
    
    def close(self):
        if self.db.isOpen():
            self.db.close()

# Global database instance
db_manager = None

def get_db():
    """Get global database manager instance"""
    global db_manager
    if db_manager is None:
        db_manager = DatabaseManager()
    return db_manager