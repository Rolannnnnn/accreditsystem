# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createaccount.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(473, 445)
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
"	border-radius: 8px;\n"
"	border: 2px solid #0078d4;\n"
"}\n"
"\n"
"QRadioButton::indicato"
                        "r:unchecked {\n"
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
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Quicksand"])
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.nameLine = QLineEdit(self.centralwidget)
        self.nameLine.setObjectName(u"nameLine")

        self.verticalLayout.addWidget(self.nameLine)

        self.positionLine = QLineEdit(self.centralwidget)
        self.positionLine.setObjectName(u"positionLine")

        self.verticalLayout.addWidget(self.positionLine)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_2.addWidget(self.label_2)

        self.usernameLine = QLineEdit(self.centralwidget)
        self.usernameLine.setObjectName(u"usernameLine")

        self.verticalLayout_2.addWidget(self.usernameLine)

        self.passwordLine = QLineEdit(self.centralwidget)
        self.passwordLine.setObjectName(u"passwordLine")
        self.passwordLine.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_2.addWidget(self.passwordLine)

        self.confirmPassLine = QLineEdit(self.centralwidget)
        self.confirmPassLine.setObjectName(u"confirmPassLine")
        self.confirmPassLine.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_2.addWidget(self.confirmPassLine)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancelBttn = QPushButton(self.centralwidget)
        self.cancelBttn.setObjectName(u"cancelBttn")

        self.horizontalLayout.addWidget(self.cancelBttn)

        self.createBttn = QPushButton(self.centralwidget)
        self.createBttn.setObjectName(u"createBttn")

        self.horizontalLayout.addWidget(self.createBttn)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 473, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Create Account", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Personal Information</span></p></body></html>", None))
        self.nameLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Full Name", None))
        self.positionLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Account Information</span></p></body></html>", None))
        self.usernameLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.passwordLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.confirmPassLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.cancelBttn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.createBttn.setText(QCoreApplication.translate("MainWindow", u"Create", None))
    # retranslateUi

