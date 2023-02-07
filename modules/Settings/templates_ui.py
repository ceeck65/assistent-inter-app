# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\templates.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1378, 694)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1332, 671))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 20, 991, 231))
        self.groupBox_2.setObjectName("groupBox_2")
        self.cancel_template = QtWidgets.QPushButton(self.groupBox_2)
        self.cancel_template.setGeometry(QtCore.QRect(870, 190, 110, 32))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/icons/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_template.setIcon(icon)
        self.cancel_template.setObjectName("cancel_template")
        self.save_template = QtWidgets.QPushButton(self.groupBox_2)
        self.save_template.setGeometry(QtCore.QRect(740, 190, 110, 32))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/images/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_template.setIcon(icon1)
        self.save_template.setObjectName("save_template")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 40, 271, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.template_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.template_name.setClearButtonEnabled(True)
        self.template_name.setObjectName("template_name")
        self.verticalLayout_5.addWidget(self.template_name)
        self.layoutWidget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget_3.setGeometry(QtCore.QRect(760, 40, 211, 51))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_11.addWidget(self.label_11)
        self.type_template = QtWidgets.QComboBox(self.layoutWidget_3)
        self.type_template.setObjectName("type_template")
        self.verticalLayout_11.addWidget(self.type_template)
        self.template_txt = QtWidgets.QTextEdit(self.groupBox_2)
        self.template_txt.setGeometry(QtCore.QRect(20, 140, 661, 71))
        self.template_txt.setObjectName("template_txt")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(21, 111, 44, 16))
        self.label.setObjectName("label")
        self.layoutWidget_4 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget_4.setGeometry(QtCore.QRect(310, 40, 211, 51))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_10.addWidget(self.label_10)
        self.products = QtWidgets.QComboBox(self.layoutWidget_4)
        self.products.setObjectName("products")
        self.verticalLayout_10.addWidget(self.products)
        self.layoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(540, 40, 201, 51))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_9.addWidget(self.label_9)
        self.plans_package = QtWidgets.QComboBox(self.layoutWidget_2)
        self.plans_package.setObjectName("plans_package")
        self.verticalLayout_9.addWidget(self.plans_package)
        self.tbl_templates = QtWidgets.QTableView(self.tab)
        self.tbl_templates.setGeometry(QtCore.QRect(20, 280, 1000, 340))
        self.tbl_templates.setObjectName("tbl_templates")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(1060, 20, 221, 271))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 191, 211))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.label_2.setIndent(-2)
        self.label_2.setObjectName("label_2")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/images/icons/content.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_2.setTitle(_translate("Dialog", "Nueva Plantilla"))
        self.cancel_template.setText(_translate("Dialog", "Cancelar"))
        self.save_template.setText(_translate("Dialog", "Registrar"))
        self.label_5.setText(_translate("Dialog", "Nombre"))
        self.template_name.setPlaceholderText(_translate("Dialog", "Ingrese nombre de plan o paquete"))
        self.label_11.setText(_translate("Dialog", "Tipo de Plantilla"))
        self.label.setText(_translate("Dialog", "Plantilla"))
        self.label_10.setText(_translate("Dialog", "Producto"))
        self.label_9.setText(_translate("Dialog", "Categoría"))
        self.groupBox.setTitle(_translate("Dialog", "Ayudas"))
        self.label_2.setText(_translate("Dialog", "Para agregar datos:\n"
"\n"
"%d     Si es un número entero.\n"
"\n"
"%s     Si es un texto.\n"
"\n"
"%.2f  Si es un número \n"
"         real con decimales.\n"
""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Plantillas"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
