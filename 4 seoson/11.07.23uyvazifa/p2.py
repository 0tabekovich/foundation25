import os
import sys
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
class restaran(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ls=list()
        self.oyna = QWidget()
        self.oyna.setMinimumSize(700,500)
        self.oyna.setMaximumSize(700,500)
        self.vb=QVBoxLayout()
        self.hb=QHBoxLayout()

        self.taom1=QLabel("1-Taomlar royxati")
        self.vb.addWidget(self.taom1)
        self.create_checkbox("Mastava               25000 So'm")
        self.create_checkbox("Bishteks              30000 So'm")
        self.create_checkbox("Kuzasho'rva           35000 So'm")
        self.taom2=QLabel("2-Taomlar royxati")
        self.vb.addWidget(self.taom2)
        self.create_checkbox("Kabob                 40000 So'm")
        self.create_checkbox("Beshbarmoq            70000 So'm")
        self.create_checkbox("Assorti               150000 So'm")
        self.create_checkbox("Qozonkabob            50000 So'm")
        self.ichimlik = QLabel("Ichimliklar royxati")
        self.vb.addWidget(self.ichimlik)
        self.create_checkbox("Cocacola              15000 So'm")
        self.create_checkbox("Dena                  15000 So'm")
        self.create_checkbox("Sprite                8000 So'm")
        self.create_checkbox("Choy                  10000 So'm")
        self.desert = QLabel("Desertlar royxati")
        self.vb.addWidget(self.desert)
        self.create_checkbox("«Brauni»pirogi        50000 So'm")
        self.create_checkbox("«Nyu-York»chizkeyki   25000 So'm")
        self.create_checkbox("Olchali«Brauni»pirogi 25000 So'm")
        self.btn = QPushButton("Hisob")
        self.create_checkbox("«Mikado»to’rti 25000 So'm")
        self.btn.clicked.connect(self.hisob)
        self.vb.addWidget(self.btn)
        self.oyna.setLayout(self.vb)
        self.oyna.show()
    def create_checkbox(self,k):
        cbx=QCheckBox(k)
        self.vb.addWidget(cbx)
        self.ls.append(cbx)
    def hisob(self):
        c=0
        l=[]
        for x in self.ls:
            if x.isChecked():
                l.append(x.text())
                k=int(x.text().split()[1])
                c+=k

        msg=QMessageBox(self)
        msg.setMaximumSize(300,750)
        msg.setMinimumSize(300,750)
        msg.setFont(QFont("Regular", 15))
        for x in l:
            msg.setText(msg.text()+f"{str(x)}\n")
        msg.setInformativeText(f"Umimiy hisob:{c} So'm")
        msg.show()
        msg.exec_()




app = QApplication(sys.argv)
cal = restaran()
sys.exit(app.exec_())
