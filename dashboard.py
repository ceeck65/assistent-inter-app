import sys 
from builtins import super 
from datetime import date


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QDoubleValidator
from main_ui import Ui_MainWindow


from PyQt5.QtWidgets import (
    QApplication,
    QMessageBox,
    QWidget,
)



from data import getDolar, setDolar


class DashboardScreen(QWidget):
    def __init__(self):
        super(DashboardScreen, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
  
        self.ui.lblDolar.setText("$1 = Bs. 0")      
        self.ui.onlyDouble= QDoubleValidator()
        self.ui.txtDolar.setValidator(self.ui.onlyDouble)
        self.ui.btnSetDolar.clicked.connect(self.setDollar)
        
        self.ui.lblPriceReferentialDolarDTH.setText("Precio del dolar del día %s, Bs. %.2f" % (_date, _dolar))
        self.ui.txtDolar.returnPressed.connect(self.ui.btnSetDolar.click)
        self.ui.txtDolar.setText(str(_dolar))
        
        

        
    def setDollar(self):
        global _dolar
        if self.ui.txtDolar.text() == "":
            __dolar = 0
            self.data.setDolar(__dolar)
            self.ui.txtDolar.setText(str(getDolar()))
        else:
            __dolar = float(self.ui.txtDolar.text())
            setDolar(__dolar)
            _dolar = getDolar()
            self.ui.txtDolar.setText(str(_dolar))
        self.ui.lblDolar.setText("$1 = Bs. %.2f" % (_dolar))
        self.ui.lblPriceReferentialDolarDTH.setText("Precio del dolar del día %s, Bs. %.2f" % (_date, _dolar))



    

   ##################################
   #                                #
   #    MODULOS PARA TICKETS HFC    #
   #                                #
   ##################################




    def clearInternetHCF(self):
        self.ui.rf_dwpw.setChecked(False)
        self.ui.rf_rxpw.setChecked(False)
        self.ui.rf_uppw.setChecked(False)
        self.ui.rf_dwsnr.setChecked(False)
        self.ui.rf_upsnr.setChecked(False)
        self.ui.rf_hit_miss.setChecked(False)
        self.ui.rf_flaps.setChecked(False)
        self.ui.rf_ajust_pot.setChecked(False)
        self.ui.rf_ok.setChecked(False)
        self.ui.ping_ok.setChecked(False)
        self.ui.ping_sin_respuesta.setChecked(False)
        self.ui.ping_low.setChecked(False)
        self.ui.ping_txt.setValue(200)
        self.ui.ticket_ab_hfc_internet.clear()
        self.ui.ticket_k2b_hfc_internet.clear()
        self.ui.combo_internet.setCurrentIndex(0)
        self.ui.combo_cm_mta.setCurrentIndex(0)
        self.ui.combo_plan_internet.setCurrentIndex(0)
        self.ui.widget_2.setStyleSheet("background-color: rgb(235, 235, 235);")


app = QApplication(sys.argv)
screen_resolution = app.desktop().screenGeometry()
width_screen = screen_resolution.width()
height_screen = screen_resolution.height()
widgetWelcome = QtWidgets.QStackedWidget()
# main
today =  date.today()
_date = today.strftime("%d/%m/%Y")
_dolar = getDolar()