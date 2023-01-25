

from datetime import date
from PyQt5.QtWidgets import QDialog, QMessageBox
from modules.Dth.dth_ui import Ui_Dialog
from modules.Data.data import getDolar
from modules.Data.templates import getTemplate, getLabel



class Dth(QDialog):
	def __init__(self):
         super(Dth, self).__init__()
         self.ui = Ui_Dialog()
         self.ui.setupUi(self)
         self.ui.btn_ticket_dth.clicked.connect(self.generateTicketsDTH)
         self.ui.btn_ticket_dth_support.clicked.connect(self.generateTicketSupport)
         self.ui.btn_clear_dth.clicked.connect(self.clearDHT)
         get_dolar = getDolar()
         self.ui.lblPriceReferentialDolarDTH.setText("Precio del dolar del día %s, Bs. %.2f" % (_date, get_dolar))

         self.ui.combo_dth_failure.activated.connect(self.changeFailure)
         self.decoders = []
         self.ui.btn_add_decoder_dth.clicked.connect(self.listDecoders)
         self.ui.btn_remove_decoder_dth.clicked.connect(self.removeDecoder)
         self.ui.txt_dth_decoder.returnPressed.connect(self.ui.btn_add_decoder_dth.click)
         

	def generateTicketsDTH(self):
         get_dolar = getDolar()
         self.ui.lblPriceReferentialDolarDTH.setText("Precio del dolar del día %s, Bs. %.2f" % (_date, get_dolar))
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
         _deco_dth_inter, _deco_dht_movistar = 34.22, _dolar
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

         self.ui.txtticket_ab_dth.insertPlainText(_txt_label_ab_dth + ", para un total de Bs %.2f.Todos nuestros precios incluyen IVA." % total_dth )
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

	def generateTicketSupport(self):
         self.ui.txt_ticket_k2b_dth_support.clear()
         labels = getLabel('dth')
         txt_k2b = ""
         stb = self.ui.txt_dth_decoder.text()
         failure = self.ui.combo_dth_failure.currentText()
         comand_action = self.ui.combo_dth_command.currentText()
         support = ""
         connections_ok = ""
         # manupulate_ant = ""
         # refresh = ""
         # coomand_not_send = ""
         command = ""
         clear_weather = ""
         
         if self.ui.dth_list_decoder.count() > 0:
             decoders = ""
             for index in range(self.ui.dth_list_decoder.count()):
                 deco = self.ui.dth_list_decoder.item(index)
                 decoders = decoders + deco.text() + "/"    
             stb_ = labels["STB"] + decoders
             stb = stb_.replace("/,", ",")
                     
         if not self.ui.dth_coomand_not_send.isChecked():
            if self.ui.dth_refresh.isChecked():
                command = "%s %s %s + %s"  % (txt_k2b, labels["SEND_COMAND"], comand_action.upper(), labels["REFRESH"])
            else:
                if self.ui.combo_dth_failure.currentIndex() != 0:
                    command = txt_k2b + labels["SEND_COMAND"] + comand_action.upper() + ", "
         else:
            command = txt_k2b + labels["NOT_SEND_COMAND"]

         if self.ui.dth_successful_support.isChecked():
            support = txt_k2b + labels["SUPPORT_SUCESSFUL"]

         if self.ui.dth_unsuccessful_support.isChecked():
            support = txt_k2b + labels["CONTACT_SERVICE"]

         if self.ui.dth_waiting_period.isChecked():
            support = txt_k2b + labels["WAITING"]

         if self.ui.dth_clear_weather.isChecked():
            clear_weather = txt_k2b + labels["CLEAR_WEATHER"]

         if self.ui.dth_connections_ok.isChecked():
            connections_ok = txt_k2b + labels["CONNECTION_OK"] 
         failure = ", " + failure.upper() 

         txt_k2b = "%s%s%s%s%s%s" % (stb, failure, command, clear_weather, connections_ok, support)
         self.ui.txt_ticket_k2b_dth_support.insertHtml(txt_k2b)
    
	def changeFailure(self, state):
         template = getTemplate("dth_support")
         self.ui.text_motive_dth.clear()
         self.ui.text_commands_dth.clear()
         self.ui.txt_ticket_ab_dth_support.clear()
         if state == 0:
             self.ui.text_motive_dth.clear()
         if state == 1:
             self.ui.text_motive_dth.insertHtml(template['motives'][0]["364_373"])
             self.ui.text_commands_dth.insertHtml(template['comands'][0]["no"])
             self.ui.txt_ticket_ab_dth_support.insertHtml(template['subscriber'][1]["service"])
         if state == 2:
             self.ui.text_motive_dth.insertHtml(template['motives'][1]["364_1127"])
             self.ui.text_commands_dth.insertHtml(template['comands'][1]["rescan_channels"])
             self.ui.txt_ticket_ab_dth_support.insertHtml(template['subscriber'][0]["send_comand"])
         if state == 3:
             self.ui.text_motive_dth.insertHtml(template['motives'][2]["364_250"])
             self.ui.text_commands_dth.insertHtml(template['comands'][2]["resend_key"])
             self.ui.txt_ticket_ab_dth_support.insertHtml(template['subscriber'][0]["send_comand"])
         if state == 4 or state == 5 or state == 6 or state == 7  or state == 8 :
             self.ui.text_motive_dth.insertHtml(template['motives'][0]["364_373"])
             self.ui.text_commands_dth.insertHtml(template['comands'][0]["no"])
             self.ui.txt_ticket_ab_dth_support.insertHtml(template['subscriber'][1]["service"])
         if state == 9:
             self.ui.text_motive_dth.insertHtml(template['motives'][3]["364_1744"])
             self.ui.text_commands_dth.insertHtml(template['comands'][3]["update_pin"])
             self.ui.txt_ticket_ab_dth_support.insertHtml(template['subscriber'][0]["send_comand"])
         if state == 10:
             self.ui.text_motive_dth.insertHtml(template['motives'][2]["364_250"])
             self.ui.text_commands_dth.insertHtml(template['comands'][4]["refresh_recharge_inactive"])
             self.ui.txt_ticket_ab_dth_support.insertHtml(template['subscriber'][0]["send_comand"])
         if state == 11:
             self.ui.text_motive_dth.insertHtml(template['motives'][2]["364_250"])
             self.ui.text_commands_dth.insertHtml(template['comands'][5]["refresh_recharge_active"])
             self.ui.txt_ticket_ab_dth_support.insertHtml(template['subscriber'][0]["send_comand"])
         if state == 12:
             self.ui.text_motive_dth.insertHtml(template['motives'][2]["364_250"])
             self.ui.text_commands_dth.insertHtml(template['comands'][2]["resend_key"])
             self.ui.txt_ticket_ab_dth_support.insertHtml(template['subscriber'][0]["send_comand"])
         if state == 13:
             self.ui.text_motive_dth.insertHtml(template['motives'][2]["364_250"])
             self.ui.text_commands_dth.insertHtml(template['comands'][6]["refresh"])
             self.ui.txt_ticket_ab_dth_support.insertHtml(template['subscriber'][0]["send_comand"])

	def listDecoders(self):
         decoder = self.ui.txt_dth_decoder.text()
         if decoder != "":
             self.ui.dth_list_decoder.addItem(decoder)
         self.ui.txt_dth_decoder.clear()
    
            
	def removeDecoder(self):
         self.ui.dth_list_decoder.takeItem(self.ui.dth_list_decoder.currentRow())

	def selectTemplate(self):
         pass

	def mi():
         pass




today =  date.today()
_date = today.strftime("%d/%m/%Y")
_dolar = getDolar()