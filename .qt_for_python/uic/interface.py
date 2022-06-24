# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Leung\Documents\GitHub\LiteraPy\interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_litera_window(object):
    def setupUi(self, litera_window):
        litera_window.setObjectName("litera_window")
        litera_window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(litera_window)
        self.centralwidget.setObjectName("centralwidget")
        self.search_input = QtWidgets.QLineEdit(self.centralwidget)
        self.search_input.setGeometry(QtCore.QRect(10, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.search_input.setFont(font)
        self.search_input.setObjectName("search_input")
        self.adsearch_browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.adsearch_browser.setGeometry(QtCore.QRect(400, 50, 381, 491))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.adsearch_browser.setFont(font)
        self.adsearch_browser.setObjectName("adsearch_browser")
        self.search_browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.search_browser.setGeometry(QtCore.QRect(10, 50, 381, 491))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.search_browser.setFont(font)
        self.search_browser.setObjectName("search_browser")
        self.lang_chs = QtWidgets.QCheckBox(self.centralwidget)
        self.lang_chs.setGeometry(QtCore.QRect(690, 8, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.lang_chs.setFont(font)
        self.lang_chs.setObjectName("lang_chs")
        litera_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(litera_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        litera_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(litera_window)
        self.statusbar.setObjectName("statusbar")
        litera_window.setStatusBar(self.statusbar)
        self.actionDictionary_Modifier = QtWidgets.QAction(litera_window)
        self.actionDictionary_Modifier.setObjectName("actionDictionary_Modifier")
        self.dmod_action = QtWidgets.QAction(litera_window)
        self.dmod_action.setObjectName("dmod_action")
        self.menu.addAction(self.dmod_action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(litera_window)
        QtCore.QMetaObject.connectSlotsByName(litera_window)

    def retranslateUi(self, litera_window):
        _translate = QtCore.QCoreApplication.translate
        litera_window.setWindowTitle(_translate("litera_window", "Litera"))
        self.search_input.setPlaceholderText(_translate("litera_window", "搜尋中文字詞"))
        self.lang_chs.setText(_translate("litera_window", "zh-CHS"))
        self.menu.setTitle(_translate("litera_window", "Menu"))
        self.actionDictionary_Modifier.setText(_translate("litera_window", "Dictionary Modifier"))
        self.dmod_action.setText(_translate("litera_window", "Dictionary Modifier"))
