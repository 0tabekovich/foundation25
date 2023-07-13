import os
import sys
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
from PyQt5.QtGui import *
class oyna1(QMainWindow):
    st=""

    def __init__(self):
        super().__init__()
        self.setMaximumSize(450, 450)
        self.setMinimumSize(450, 450)
        self.setFont(QFont("Regular", 20))
        self.setStyleSheet("bacground-color: rgb(0,205,0)")
        self.btn=QPushButton("Second window",self)
        self.btn.setGeometry(60,210,200,50)
        self.btn.clicked.connect(self.ulan)
        self.btn1=QPushButton("Save",self)
        self.btn1.setGeometry(10,210,200,50)
        self.btn1.clicked.connect(self.save)
        self.lin=QLineEdit(self)

    def save(self):
        oyna1.st+=self.lin.text()
        self.lin.setText("")

    def ulan(self):
        self.oyna=oyna2()
        self.oyna.show()
        self.hide()
class oyna2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMaximumSize(450,450)
        self.setMinimumSize(450,450)
        self.setFont(QFont("Regular",20))
        self.setStyleSheet("bacground-color: rgb(0,205,0)")

        lin=QLabel(f"{oyna1.st}",self)



app = QApplication(sys.argv)
cal = oyna1()
cal.show()
sys.exit(app.exec_())
