# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(446, 241)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 30, 71, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 60, 71, 16))
        self.userText = QLineEdit(self.centralwidget)
        self.userText.setObjectName(u"userText")
        self.userText.setGeometry(QRect(130, 30, 261, 21))
        self.passText = QLineEdit(self.centralwidget)
        self.passText.setObjectName(u"passText")
        self.passText.setGeometry(QRect(130, 60, 261, 21))
        self.createBttn = QLabel(self.centralwidget)
        self.createBttn.setObjectName(u"createBttn")
        self.createBttn.setGeometry(QRect(290, 90, 101, 20))
        font = QFont()
        font.setUnderline(True)
        self.createBttn.setFont(font)
        self.loginBttn = QPushButton(self.centralwidget)
        self.loginBttn.setObjectName(u"loginBttn")
        self.loginBttn.setGeometry(QRect(350, 150, 79, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 446, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Main", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.createBttn.setText(QCoreApplication.translate("MainWindow", u"Create an Account", None))
        self.loginBttn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

