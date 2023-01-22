import sys 
from builtins import super 
from datetime import date
from PyQt5.uic import loadUi

from PyQt5.QtWidgets import (
    QApplication,
    QSplashScreen
)


import time
from main import WelcomeScreen


class SplashScreen(QSplashScreen):
    def __init__(self):
        super(QSplashScreen, self).__init__()
        loadUi("splash.ui", self)

    def progress(self):
        for i in range(100):
            time.sleep(0.01)
            self.progressBar.setValue(i)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    today =  date.today()
    _date = today.strftime("%d/%m/%Y")
    splash = SplashScreen()
    splash.show()
    splash.progress()
    main = WelcomeScreen()
    splash.finish(main)
    main.show()

try:
    sys.exit(app.exec_())
except:
    print("Saliendo")
