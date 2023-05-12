import sys
from builtins import super 
from datetime import date
from PyQt5 import QtWidgets
from modules.Main.main_ui import Ui_MainWindow
from PyQt5.QtWidgets import (QApplication, QMainWindow, QStackedWidget, qApp, QFrame)


from modules.Fibrahogar.fibrahogar import FibraHogar
from modules.Dth.dth import Dth
from modules.Hfc.hfc_tv import HfcTv
from modules.Hfc.hfc import Hfc
from modules.Settings.settings import Settings
from modules.Dashboard.dashboard import Dashboard
from modules.Settings.prices import Prices
from modules.Settings.templates import Templates



class MainScreen(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        frame = QFrame(self)
        self.setCentralWidget(frame)
        # frame.setStyleSheet("background-color:lightblue;")
        frame.setAutoFillBackground(True)
        
        fibraWindows = FibraHogar()
        dthWindows = Dth()
        hfcWindows = Hfc()
        hfcTvWindows = HfcTv()
        dashboardWindows = Dashboard()
        pricesWindows = Prices()
        templatesWindows = Templates()
        
        self.settingsWindows = Settings()
        self.stackedWidget = QStackedWidget(self)
        # Stacked Widgets
        self.stackedWidget.addWidget(dashboardWindows)
        self.stackedWidget.addWidget(dthWindows)
        self.stackedWidget.addWidget(hfcWindows)
        self.stackedWidget.addWidget(fibraWindows)
        self.stackedWidget.addWidget(hfcTvWindows)
        self.stackedWidget.addWidget(pricesWindows)
        self.stackedWidget.addWidget(templatesWindows)
        self.stackedWidget.setGeometry(0, 30, width_screen, height_screen + 30)
        #Actions call
        self.ui.actionFibra_Hogar.triggered.connect(self.fibraHogar)
        self.ui.actionInternet_HFC.triggered.connect(self.hfcWindow)
        self.ui.actionTelevisi_n_Satalital_DTH.triggered.connect(self.dthWindow)
        self.ui.action_hfc_tv.triggered.connect(self.hfcTvWindow)
        self.ui.actionSettingsDolar.triggered.connect(self.settingsWindow)
        self.ui.actionPrincipal.triggered.connect(self.dashboardWindow)
        self.ui.actionConfiguraci_n_Precios.triggered.connect(self.pricesWindow)
        self.ui.action_Templates.triggered.connect(self.templatesWindow)
        self.ui.exitAction.triggered.connect(qApp.quit)
        
       
        
    def dashboardWindow(self):
        self.stackedWidget.setCurrentIndex(0)
        
    def dthWindow(self):
        self.stackedWidget.setCurrentIndex(1)
        
    def hfcWindow(self):
        self.stackedWidget.setCurrentIndex(2)

    def fibraHogar(self):
        self.stackedWidget.setCurrentIndex(3)
    
    def settingsWindow(self):
        self.settingsWindows.show()

    def hfcTvWindow(self):
        self.stackedWidget.setCurrentIndex(4)
        
    def pricesWindow(self):
        self.stackedWidget.setCurrentIndex(5)

    def templatesWindow(self):
        self.stackedWidget.setCurrentIndex(6)
        


app = QApplication(sys.argv)
widgetWelcome = QtWidgets.QStackedWidget()
today =  date.today()
_date = today.strftime("%d/%m/%Y")
screen_resolution = app.desktop().screenGeometry()
width_screen = screen_resolution.width()
height_screen = screen_resolution.height()