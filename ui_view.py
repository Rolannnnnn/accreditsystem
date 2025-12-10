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
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableView,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(525, 357)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(40, 20, 431, 201))
        self.documentBttn = QPushButton(self.centralwidget)
        self.documentBttn.setObjectName(u"documentBttn")
        self.documentBttn.setGeometry(QRect(30, 250, 79, 24))
        self.classificationBttn = QPushButton(self.centralwidget)
        self.classificationBttn.setObjectName(u"classificationBttn")
        self.classificationBttn.setGeometry(QRect(150, 250, 91, 24))
        self.logBttn = QPushButton(self.centralwidget)
        self.logBttn.setObjectName(u"logBttn")
        self.logBttn.setGeometry(QRect(280, 250, 79, 24))
        self.accountBttn = QPushButton(self.centralwidget)
        self.accountBttn.setObjectName(u"accountBttn")
        self.accountBttn.setGeometry(QRect(400, 250, 79, 24))
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

