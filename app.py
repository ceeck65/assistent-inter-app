import sys 
from builtins import super 
from datetime import date
from splash_ui import Ui_Dialog

from PyQt5.QtWidgets import (
    QApplication,
    QSplashScreen
)

from PyQt5.QtWidgets import QDesktopWidget
import time
from modules.Main.main import MainScreen
from PyQt5.QtCore    import Qt

class SplashScreen(QSplashScreen):
    def __init__(self):
        super(QSplashScreen, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.center()

    def progress(self):
        for i in range(101):
            time.sleep(0.01)
            self.ui.progressBar.setValue(i)
            
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    today =  date.today()
    _date = today.strftime("%d/%m/%Y")
    splash = SplashScreen()
    splash.show()
    splash.progress()
    main = MainScreen()
    splash.finish(main)
    main.showMaximized()

try:
    sys.exit(app.exec_())
except:
    print("Exit App")
