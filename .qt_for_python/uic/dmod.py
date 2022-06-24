# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Leung\Documents\GitHub\LiteraPy\dmod.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dmod_window(object):
    def setupUi(self, dmod_window):
        dmod_window.setObjectName("dmod_window")
        dmod_window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(dmod_window)
        self.centralwidget.setObjectName("centralwidget")
        self.cht_input = QtWidgets.QLineEdit(self.centralwidget)
        self.cht_input.setGeometry(QtCore.QRect(410, 50, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.cht_input.setFont(font)
        self.cht_input.setObjectName("cht_input")
        self.chs_input = QtWidgets.QLineEdit(self.centralwidget)
        self.chs_input.setGeometry(QtCore.QRect(410, 90, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.chs_input.setFont(font)
        self.chs_input.setObjectName("chs_input")
        self.pinyin_input = QtWidgets.QLineEdit(self.centralwidget)
        self.pinyin_input.setGeometry(QtCore.QRect(410, 130, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.pinyin_input.setFont(font)
        self.pinyin_input.setObjectName("pinyin_input")
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setGeometry(QtCore.QRect(430, 170, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.dmod_browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.dmod_browser.setGeometry(QtCore.QRect(10, 50, 381, 491))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.dmod_browser.setFont(font)
        self.dmod_browser.setObjectName("dmod_browser")
        self.preview_label = QtWidgets.QLabel(self.centralwidget)
        self.preview_label.setGeometry(QtCore.QRect(10, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.preview_label.setFont(font)
        self.preview_label.setObjectName("preview_label")
        self.confirm_button = QtWidgets.QPushButton(self.centralwidget)
        self.confirm_button.setGeometry(QtCore.QRect(680, 510, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.confirm_button.setFont(font)
        self.confirm_button.setObjectName("confirm_button")
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setGeometry(QtCore.QRect(430, 210, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.delete_button.setFont(font)
        self.delete_button.setObjectName("delete_button")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(430, 250, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.clear_button.setFont(font)
        self.clear_button.setObjectName("clear_button")
        dmod_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(dmod_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        dmod_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(dmod_window)
        self.statusbar.setObjectName("statusbar")
        dmod_window.setStatusBar(self.statusbar)

        self.retranslateUi(dmod_window)
        QtCore.QMetaObject.connectSlotsByName(dmod_window)

    def retranslateUi(self, dmod_window):
        _translate = QtCore.QCoreApplication.translate
        dmod_window.setWindowTitle(_translate("dmod_window", "Dictionary Modifier"))
        self.cht_input.setPlaceholderText(_translate("dmod_window", "輸入繁體字詞"))
        self.chs_input.setPlaceholderText(_translate("dmod_window", "輸入簡體字詞"))
        self.pinyin_input.setPlaceholderText(_translate("dmod_window", "輸入拼音"))
        self.add_button.setText(_translate("dmod_window", "加入字詞"))
        self.preview_label.setText(_translate("dmod_window", "修改預覽"))
        self.confirm_button.setText(_translate("dmod_window", "確定修改"))
        self.delete_button.setText(_translate("dmod_window", "刪除字詞"))
        self.clear_button.setText(_translate("dmod_window", "清除"))
