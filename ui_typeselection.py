# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'typeselection.ui'
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
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(446, 531)
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
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Quicksand"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.vlayoutbest = QWidget(self.centralwidget)
        self.vlayoutbest.setObjectName(u"vlayoutbest")
        self.vlayoutbest.setMinimumSize(QSize(0, 100))

        self.verticalLayout.addWidget(self.vlayoutbest)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.vlayoutkeyword = QWidget(self.centralwidget)
        self.vlayoutkeyword.setObjectName(u"vlayoutkeyword")
        self.vlayoutkeyword.setMinimumSize(QSize(0, 100))

        self.verticalLayout.addWidget(self.vlayoutkeyword)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3)

        self.vlayoutmodel = QWidget(self.centralwidget)
        self.vlayoutmodel.setObjectName(u"vlayoutmodel")
        self.vlayoutmodel.setMinimumSize(QSize(0, 100))

        self.verticalLayout.addWidget(self.vlayoutmodel)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancelBttn = QPushButton(self.centralwidget)
        self.cancelBttn.setObjectName(u"cancelBttn")

        self.horizontalLayout.addWidget(self.cancelBttn)

        self.confirmBttn = QPushButton(self.centralwidget)
        self.confirmBttn.setObjectName(u"confirmBttn")

        self.horizontalLayout.addWidget(self.confirmBttn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Type Selection", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"BEST MATCHES", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"KEYWORD MATCHES", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"MODEL MATCHES", None))
        self.cancelBttn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.confirmBttn.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
    # retranslateUi

