# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 100)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/icons/dollar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 50, 151, 30))
        self.label_4.setObjectName("label_4")
        self.bn_set_dolar = QtWidgets.QPushButton(Dialog)
        self.bn_set_dolar.setGeometry(QtCore.QRect(380, 20, 32, 32))
        self.bn_set_dolar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/images/icons/ok.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_set_dolar.setIcon(icon1)
        self.bn_set_dolar.setIconSize(QtCore.QSize(24, 24))
        self.bn_set_dolar.setObjectName("bn_set_dolar")
        self.txt_dolar = QtWidgets.QLineEdit(Dialog)
        self.txt_dolar.setGeometry(QtCore.QRect(250, 20, 121, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_dolar.sizePolicy().hasHeightForWidth())
        self.txt_dolar.setSizePolicy(sizePolicy)
        self.txt_dolar.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhPreferNumbers)
        self.txt_dolar.setInputMask("")
        self.txt_dolar.setText("")
        self.txt_dolar.setMaxLength(5)
        self.txt_dolar.setFrame(True)
        self.txt_dolar.setPlaceholderText("")
        self.txt_dolar.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.txt_dolar.setObjectName("txt_dolar")
        self.lbl_date = QtWidgets.QLabel(Dialog)
        self.lbl_date.setGeometry(QtCore.QRect(20, 20, 221, 31))
        self.lbl_date.setObjectName("lbl_date")
        self.lbl_dolar = QtWidgets.QLabel(Dialog)
        self.lbl_dolar.setGeometry(QtCore.QRect(120, 50, 111, 30))
        self.lbl_dolar.setObjectName("lbl_dolar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Configuración precio dolar BCV"))
        self.label_4.setText(_translate("Dialog", "Precio Dolar BCV"))
        self.lbl_date.setText(_translate("Dialog", "Precio del dolar del día 18/01/2023"))
        self.lbl_dolar.setText(_translate("Dialog", "$1 = Bs. 150.55"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
