# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'flag.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
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
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.rb1_green = QRadioButton(self.groupBox)
        self.rb1_green.setObjectName(u"rb1_green")
        self.rb1_green.setGeometry(QRect(10, 60, 99, 20))
        self.rb1_white = QRadioButton(self.groupBox)
        self.rb1_white.setObjectName(u"rb1_white")
        self.rb1_white.setGeometry(QRect(10, 90, 99, 20))
        self.rb1_red = QRadioButton(self.groupBox)
        self.rb1_red.setObjectName(u"rb1_red")
        self.rb1_red.setGeometry(QRect(10, 30, 99, 20))

        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.rb2_red = QRadioButton(self.groupBox_2)
        self.rb2_red.setObjectName(u"rb2_red")
        self.rb2_red.setGeometry(QRect(10, 30, 99, 20))
        self.rb2_green = QRadioButton(self.groupBox_2)
        self.rb2_green.setObjectName(u"rb2_green")
        self.rb2_green.setGeometry(QRect(10, 60, 99, 20))
        self.rb2_white = QRadioButton(self.groupBox_2)
        self.rb2_white.setObjectName(u"rb2_white")
        self.rb2_white.setGeometry(QRect(10, 90, 99, 20))

        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.rb3_red = QRadioButton(self.groupBox_3)
        self.rb3_red.setObjectName(u"rb3_red")
        self.rb3_red.setGeometry(QRect(10, 30, 99, 20))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rb3_red.sizePolicy().hasHeightForWidth())
        self.rb3_red.setSizePolicy(sizePolicy)
        self.rb3_green = QRadioButton(self.groupBox_3)
        self.rb3_green.setObjectName(u"rb3_green")
        self.rb3_green.setGeometry(QRect(10, 60, 99, 20))
        self.rb3_white = QRadioButton(self.groupBox_3)
        self.rb3_white.setObjectName(u"rb3_white")
        self.rb3_white.setGeometry(QRect(10, 90, 99, 20))

        self.verticalLayout.addWidget(self.groupBox_3)

        self.btn_draw = QPushButton(self.centralwidget)
        self.btn_draw.setObjectName(u"btn_draw")

        self.verticalLayout.addWidget(self.btn_draw)

        self.label_result = QLabel(self.centralwidget)
        self.label_result.setObjectName(u"label_result")

        self.verticalLayout.addWidget(self.label_result)

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
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.rb1_green.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0435\u043b\u0451\u043d\u044b\u0439", None))
        self.rb1_white.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0435\u043b\u044b\u0439", None))
        self.rb1_red.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0430\u0441\u043d\u044b\u0439", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.rb2_red.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0430\u0441\u043d\u044b\u0439", None))
        self.rb2_green.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0435\u043b\u0451\u043d\u044b\u0439", None))
        self.rb2_white.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0435\u043b\u044b\u0439", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.rb3_red.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0430\u0441\u043d\u044b\u0439", None))
        self.rb3_green.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0435\u043b\u0451\u043d\u044b\u0439", None))
        self.rb3_white.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0435\u043b\u044b\u0439", None))
        self.btn_draw.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0440\u0438\u0441\u043e\u0432\u0430\u0442\u044c", None))
        self.label_result.setText("")
    # retranslateUi

