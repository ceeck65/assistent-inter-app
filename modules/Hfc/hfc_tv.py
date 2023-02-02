# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 02:42:38 2023

@author: alesp
"""
import sys
import locale
from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QDialog,
)
from modules.Databases.modeldb import modelDb
from modules.Hfc.hfc_tv_ui import Ui_Dialog
from modules.Data.templates import getTemplate, getLabel
from modules.Data.data import getDolar


class HfcTv(QDialog):
    def __init__(self):
        super(HfcTv, self).__init__()
        self.db = modelDb()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.dolar = getDolar()
        self.ui.is_internet_hfc.stateChanged.connect (self.fillComboInternet)
        self.ui.btn_ticket_hfc_tv.clicked.connect(self.generateTicketTVHCFSales)
        


    def fillComboInternet(self, state):
        combo = self.ui.combo_internet_hfc
        if state == QtCore.Qt.Checked:
            model = self.getPriceProducts(2)
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


    def generateTicketTVHCFSales(self):
        try:
            text = ""
            labels = getLabel('hfc_tv_sales_ab')
            labels_k2b = getLabel('hfc_tv_sales_kb2')
            prefix = labels["PREFIX"]
            basic = ""
            tv_family = ""
            tv_bym = ""
            tv_dsports = ""
            tv_international = ""
            tv_hot_pack = ""
            tv_fsn = ""
            tv_venus = ""
            tv_playboy = ""
            tv_digital = ""
            tv_hbo = ""
            tv_golden = ""
            tv_gold = ""
            internet=""


            #labes K2B
            basic_k2b =""
            tv_family_k2b =""
            tv_bym_k2b =""
            tv_dsports_k2b =""
            tv_international_k2b=""
            tv_hot_pack_k2b =""
            tv_fsn_k2b =""
            tv_venus_k2b =""
            tv_playboy_k2b=""
            tv_digital_k2b = ""
            tv_hbo_k2b = ""
            tv_golden_k2b = ""
            tv_gold_k2b = ""
            internet_k2b=""
            
            total = 0
            total_usd = 0
            
            if self.ui.hfc_tv_basic.isChecked():
                prices = self.db.getPricePlansPackage("basico_cable")
                basic = labels["BASIC_CABLE"] % prices['price_ves']
                basic_k2b = labels_k2b["BASIC_CABLE"] % prices['price_ves']
                total = total + self.db.getPriceVES(prices['price_ves'], prices['price_usd'])
                total_usd = total_usd + self.db.getPriceUSD(prices['price_ves'], prices['price_usd'])

            if self.ui.hfc_tv_family.isChecked():
                prices = self.db.getPricePlansPackage("cable_familiar")
                tv_family = labels["FAMILY_CABLE"] % prices['price_ves']
                tv_family_k2b = labels_k2b["FAMILY_CABLE"] % prices['price_ves']
                total = total + self.db.getPriceVES(prices['price_ves'], prices['price_usd'])
                total_usd = total_usd + self.db.getPriceUSD(prices['price_ves'], prices['price_usd'])

            if self.ui.hfc_tv_bym.isChecked():
                prices = self.db.getPricePlansPackage("canal_bym_sport")
                tv_bym = labels["BYM"] % prices['price_ves']
                tv_bym_k2b = labels_k2b["BYM"] % prices['price_ves']
                total = total + self.db.getPriceVES(prices['price_ves'], prices['price_usd'])
                total_usd = total_usd + self.db.getPriceUSD(prices['price_ves'], prices['price_usd'])

            if self.ui.hfc_tv_dsports.isChecked():
                prices = self.db.getPricePlansPackage("d_sports")
                tv_dsports = labels["DSPORTS"] % prices['price_ves']
                tv_dsports_k2b = labels_k2b["DSPORTS"] % prices['price_ves']
                total = total + self.db.getPriceVES(prices['price_ves'], prices['price_usd'])
                total_usd = total_usd + self.db.getPriceUSD(prices['price_ves'], prices['price_usd'])

            if self.ui.hfc_tv_international.isChecked():
                prices = self.db.getPricePlansPackage("paquete_internacional")
                tv_international = labels["INTERNATIONAL"] % prices['price_ves']
                tv_international_k2b = labels_k2b["INTERNATIONAL"] % prices['price_ves']
                total = total + self.db.getPriceVES(prices['price_ves'], prices['price_usd'])
                total_usd = total_usd + self.db.getPriceUSD(prices['price_ves'], prices['price_usd'])

            if self.ui.hfc_tv_hot_pack.isChecked():
                prices = self.db.getPricePlansPackage("hot_pack_go")
                tv_hot_pack = labels["HOT_GO"] % prices['price_ves']
                tv_hot_pack_k2b = labels_k2b["HOT_GO"] % prices['price_ves']
                total = total + self.db.getPriceVES(prices['price_ves'], prices['price_usd'])
                total_usd = total_usd + self.db.getPriceUSD(prices['price_ves'], prices['price_usd'])

            if self.ui.hfc_tv_fsn.isChecked():
                prices = self.db.getPricePlansPackage("canal_fsn")
                tv_fsn = labels["FSN"] % prices['price_ves']
                tv_fsn_k2b = labels_k2b["FSN"] % prices['price_ves']
                total = total + self.db.getPriceVES(prices['price_ves'], prices['price_usd'])
                total_usd = total_usd + self.db.getPriceUSD(prices['price_ves'], prices['price_usd'])

            if self.ui.hfc_tv_venus.isChecked():
                prices = self.db.getPricePlansPackage("venus")
                tv_venus = labels["VENUS"] % prices['price_ves']
                tv_venus_k2b = labels_k2b["VENUS"] % prices['price_ves']
                total = total + self.db.getPriceVES(prices['price_ves'], prices['price_usd'])
                total_usd = total_usd + self.db.getPriceUSD(prices['price_ves'], prices['price_usd'])

            if self.ui.hfc_tv_playboy.isChecked():
                prices = self.db.getPricePlansPackage("play_boy")
                tv_playboy = labels["PLAYBOY"] % prices['price_ves']
                tv_playboy_k2b = labels_k2b["PLAYBOY"] % prices['price_ves']
                total = total + self.db.getPriceVES(prices['price_ves'], prices['price_usd'])
                total_usd = total_usd + self.db.getPriceUSD(prices['price_ves'], prices['price_usd'])

            if self.ui.hfc_tv_digital.isChecked():
                prices = self.db.getPricePlansPackage("servicio_digital")
                tv_digital = labels["TV_DIGITAL"] % prices['price_ves']
                tv_digital_k2b = labels_k2b["TV_DIGITAL"] % prices['price_ves']
                total = total + self.db.getPriceVES(prices['price_ves'], prices['price_usd'])
                total_usd = total_usd + self.db.getPriceUSD(prices['price_ves'], prices['price_usd'])

            if self.ui.hfc_tv_hbo.isChecked():
                prices = self.db.getPricePlansPackage("hbo")
                tv_hbo = labels["HBO"] % prices['price_ves']
                tv_hbo_k2b = labels_k2b["HBO"] % prices['price_ves']
                total = total + self.db.getPriceVES(prices['price_ves'], prices['price_usd'])
                total_usd = total_usd + self.db.getPriceUSD(prices['price_ves'], prices['price_usd'])

            if self.ui.hfc_tv_golden.isChecked():
                prices = self.db.getPricePlansPackage("golden")
                tv_golden = labels["GOLDEN"] % prices['price_ves']
                tv_golden_k2b = labels_k2b["GOLDEN"] % prices['price_ves']
                total = total + self.db.getPriceVES(prices['price_ves'], prices['price_usd'])
                total_usd = total_usd + self.db.getPriceUSD(prices['price_ves'], prices['price_usd'])

            if self.ui.hfc_tv_gold.isChecked():
                prices = self.db.getPricePlansPackage("gold")
                tv_gold = labels["GOLD"] % prices['price_ves']
                tv_gold_k2b = labels_k2b["GOLD"] % prices['price_ves']
                total = total + self.db.getPriceVES(prices['price_ves'], prices['price_usd'])
                total_usd = total_usd + self.db.getPriceUSD(prices['price_ves'], prices['price_usd'])

            if self.ui.is_internet_hfc.isChecked():
                internet_ = self.ui.combo_internet_hfc.currentText()
                prices = self.db.getPricePlansPackageByName(internet_)
                internet = labels["PLAN_INTERNET"] % (internet_, prices['price_ves'])
                internet_k2b = labels_k2b["PLAN_INTERNET"] % (internet_, prices['price_ves'])
                total = total + self.db.getPriceVES(prices['price_ves'], prices['price_usd'])
                total_usd = total_usd + self.db.getPriceUSD(prices['price_ves'], prices['price_usd'])

            if self.ui.hfc_tv_aditional_cable.isChecked():
                internet_ = self.ui.combo_internet_hfc.currentText()
                prices = self.db.getPricePlansPackageByName(internet_)
                internet = labels["PLAN_INTERNET"] % (internet_, prices['price_ves'])
                internet_k2b = labels_k2b["PLAN_INTERNET"] % (internet_, prices['price_ves'])
                total = total + self.db.getPriceVES(prices['price_ves'], prices['price_usd'])
                total_usd = total_usd + self.db.getPriceUSD(prices['price_ves'], prices['price_usd'])

            if self.ui.is_internet_hfc.isChecked():
                internet_ = self.ui.combo_internet_hfc.currentText()
                prices = self.db.getPricePlansPackageByName(internet_)
                internet = labels["PLAN_INTERNET"] % (internet_, prices['price_ves'])
                internet_k2b = labels_k2b["PLAN_INTERNET"] % (internet_, prices['price_ves'])
                total = total + self.db.getPriceVES(prices['price_ves'], prices['price_usd'])
                total_usd = total_usd + self.db.getPriceUSD(prices['price_ves'], prices['price_usd'])

            if self.ui.is_internet_hfc.isChecked():
                internet_ = self.ui.combo_internet_hfc.currentText()
                prices = self.db.getPricePlansPackageByName(internet_)
                internet = labels["PLAN_INTERNET"] % (internet_, prices['price_ves'])
                internet_k2b = labels_k2b["PLAN_INTERNET"] % (internet_, prices['price_ves'])
                total = total + self.db.getPriceVES(prices['price_ves'], prices['price_usd'])
                total_usd = total_usd + self.db.getPriceUSD(prices['price_ves'], prices['price_usd'])

            if total > 0:
                total_ves = labels["TOTAL_VES"] % float(total)
                total_ves_k2b = labels_k2b["TOTAL_VES"] % float(total)
            else:
                total_ves = ""
                total_ves_k2b = ""

            text =      "%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s" % (prefix, basic, tv_family, tv_bym, tv_dsports, tv_international, tv_hot_pack, tv_fsn, tv_venus, tv_playboy, tv_digital, tv_hbo, tv_golden, tv_gold, internet, total_ves)
            text_k2b =  "%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s" % (labels_k2b["PREFIX"],
            basic_k2b, tv_family_k2b, tv_bym_k2b, tv_dsports_k2b, tv_international_k2b, tv_hot_pack_k2b, tv_fsn_k2b, tv_venus_k2b, tv_playboy_k2b, tv_digital_k2b, tv_hbo_k2b, tv_golden_k2b, tv_gold_k2b, internet_k2b, total_ves_k2b)
            
            self.ui.ticket_ab_hfc_tv.setText(text)
            self.ui.ticket_k2b_hfc_tv.setText(text_k2b)
            self.ui.lbl_total_dth.setText("Total Bs %.2f / Total $ %.2f" % (total, total_usd))
        except:
            print("An exception occurred")



    
