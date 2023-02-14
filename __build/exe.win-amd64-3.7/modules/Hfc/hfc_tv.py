# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 02:42:38 2023

@author: alesp
"""
import sys
import locale
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (
    QDialog,
    QCheckBox,
    QMessageBox,
    QSpinBox
)
from modules.Databases.modeldb import modelDb
from modules.Hfc.hfc_tv_ui import Ui_Dialog
from modules.Data.templates import getTemplate, getLabel
from modules.Data.data import getDolar
from modules.Databases.modeldb import modelDb


class HfcTv(QDialog):
    def __init__(self):
        super(HfcTv, self).__init__()
        self.db = modelDb()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.dolar = getDolar()
        self.ui.is_internet_hfc.stateChanged.connect (self.fillComboInternet)
        self.ui.is_tv_hfc.stateChanged.connect (self.fillComboTv)
        self.ui.btn_ticket_hfc_tv.clicked.connect(self.generateTicketTVHCFSales)
        self.ui.btn_clear_hfc_tv.clicked.connect(self.clearHfc)
        self.generatePremium()
        self.generateAditionales()
        


    def fillComboInternet(self, state):
        combo = self.ui.combo_internet_hfc
        if state == QtCore.Qt.Checked:
            model = self.getPriceProducts(2)
            combo.setEnabled(True)
            combo.setModel(model)
            combo.setModelColumn(1)
        else:
            combo.setEnabled(False)

    def fillComboTv(self, state):
        combo = self.ui.combo_tv_hfc
        if state == QtCore.Qt.Checked:
            model = sql = self.db.getProductsByIdAndTypeProduct(3, 12)
            combo.setEnabled(True)
            combo.setModel(model)
            combo.setModelColumn(1)
        else:
            combo.setEnabled(False)

    def getPriceProducts(self, product):
        sql = "SELECT plans_packages.id, plans_packages.name as name, price_ves, price_usd, alias FROM products \
                INNER JOIN plans_packages on plans_packages.product_id = products.id \
                WHERE products.id = %d" % product
        query = self.db.getData(sql)
        return query 
    
    def getPriceTvPlans(self, product):
        sql = self.db.getProductsByIdAndTypeProduct(3, 9)
        query = self.db.getData(sql)
        return query 

    def generateTicketTVHCFSales(self):
        try:
            text = ""
            labels = getLabel('hfc_tv_sales_ab')
            labels_k2b = getLabel('hfc_tv_sales_kb2')
            prefix = labels["PREFIX"]
            internet=""
            tv=""
            premium = self.db.getProductsByIdAndTypeProduct(3, 9)
            aditionals = self.db.getProductsByIdAndTypeProduct(3, 3)
            list_plans_tv = []
            list_adiotionals = []
            #labes K2B
            
            total = 0
            total_usd = 0
            
            if self.ui.is_tv_hfc.isChecked():
                tv_ = self.ui.combo_tv_hfc.currentText()
                prices = self.db.getPricePlansPackageByName(tv_)
                alias  = self.db.getAliasByName(tv_)
                template = self.db.getTemplateByAlias(alias)
                price_ves = self.db.getPriceVES(prices['price_ves'], prices['price_usd'])
                price_usd = self.db.getPriceUSD(prices['price_ves'], prices['price_usd'])
                if template == None:
                    self.templateUndefined("Plantilla %s no definida, por favor configure la plantilla."  % tv_)
                    self.ui.is_tv_hfc.setChecked(False)
                else:
                    tv = template % (price_ves)
                    total = total + price_ves
                    total_usd = total_usd + price_usd

            if self.ui.is_internet_hfc.isChecked():
                internet_ = self.ui.combo_internet_hfc.currentText()
                prices = self.db.getPricePlansPackageByName(internet_)
                alias  = self.db.getAliasByName(internet_)
                template = self.db.getTemplateByAlias(alias)
                price_ves = self.db.getPriceVES(prices['price_ves'], prices['price_usd'])
                price_usd = self.db.getPriceUSD(prices['price_ves'], prices['price_usd'])
                if template == None:
                    self.templateUndefined("Plantilla %s no definida, por favor configure la plantilla."  % internet_)
                    self.ui.is_internet_hfc.setChecked(False)
                else:
                    internet = template % (price_ves)
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
                total_ves_k2b = labels_k2b["TOTAL"] % float(total)
            else:
                total_ves = ""
                total_ves_k2b = ""

            text =      "%s%s%s%s%s%s" % (prefix, tv, premium_tv, internet, aditional, total_ves)
            temp_ =  "%s%s%s%s%s%s" % (labels_k2b["PREFIX"], tv, premium_tv, internet, aditional, total_ves_k2b)
            temp_ = temp_.replace(" el cual tiene un costo de", "")
            temp_ = temp_.replace(" todos nuestros precios incluyen IVA.", "")
            temp_ = temp_.replace("para un monto total de ", "")
            text_k2b = temp_.replace("(Sujeto a cambio tasa BCV)", "")
            
            self.ui.ticket_ab_hfc_tv.setText(text)
            self.ui.ticket_k2b_hfc_tv.setText(text_k2b)
            self.ui.lbl_total_dth.setText("Total Bs %.2f / Total $ %.2f" % (total, total_usd))
        except Exception as e:
            print(e)


    def generatePremium(self):
        product_id = 3
        type_product = 9
        query = self.db.getProductsByIdAndTypeProduct(product_id, type_product)
        with_box = 280
        heigth_box = 0
        name = ""
        position_x = 20
        position_y = 0
        for i in range(0, query.rowCount()):
            position_y = position_y + 35
            heigth_box = heigth_box + 40
            name = query.record(i).value("name")
            alias = query.record(i).value("alias")
            self.createCheckboxesPremium(name, alias, position_x, position_y, with_box, heigth_box)

    def generateAditionales(self):
        product_id = 3
        type_product = 3
        query = self.db.getProductsByIdAndTypeProduct(product_id, type_product)
        with_box = 280
        heigth_box = 0
        name = ""
        position_x = 20
        position_y = 0
        for i in range(0, query.rowCount()):
            position_y = position_y + 35
            heigth_box = heigth_box + 50
            name = query.record(i).value("name")
            alias = query.record(i).value("alias")
            self.createCheckboxesAditionnal(name, alias, position_x, position_y, with_box, heigth_box)

    def createCheckboxesPremium(self, name, alias, position_x, position_y, with_box, heigth_box):
        self.ui.groupBoxPremiumTVHfc.setGeometry(QtCore.QRect(20, 60, 280, heigth_box))
        self.checkBox = QtWidgets.QCheckBox(self.ui.groupBoxPremiumTVHfc)
        self.checkBox.setGeometry(QtCore.QRect(position_x, position_y, 260, 30))
        self.checkBox.setObjectName(alias)
        self.checkBox.setText(name)
     
    def createCheckboxesAditionnal(self, name, alias, position_x, position_y, with_box, heigth_box):
        self.ui.groupBoxAditionalTVHfc.setGeometry(QtCore.QRect(330, 360, 310, heigth_box))
        self.checkBox = QtWidgets.QCheckBox(self.ui.groupBoxAditionalTVHfc)
        self.checkBox.setGeometry(QtCore.QRect(position_x, position_y, 220, 30))
        self.checkBox.setObjectName(alias)
        self.checkBox.setText(name)

        self.spinBox = QtWidgets.QSpinBox(self.ui.groupBoxAditionalTVHfc)
        self.spinBox.setMinimum(1)
        self.spinBox.setProperty("value", 1)
        self.spinBox.setGeometry(QtCore.QRect(position_x + 200, position_y, 50, 30))
        self.spinBox.setObjectName(alias + "_qty")



    def clearHfc(self):
        query = self.db.getProductsByIdAndTypeProduct(3, 9)
        for i in range(0, query.rowCount()):
            alias = query.record(i).value("alias")
            checkbox = self.findChild(QCheckBox, alias)
            checkbox.setChecked(False)

        aditionals = self.db.getProductsByIdAndTypeProduct(3, 3)
        for i in range(0, aditionals.rowCount()):
            alias = aditionals.record(i).value("alias")
            checkbox = self.findChild(QCheckBox, alias)
            spinBox = self.findChild(QSpinBox, alias+"_qty")
            spinBox.setProperty("value", 1)
            checkbox.setChecked(False)
        self.ui.ticket_ab_hfc_tv.clear()
        self.ui.ticket_k2b_hfc_tv.clear()
        self.ui.is_internet_hfc.setChecked(False)
        self.ui.is_tv_hfc.setChecked(False)

    def templateUndefined(self, message):
        QMessageBox.about(self, "Plantilla no definida", message)
    
