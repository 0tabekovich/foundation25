import os
import sys
import random
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
from PyQt5.QtGui import *
class oyin(QMainWindow):
    c=0
    def __init__(self):
        super().__init__()
        self.setMaximumSize(450, 450)
        self.setMinimumSize(450, 450)
        self.setFont(QFont("Regular", 30))
        self.setStyleSheet("bacground-color: rgb(0,205,0)")
        self.k=random.randint(9,100)
        self.line=QLineEdit(self)
        self.line.setGeometry(250,60,100,50)
        self.line.setFont(QFont("Regular", 15))
        self.lin=QLabel("2 xonali son kiriting",self)
        self.lin.setGeometry(10,60,250,50)
        self.lin.setFont(QFont("Regular", 15))
        self.btn=QPushButton("enter",self)
        self.btn.setGeometry(210,160,150,50)
        self.btn.setFont(QFont("Regular", 15))
        self.btn.clicked.connect(self.ulan)

    def ulan(self):
        oyin.c+=1
        mgb = QMessageBox(self)
        if self.line.text()==str(self.k):
            mgb.setInformativeText(f"{oyin.c} urinishda topdingiz")


        else:
            if self.k>int(self.line.text()):
                mgb.setInformativeText(f"{self.line.text()} dan katta ,xato topdiz")
            else:
                mgb.setInformativeText(f"{self.line.text()} dan kichik ,xato topdiz")
        mgb.exec_()
app = QApplication(sys.argv)
cal = oyin()
cal.show()
sys.exit(app.exec_())