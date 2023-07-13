import os
import sys
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*

class test(QMainWindow):
    def __init__(self):
        super().__init__()
        self.oyna = QWidget()
        self.oyna.setMinimumSize(300,300)
        self.oyna.setMaximumSize(300,300)
        self.vb=QVBoxLayout()
        ls1=["Andijon viloyati","Buxoro viloyati","Fargʻona viloyati","Jizzax viloyati","Xorazm viloyati","Namangan viloyati","Navoiy viloyati","Qashqadaryo viloyati","Qoraqalpogʻiston Respublikasi","Samarqand viloyati	","Sirdaryo viloyati","Surxondaryo viloyati","Toshkent viloyati"]
        ls2=[" Erkak"," ayol"]
        ls3=[" o'zbek"," tojik"," qozoq"]
        self.cmb1=QComboBox()
        self.cmb1.addItems(ls1)
        self.cmb2=QComboBox()
        self.cmb2.addItems(ls2)
        self.cmb3=QComboBox()
        self.cmb3.addItems(ls3)
        self.vb.addWidget(self.cmb1)
        self.vb.addWidget(self.cmb2)
        self.vb.addWidget(self.cmb3)
        btn=QPushButton("enter")
        btn.clicked.connect(self.enter)
        self.vb.addWidget(btn)

        self.oyna.setLayout(self.vb)
        self.oyna.show()

    def enter(self):
        f=open("file.txt","w+")
        st=""
        st+=self.cmb1.currentText()
        st+=self.cmb2.currentText()
        st+=self.cmb3.currentText()
        ls=st.split()
        f.write("Tug'ilgan viloyati "+str(ls[0])+str(ls[1])+"\n")
        f.write("Jinsi " + str(ls[2])+"\n")
        f.write("Millati " + str(ls[3]) + "\n")
        print(st)


app = QApplication(sys.argv)
cal = test()

sys.exit(app.exec_())




