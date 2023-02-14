

from datetime import date
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (
    QDialog,
    QCheckBox,
    QMessageBox,
    QSpinBox
)
from modules.Dth.dth_ui import Ui_Dialog
from modules.Data.data import getDolar
from modules.Data.templates import getTemplate, getLabel
from modules.Databases.modeldb import modelDb


class Dth(QDialog):
	global current_product_id
	global current_premium
	global current_aditionals

	current_product_id = 1
	current_premium = 11
	current_aditionals = 3
	def __init__(self):
		super(Dth, self).__init__()
		self.db = modelDb()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.btn_ticket_dth.clicked.connect(self.generateTicketsDTH)
		self.ui.btn_ticket_dth_support.clicked.connect(self.generateTicketSupport)
		self.ui.btn_clear_dth__support.clicked.connect(self.clearDTHSupport)
		self.ui.btn_clear_dth.clicked.connect(self.clearDHT)
		
		get_dolar = getDolar()
		self.ui.lblPriceReferentialDolarDTH.setText("Precio del dolar del día %s, Bs. %.2f" % (_date, get_dolar))
		self.ui.combo_dth_failure.activated.connect(self.changeFailure)
		self.decoders = []
		self.ui.btn_add_decoder_dth.clicked.connect(self.listDecoders)
		self.ui.btn_remove_decoder_dth.clicked.connect(self.removeDecoder)
		self.ui.txt_dth_decoder.returnPressed.connect(self.ui.btn_add_decoder_dth.click)
		self.current_product_id = current_product_id
		self.current_premium = current_premium
		self.current_aditionals = current_aditionals
		self.fillComboPlans()
		self.generatePremiumInter(self.current_product_id, self.current_premium)
		self.generatePremiumMovistar(self.current_product_id, 10)
		self.generateAditionales(self.current_product_id, self.current_aditionals)
		self.ui.plans_dth.currentTextChanged.connect(self.changedPlans)
		self.ui.groupBoxPremiumDTHMovistar.setVisible(False)

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
		# try: 
		print(self.current_product_id, self.current_premium)
		labels = getLabel('dth_sales_ab')
		labels_k2b = getLabel('dth_sales_kb2')
		self.ui.txtticket_ab_dth.clear()
		self.ui.txtticket_k2b_dth.clear()
		get_dolar = getDolar()
		self.ui.lblPriceReferentialDolarDTH.setText("Precio del dolar del día %s, Bs. %.2f" % (_date, get_dolar))
		combo_plans = self.ui.plans_dth.currentText()
		plans_ = self.getPlansByName(combo_plans)
		premium = self.db.getProductsByIdAndTypeProduct(self.current_product_id, self.current_premium)
		aditionals = self.db.getProductsByIdAndTypeProduct(self.current_product_id, self.current_aditionals)
		total = 0
		total_usd = 0
		list_plans_tv = []
		list_adiotionals = []

		plan_label = self.getTemplateByAlias(plans_["alias"])
		price_ves = self.db.getPriceVES(plans_['price_ves'], plans_['price_usd'])
		price_usd  = self.db.getPriceUSD(plans_['price_ves'], plans_['price_usd'])
		plans_package = plan_label % price_ves
		total = total + price_ves
		total_usd = total_usd + price_usd


		for i in range(0, premium.rowCount()):
			alias = premium.record(i).value("alias")
			checkbox = self.findChild(QCheckBox, alias)
			if checkbox.isChecked():
				prices = self.db.getPricePlansPackageByAlias(alias)
				template = self.db.getTemplateByAlias(alias)
				name_package = self.db.findPackageNameByAlias(alias)
				price_ves = self.db.getPriceVES(prices['price_ves'], prices['price_usd'])
				price_usd = self.db.getPriceUSD(prices['price_ves'], prices['price_usd'])
				if template == None:
					self.templateUndefined("Plantilla %s no definida, por favor configure la plantilla." % name_package)
					checkbox.setChecked(False)
				else:
					premium_tv_ = template % (price_ves)
					total = total + price_ves
					total_usd = total_usd + price_usd
					list_plans_tv.append(premium_tv_)

		premium_tv =""
		for item in list_plans_tv:
			premium_tv += item
	

		for i in range(0, aditionals.rowCount()):
			alias = aditionals.record(i).value("alias")
			checkbox = self.findChild(QCheckBox, alias)
			qty = self.findChild(QSpinBox, alias+"_qty")
			if checkbox.isChecked():
				prices = self.db.getPricePlansPackageByAlias(alias)
				template = self.db.getTemplateByAlias(alias)
				name_package = self.db.findPackageNameByAlias(alias)
				price_ves = self.db.getPriceVES(prices['price_ves'], prices['price_usd'])
				price_usd = self.db.getPriceUSD(prices['price_ves'], prices['price_usd'])
				if template == None:
					self.templateUndefined("Plantilla %s no definida, por favor configure la plantilla." %  name_package)
					checkbox.setChecked(False)
				else:
					qty_ = qty.value()
					aditional_ = template % (qty_, price_ves)
					total = total + (price_ves * qty_)
					total_usd = total_usd + (price_usd * qty_)
					list_adiotionals.append(aditional_)

		aditional=""
		for item in list_adiotionals:
			aditional+= item

		if total > 0:
			total_ves = labels["TOTAL"] % float(total)
			total_ves_k2b = labels_k2b["TOTAL_VES"] % float(total)
		else:
			total_ves = ""
			total_ves_k2b = ""


		text_ab = "%s%s%s%s%s" % (labels["PREFIX"], plans_package, premium_tv,aditional, total_ves)
		temp_ = "%s%s%s%s%s%s"  % (labels_k2b["PREFIX"], plans_package, premium_tv, aditional, total_ves_k2b, labels_k2b["END"])
		temp_ = temp_.replace(" el cual tiene un costo de", "")
		temp_ = temp_.replace(" todos nuestros precios incluyen IVA", "")
		temp_ = temp_.replace("para un monto total de ", "")
		text_k2b = temp_.replace("(Sujeto a cambio tasa BCV)", "")


		self.ui.txtticket_ab_dth.insertPlainText(text_ab)
		self.ui.txtticket_k2b_dth.insertPlainText(text_k2b)
		self.ui.lbl_total_dth.setText("Total Bs %.2f / $ %.2f" % (total, total_usd))
		# except Exception as e:
		# 	print(e)
 
	def generatePremiumInter(self, product_id, type_product):
		query = self.db.getProductsByIdAndTypeProduct(product_id, type_product)
		with_box = 280
		heigth_box = 0
		name = ""
		position_x = 20
		position_y = 0
		for i in range(0, query.rowCount()):
			position_y = position_y + 35
			heigth_box = heigth_box + 55
			name = query.record(i).value("name")
			alias = query.record(i).value("alias")
			self.createCheckboxesPremiumInter(name, alias, position_x, position_y, with_box, heigth_box)
			
	def generatePremiumMovistar(self, product_id, type_product):
		query = self.db.getProductsByIdAndTypeProduct(product_id, type_product)
		with_box = 280
		heigth_box = 0
		name = ""
		position_x = 20
		position_y = 0
		for i in range(0, query.rowCount()):
			position_y = position_y + 35
			heigth_box = heigth_box + 55
			name = query.record(i).value("name")
			alias = query.record(i).value("alias")
			self.createCheckboxesPremiumMovistar(name, alias, position_x, position_y, with_box, heigth_box)

	def generateAditionales(self, product_id, type_product):
		query = self.db.getProductsByIdAndTypeProduct(product_id, type_product)
		with_box = 280
		heigth_box = 0
		name = ""
		position_x = 20
		position_y = 0
		for i in range(0, query.rowCount()):
			position_y = position_y + 35
			heigth_box = heigth_box + 60
			name = query.record(i).value("name")
			alias = query.record(i).value("alias")
			self.createCheckboxesAditionnal(name, alias, position_x, position_y, with_box, heigth_box)

	def createCheckboxesPremiumInter(self, name, alias, position_x, position_y, with_box, heigth_box):
		self.ui.groupBoxPremiumDTHInter.setGeometry(QtCore.QRect(420, 60, 280, heigth_box))
		self.checkBox = QtWidgets.QCheckBox(self.ui.groupBoxPremiumDTHInter)
		self.checkBox.setGeometry(QtCore.QRect(position_x, position_y, 260, 30))
		self.checkBox.setObjectName(alias)
		self.checkBox.setText(name)

	def createCheckboxesPremiumMovistar(self, name, alias, position_x, position_y, with_box, heigth_box):
		self.ui.groupBoxPremiumDTHMovistar.setGeometry(QtCore.QRect(420, 60, 280, heigth_box))
		self.checkBox = QtWidgets.QCheckBox(self.ui.groupBoxPremiumDTHMovistar)
		self.checkBox.setGeometry(QtCore.QRect(position_x, position_y, 260, 30))
		self.checkBox.setObjectName(alias)
		self.checkBox.setText(name)
     
	def createCheckboxesAditionnal(self, name, alias, position_x, position_y, with_box, heigth_box):
		self.ui.groupBoxAditionalsDTH.setGeometry(QtCore.QRect(20, 190, 360, heigth_box))
		self.checkBox = QtWidgets.QCheckBox(self.ui.groupBoxAditionalsDTH)
		self.checkBox.setGeometry(QtCore.QRect(position_x, position_y, 220, 30))
		self.checkBox.setObjectName(alias)
		self.checkBox.setText(name)

		self.spinBox = QtWidgets.QSpinBox(self.ui.groupBoxAditionalsDTH)
		self.spinBox.setMinimum(1)
		self.spinBox.setProperty("value", 1)
		self.spinBox.setGeometry(QtCore.QRect(position_x + 200, position_y, 50, 30))
		self.spinBox.setObjectName(alias + "_qty")

	def clearDHT(self):
		query = self.db.getProductsByIdAndTypeProduct(self.current_product_id, self.current_premium)
		for i in range(0, query.rowCount()):
			alias = query.record(i).value("alias")
			checkbox = self.findChild(QCheckBox, alias)
			checkbox.setChecked(False)

		aditionals = self.db.getProductsByIdAndTypeProduct(self.current_product_id, self.current_aditionals)
		for i in range(0, aditionals.rowCount()):
			alias = aditionals.record(i).value("alias")
			checkbox = self.findChild(QCheckBox, alias)
			checkbox.setChecked(False)

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

		dth_potency = "" if self.ui.dth_potency.text() == "" else "P:%sdB/ " % self.ui.dth_potency.text() 
		dth_quality="" if self.ui.dth_quality.text() == "" else "C%s/ " % self.ui.dth_quality.text() 
		dth_intensity= "" if self.ui.dth_intensity.text() == "" else "I:%s/" % self.ui.dth_intensity.text() 
		dth_cnr= "" if self.ui.dth_cnr.text() == "" else "CNR:%s/ " % self.ui.dth_cnr.text() 
		dth_vber= "" if self.ui.dth_vber.text() == "" else "VBER:%s/ " % self.ui.dth_vber.text() 

		values = "%s%s%s%s%s%s," % (dth_potency, dth_quality, dth_intensity, dth_intensity, dth_cnr, dth_vber)

		txt_k2b = "%s%s%s%s%s%s%s" % (stb, failure, command, values, clear_weather, connections_ok, support)
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

	def templateUndefined(self, message):
		QMessageBox.about(self, "Plantilla no definida", message)

	def changedPlans(self, value):
		value = value.lower()
		if value.find('inter') != -1:
			self.ui.groupBoxPremiumDTHMovistar.setVisible(False)
			self.ui.groupBoxPremiumDTHInter.setVisible(True)
			self.current_premium = 11
			self.generatePremiumInter(self.current_product_id, self.current_premium)
		else:
			self.ui.groupBoxPremiumDTHMovistar.setVisible(True)
			self.ui.groupBoxPremiumDTHInter.setVisible(False)
			self.current_premium = 10
			self.generatePremiumMovistar(self.current_product_id, self.current_premium)



	def clearDTHSupport(self):
		self.ui.txt_ticket_k2b_dth_support.clear()
		self.ui.dth_potency.clear()
		self.ui.dth_quality.clear()
		self.ui.dth_intensity.clear()
		self.ui.dth_cnr.clear()
		self.ui.dth_vber.clear()
		self.ui.dth_list_decoder.clear()
		self.ui.text_motive_dth.clear()
		self.ui.text_commands_dth.clear()
		self.ui.txt_ticket_ab_dth_support.clear()
		self.ui.dth_clear_weather.setChecked(False)
		self.ui.dth_connections_ok.setChecked(False)
		self.ui.dth_clear_weather.setChecked(False)
		self.ui.dth_not_manupulate_ant.setChecked(False)



today =  date.today()
_date = today.strftime("%d/%m/%Y")
_dolar = getDolar()