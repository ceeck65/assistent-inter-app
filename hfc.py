# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 05:02:29 2023

@author: alesp
"""
# from datetime import date
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from hfc_ui import Ui_Dialog
# from data import getDolar


class Hfc(QDialog):
	def __init__(self):
         super(Hfc, self).__init__()
         self.ui = Ui_Dialog()
         self.ui.setupUi(self) 
         
         
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
             if not self.ui.rf_dwpw.isChecked() and not self.ui.rf_rxpw.isChecked() and not self.ui.rf_uppw.isChecked() and not self.ui.rf_dwsnr.isChecked() and not self.ui.rf_upsnr.isChecked() and not self.ui.rf_hit_miss.isChecked() and not self.ui.rf_flaps.isChecked() and not self.ui.rf_ajust_pot.isChecked():
                 self.ui.widget_2.setStyleSheet("background-color: rgb(235, 235, 235);")    
         
         
	def textVRF(self):
         _textVRF_ = ""
         prefix_textVRF = ""
         if self.ui.rf_ok.isChecked():
            prefix_textVRF = "Valores RF"
            _textVRF_ = "(OK)"
         else:
            if self.ui.rf_dwpw.isChecked() or self.ui.rf_uppw.isChecked() or self.ui.rf_rxpw.isChecked() or self.ui.rf_dwsnr.isChecked() or self.ui.rf_upsnr.isChecked() or self.ui.rf_hit_miss.isChecked() or self.ui.rf_ajust_pot.isChecked() or self.ui.rf_flaps.isChecked():
                prefix_textVRF = "Valores RF"
                _textVRF_ = ""
                if self.ui.rf_dwpw.isChecked():
                    _textVRF_ = _textVRF_ + "DwPw, "
                if self.ui.rf_uppw.isChecked():
                    _textVRF_ = _textVRF_ + "DwPW, "
                if self.ui.rf_rxpw.isChecked():
                    _textVRF_ = _textVRF_ + "RxPw(CMTS), "
                if self.ui.rf_dwsnr.isChecked():
                    _textVRF_ = _textVRF_ + "DwSNR, "
                if self.ui.rf_upsnr.isChecked():
                    _textVRF_ = _textVRF_ + "UpSNR, "
                if self.ui.rf_hit_miss.isChecked():
                    _textVRF_ = _textVRF_ + "Hit/Miss, "
                if self.ui.rf_ajust_pot.isChecked():
                    _textVRF_ = _textVRF_ + "Ajust Pot, "
                if self.ui.rf_flaps.isChecked():
                    _textVRF_ = _textVRF_ + "Flaps, "
                temp = "(%s)" % _textVRF_
                temp = temp.replace(", )", ")")
                _textVRF_ = temp
            else:
                _textVRF_ = ""
                prefix_textVRF = ""
         return "%s %s alterados" %(prefix_textVRF, _textVRF_)

        

	def changeMtaModen(self, state):
         if state == 0:
            self.rfChange()
            self.ui.service_hfc.setText("")
         else:
            self.ui.service_hfc.setText("SE SUGIERE INGRESAR ORDEN DE SERVICIO TÉCNICO")
            self.ui.widget_2.setStyleSheet("background-color: rgb(249, 231, 159);")
         pass
         
     
        
	def generateTicketInternetHCF(self):
         self.ui.ticket_k2b_hfc_internet.clear()
         vrf = self.textVRF()
         cm_mta = self.ui.combo_cm_mta.currentText()
         hfc_tv = ""
         hfc_reset = ", Conect/Desc," if self.ui.hfc_reset.isChecked() else ""
         plan_internet = self.ui.combo_plan_internet.currentText()
         ping = ""
         soporte = ""
         descarga = "" 
         if self.ui.hfc_descarga.text() == "":
            pass
         else:
            dd = self.ui.hfc_descarga.text()
            vd = self.ui.hfc_velocidad_descarga.currentText()
            descarga = "Dw: %s%s," % (dd, vd)
    
         subida = "" 
         if self.ui.hcf_subida.text() == "":
            pass
         else:
            sd = self.ui.hcf_subida.text()
            sv = self.ui.hfc_velocidad_subida.currentText()
            subida = "Up: %s%s," % (sd, sv)

         if self.ui.ping_ok.isChecked():
            ping = "ping 200 ok"
         if self.ui.ping_sin_respuesta.isChecked():
            ping = "ping sin respuesta"
         if self.ui.ping_low.isChecked():
            ping = "ping %s/200" % self.ui.ping_txt.value()

         if self.ui.hfc_tv_ok.isChecked():
            hfc_tv = ", TV OK,"
         if self.ui.hfc_tv_fail.isChecked():
            hfc_tv = ", TV FALLA,"

         if self.ui.hfc_soporte_xon_exitos.isChecked():
            soporte = ", soporte c/e"
         if self.ui.hfc_soporte_sin_exitos.isChecked():
            soporte = ", soporte s/e"

         txtTicketK2B = "// Ab alega fallas en servicio de internet, CM: %s %s %s %s %s, %s  %s  %s %s, favor agilizar, llamar antes.-" % (cm_mta, vrf, hfc_tv, hfc_reset, plan_internet, ping, descarga, subida, soporte)
      
         self.ui.ticket_k2b_hfc_internet.insertPlainText(txtTicketK2B)
         
         
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
         self.ui.ping_txt.setValue(200)
         self.ui.ticket_ab_hfc_internet.clear()
         self.ui.ticket_k2b_hfc_internet.clear()
         self.ui.combo_internet.setCurrentIndex(0)
         self.ui.combo_cm_mta.setCurrentIndex(0)
         self.ui.combo_plan_internet.setCurrentIndex(0)
         self.ui.widget_2.setStyleSheet("background-color: rgb(235, 235, 235);")
