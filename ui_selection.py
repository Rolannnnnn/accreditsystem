# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'selection.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(488, 506)
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
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pathEdit = QLineEdit(self.centralwidget)
        self.pathEdit.setObjectName(u"pathEdit")

        self.gridLayout.addWidget(self.pathEdit, 1, 0, 1, 1)

        self.chooseBttn = QPushButton(self.centralwidget)
        self.chooseBttn.setObjectName(u"chooseBttn")

        self.gridLayout.addWidget(self.chooseBttn, 1, 1, 1, 1)

        self.imageframe = QLabel(self.centralwidget)
        self.imageframe.setObjectName(u"imageframe")
        self.imageframe.setMinimumSize(QSize(0, 280))
        self.imageframe.setFrameShadow(QFrame.Shadow.Raised)
        self.imageframe.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.imageframe, 0, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.backBttn = QPushButton(self.centralwidget)
        self.backBttn.setObjectName(u"backBttn")
        self.backBttn.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.horizontalLayout.addWidget(self.backBttn)

        self.isImageCB = QCheckBox(self.centralwidget)
        self.isImageCB.setObjectName(u"isImageCB")

        self.horizontalLayout.addWidget(self.isImageCB)

        self.processBttn = QPushButton(self.centralwidget)
        self.processBttn.setObjectName(u"processBttn")

        self.horizontalLayout.addWidget(self.processBttn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.logsBttn = QPushButton(self.centralwidget)
        self.logsBttn.setObjectName(u"logsBttn")

        self.horizontalLayout_4.addWidget(self.logsBttn)

        self.createBttn = QPushButton(self.centralwidget)
        self.createBttn.setObjectName(u"createBttn")

        self.horizontalLayout_4.addWidget(self.createBttn)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 488, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.pathEdit, self.chooseBttn)
        QWidget.setTabOrder(self.chooseBttn, self.backBttn)
        QWidget.setTabOrder(self.backBttn, self.isImageCB)
        QWidget.setTabOrder(self.isImageCB, self.processBttn)
        QWidget.setTabOrder(self.processBttn, self.logsBttn)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Selection", None))
        self.pathEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"No File Selected...", None))
        self.chooseBttn.setText(QCoreApplication.translate("MainWindow", u"Select File", None))
        self.imageframe.setText(QCoreApplication.translate("MainWindow", u"No File Selected", None))
        self.backBttn.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.isImageCB.setText(QCoreApplication.translate("MainWindow", u"This Document is Mostly Imagery", None))
        self.processBttn.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.logsBttn.setText(QCoreApplication.translate("MainWindow", u"View Logs", None))
        self.createBttn.setText(QCoreApplication.translate("MainWindow", u"Create Account", None))
    # retranslateUi

