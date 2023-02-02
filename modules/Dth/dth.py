

from datetime import date
from PyQt5.QtWidgets import QDialog, QMessageBox
from modules.Dth.dth_ui import Ui_Dialog
from modules.Data.data import getDolar
from modules.Data.templates import getTemplate, getLabel
from modules.Databases.modeldb import modelDb


class Dth(QDialog):
	def __init__(self):
		super(Dth, self).__init__()
		self.db = modelDb()
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
		self.fillComboPlans()

	def fillComboPlans(self):
		sql= "SELECT id, name FROM plans_packages WHERE product_id = 1 AND type_product_id = 1;"
		model = self.db.getData(sql)
		combo = self.ui.plans_dth
		combo.setModel(model)
		combo.setModelColumn(1)
		

	def getPlansByName(self, name):
		sql = "SELECT * from plans_packages where name LIKE '%s'" % name
		query = self.db.getSingleData(sql)
		price_ves = query.record(0).value("price_ves")
		price_usd = query.record(0).value("price_usd")
		alias = query.record(0).value("alias")
		id = query.record(0).value("id")
		dict = {"id": id, "price_ves": price_ves, "price_usd": price_usd, "alias": alias}
		return dict

	def getPlansByAlias(self, alias):
		sql = "SELECT * from plans_packages where alias = '%s'" % alias
		query = self.db.getSingleData(sql)
		price_ves = query.record(0).value("price_ves")
		price_usd = query.record(0).value("price_usd")
		alias = query.record(0).value("alias")
		id = query.record(0).value("id")
		dict = {"id": id, "price_ves": price_ves, "price_usd": price_usd, "alias": alias}
		return dict
	
	def getTemplateByAlias(self, alias):
		sql = "SELECT  template, alias FROM templates where alias = '%s';" % alias
		query = self.db.getSingleData(sql)
		template = query.record(0).value("template")
		return template


	def generateTicketsDTH(self):
		try: 
			labels = getLabel('dth_sales_ab')
			labels_k2b = getLabel('dth_sales_kb2')
			self.ui.txtticket_ab_dth.clear()
			self.ui.txtticket_k2b_dth.clear()
			get_dolar = getDolar()
			self.ui.lblPriceReferentialDolarDTH.setText("Precio del dolar del día %s, Bs. %.2f" % (_date, get_dolar))
			combo_plans = self.ui.plans_dth.currentText()
			plans_ = self.getPlansByName(combo_plans)
			total = 0
			total_usd = 0
			satelital_dth = ""

			if self.ui.basico_satelital_dth.isChecked():
				satelital_ = self.getPlansByAlias("dth_basico_satelital")
				plan_label = self.getTemplateByAlias(satelital_["alias"])
				price_ves = self.db.getPriceVES(satelital_['price_ves'], satelital_['price_usd'])
				price_usd  = self.db.getPriceUSD(satelital_['price_ves'], satelital_['price_usd'])
				satelital_dth = plan_label % price_ves
				total = total + price_ves
				total_usd = total_usd + price_usd


			plan_label = self.getTemplateByAlias(plans_["alias"])
			price_ves = self.db.getPriceVES(plans_['price_ves'], plans_['price_usd'])
			price_usd  = self.db.getPriceUSD(plans_['price_ves'], plans_['price_usd'])
			plans_package = plan_label % price_ves
			total = total + price_ves
			total_usd = total_usd + price_usd

			plans_package_k2b = plans_package.replace(" el cual tiene un costo de", "")
			plans_package_k2b = plans_package_k2b.replace(" (Sujeto a cambio tasa BCV)", "")

			text_ab = "%s%s%s" % (labels["PREFIX"], satelital_dth, plans_package)
			text_k2b = "%s%s%s"  % (labels_k2b["PREFIX"], satelital_dth, plans_package_k2b)

			self.ui.txtticket_ab_dth.insertPlainText(text_ab)
			self.ui.txtticket_k2b_dth.insertPlainText(text_k2b)
			self.ui.lbl_total_dth.setText("Total Bs %.2f / $ %.2f" % (total, total_usd))
		except:
			print("An exception occurred")
 

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




today =  date.today()
_date = today.strftime("%d/%m/%Y")
_dolar = getDolar()