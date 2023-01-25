# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 599)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(48, 48))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1368, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuInicio = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.menuInicio.setFont(font)
        self.menuInicio.setSeparatorsCollapsible(True)
        self.menuInicio.setToolTipsVisible(True)
        self.menuInicio.setObjectName("menuInicio")
        self.menuSoportes = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.menuSoportes.setFont(font)
        self.menuSoportes.setMouseTracking(True)
        self.menuSoportes.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.menuSoportes.setTearOffEnabled(False)
        self.menuSoportes.setSeparatorsCollapsible(True)
        self.menuSoportes.setToolTipsVisible(True)
        self.menuSoportes.setObjectName("menuSoportes")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.menuAyuda.setFont(font)
        self.menuAyuda.setObjectName("menuAyuda")
        self.menuAyuda_2 = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.menuAyuda_2.setFont(font)
        self.menuAyuda_2.setTearOffEnabled(True)
        self.menuAyuda_2.setSeparatorsCollapsible(True)
        self.menuAyuda_2.setToolTipsVisible(True)
        self.menuAyuda_2.setObjectName("menuAyuda_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionManual_de_usuario = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/images/icons/user-manual.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionManual_de_usuario.setIcon(icon1)
        self.actionManual_de_usuario.setObjectName("actionManual_de_usuario")
        self.actionAcerca_de = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/images/icons/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAcerca_de.setIcon(icon2)
        self.actionAcerca_de.setObjectName("actionAcerca_de")
        self.actionInternet_HFC = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/images/icons/ethernet.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInternet_HFC.setIcon(icon3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.actionInternet_HFC.setFont(font)
        self.actionInternet_HFC.setObjectName("actionInternet_HFC")
        self.action_hfc_tv = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/images/icons/tv-antenna.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_hfc_tv.setIcon(icon4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.action_hfc_tv.setFont(font)
        self.action_hfc_tv.setObjectName("action_hfc_tv")
        self.actionTelevisi_n_Satalital_DTH = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/images/icons/satelital.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTelevisi_n_Satalital_DTH.setIcon(icon5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.actionTelevisi_n_Satalital_DTH.setFont(font)
        self.actionTelevisi_n_Satalital_DTH.setObjectName("actionTelevisi_n_Satalital_DTH")
        self.actionFibra_Hogar = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/images/icons/wi-fi-router.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFibra_Hogar.setIcon(icon6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.actionFibra_Hogar.setFont(font)
        self.actionFibra_Hogar.setObjectName("actionFibra_Hogar")
        self.actionCorreos_electr_nicos = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/images/icons/circled-envelope.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCorreos_electr_nicos.setIcon(icon7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.actionCorreos_electr_nicos.setFont(font)
        self.actionCorreos_electr_nicos.setObjectName("actionCorreos_electr_nicos")
        self.exitAction = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/images/icons/close-window.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitAction.setIcon(icon8)
        self.exitAction.setObjectName("exitAction")
        self.actionSettingsDolar = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/images/icons/dollar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettingsDolar.setIcon(icon9)
        self.actionSettingsDolar.setObjectName("actionSettingsDolar")
        self.actionConfiguraci_n_Precios = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/images/icons/money.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConfiguraci_n_Precios.setIcon(icon10)
        self.actionConfiguraci_n_Precios.setObjectName("actionConfiguraci_n_Precios")
        self.actionConfiguraci_n_Plantillas = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/images/images/icons/content.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConfiguraci_n_Plantillas.setIcon(icon11)
        self.actionConfiguraci_n_Plantillas.setObjectName("actionConfiguraci_n_Plantillas")
        self.actionProductos = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/images/images/icons/package.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProductos.setIcon(icon12)
        self.actionProductos.setObjectName("actionProductos")
        self.actionPrincipal = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/images/images/icons/dashboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrincipal.setIcon(icon13)
        self.actionPrincipal.setObjectName("actionPrincipal")
        self.menuInicio.addAction(self.actionPrincipal)
        self.menuInicio.addAction(self.exitAction)
        self.menuSoportes.addAction(self.actionInternet_HFC)
        self.menuSoportes.addAction(self.action_hfc_tv)
        self.menuSoportes.addAction(self.actionTelevisi_n_Satalital_DTH)
        self.menuSoportes.addAction(self.actionFibra_Hogar)
        self.menuSoportes.addAction(self.actionCorreos_electr_nicos)
        self.menuAyuda.addAction(self.actionSettingsDolar)
        self.menuAyuda.addAction(self.actionConfiguraci_n_Precios)
        self.menuAyuda.addAction(self.actionConfiguraci_n_Plantillas)
        self.menuAyuda.addAction(self.actionProductos)
        self.menuAyuda_2.addAction(self.actionManual_de_usuario)
        self.menuAyuda_2.addAction(self.actionAcerca_de)
        self.menubar.addAction(self.menuInicio.menuAction())
        self.menubar.addAction(self.menuSoportes.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menubar.addAction(self.menuAyuda_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Asistente Soporte Inter WhatsApp Venezuela"))
        self.menuInicio.setTitle(_translate("MainWindow", "Inicio"))
        self.menuSoportes.setToolTip(_translate("MainWindow", "Soportes"))
        self.menuSoportes.setTitle(_translate("MainWindow", "Soportes"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Configuraciones"))
        self.menuAyuda_2.setTitle(_translate("MainWindow", "Ayuda"))
        self.actionManual_de_usuario.setText(_translate("MainWindow", "Manual de usuario"))
        self.actionManual_de_usuario.setShortcut(_translate("MainWindow", "F1"))
        self.actionAcerca_de.setText(_translate("MainWindow", "Acerca de"))
        self.actionAcerca_de.setShortcut(_translate("MainWindow", "F11"))
        self.actionInternet_HFC.setText(_translate("MainWindow", "Internet (HFC)"))
        self.action_hfc_tv.setText(_translate("MainWindow", "Televsión por cable (HFC)"))
        self.actionTelevisi_n_Satalital_DTH.setText(_translate("MainWindow", "Televisión Satalital DTH"))
        self.actionFibra_Hogar.setText(_translate("MainWindow", "Fibra Hogar"))
        self.actionCorreos_electr_nicos.setText(_translate("MainWindow", "Correos electrónicos"))
        self.exitAction.setText(_translate("MainWindow", "Salir"))
        self.exitAction.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionSettingsDolar.setText(_translate("MainWindow", "Precio dolar BCV"))
        self.actionConfiguraci_n_Precios.setText(_translate("MainWindow", "Precios"))
        self.actionConfiguraci_n_Plantillas.setText(_translate("MainWindow", "Plantillas"))
        self.actionProductos.setText(_translate("MainWindow", "Productos"))
        self.actionPrincipal.setText(_translate("MainWindow", "Principal"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
