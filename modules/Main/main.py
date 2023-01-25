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
        self.settingsWindows = Settings()
        self.stackedWidget = QStackedWidget(self)
        # Stacked Widgets
        self.stackedWidget.addWidget(dthWindows)
        self.stackedWidget.addWidget(hfcWindows)
        self.stackedWidget.addWidget(fibraWindows)
        self.stackedWidget.addWidget(hfcTvWindows)
        self.stackedWidget.setGeometry(0, 30, width_screen, height_screen + 30)
        #Actions call
        self.ui.actionFibra_Hogar.triggered.connect(self.fibraHogar)
        self.ui.actionInternet_HFC.triggered.connect(self.hfcWindow)
        self.ui.actionTelevisi_n_Satalital_DTH.triggered.connect(self.dthWindow)
        self.ui.action_hfc_tv.triggered.connect(self.hfcTvWindow)
        self.ui.actionSettingsDolar.triggered.connect(self.settingsWindow)
        self.ui.exitAction.triggered.connect(qApp.quit)
        
        
    def dthWindow(self):
        self.stackedWidget.setCurrentIndex(0)
        
    def hfcWindow(self):
        self.stackedWidget.setCurrentIndex(1)

    def fibraHogar(self):
        self.stackedWidget.setCurrentIndex(2)
    
    def settingsWindow(self):
        self.settingsWindows.show()

    def hfcTvWindow(self):
        self.stackedWidget.setCurrentIndex(3)
        


app = QApplication(sys.argv)
widgetWelcome = QtWidgets.QStackedWidget()
today =  date.today()
_date = today.strftime("%d/%m/%Y")
screen_resolution = app.desktop().screenGeometry()
width_screen = screen_resolution.width()
height_screen = screen_resolution.height()