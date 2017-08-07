# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.btnAccion = QtWidgets.QPushButton(Dialog)
        self.btnAccion.setEnabled(True)
        self.btnAccion.setGeometry(QtCore.QRect(90, 40, 85, 27))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.btnAccion.setFont(font)
        self.btnAccion.setObjectName("btnAccion")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(90, 70, 87, 22))
        self.checkBox.setObjectName("checkBox")
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(100, 140, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(90, 100, 110, 27))
        self.dateEdit.setObjectName("dateEdit")
        self.lineEdit_1 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_1.setGeometry(QtCore.QRect(100, 190, 113, 27))
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 240, 113, 27))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 190, 54, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 240, 54, 17))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        self.lineEdit_1.textEdited['QString'].connect(self.lineEdit_2.setText)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit_1, self.lineEdit_2)
        Dialog.setTabOrder(self.lineEdit_2, self.dateEdit)
        Dialog.setTabOrder(self.dateEdit, self.btnAccion)
        Dialog.setTabOrder(self.btnAccion, self.checkBox)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnAccion.setText(_translate("Dialog", "PushButton"))
        self.checkBox.setText(_translate("Dialog", "CheckBox"))
        self.label.setText(_translate("Dialog", "Uno:"))
        self.label_2.setText(_translate("Dialog", "Dos:"))

