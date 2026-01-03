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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(463, 324)
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
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(25, 25, 25, 25)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Quicksand"])
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel {\n"
"	margin-bottom: 10px;\n"
"}")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.passText = QLineEdit(self.centralwidget)
        self.passText.setObjectName(u"passText")
        self.passText.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout_2.addWidget(self.passText, 1, 0, 1, 1)

        self.userText = QLineEdit(self.centralwidget)
        self.userText.setObjectName(u"userText")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userText.sizePolicy().hasHeightForWidth())
        self.userText.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.userText, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.loginBttn = QPushButton(self.centralwidget)
        self.loginBttn.setObjectName(u"loginBttn")
        self.loginBttn.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.loginBttn)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 463, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.passText, self.loginBttn)
        QWidget.setTabOrder(self.loginBttn, self.userText)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Main", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">AutoAccred: Automatic Classification and File Management for School Accreditation</span></p></body></html>", None))
        self.passText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.userText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.loginBttn.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
    # retranslateUi

