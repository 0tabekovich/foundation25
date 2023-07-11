from PyQt5.QtGui import *#Qbutton
from PyQt5.QtCore import *#QFOnt
from PyQt5.QtWidgets import *#Qmainwindow
from os import system
import sys
system("cls")
class dastur(QMainWindow):
    check=False
    def __init__(self):
        
        #aosiy oynani chiqarish
        
        super().__init__()
        self.setMinimumSize(640,240)
        self.setMaximumSize(640,240)
        self.setWindowTitle("PyQt5da birinchi dastur")
        self.setStyleSheet("background-color: rgb(0,0,0);")
        self.setWindowIcon(QIcon("C:\\Users\\User\\Downloads\\calculator.ico"))
        
        #Qlabel qo'shish
        lbl=QLabel("1-sonni kiriting:  ",self)
        lbl.setFont(QFont("Times New Roman",22))
        lbl.setStyleSheet("color: rgb(255,69,0)")
        lbl.move(50,50)
        lbl.resize(300,50)
        lbl.setPixmap(QPixmap("D:\\rasm.jpg"))
        #Qlineedit
        self.ldt=QLineEdit(self)
        self.ldt.setGeometry(360,50,250,50)
        self.ldt.setFont(QFont("Times New Roman",20))
        self.ldt.setStyleSheet("""
                           background-color: rgb(255,160,122);
                           color: rgb(138,34,34);
                           border-width: 3px;
                           border-style: solid;
                           border-radius: 25px;
                           border-color: red;""")
        self.ldt.setAlignment(Qt.AlignCenter)
        self.ldt.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        
        
        lb2=QLabel("2-sonni kiriting:  ",self)
        lb2.setFont(QFont("Times New Roman",22))
        lb2.setStyleSheet("color: rgb(255,69,0)")
        lb2.move(50,110)
        lb2.resize(300,50)
        
        #Qlineedit
        self.ldt1=QLineEdit(self)
        self.ldt1.setGeometry(360,110,250,50)
        self.ldt1.setFont(QFont("Times New Roman",20))
        self.ldt1.setStyleSheet("""
                           background-color: rgb(255,160,122);
                           color: rgb(138,34,34);
                           border-width: 3px;
                           border-style: solid;
                           border-radius: 25px;
                           border-color: red;""")
        self.ldt1.setAlignment(Qt.AlignCenter)
        
        #Tugma qo'shish
        
        btn=QPushButton("Calculate",self)
        #btn.setText("Calculate")
        btn.setGeometry(410,170,200,50)
        btn.setStyleSheet("""
                           background-color: rgb(0,0,0);
                           color: rgb(102,255,0);
                           border-width: 5px;
                           border-style: dotted;
                           border-radius: 25px;
                           border-color: rgb(102,255,0)""")
        btn.setFont(QFont("Consolas",18))
        btn.clicked.connect(self.hisobla)
        self.lbl3=QLabel(self)
        self.lbl3.setGeometry(50,170,250,50)
        self.lbl3.setFont(QFont("Times New Roman",22))
        self.lbl3.setStyleSheet("color: rgb(125,29,60)")
        
    def hisobla(self):
        
        print(f"Result: {int(self.ldt.text())+int(self.ldt1.text())}")
        self.lbl3.setText(f"Result: {int(self.ldt.text())+int(self.ldt1.text())}")
    
    def tozalash(self):
        self.ldt.clear()

app=QApplication(sys.argv)
project=dastur()
project.show()
sys.exit(app.exec_())