# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task3.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit_name = QLineEdit(self.centralwidget)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.verticalLayout.addWidget(self.lineEdit_name)

        self.lineEdit_phone = QLineEdit(self.centralwidget)
        self.lineEdit_phone.setObjectName(u"lineEdit_phone")

        self.verticalLayout.addWidget(self.lineEdit_phone)

        self.btn_add = QPushButton(self.centralwidget)
        self.btn_add.setObjectName(u"btn_add")

        self.verticalLayout.addWidget(self.btn_add)

        self.listWidget_contacts = QListWidget(self.centralwidget)
        self.listWidget_contacts.setObjectName(u"listWidget_contacts")

        self.verticalLayout.addWidget(self.listWidget_contacts)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 36))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u0430", None))
        self.lineEdit_phone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

