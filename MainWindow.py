# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(262, 258)
        self.b_quit = QtWidgets.QPushButton(MainWindow)
        self.b_quit.setGeometry(QtCore.QRect(10, 170, 241, 41))
        self.b_quit.setObjectName("b_quit")
        self.b_redo = QtWidgets.QPushButton(MainWindow)
        self.b_redo.setGeometry(QtCore.QRect(10, 120, 111, 41))
        self.b_redo.setObjectName("b_redo")
        self.b_erase = QtWidgets.QPushButton(MainWindow)
        self.b_erase.setGeometry(QtCore.QRect(140, 20, 111, 41))
        self.b_erase.setObjectName("b_erase")
        self.b_clear = QtWidgets.QPushButton(MainWindow)
        self.b_clear.setGeometry(QtCore.QRect(140, 120, 111, 41))
        self.b_clear.setObjectName("b_clear")
        self.b_undo = QtWidgets.QPushButton(MainWindow)
        self.b_undo.setGeometry(QtCore.QRect(140, 70, 111, 41))
        self.b_undo.setObjectName("b_undo")
        self.b_write = QtWidgets.QPushButton(MainWindow)
        self.b_write.setGeometry(QtCore.QRect(10, 20, 111, 41))
        self.b_write.setObjectName("b_write")
        self.b_select = QtWidgets.QPushButton(MainWindow)
        self.b_select.setGeometry(QtCore.QRect(10, 70, 111, 41))
        self.b_select.setObjectName("b_select")
        self.c_info = QtWidgets.QCheckBox(MainWindow)
        self.c_info.setGeometry(QtCore.QRect(20, 220, 151, 19))
        self.c_info.setChecked(True)
        self.c_info.setObjectName("c_info")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MathType快捷键"))
        self.b_quit.setText(_translate("MainWindow", "退出程序"))
        self.b_redo.setText(_translate("MainWindow", "重做(Ctrl+Y)"))
        self.b_erase.setText(_translate("MainWindow", "擦除(Ctrl+E)"))
        self.b_clear.setText(_translate("MainWindow", "清除(Ctrl+Q)"))
        self.b_undo.setText(_translate("MainWindow", "撤销(Ctrl+Z)"))
        self.b_write.setText(_translate("MainWindow", "写入(Ctrl+W)"))
        self.b_select.setText(_translate("MainWindow", "选择(Ctrl+D)"))
        self.c_info.setText(_translate("MainWindow", "使用系统消息提示"))

