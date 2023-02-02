# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 02:42:38 2023

@author: alesp
"""
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (
    QDialog,
    QCheckBox
)
import string
from modules.Fibrahogar.fibrahogar_ui import Ui_Dialog
from modules.Databases.modeldb import modelDb



class FibraHogar(QDialog):
    def __init__(self):
        super(FibraHogar, self).__init__()
        self.db = modelDb()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.generatePremium()
        self.ui.is_internet_fibrahogar.stateChanged.connect (self.fillComboInternet)
        self.ui.btn_clear_fibrahogar.clicked.connect(self.clearFibra)


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
            self.createCheckboxes(name, alias, position_x, position_y, with_box, heigth_box)

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



    def createCheckboxes(self, name, alias, position_x, position_y, with_box, heigth_box):
        
        self.ui.groupBoxPremiumFibrahogar.setGeometry(QtCore.QRect(20, 200, 280, heigth_box))
        self.checkBox = QtWidgets.QCheckBox(self.ui.groupBoxPremiumFibrahogar)
        self.checkBox.setGeometry(QtCore.QRect(position_x, position_y, 260, 30))
        self.checkBox.setObjectName(alias)
        self.checkBox.setText(name)

    def clearFibra(self):
        product_id = 5
        type_product = 7
        query = self.db.getProductsByIdAndTypeProduct(product_id, type_product)
        for i in range(0, query.rowCount()):
            alias = query.record(i).value("alias")
            self.+alias+.setChecked(False)

