# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 02:42:38 2023

@author: alesp
"""
import sys 
from PyQt5.QtWidgets import (
    QDialog,
)

from modules.Hfc.hfc_tv_ui import Ui_Dialog


class HfcTv(QDialog):
    def __init__(self):
        super(HfcTv, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)