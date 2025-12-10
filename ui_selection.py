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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(488, 465)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.chooseBttn = QPushButton(self.centralwidget)
        self.chooseBttn.setObjectName(u"chooseBttn")
        self.chooseBttn.setGeometry(QRect(370, 300, 79, 24))
        self.backBttn = QPushButton(self.centralwidget)
        self.backBttn.setObjectName(u"backBttn")
        self.backBttn.setGeometry(QRect(10, 350, 79, 24))
        self.backBttn.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.processBttn = QPushButton(self.centralwidget)
        self.processBttn.setObjectName(u"processBttn")
        self.processBttn.setGeometry(QRect(400, 350, 79, 24))
        self.pathEdit = QLineEdit(self.centralwidget)
        self.pathEdit.setObjectName(u"pathEdit")
        self.pathEdit.setGeometry(QRect(50, 300, 301, 21))
        self.imageframe = QLabel(self.centralwidget)
        self.imageframe.setObjectName(u"imageframe")
        self.imageframe.setGeometry(QRect(80, 29, 341, 241))
        self.imageframe.setFrameShadow(QFrame.Shadow.Raised)
        self.imageframe.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.isImageCB = QCheckBox(self.centralwidget)
        self.isImageCB.setObjectName(u"isImageCB")
        self.isImageCB.setGeometry(QRect(150, 350, 201, 20))
        self.logsBttn = QPushButton(self.centralwidget)
        self.logsBttn.setObjectName(u"logsBttn")
        self.logsBttn.setGeometry(QRect(200, 380, 79, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 488, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Selection", None))
        self.chooseBttn.setText(QCoreApplication.translate("MainWindow", u"Select File", None))
        self.backBttn.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.processBttn.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.pathEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"No File Selected...", None))
        self.imageframe.setText(QCoreApplication.translate("MainWindow", u"No File Selected", None))
        self.isImageCB.setText(QCoreApplication.translate("MainWindow", u"This Document is Mostly Imagery", None))
        self.logsBttn.setText(QCoreApplication.translate("MainWindow", u"View Logs", None))
    # retranslateUi

