# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '100.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TextEditFormula = QtWidgets.QTextEdit(self.centralwidget)
        self.TextEditFormula.setGeometry(QtCore.QRect(30, 370, 631, 41))
        self.TextEditFormula.setObjectName("TextEditFormula")
        self.ButtonCalculate = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonCalculate.setGeometry(QtCore.QRect(430, 420, 111, 23))
        self.ButtonCalculate.setObjectName("ButtonCalculate")
        self.ButtonClear = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonClear.setGeometry(QtCore.QRect(560, 420, 101, 23))
        self.ButtonClear.setObjectName("ButtonClear")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 70, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 70, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 70, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(360, 70, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(450, 70, 47, 13))
        self.label_5.setObjectName("label_5")
        self.TextEdit_LG = QtWidgets.QTextEdit(self.centralwidget)
        self.TextEdit_LG.setGeometry(QtCore.QRect(110, 420, 61, 31))
        self.TextEdit_LG.setObjectName("TextEdit_LG")
        self.TextEdit_PG = QtWidgets.QTextEdit(self.centralwidget)
        self.TextEdit_PG.setGeometry(QtCore.QRect(180, 420, 61, 31))
        self.TextEdit_PG.setObjectName("TextEdit_PG")
        self.TextEdit_KolPer = QtWidgets.QTextEdit(self.centralwidget)
        self.TextEdit_KolPer.setGeometry(QtCore.QRect(110, 460, 61, 31))
        self.TextEdit_KolPer.setObjectName("TextEdit_KolPer")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "???????????????????? ?????????????????? ??????????????"))
        self.ButtonCalculate.setText(_translate("MainWindow", "?????????????????? ????????????????"))
        self.ButtonClear.setText(_translate("MainWindow", "????????????????"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
