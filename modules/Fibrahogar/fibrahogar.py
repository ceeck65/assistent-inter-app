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


    



    # def generateCheck(self):
    #     position_y = 0
    #     heigth_box = 0
    #     with_box = 0
    #     position_x = 0
    #     with_checkbox = 0
    #     heigth_checkbox = 0

    #     for x in range(2):
    #         position_x = position_x + with_checkbox
    #         with_box = position_x + with_box + 100
    #         for y in range(2):
    #             position_y = position_y + heigth_checkbox
    #             heigth_box = heigth_box + 20
    #             name = "%d_%d - " % (x, y)
    #             x = position_x + position_y
    #             y = position_y + position_x
    #             self.createCheckboxes(name, x, y, with_box, heigth_box)
    #             print(name, x, y)
    #             heigth_checkbox = 20
    #         with_checkbox = 20
                

    def createCheckboxes(self, name, alias, position_x, position_y, with_box, heigth_box):
        
        self.ui.groupBoxPremiumFibrahogar.setGeometry(QtCore.QRect(20, 200, 280, heigth_box))
        self.checkBox = QtWidgets.QCheckBox(self.ui.groupBoxPremiumFibrahogar)
        self.checkBox.setGeometry(QtCore.QRect(position_x, position_y, 260, 30))
        self.checkBox.setObjectName(alias)
        self.checkBox.setText(name)


