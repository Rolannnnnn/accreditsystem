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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(496, 556)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 131, 31))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(90, 60, 301, 91))
        self.vlayoutbest = QVBoxLayout(self.verticalLayoutWidget)
        self.vlayoutbest.setObjectName(u"vlayoutbest")
        self.vlayoutbest.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 160, 211, 31))
        self.label_2.setFont(font)
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(90, 200, 301, 91))
        self.vlayoutkeyword = QVBoxLayout(self.verticalLayoutWidget_2)
        self.vlayoutkeyword.setObjectName(u"vlayoutkeyword")
        self.vlayoutkeyword.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 300, 211, 31))
        self.label_3.setFont(font)
        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(90, 340, 301, 91))
        self.vlayoutmodel = QVBoxLayout(self.verticalLayoutWidget_3)
        self.vlayoutmodel.setObjectName(u"vlayoutmodel")
        self.vlayoutmodel.setContentsMargins(0, 0, 0, 0)
        self.confirmBttn = QPushButton(self.centralwidget)
        self.confirmBttn.setObjectName(u"confirmBttn")
        self.confirmBttn.setGeometry(QRect(400, 460, 79, 24))
        self.cancelBttn = QPushButton(self.centralwidget)
        self.cancelBttn.setObjectName(u"cancelBttn")
        self.cancelBttn.setGeometry(QRect(20, 460, 79, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 496, 33))
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
        self.confirmBttn.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.cancelBttn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
    # retranslateUi

