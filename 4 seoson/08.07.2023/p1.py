import os
import sys
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
from PyQt5.QtGui import *

class fasl():
    def __init__(self):
        super().__init__()
        self.oyna=
        self.setMinimumSize(380, 740)
        self.setMaximumSize(380, 740)
        self.setWindowTitle("Fasl")
        grid=QGridLayout()


        lin= QLabel(self)
        lin.resize(150, 150)
        lin.setPixmap(QPixmap("C:\\Users\\ozodb\\Downloads\\java.png"))

        lin1 = QLabel(self)
        lin1.resize(150,150)
        lin1.setPixmap(QPixmap("C:\\Users\\ozodb\\Downloads\\java.png"))

        lin2 = QLabel(self)
        lin2.resize(150, 150)
        lin2.setPixmap(QPixmap("C:\\Users\\ozodb\\Downloads\\java.png"))

        lin3 = QLabel(self)
        lin3.resize(150, 150)
        lin3.setPixmap(QPixmap("C:\\Users\\ozodb\\Downloads\\java.png"))

        grid.addWidget(lin,1,1)
        grid.addWidget(lin2,1,2)
        grid.addWidget(lin3,2,1)
        grid.addWidget(lin1,2,2)

app = QApplication(sys.argv)
cal = fasl()
cal.show()
sys.exit(app.exec_())