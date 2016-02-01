# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Mon Feb  1 14:58:14 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 791, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBoxTEST = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBoxTEST.setObjectName("comboBoxTEST")
        self.comboBoxTEST.addItem("")
        self.comboBoxTEST.addItem("")
        self.comboBoxTEST.addItem("")
        self.comboBoxTEST.addItem("")
        self.verticalLayout.addWidget(self.comboBoxTEST)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 320, 80, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.menuTest = QtWidgets.QMenu(self.menubar)
        self.menuTest.setObjectName("menuTest")
        self.menuHerewe_are = QtWidgets.QMenu(self.menubar)
        self.menuHerewe_are.setObjectName("menuHerewe_are")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionThings = QtWidgets.QAction(MainWindow)
        self.actionThings.setObjectName("actionThings")
        self.actionMore_things = QtWidgets.QAction(MainWindow)
        self.actionMore_things.setObjectName("actionMore_things")
        self.actionI_am_a_button = QtWidgets.QAction(MainWindow)
        self.actionI_am_a_button.setObjectName("actionI_am_a_button")
        self.menuTest.addAction(self.actionThings)
        self.menuTest.addAction(self.actionMore_things)
        self.menuHerewe_are.addAction(self.actionI_am_a_button)
        self.menubar.addAction(self.menuTest.menuAction())
        self.menubar.addAction(self.menuHerewe_are.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBoxTEST.setItemText(0, _translate("MainWindow", "This"))
        self.comboBoxTEST.setItemText(1, _translate("MainWindow", "is"))
        self.comboBoxTEST.setItemText(2, _translate("MainWindow", "a"))
        self.comboBoxTEST.setItemText(3, _translate("MainWindow", "test"))
        self.pushButton.setText(_translate("MainWindow", "ClickMe"))
        self.menuTest.setTitle(_translate("MainWindow", "Test"))
        self.menuHerewe_are.setTitle(_translate("MainWindow", "Herewe are"))
        self.actionThings.setText(_translate("MainWindow", "things"))
        self.actionMore_things.setText(_translate("MainWindow", "more things"))
        self.actionI_am_a_button.setText(_translate("MainWindow", "i am a button"))

