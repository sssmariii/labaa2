# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task4.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.spinBox_N = QSpinBox(self.centralwidget)
        self.spinBox_N.setObjectName(u"spinBox_N")
        self.spinBox_N.setMinimum(1)
        self.spinBox_N.setMaximum(1000)

        self.verticalLayout.addWidget(self.spinBox_N)

        self.btn_start = QPushButton(self.centralwidget)
        self.btn_start.setObjectName(u"btn_start")

        self.verticalLayout.addWidget(self.btn_start)

        self.label_remaining = QLabel(self.centralwidget)
        self.label_remaining.setObjectName(u"label_remaining")

        self.verticalLayout.addWidget(self.label_remaining)

        self.spinBox_take = QSpinBox(self.centralwidget)
        self.spinBox_take.setObjectName(u"spinBox_take")
        self.spinBox_take.setMinimum(1)
        self.spinBox_take.setMaximum(3)

        self.verticalLayout.addWidget(self.spinBox_take)

        self.btn_take = QPushButton(self.centralwidget)
        self.btn_take.setObjectName(u"btn_take")

        self.verticalLayout.addWidget(self.btn_take)

        self.textEdit_log = QTextEdit(self.centralwidget)
        self.textEdit_log.setObjectName(u"textEdit_log")
        self.textEdit_log.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit_log)

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
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0438\u0433\u0440\u0443", None))
        self.label_remaining.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043b\u043e\u0441\u044c \u043a\u0430\u043c\u043d\u0435\u0439: 0", None))
        self.btn_take.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0437\u044f\u0442\u044c", None))
    # retranslateUi

