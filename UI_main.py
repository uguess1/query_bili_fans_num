# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
from base64 import b64decode

from PyQt5 import QtCore, QtGui, QtWidgets

from memory_pic import *


def get_pic(pic_code, pic_name):
    image = open(pic_name, "wb")
    image.write(b64decode(pic_code))
    image.close()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(301, 174)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.query_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.query_line_edit.setGeometry(QtCore.QRect(10, 10, 211, 20))
        self.query_line_edit.setObjectName("query_line_edit")
        self.refresh_Button = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_Button.setGeometry(QtCore.QRect(230, 10, 61, 21))
        self.refresh_Button.setObjectName("refresh_Button")

        self.help_Button = QtWidgets.QPushButton(self.centralwidget)
        self.help_Button.setGeometry(QtCore.QRect(13, 135, 16, 16))
        self.help_Button.setObjectName("help_Button")

        get_pic(help_png, "help.png")
        self.help_Button.setIcon(QtGui.QIcon("help.png"))
        self.help_Button.setStyleSheet("border-radius: 8px;")
        self.help_Button.setToolTip("帮助")
        os.remove("help.png")

        self.label_fansnum = QtWidgets.QLabel(self.centralwidget)
        self.label_fansnum.setGeometry(QtCore.QRect(10, 40, 281, 81))
        self.label_fansnum.setObjectName("label_fansnum")
        # 居中
        self.label_fansnum.setAlignment(QtCore.Qt.AlignCenter)
        # 字号字体
        self.label_fansnum.setStyleSheet("QLabel{font-size:58px;font-family:微软雅黑;}")

        self.label_change = QtWidgets.QLabel(self.centralwidget)
        self.label_change.setGeometry(QtCore.QRect(130, 130, 171, 20))
        self.label_change.setObjectName("label_change")
        self.label_change.setStyleSheet("QLabel{font-size:12px;font-family:微软雅黑;}")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "粉丝数查询"))
        self.refresh_Button.setText(_translate("MainWindow", "刷新"))
        # self.help_Button.setText(_translate("MainWindow", "?"))
