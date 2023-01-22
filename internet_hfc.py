import sys 
import typing 
from builtins import super 
from datetime import date

from images import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from dashboard_ui import *


from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QDesktopWidget,
    QMessageBox,
)

from random import randint
from dth import *
from data import *


class IntertScreen(QWidget):
    def __init__(self):
        super(DashboardScreen, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.dth = dth()
        self.data = Data()
        self.ui.lblDolar.setText("$1 = Bs. 0")
        self.ui.tabWidget.setMaximumWidth(width_screen)
        self.ui.tabWidget.setMaximumHeight(height_screen)
        self.ui.tabWidgetTicketsDTH.setMaximumWidth(width_screen)
        self.ui.tabWidgetTicketsDTH.setMaximumHeight(height_screen)        
        self.ui.onlyDouble= QDoubleValidator()
        self.ui.txtDolar.setValidator(self.ui.onlyDouble)
        self.ui.btnSetDolar.clicked.connect(self.setDolar)
        self.ui.btn_ticket_dth.clicked.connect(self.generateTicketsDTH)
        self.ui.btn_clear_dth.clicked.connect(self.clearDHT)
        self.ui.lblPriceReferentialDolarDTH.setText("Precio del dolar del día %s, Bs. %.2f" % (_date, _dolar))
        self.ui.txtDolar.returnPressed.connect(self.ui.btnSetDolar.click)
        self.ui.txtDolar.setText(str(_dolar))

        self.ui.btn_ticket_internet_hfc.clicked.connect(self.generateTicketInternetHCF)
        self.ui.btn_clear_internet_hfc.clicked.connect(self.clearInternetHCF)

        # Checkbox RF
        self.ui.rf_ok.stateChanged.connect(self.disableRf)
        self.ui.rf_dwpw.stateChanged.connect (self.checkRf)
        self.ui.rf_rxpw.stateChanged.connect (self.checkRf)
        self.ui.rf_uppw.stateChanged.connect (self.checkRf)
        self.ui.rf_dwsnr.stateChanged.connect (self.checkRf)
        self.ui.rf_upsnr.stateChanged.connect (self.checkRf)
        self.ui.rf_hit_miss.stateChanged.connect (self.checkRf)
        self.ui.rf_flaps.stateChanged.connect (self.checkRf)
        self.ui.rf_ajust_pot.stateChanged.connect (self.checkRf)
        self.ui.service_hfc.setText("")
        self.ui.combo_cm_mta.activated.connect(self.changeMtaModen)

    def setDolar(self):
        global _dolar
        if self.ui.txtDolar.text() == "":
            __dolar = 0
            self.data.setDolar(__dolar)
            self.ui.txtDolar.setText(str(self.data.getDolar()))
        else:
            __dolar = float(self.ui.txtDolar.text())
            self.data.setDolar(__dolar)
            _dolar = self.data.getDolar()
            self.ui.txtDolar.setText(str(_dolar))
        self.ui.lblDolar.setText("$1 = Bs. %.2f" % (_dolar))
        self.ui.lblPriceReferentialDolarDTH.setText("Precio del dolar del día %s, Bs. %.2f" % (_date, _dolar))

   ##################################
   #                                #
   #    MODULOS PARA TICKETS DTH    #
   #                                #
   ##################################

    def generateTicketsDTH(self):
        self.ui.txtticket_ab_dth.clear()
        self.ui.txtticket_k2b_dth.clear()
        _plan_satelital, _optimo_hd_inter = 12.75, 8
        _optimo_full_hd_inter = 16
        _optimo_hd_movistar = 8
        _optimo_full_hd_movistar = 10
        total_dth = 0
        # Variables paquetes
        _bym_inter,_dsport_inter,_hbo_inter, _venus_inter, _goldem_inter = 5, 5, 7, 7, 7
        _bym_movistar,_dsport_movistar,_hbo_movistar, _venus_movistar, _goldem_movistar = 5, 5, 7, 7, 7
        _deco_dth_inter, _deco_dht_movistar = 15.50, _dolar
        _prefix = "Usted posee "
        _lbl_basico_satelital = ""
        _txt_label_ab_dth = ""
        _txt_label_k2b_dth = ""
        
        if _dolar == 0:
            QMessageBox.about(self, "Dólar requerido", "Por favor configure el valor de la divisa BCV")
            self.clearDHT()
            return False

        if self.ui.basico_satelital_dth.isChecked():
            _txt_label_ab_dth = _prefix + "el plan básico satelital el cual tiene un costo de Bs %.2f" % _plan_satelital
            _txt_label_k2b_dth = "plan básico satelital Bs %.2f" % _plan_satelital
            total_dth = total_dth + _plan_satelital
        else:
            _txt_label_ab_dth = _prefix
            total_dth = 0

        if self.ui.optimo_hd_inter.isChecked():
            optimo_hd_inter = _optimo_hd_inter * _dolar
            _txt_label_ab_dth = _txt_label_ab_dth + " + Plan Óptimo HD el cual tiene un costo de Bs %.2f (sujeto a cambio por tasa BCV)" %  (optimo_hd_inter)
            _txt_label_k2b_dth = _txt_label_k2b_dth + " + plan optimo hd Bs %.2f" %  (optimo_hd_inter)
            total_dth = total_dth + optimo_hd_inter


        if self.ui.optimo_full_hd_inter.isChecked():
            optimo_full_hd_inter = _optimo_full_hd_inter * _dolar
            _txt_label_ab_dth = _txt_label_ab_dth + " + Plan Óptimo Full HD el cual tiene un costo de Bs %.2f (sujeto a cambio por tasa BCV)" %  (optimo_full_hd_inter)
            _txt_label_k2b_dth = _txt_label_k2b_dth + " + plan Óptimo Full HD Bs %.2f" %  (optimo_full_hd_inter)
            total_dth = total_dth + optimo_full_hd_inter


        if self.ui.optimo_hd_movistar.isChecked():
            optimo_hd_movistar = _optimo_hd_movistar * _dolar
            _txt_label_ab_dth = _txt_label_ab_dth + " + Plan Óptimo HD el cual tiene un costo de Bs %.2f (sujeto a cambio por tasa BCV)" %  (optimo_hd_movistar)
            _txt_label_k2b_dth = _txt_label_k2b_dth + " + plan Óptimo HD Bs %.2f" %  (optimo_hd_movistar)
            total_dth = total_dth + optimo_hd_movistar


        if self.ui.optimo_full_hd_movistar.isChecked():
            optimo_full_hd_movistar = _optimo_full_hd_movistar * _dolar
            _txt_label_ab_dth = _txt_label_ab_dth + " + Plan Óptimo Full HD el cual tiene un costo de Bs %.2f (sujeto a cambio por tasa BCV)" %  (optimo_full_hd_movistar)
            _txt_label_k2b_dth = _txt_label_k2b_dth + " + plan Óptimo Full HD Bs %.2f" %  (optimo_full_hd_movistar)
            total_dth = total_dth + optimo_full_hd_movistar

        #PAQUETES PREMIUM INTER

        if self.ui.optimo_hd_inter.isChecked() or self.ui.optimo_full_hd_inter.isChecked():
            if self.ui.bym_dth.isChecked():
                bym_dth_inter = _bym_inter * _dolar
                _txt_label_ab_dth = _txt_label_ab_dth + " + Canal ByM Sports el cual tiene un costo de Bs %.2f (sujeto a cambio por tasa BCV)" %  (bym_dth_inter)
                _txt_label_k2b_dth = _txt_label_k2b_dth + " + ByM Sports Bs %.2f" %  (bym_dth_inter)
                total_dth = total_dth + bym_dth_inter

            if  self.ui.hbo_dth.isChecked():
                hbo_dth_inter = _hbo_inter * _dolar
                _txt_label_ab_dth = _txt_label_ab_dth + " + Paquete HBO el cual tiene un costo de Bs %.2f (sujeto a cambio por tasa BCV)" %  (hbo_dth_inter)
                _txt_label_k2b_dth = _txt_label_k2b_dth + " + HBO Bs %.2f" %  (hbo_dth_inter)
                total_dth = total_dth + hbo_dth_inter

            if  self.ui.dsports_dth.isChecked():
                dsports_dth_inter = _dsport_inter * _dolar
                _txt_label_ab_dth = _txt_label_ab_dth + " + Paquete D Sports el cual tiene un costo de Bs %.2f (sujeto a cambio por tasa BCV)" %  (dsports_dth_inter)
                _txt_label_k2b_dth = _txt_label_k2b_dth + " + DSports Bs %.2f" %  (dsports_dth_inter)
                total_dth = total_dth + dsports_dth_inter

            if  self.ui.venus_dth.isChecked():
                venus_dth_inter = _venus_inter * _dolar
                _txt_label_ab_dth = _txt_label_ab_dth + " + Paquete Adultos el cual tiene un costo de Bs %.2f (sujeto a cambio por tasa BCV)" %  (venus_dth_inter)
                _txt_label_k2b_dth = _txt_label_k2b_dth + " + Venus Bs %.2f" %  (venus_dth_inter)
                total_dth = total_dth + venus_dth_inter

            if  self.ui.goldem_dth.isChecked():
                goldem_dth_inter = _goldem_inter * _dolar
                _txt_label_ab_dth = _txt_label_ab_dth + " + Paquete Goldem Premier el cual tiene un costo de Bs %.2f (sujeto a cambio por tasa BCV)" %  (goldem_dth_inter)
                _txt_label_k2b_dth = _txt_label_k2b_dth + " + Goldem Premier Bs %.2f" %  (goldem_dth_inter)
                total_dth = total_dth + goldem_dth_inter


            if  self.ui.deco_dth.isChecked():
                qty_deco = self.ui.deco_adicional_dth.value()
                deco_dth_inter = _deco_dth_inter * qty_deco
                _txt_label_ab_dth = _txt_label_ab_dth + " + %d toma adicional tiene un costo de Bs %.2f (sujeto a cambio por tasa BCV)" %  (qty_deco, deco_dth_inter)
                _txt_label_k2b_dth = _txt_label_k2b_dth + " + %d deco Bs %.2f" %  (qty_deco, deco_dth_inter)
                total_dth = total_dth + deco_dth_inter

        #PAQUETES PREMIUM MOVISTAR

        if self.ui.optimo_hd_movistar.isChecked() or self.ui.optimo_full_hd_movistar.isChecked():
            if self.ui.bym_dth.isChecked():
                bym_dth_movistar = _bym_movistar * _dolar
                _txt_label_ab_dth = _txt_label_ab_dth + " + Canal ByM Sports el cual tiene un costo de Bs %.2f (sujeto a cambio por tasa BCV)" %  (bym_dth_movistar)
                _txt_label_k2b_dth = _txt_label_k2b_dth + " + ByM Sports Bs %.2f" %  (bym_dth_movistar)
                total_dth = total_dth + bym_dth_movistar

            if  self.ui.hbo_dth.isChecked():
                hbo_dth_movistar = _hbo_movistar * _dolar
                _txt_label_ab_dth = _txt_label_ab_dth + " + Paquete HBO el cual tiene un costo de Bs %.2f (sujeto a cambio por tasa BCV)" %  (hbo_dth_movistar)
                _txt_label_k2b_dth = _txt_label_k2b_dth + " + HBO Bs %.2f" %  (hbo_dth_movistar)
                total_dth = total_dth + hbo_dth_movistar

            if  self.ui.dsports_dth.isChecked():
                dsports_dth_movistar = _dsport_movistar * _dolar
                _txt_label_ab_dth = _txt_label_ab_dth + " + Paquete D Sports el cual tiene un costo de Bs %.2f (sujeto a cambio por tasa BCV)" %  (dsports_dth_movistar)
                _txt_label_k2b_dth = _txt_label_k2b_dth + " + DSports Bs %.2f" %  (dsports_dth_movistar)
                total_dth = total_dth + dsports_dth_movistar

            if  self.ui.venus_dth.isChecked():
                venus_dth_movistar = _venus_movistar * _dolar
                _txt_label_ab_dth = _txt_label_ab_dth + " + Paquete Adultos el cual tiene un costo de Bs %.2f (sujeto a cambio por tasa BCV)" %  (venus_dth_movistar)
                _txt_label_k2b_dth = _txt_label_k2b_dth + " + Venus Bs %.2f" %  (venus_dth_movistar)
                total_dth = total_dth + venus_dth_movistar

            if  self.ui.goldem_dth.isChecked():
                goldem_dth_movistar = _goldem_movistar * _dolar
                _txt_label_ab_dth = _txt_label_ab_dth + " + Paquete Goldem Premier el cual tiene un costo de Bs %.2f (sujeto a cambio por tasa BCV)" %  (goldem_dth_movistar)
                _txt_label_k2b_dth = _txt_label_k2b_dth + " + Goldem Premier Bs %.2f" %  (goldem_dth_movistar)
                total_dth = total_dth + goldem_dth_movistar

            if  self.ui.deco_dth.isChecked():
                qty_deco = self.ui.deco_adicional_dth.value()
                deco_dht_movistar = _deco_dht_movistar * qty_deco
                if qty_deco == 1:
                    adicional = "toma adicional tiene"  
                else:
                    adicional = "tomas adicionales tienen"

                _txt_label_ab_dth = _txt_label_ab_dth + " + %d %s un costo de Bs %.2f (sujeto a cambio por tasa BCV)" %  (qty_deco, adicional, deco_dht_movistar)
                _txt_label_k2b_dth = _txt_label_k2b_dth + " + %d deco Bs %.2f" %  (qty_deco, deco_dht_movistar)
                total_dth = total_dth + deco_dht_movistar

        total_dolar = _dolar if _dolar == 0 else total_dth / _dolar

        self.ui.txtticket_ab_dth.insertPlainText(_txt_label_ab_dth + ", para un total de Bs %.2f " % total_dth )
        self.ui.txtticket_k2b_dth.insertPlainText("// ab solicita información y costos de plan contratado, se indica posee " +_txt_label_k2b_dth+ ", ab conforme, se finaliza.-")
        self.ui.lbl_total_dth.setText("Total Bs %.2f / $ %.2f" % (total_dth, total_dolar))

    def clearDHT(self):
        self.ui.basico_satelital_dth.setChecked(True)
        self.ui.optimo_hd_inter.setChecked(False)
        self.ui.optimo_full_hd_inter.setChecked(False)
        self.ui.optimo_hd_movistar.setChecked(False)
        self.ui.optimo_full_hd_movistar.setChecked(False)
        self.ui.bym_dth.setChecked(False)
        self.ui.hbo_dth.setChecked(False)
        self.ui.dsports_dth.setChecked(False)
        self.ui.venus_dth.setChecked(False)
        self.ui.goldem_dth.setChecked(False)
        self.ui.deco_dth.setChecked(False)
        self.ui.deco_adicional_dth.setValue(1)
        self.ui.txtticket_ab_dth.clear()
        self.ui.txtticket_k2b_dth.clear()
        self.ui.lbl_total_dth.setText("Total Bs %.2f / $ %.2f" % (0, 0))

   ##################################
   #                                #
   #    MODULOS PARA TICKETS HFC    #
   #                                #
   ##################################

    def disableRf(self, state):
        if state == QtCore.Qt.Checked:
            self.ui.widget_2.setStyleSheet("background-color: rgb(125, 206, 160 );")  
            self.ui.rf_dwpw.setEnabled (False)
            self.ui.rf_rxpw.setEnabled (False)
            self.ui.rf_uppw.setEnabled (False)
            self.ui.rf_dwsnr.setEnabled (False)
            self.ui.rf_upsnr.setEnabled (False)
            self.ui.rf_hit_miss.setEnabled (False)
            self.ui.rf_flaps.setEnabled (False)
            self.ui.rf_ajust_pot.setEnabled (False)
            self.ui.rf_dwpw.setChecked(True)
            self.ui.rf_rxpw.setChecked(True)
            self.ui.rf_uppw.setChecked(True)
            self.ui.rf_dwsnr.setChecked(True)
            self.ui.rf_upsnr.setChecked(True)
            self.ui.rf_hit_miss.setChecked(True)
            self.ui.rf_flaps.setChecked(True)
            self.ui.rf_ajust_pot.setChecked(True)
        else:
            self.ui.rf_dwpw.setEnabled (True)
            self.ui.rf_rxpw.setEnabled (True)
            self.ui.rf_uppw.setEnabled (True)
            self.ui.rf_dwsnr.setEnabled (True)
            self.ui.rf_upsnr.setEnabled (True)
            self.ui.rf_hit_miss.setEnabled (True)
            self.ui.rf_flaps.setEnabled (True)
            self.ui.rf_ajust_pot.setEnabled (True)
            self.ui.rf_dwpw.setChecked(False)
            self.ui.rf_rxpw.setChecked(False)
            self.ui.rf_uppw.setChecked(False)
            self.ui.rf_dwsnr.setChecked(False)
            self.ui.rf_upsnr.setChecked(False)
            self.ui.rf_hit_miss.setChecked(False)
            self.ui.rf_flaps.setChecked(False)
            self.ui.rf_ajust_pot.setChecked(False)

    def checkRf(self, state):
        self.ui.service_hfc.setText("")
        self.ui.widget_2.setStyleSheet("background-color: rgb(235, 235, 235);")
        if state == QtCore.Qt.Checked:
            self.rfChange()

    def rfChange(self):
        if self.ui.rf_ok.isChecked():
            self.ui.widget_2.setStyleSheet("background-color: rgb(125, 206, 160);")
        else:
            if self.ui.rf_dwpw.isChecked() or self.ui.rf_uppw.isChecked() or self.ui.rf_rxpw.isChecked() or self.ui.rf_dwsnr.isChecked() or self.ui.rf_upsnr.isChecked():
                self.ui.widget_2.setStyleSheet("background-color: rgb(253, 242, 233);")
                if self.ui.combo_cm_mta.currentIndex() == 0:
                    self.ui.service_hfc.setText("SE SUGIERE BRINDAR SOPORTE")
                else:
                    self.ui.service_hfc.setText("SE SUGIERE INGRESAR ORDEN DE SERVICIO TÉCNICO")

            if self.ui.rf_dwpw.isChecked() and self.ui.rf_uppw.isChecked():
                self.ui.widget_2.setStyleSheet("background-color: rgb(249, 231, 159);")
                self.ui.service_hfc.setText("SE SUGIERE INGRESAR ORDEN DE SERVICIO TÉCNICO")
            if self.ui.rf_uppw.isChecked() and self.ui.rf_dwsnr.isChecked() and self.ui.rf_upsnr.isChecked():
                self.ui.widget_2.setStyleSheet("background-color: rgb(235, 152, 78);")
                self.ui.service_hfc.setText("SE SUGIERE INGRESAR ORDEN DE SERVICIO TÉCNICO")

            if self.ui.rf_hit_miss.isChecked() or self.ui.rf_ajust_pot.isChecked() or self.ui.rf_flaps.isChecked():
                self.ui.widget_2.setStyleSheet("background-color: rgb(231, 76, 60);")
                self.ui.service_hfc.setText("INGRESAR ORDEN DE SERVICIO TÉCNICO")

                pass
            if not self.ui.rf_dwpw.isChecked() and not self.ui.rf_rxpw.isChecked() and not self.ui.rf_uppw.isChecked() and not self.ui.rf_dwsnr.isChecked() and not self.ui.rf_upsnr.isChecked() and not self.ui.rf_hit_miss.isChecked() and not self.ui.rf_flaps.isChecked() and not self.ui.rf_ajust_pot.isChecked():
                self.ui.widget_2.setStyleSheet("background-color: rgb(235, 235, 235);") 

    def changeMtaModen(self, state):
        if state == 0:
            self.rfChange()
            self.ui.service_hfc.setText("")
        else:
            self.ui.service_hfc.setText("SE SUGIERE INGRESAR ORDEN DE SERVICIO TÉCNICO")
            self.ui.widget_2.setStyleSheet("background-color: rgb(249, 231, 159);")
        pass

    def generateTicketInternetHCF(self):
        text_ticket_k2b = ""

      
        pass

    def clearInternetHCF(self):
        self.ui.rf_dwpw.setChecked(False)
        self.ui.rf_rxpw.setChecked(False)
        self.ui.rf_uppw.setChecked(False)
        self.ui.rf_dwsnr.setChecked(False)
        self.ui.rf_upsnr.setChecked(False)
        self.ui.rf_hit_miss.setChecked(False)
        self.ui.rf_flaps.setChecked(False)
        self.ui.rf_ajust_pot.setChecked(False)
        self.ui.rf_ok.setChecked(False)
        self.ui.ping_ok.setChecked(False)
        self.ui.ping_sin_respuesta.setChecked(False)
        self.ui.ping_low.setChecked(False)
        self.ui.spinBox.setValue(200)
        self.ui.ticket_ab_hfc_internet.clear()
        self.ui.ticket_k2b_hfc_internet.clear()
        self.ui.combo_internet.setCurrentIndex(0)
        self.ui.combo_cm_mta.setCurrentIndex(0)
        self.ui.combo_plan_internet.setCurrentIndex(0)
        self.ui.widget_2.setStyleSheet("background-color: rgb(235, 235, 235);")

# main
app = QApplication(sys.argv)
screen_resolution = app.desktop().screenGeometry()
width_screen = screen_resolution.width()
height_screen = screen_resolution.height()
widgetWelcome = QtWidgets.QStackedWidget()
today =  date.today()
_date = today.strftime("%d/%m/%Y")
dolar = Data()
_dolar = dolar.getDolar()