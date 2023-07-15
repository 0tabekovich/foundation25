from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5.QtCore import*
import sys
import random


class omad_lotto(QMainWindow):
    ls=[]
    def __init__(self):
        super().__init__()
        self.setMaximumSize(840,480)
        self.setMinimumSize(840,480)
        self.setStyleSheet("""
        background-color: rgb(232,244,140);
                            """)
    #radio button
        self.rdb1=QRadioButton("Omad (36/5)",self)
        self.rdb1.setGeometry(10,5,120,50)
        self.rdb2=QRadioButton("Sharqona (36/6)",self)
        self.rdb2.setGeometry(135,5,140,50)
        self.rdb3=QRadioButton("Super (36/7)",self)
        self.rdb3.setGeometry(280,5,120,50)
    #latatiron
        stt=QPushButton("Start",self)
        stt.setGeometry(405,5,100,50)
        stt.setStyleSheet("""
                    background-color: rgb(255,188,217);
                    border-width: 3px;
                    border-radius: 20px;
                    border-color: rgb(10,10,10);
                    border-style: solid;
                """)
        stt.clicked.connect(self.rand)
        self.lb1=self.latatiron()
        self.lb1.setGeometry(520,10,40,40)
        self.lb2=self.latatiron()
        self.lb2.setGeometry(565, 10, 40, 40)
        self.lb3=self.latatiron()
        self.lb3.setGeometry(610, 10, 40, 40)
        self.lb4=self.latatiron()
        self.lb4.setGeometry(655, 10, 40, 40)
        self.lb5=self.latatiron()
        self.lb5.setGeometry(700, 10, 40, 40)
        self.lb6=self.latatiron()
        self.lb6.setGeometry(745, 10, 40, 40)
        self.lb7=self.latatiron()
        self.lb7.setGeometry(790, 10, 40, 40)
    #lieedit
        self.lne=QLineEdit(self)
        self.lne.setGeometry(10,55,260,50)
        self.lne.setFont(QFont("Arial",13))
        self.lne.setStyleSheet("""
            background-color: rgb(255,240,240);
            border-width: 3px;
            border-radius: 20px;
            border-color: rgb(0,0,255);
            border-style: solid;
        """)
        plus=QPushButton("+",self)
        plus.setGeometry(280,55,70,50)
        plus.setStyleSheet("""
            background-color: rgb(255,188,217);
            border-width: 3px;
            border-radius: 20px;
            border-color: rgb(10,10,10);
            border-style: solid;
        """)
        plus.clicked.connect(self.text_create)
    #textedit
        self.txt=QTextEdit(self)
        self.txt.setFont(QFont("Arial",13))
        self.txt.setGeometry(405,60,415,340)
    #buttons
        c=1
        self.ls=list()
        t=110
        self.grb=QButtonGroup()
        for x in range(1,7):
            k=10
            for y in range(1,7):
                bt=QPushButton(f"{c}",self)
                bt.setStyleSheet("""
            background-color: rgb(255,188,217);
            border-width: 3px;
            border-radius: 25px;
            border-color: rgb(10,10,10);
            border-style: solid;
        """)
                bt.setGeometry(k,t,50,50)
                self.grb.addButton(bt)
                c+=1
                k+=55
            t+=55
        self.grb.buttonClicked.connect(self.line_create)
    def latatiron(self):
        lb=QLabel("",self)
        lb.setFont(QFont("Arial",13))
        lb.setStyleSheet("""
            background-color: rgb(255,196,12);
            border-width: 3px;
            border-radius: 20px;
            border-color: rgb(10,10,10);
            border-style: solid;
        """)
        return lb
    def line_create(self,btn):
        self.lne.setText(self.lne.text()+f"{btn.text()}"+" ")
    def text_create(self):
        l=self.lne.text()
        omad_lotto.ls.append(l.split())
        self.txt.setText(f"{omad_lotto.ls}")
        self.lne.clear()

    def rand(self):
        ls1=[]
        self.lb1.setText(str(random.randint(1,36)))
        self.lb2.setText(str(random.randint(1, 36)))
        self.lb3.setText(str(random.randint(1, 36)))
        self.lb4.setText(str(random.randint(1, 36)))
        self.lb5.setText(str(random.randint(1, 36)))
        if self.rdb2.isChecked():
            self.lb6.setText(str(random.randint(1, 36)))
        elif self.rdb3.isChecked():
            self.lb6.setText(str(random.randint(1, 36)))
            self.lb7.setText(str(random.randint(1, 36)))
        ls1.append(self.lb1.text())
        ls1.append(self.lb2.text())
        ls1.append(self.lb3.text())
        ls1.append(self.lb4.text())
        ls1.append(self.lb5.text())
        ls1.append(self.lb6.text())
        ls1.append(self.lb7.text())
        self.txt.clear()
        for x in omad_lotto.ls:
            count=0
            for y in x:
                for z in ls1:
                    if z==y:
                        ls1.remove(z)
                        count+=1
            self.txt.setText(self.txt.toPlainText()+f"{x} raqamlaringiz orasida {count}ta oxshashli topildi\n")
            if count==len(x):
                self.txt.setText(self.txt.toPlainText()+f"\n\n\n\t Siz g'olib bo'ldingiz !!! \n"
                                                        f"\t 100.000.000 $ yutdingiz \n\n\n")
                return

def main():
    app=QApplication(sys.argv)
    project=omad_lotto()
    project.show()
    sys.exit(app.exec_())

main()