import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
import mysql.connector as sq
class registratsiya(QMainWindow):
    def __init__(self,database_name):
        super().__init__()
        self.Con=sq.connect(host='localhost',password='root',user='root')
        self.resize(1920,1080)
        self.setStyleSheet("background-color: rgb(10,60,10);")
        tb=QTabWidget(self)
        tb.setFont(QFont('Arial',22))
        tb.resize(1920,1080)
        self.reg=QWidget()
        tb.addTab(self.reg,"Registrtion")
        self.upda=QWidget()
        self.upda.setStyleSheet("background-color: rgb(230,240,0);")
        tb.addTab(self.upda,"Update part")

    #add widget

        lbl1=QLabel("Ism: ",self.reg)
        lbl1.setGeometry(100,100,250,50)
        lbl1.setFont(QFont('Arial',22))

        lbl2 = QLabel("Familiya: ", self.reg)
        lbl2.setGeometry(100,200, 250, 50)
        lbl2.setFont(QFont('Arial', 22))

        lbl3 = QLabel("Jins: ", self.reg)
        lbl3.setGeometry(100,300, 250, 50)
        lbl3.setFont(QFont('Arial', 22))

        lbl4 = QLabel("Login: ", self.reg)
        lbl4.setGeometry(100, 400, 250, 50)
        lbl4.setFont(QFont('Arial', 22))

        lbl5 = QLabel("Parol: ", self.reg)
        lbl5.setGeometry(100, 500, 250, 50)
        lbl5.setFont(QFont('Arial', 22))

        lbl6 = QLabel("Parol_: ", self.reg)
        lbl6.setGeometry(100, 600, 250, 50)
        lbl6.setFont(QFont('Arial', 22))

        self.let1=QLineEdit(self.reg)
        self.let1.setFont(QFont('Arial', 22))
        self.let1.setGeometry(400,100,400,50)

        self.let2 = QLineEdit(self.reg)
        self.let2.setFont(QFont('Arial', 22))
        self.let2.setGeometry(400, 200, 400, 50)

        self.rdb1=QRadioButton("Ayol",self.reg)
        self.rdb1.setFont(QFont('Arial', 22))
        self.rdb1.setGeometry(400,300,200,50)

        self.rdb2 = QRadioButton("Erkak", self.reg)
        self.rdb2.setFont(QFont('Arial', 22))
        self.rdb2.setGeometry(600,300, 200, 50)

        self.let4 = QLineEdit(self.reg)
        self.let4.setFont(QFont('Arial', 22))
        self.let4.setGeometry(400,400, 400, 50)

        self.let5 = QLineEdit(self.reg)
        self.let5.setFont(QFont('Arial', 22))
        self.let5.setGeometry(400,500, 400, 50)
        self.let5.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.let6 = QLineEdit(self.reg)
        self.let6.setFont(QFont('Arial', 22))
        self.let6.setGeometry(400,600, 400, 50)
        self.let6.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.ckb=QCheckBox("Ma'lumotning faylga saqlashga roziman",self.reg)
        self.ckb.setFont(QFont('Arial', 18))
        self.ckb.setGeometry(150,700,600, 150)

        self.mainb=QPushButton('Registr',self.reg)
        self.mainb.setFont(QFont('Arial',35))
        self.mainb.setGeometry(1200,200,500,500)
        self.mainb.setStyleSheet("background-color: rgb(230,240,0);")
        self.mainb.clicked.connect(self.create_table)
    #mysql part
        self.cur=self.Con.cursor()
        sql=f'Create database if not exists {database_name}'
        self.cur.execute(sql)
        self.Con.commit()
        sql=f'Use {database_name}'
        self.cur.execute(sql)

    #update widget
        lblup=QLabel("Qaysini o'zgartirmoqchisiz ",self.upda)
        lblup.setFont(QFont('Arial',22))
        lblup.setGeometry(150,150,500,50)
        self.Cmb=QComboBox(self.upda)
        self.Cmb.addItems(["name","surname",'jins','login','parol'])
        self.Cmb.setGeometry(100,250,250,75)
        self.Cmb.setFont(QFont('Arial', 22))
        self.Cmb.setStyleSheet("background-color: rgb(10,60,10);")
        l1=QLabel("=",self.upda)
        l1.setFont(QFont('Arial', 22))
        l1.setGeometry(500,265,50,50)
        self.le1=QLineEdit(self.upda)
        self.le1.setFont(QFont('Arial', 22))
        self.le1.setGeometry(580, 265, 350, 50)

        lblup = QLabel("Qaysi biridan (Where)", self.upda)
        lblup.setFont(QFont('Arial', 22))
        lblup.setGeometry(150, 350, 500, 50)
        self.Cmb1 = QComboBox(self.upda)
        self.Cmb1.addItems(["name", "surname", 'jins', 'login', 'parol'])
        self.Cmb1.setGeometry(100,450, 250,75)
        self.Cmb1.setFont(QFont('Arial', 22))
        self.Cmb1.setStyleSheet("background-color: rgb(10,60,10);")
        l2 = QLabel("=", self.upda)
        l2.setFont(QFont('Arial', 22))
        l2.setGeometry(500, 465, 50, 50)
        self.le2 = QLineEdit(self.upda)
        self.le2.setFont(QFont('Arial', 22))
        self.le2.setGeometry(580, 465, 350, 50)

        btn=QPushButton("Update",self.upda)
        btn.setFont(QFont('Arial', 22))
        btn.setStyleSheet("background-color: rgb(10,60,10);")
        btn.setGeometry(1200,200,500,500)
        btn.clicked.connect(self.update_)
    def create_table(self):
        if self.let5.text()==self.let6.text():
            self.mainb.setText("Registr")
            if self.ckb.isChecked():
                sql=f"Create table if not exists registr(id int auto_increment primary key,name varchar(20),surname varchar(20),jins varchar(20),login varchar(20),parol varchar(10))"
                self.cur.execute(sql)
                self.Con.commit()
                sql="Insert into registr(name,surname,jins,login,parol) value(%s,%s,%s,%s,%s)"
                if self.rdb2.isChecked():
                    k="Erkak"
                else:
                    k="Ayol"
                val=(self.let1.text(),self.let2.text(),k,self.let4.text(),self.let5.text())
                self.cur.execute(sql,val)
                self.Con.commit()
                self.clear()
            else:
                self.clear()
        else:
            self.mainb.setText("Parol bir xil emas!")

    def update_(self):
        sql=f"update registr set {self.Cmb.currentText()} = '{self.le1.text()}' where {self.Cmb1.currentText()} = '{self.le2.text()}';"
        self.cur.execute(sql)
        self.Con.commit()

    def clear(self):
        self.let6.clear()
        self.let5.clear()
        self.let4.clear()
        self.let2.clear()
        self.let1.clear()

app=QApplication(sys.argv)
re=registratsiya('Registr')
re.show()
sys.exit(app.exec_())