

from datetime import date
from PyQt5.QtWidgets import QDialog, QMessageBox
from dth_ui import Ui_Dialog
from data import getDolar


class Dth(QDialog):
	def __init__(self):
         super(Dth, self).__init__()
         self.ui = Ui_Dialog()
         self.ui.setupUi(self) 
         self.ui.btn_ticket_dth.clicked.connect(self.generateTicketsDTH)
         self.ui.btn_clear_dth.clicked.connect(self.clearDHT)
         self.ui.lblPriceReferentialDolarDTH.setText("Precio del dolar del día %s, Bs. %.2f" % (_date, _dolar))


	def generateTicketsDTH(self):
         self.ui.txtticket_ab_dth.clear()
         self.ui.txtticket_k2b_dth.clear()
         _plan_satelital, _optimo_hd_inter = 12.75, 8
         _optimo_full_hd_inter = 16
         _optimo_hd_movistar = 8
         _optimo_full_hd_movistar = 10
         total_dth = 0
        # Variables paquetes
         _bym_inter,_dsport_inter,_hbo_inter, _venus_inter, _goldem_inter = 85.55, 5, 92.56, 78.32, 56.96
         _bym_movistar,_dsport_movistar,_hbo_movistar, _venus_movistar, _goldem_movistar = 5, 5, 7, 7, 7
         _deco_dth_inter, _deco_dht_movistar = 15.50, _dolar
         _prefix = "Usted posee "
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
                bym_dth_inter = _bym_inter
                _txt_label_ab_dth = _txt_label_ab_dth + " + Canal ByM Sports el cual tiene un costo de Bs %.2f (sujeto a cambio por tasa BCV)" %  (bym_dth_inter)
                _txt_label_k2b_dth = _txt_label_k2b_dth + " + ByM Sports Bs %.2f" %  (bym_dth_inter)
                total_dth = total_dth + bym_dth_inter

            if  self.ui.hbo_dth.isChecked():
                hbo_dth_inter = _hbo_inter 
                _txt_label_ab_dth = _txt_label_ab_dth + " + Paquete HBO el cual tiene un costo de Bs %.2f (sujeto a cambio por tasa BCV)" %  (hbo_dth_inter)
                _txt_label_k2b_dth = _txt_label_k2b_dth + " + HBO Bs %.2f" %  (hbo_dth_inter)
                total_dth = total_dth + hbo_dth_inter

            if  self.ui.dsports_dth.isChecked():
                dsports_dth_inter = _dsport_inter * _dolar
                _txt_label_ab_dth = _txt_label_ab_dth + " + Paquete D Sports el cual tiene un costo de Bs %.2f (sujeto a cambio por tasa BCV)" %  (dsports_dth_inter)
                _txt_label_k2b_dth = _txt_label_k2b_dth + " + DSports Bs %.2f" %  (dsports_dth_inter)
                total_dth = total_dth + dsports_dth_inter

            if  self.ui.venus_dth.isChecked():
                venus_dth_inter = _venus_inter
                _txt_label_ab_dth = _txt_label_ab_dth + " + Paquete Adultos el cual tiene un costo de Bs %.2f (sujeto a cambio por tasa BCV)" %  (venus_dth_inter)
                _txt_label_k2b_dth = _txt_label_k2b_dth + " + Venus Bs %.2f" %  (venus_dth_inter)
                total_dth = total_dth + venus_dth_inter

            if  self.ui.goldem_dth.isChecked():
                goldem_dth_inter = _goldem_inter
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
                _txt_label_k2b_dth = _txt_label_k2b_dth + " + Golden Premier Bs %.2f" %  (goldem_dth_movistar)
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




today =  date.today()
_date = today.strftime("%d/%m/%Y")
_dolar = getDolar()