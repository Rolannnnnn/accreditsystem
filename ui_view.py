# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(525, 358)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	background-color: #B8E0FF;\n"
"}\n"
"\n"
"QWidget {\n"
"	background-color: #B8E0FF;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border-radius: 0px;\n"
"    border: 2px solid #0078d4;\n"
"    background-color: #0078d4;\n"
"    color: #ffffff;\n"
"    padding: 3px 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ffffff;\n"
"	color: #0078d4;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ffffff;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border-radius: 10px;\n"
"	padding: 10px 14px;\n"
"	margin: 2px;\n"
"	background-color: #ffffff;\n"
"}\n"
"\n"
"QTableView {\n"
"	background-color: #ffffff;\n"
"	color: #000000;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #0078d4;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #0078d4;\n"
"    border: 2px solid #0078d4;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"	border-r"
                        "adius: 8px;\n"
"	border: 2px solid #0078d4;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #0078d4;\n"
"}\n"
"\n"
"QComboBox {\n"
"	background-color: #ffffff;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background-color: #ffffff;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::indicator {\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::indicator:unchecked {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #000000;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::indicator:checked {\n"
"    background-color: #000000;\n"
"    border: 2px solid #000000;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.documentBttn = QPushButton(self.centralwidget)
        self.documentBttn.setObjectName(u"documentBttn")

        self.horizontalLayout.addWidget(self.documentBttn)

        self.classificationBttn = QPushButton(self.centralwidget)
        self.classificationBttn.setObjectName(u"classificationBttn")

        self.horizontalLayout.addWidget(self.classificationBttn)

        self.logBttn = QPushButton(self.centralwidget)
        self.logBttn.setObjectName(u"logBttn")

        self.horizontalLayout.addWidget(self.logBttn)

        self.accountBttn = QPushButton(self.centralwidget)
        self.accountBttn.setObjectName(u"accountBttn")

        self.horizontalLayout.addWidget(self.accountBttn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 525, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"View Table", None))
        self.documentBttn.setText(QCoreApplication.translate("MainWindow", u"Document", None))
        self.classificationBttn.setText(QCoreApplication.translate("MainWindow", u"Classification", None))
        self.logBttn.setText(QCoreApplication.translate("MainWindow", u"Log", None))
        self.accountBttn.setText(QCoreApplication.translate("MainWindow", u"Account", None))
    # retranslateUi

