import os
import sys
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
from PyQt5.QtGui import *

class registration():
    def __init__(self):
        self.oyna=QWidget()
        self.oyna.setMinimumSize(780,780)
        self.oyna.setMaximumSize(780,780)
        self.oyna.setWindowTitle("Registratsiya")
        self.oyna.setFont(QFont("Arial",20))
        vb=QVBoxLayout()
        hb=QHBoxLayout()

        lin1=QLabel("Ismingizni kiriting")
        self.lin1e=QLineEdit()

        linfa=QLabel("Familiyangizni kiriting")
        self.linfae=QLineEdit()

        linji=QLabel("Jinsingizni tanlang")
        self.linji1=QCheckBox("Ayol")
        self.linji2=QCheckBox("Erkak")

        linlogin=QLabel("Login")
        self.linloge=QLineEdit()

        linparol=QLabel("Parol ")
        self.linparole=QLineEdit()

        lin1parol=QLabel("Parolni qayta kiriting")
        self.lin1parole=QLineEdit()

        lininfo=QLabel("Malumotlarni faylga saqlashga roziman")
        self.lininfocheck=QCheckBox()


        linfinish=QPushButton("Registratsiya")
        linfinish.clicked.connect(self.add_file)
        hb.addWidget(lin1)
        hb.addWidget(self.lin1e)
        vb.addLayout(hb)
        hb = QHBoxLayout()
        hb.addWidget(linfa)
        hb.addWidget(self.linfae)
        vb.addLayout(hb)
        hb = QHBoxLayout()
        hb.addWidget(linji)
        hb.addWidget(self.linji1)
        hb.addWidget(self.linji2)
        vb.addLayout(hb)
        hb = QHBoxLayout()
        hb.addWidget(linlogin)
        hb.addWidget(self.linloge)
        vb.addLayout(hb)
        hb = QHBoxLayout()
        hb.addWidget(linparol)
        hb.addWidget(self.linparole)
        vb.addLayout(hb)
        hb = QHBoxLayout()
        hb.addWidget(lin1parol)
        hb.addWidget(self.lin1parole)
        vb.addLayout(hb)
        hb = QHBoxLayout()
        hb.addWidget(self.lininfocheck)
        hb.addWidget(lininfo)
        vb.addLayout(hb)
        vb.addWidget(linfinish)
        self.oyna.setLayout(vb)
        self.oyna.show()
    def add_file(self):
        jins=str()
        if self.linji1.isChecked():
            jins="Ayol"
        else:
            jins="Erkak"
        if self.lininfocheck.isChecked():
            f=open("File.txt","w+")
            f.write(f"ismi {self.lin1e.text()}\nfamiliyasi  {self.linfae.text()}\njinsi  {jins}\nLogin  {self.linloge.text()}\nparol  {self.linparole.text()}")
            f.close()
            print("boldi")


app = QApplication(sys.argv)
cal = registration()
sys.exit(app.exec_())