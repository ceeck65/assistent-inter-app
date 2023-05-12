# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 16:17:44 2023

@author: alesp
"""
from datetime import date
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QDoubleValidator
from modules.Settings.settings_ui import Ui_Dialog
from modules.Data.data import getDolar, setDolar


class Settings(QDialog):
    def __init__(self):
         super(Settings, self).__init__()
         self.ui = Ui_Dialog()
         self.ui.setupUi(self)
         self.ui.lbl_dolar.setText("$1 = Bs. 0")      
         self.ui.onlyDouble= QDoubleValidator()
         self.ui.txt_dolar.setValidator(self.ui.onlyDouble)
         self.ui.bn_set_dolar.clicked.connect(self.setDollar)
         self.ui.lbl_date.setText("Precio del dolar del día %s, Bs. %.2f" % (_date, _dolar))
         self.ui.txt_dolar.returnPressed.connect(self.ui.bn_set_dolar.click)
         self.ui.txt_dolar.setText(str(_dolar))
    
    
    def setDollar(self):
        global _dolar
        if self.ui.txt_dolar.text() == "":
            __dolar = 0
            self.data.setDolar(__dolar)
            self.ui.txt_dolar.setText(str(getDolar()))
        else:
            __dolar = float(self.ui.txt_dolar.text())
            setDolar(__dolar)
            _dolar = getDolar()
            self.ui.txt_dolar.setText(str(_dolar))
        self.ui.lbl_dolar.setText("$1 = Bs. %.2f" % (_dolar))
        self.ui.lbl_date.setText("Precio del dolar del día %s, Bs. %.2f" % (_date, _dolar))



today =  date.today()
_date = today.strftime("%d/%m/%Y")
_dolar = getDolar()