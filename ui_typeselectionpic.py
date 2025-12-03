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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, typeselectorpic):
        if not typeselectorpic.objectName():
            typeselectorpic.setObjectName(u"typeselectorpic")
        typeselectorpic.resize(345, 409)
        self.centralwidget = QWidget(typeselectorpic)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 101, 31))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)
        self.confirmBttn = QPushButton(self.centralwidget)
        self.confirmBttn.setObjectName(u"confirmBttn")
        self.confirmBttn.setGeometry(QRect(250, 320, 79, 24))
        self.cancelBttn = QPushButton(self.centralwidget)
        self.cancelBttn.setObjectName(u"cancelBttn")
        self.cancelBttn.setGeometry(QRect(20, 320, 79, 24))
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(30, 60, 281, 241))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 279, 239))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        typeselectorpic.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(typeselectorpic)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 345, 33))
        typeselectorpic.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(typeselectorpic)
        self.statusbar.setObjectName(u"statusbar")
        typeselectorpic.setStatusBar(self.statusbar)

        self.retranslateUi(typeselectorpic)

        QMetaObject.connectSlotsByName(typeselectorpic)
    # setupUi

    def retranslateUi(self, typeselectorpic):
        typeselectorpic.setWindowTitle(QCoreApplication.translate("typeselectorpic", u"typeselectorpic", None))
        self.label.setText(QCoreApplication.translate("typeselectorpic", u"Select Type", None))
        self.confirmBttn.setText(QCoreApplication.translate("typeselectorpic", u"Confirm", None))
        self.cancelBttn.setText(QCoreApplication.translate("typeselectorpic", u"Cancel", None))
    # retranslateUi

