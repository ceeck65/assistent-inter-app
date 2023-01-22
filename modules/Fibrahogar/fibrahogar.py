# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 02:42:38 2023

@author: alesp
"""
import sys 
from PyQt5.QtWidgets import (
    QDialog,
)

from modules.Fibrahogar.fibrahogar_ui import Ui_Dialog


class FibraHogar(QDialog):
    def __init__(self):
        super(FibraHogar, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


