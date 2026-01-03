# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'typeselectionpic.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_typeselectorpic(object):
    def setupUi(self, typeselectorpic):
        if not typeselectorpic.objectName():
            typeselectorpic.setObjectName(u"typeselectorpic")
        typeselectorpic.resize(423, 409)
        typeselectorpic.setStyleSheet(u"QMainWindow {\n"
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
        self.centralwidget = QWidget(typeselectorpic)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 381, 331))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Quicksand"])
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 377, 268))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancelBttn = QPushButton(self.widget)
        self.cancelBttn.setObjectName(u"cancelBttn")

        self.horizontalLayout.addWidget(self.cancelBttn)

        self.confirmBttn = QPushButton(self.widget)
        self.confirmBttn.setObjectName(u"confirmBttn")

        self.horizontalLayout.addWidget(self.confirmBttn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        typeselectorpic.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(typeselectorpic)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 423, 33))
        typeselectorpic.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(typeselectorpic)
        self.statusbar.setObjectName(u"statusbar")
        typeselectorpic.setStatusBar(self.statusbar)

        self.retranslateUi(typeselectorpic)

        QMetaObject.connectSlotsByName(typeselectorpic)
    # setupUi

    def retranslateUi(self, typeselectorpic):
        typeselectorpic.setWindowTitle(QCoreApplication.translate("typeselectorpic", u"Type Selector", None))
        self.label.setText(QCoreApplication.translate("typeselectorpic", u"SELECT TYPE", None))
        self.cancelBttn.setText(QCoreApplication.translate("typeselectorpic", u"Cancel", None))
        self.confirmBttn.setText(QCoreApplication.translate("typeselectorpic", u"Confirm", None))
    # retranslateUi

