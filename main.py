import sys
from builtins import super 
from datetime import date
from PyQt5 import QtWidgets
from main_ui import Ui_MainWindow
from PyQt5.QtWidgets import (QApplication, QMainWindow, QStackedWidget, qApp, QFrame)


from fibrahogar import FibraHogar
from dth import Dth
from hfc import Hfc



class WelcomeScreen(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        frame = QFrame(self)
        self.setCentralWidget(frame)
        frame.setStyleSheet("background-color:lightblue;")
        frame.setAutoFillBackground(True)
        
        fibraWindows = FibraHogar()
        dthWindows = Dth()
        hfcWindows = Hfc()
        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.addWidget(dthWindows)
        self.stackedWidget.addWidget(hfcWindows)
        self.stackedWidget.addWidget(fibraWindows)
        self.stackedWidget.setGeometry(0, 30, width_screen, height_screen)
        
        
        
        
        self.ui.actionFibra_Hogar.triggered.connect(self.fibraHogar)
        self.ui.actionInternet_HFC.triggered.connect(self.hfcWindow)
        self.ui.actionTelevisi_n_Satalital_DTH.triggered.connect(self.dthWindow)
        self.ui.exitAction.triggered.connect(qApp.quit)
        
        


    def dthWindow(self):
        self.stackedWidget.setCurrentIndex(0)

        
    def hfcWindow(self):
        self.stackedWidget.setCurrentIndex(1)

    def fibraHogar(self):
        self.stackedWidget.setCurrentIndex(2)
        


app = QApplication(sys.argv)
widgetWelcome = QtWidgets.QStackedWidget()
today =  date.today()
_date = today.strftime("%d/%m/%Y")
screen_resolution = app.desktop().screenGeometry()
width_screen = screen_resolution.width()
height_screen = screen_resolution.height()