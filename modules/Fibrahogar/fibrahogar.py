# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 02:42:38 2023

@author: alesp
"""
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (
    QDialog,
    QCheckBox,
    QMessageBox,
    QSpinBox
)
import string
from modules.Fibrahogar.fibrahogar_ui import Ui_Dialog
from modules.Databases.modeldb import modelDb
from modules.Data.templates import getTemplate, getLabel, getMessages
from modules.Data.data import getDolar


class FibraHogar(QDialog):
    def __init__(self):
        super(FibraHogar, self).__init__()
        self.db = modelDb()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.generatePremium()
        self.generateAditionales()
        self.ui.is_internet_fibrahogar.stateChanged.connect (self.fillComboInternet)
        self.ui.btn_clear_fibrahogar.clicked.connect(self.clearFibra)
        self.ui.btn_ticket_fibrahogar.clicked.connect(self.generateTicketFibrahogarSales)
        self.ui.is_tv_fibrahogar.stateChanged.connect (self.fillComboTv)
        

    def generateTicketFibrahogarSales(self):
        premium = self.db.getProductsByIdAndTypeProduct(5, 7)
        aditionals = self.db.getProductsByIdAndTypeProduct(5, 3)
        text = ""
        labels = getLabel('fibrahogar_sales_ab')
        labels_k2b = getLabel('fibrahogar_kb2')
        prefix = labels["PREFIX"]
        prefix_k2b = labels_k2b["PREFIX"]
        internet=""
        total = 0
        total_usd = 0
        plans_tv = ""
        premium_tv = ""
        premium_tv_ = ""
        list_plans_tv = []
        list_adiotionals = []

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
                    self.templateUndefined(getMessages("TEMPLATE_UNDEFINED") % name_package)
                    checkbox.setChecked(False)
                else:
                    premium_tv_ = template % (price_ves)
                    total = total + price_ves
                    total_usd = total_usd + price_usd
                    list_plans_tv.append(premium_tv_)

        
        premium_tv_fibra =""
        for item in list_plans_tv:
            premium_tv_fibra+= item
        premium_tv = premium_tv_fibra


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
                    self.templateUndefined(getMessages("TEMPLATE_UNDEFINED") %  name_package)
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


        if self.ui.is_internet_fibrahogar.isChecked():
                internet_ = self.ui.combo_internet_fibrahogar.currentText()
                prices = self.db.getPricePlansPackageByName(internet_)
                alias  = self.db.getAliasByName(internet_)
                template = self.db.getTemplateByAlias(alias)
                price_ves = self.db.getPriceVES(prices['price_ves'], prices['price_usd'])
                price_usd = self.db.getPriceUSD(prices['price_ves'], prices['price_usd'])
                if template == None:
                    self.templateUndefined(getMessages("TEMPLATE_UNDEFINED") % internet)
                    self.ui.is_internet_fibrahogar.setChecked(False)
                else:
                    internet = template % (price_ves)
                    total = total + price_ves
                    total_usd = total_usd + price_usd


        if self.ui.is_tv_fibrahogar.isChecked():
                tv = self.ui.plans_tv_fibrahogar.currentText()
                prices = self.db.getPricePlansPackageByName(tv)
                alias  = self.db.getAliasByName(tv)
                template = self.db.getTemplateByAlias(alias)
                price_ves = self.db.getPriceVES(prices['price_ves'], prices['price_usd'])
                price_usd = self.db.getPriceUSD(prices['price_ves'], prices['price_usd'])
                if template == None:
                    self.templateUndefined(getMessages("TEMPLATE_UNDEFINED") % tv)
                    self.ui.is_tv_fibrahogar.setChecked(False)
                else:
                    plans_tv = template % (price_ves)
                    total = total + price_ves
                    total_usd = total_usd + price_usd


        if total > 0:
            total_ves = labels["TOTAL"] % float(total)
        else:
            total_ves = ""

        text = "%s%s%s%s%s%s" % (prefix, plans_tv, premium_tv, internet, aditional, total_ves)
        temp_ = "%s%s%s%s%s%s" % (prefix_k2b, premium_tv, internet, aditional, total_ves, labels_k2b["END"])
        temp_ = temp_.replace(" el cual tiene un costo de", "")
        temp_ = temp_.replace(" todos nuestros precios incluyen IVA", "")
        temp_ = temp_.replace("para un monto total de ", "")
        text_k2b = temp_.replace("(Sujeto a cambio tasa BCV)", "")

        self.ui.ticket_ab_fibrahogar.setText(text)
        self.ui.ticket_k2b_fibrahogar.setText(text_k2b)
        self.ui.lbl_total_fibrahogar.setText("Total Bs %.2f / $ %.2f" % (total, total_usd))

    def generatePremium(self):
        product_id = 5
        type_product = 7
        query = self.db.getProductsByIdAndTypeProduct(product_id, type_product)
        with_box = 280
        heigth_box = 0
        name = ""
        position_x = 20
        position_y = 0
        for i in range(0, query.rowCount()):
            position_y = position_y + 35
            heigth_box = heigth_box + 45
            name = query.record(i).value("name")
            alias = query.record(i).value("alias")
            self.createCheckboxesPremium(name, alias, position_x, position_y, with_box, heigth_box)

    def fillComboTv(self, state):
        combo = self.ui.plans_tv_fibrahogar
        if state == QtCore.Qt.Checked:
            model = self.db.getProductsByIdAndTypeProduct(5, 6)
            combo.setEnabled(True)
            combo.setModel(model)
            combo.setModelColumn(1)
        else:
            combo.setEnabled(False)
        
    def generateAditionales(self):
        product_id = 5
        type_product = 3
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
            self.createCheckboxesAditionnal(name, alias, position_x, position_y, with_box, heigth_box)

    def fillComboInternet(self, state):
        combo = self.ui.combo_internet_fibrahogar
        if state == QtCore.Qt.Checked:
            model = self.getPriceProducts(5)
            combo.setEnabled(True)
            combo.setModel(model)
            combo.setModelColumn(1)
        else:
            combo.setEnabled(False)
    
    def getPriceProducts(self, product):
        sql = "SELECT plans_packages.id, plans_packages.name as name, price_ves, price_usd, alias FROM products \
                INNER JOIN plans_packages on plans_packages.product_id = products.id \
                WHERE products.id = %d and type_product_id = 5 or type_product_id = 8" % (product)
        query = self.db.getData(sql)
        return query

    def createCheckboxesPremium(self, name, alias, position_x, position_y, with_box, heigth_box):
        self.ui.groupBoxPremiumFibrahogar.setGeometry(QtCore.QRect(20, 200, 280, heigth_box))
        self.checkBox = QtWidgets.QCheckBox(self.ui.groupBoxPremiumFibrahogar)
        self.checkBox.setGeometry(QtCore.QRect(position_x, position_y, 260, 30))
        self.checkBox.setObjectName(alias)
        self.checkBox.setText(name)
     
    def createCheckboxesAditionnal(self, name, alias, position_x, position_y, with_box, heigth_box):
        self.ui.groupBoxAditionalFribrahogar.setGeometry(QtCore.QRect(330, 340, 280, heigth_box))
        self.checkBox = QtWidgets.QCheckBox(self.ui.groupBoxAditionalFribrahogar)
        self.checkBox.setGeometry(QtCore.QRect(position_x, position_y, 200, 30))
        self.checkBox.setObjectName(alias)
        self.checkBox.setText(name)

        self.spinBox = QtWidgets.QSpinBox(self.ui.groupBoxAditionalFribrahogar)
        self.spinBox.setMinimum(1)
        self.spinBox.setProperty("value", 1)
        self.spinBox.setGeometry(QtCore.QRect(position_x + 200, position_y, 50, 30))
        self.spinBox.setObjectName(alias + "_qty")

    def clearFibra(self):
        product_id = 5
        type_product = 7
        query = self.db.getProductsByIdAndTypeProduct(product_id, type_product)
        for i in range(0, query.rowCount()):
            alias = query.record(i).value("alias")
            checkbox = self.findChild(QCheckBox, alias)
            checkbox.setChecked(False)

        aditionals = self.db.getProductsByIdAndTypeProduct(5, 3)
        for i in range(0, aditionals.rowCount()):
            alias = aditionals.record(i).value("alias")
            checkbox = self.findChild(QCheckBox, alias)
            checkbox.setChecked(False)
        self.ui.ticket_ab_fibrahogar.clear()
        self.ui.ticket_k2b_fibrahogar.clear()

    def templateUndefined(self, message):
        QMessageBox.about(self, "Plantilla no definida", message)