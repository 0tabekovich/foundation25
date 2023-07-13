import os
import sys
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*

class test(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(600,600)
        self.setMaximumSize(600,600)
        lbl1=QLabel("Test 1\nA",self)
        lbl1.setFont(QFont("Arial",13))
        lbl1.setGeometry(10,10,100,50)
        self.lblr1=QRadioButton("2",self)
        self.lblr1.setGeometry(20,60,100,50)
        self.lblr2=QRadioButton("2",self)
        self.lblr2.setGeometry(130,60,100,50)

        lbl21 = QLabel("Test 2\nA", self)
        
        lbl21.setFont(QFont("Arial", 13))
        lbl21.setGeometry(10, 110, 100, 50)
        self.lblr21 = QRadioButton("2", self)
        self.lblr21.setGeometry(20, 170, 100, 50)
        self.lblr22 = QRadioButton("2", self)
        self.lblr22.setGeometry(130, 170, 100, 50)

        lbl31 = QLabel("Test 3\nA", self)
        lbl31.setFont(QFont("Arial", 13))
        lbl31.setGeometry(10, 220, 100, 50)
        self.lblr31 = QRadioButton("2", self)
        self.lblr31.setGeometry(20,280, 100, 50)
        self.lblr32 = QRadioButton("2", self)
        self.lblr32.setGeometry(130,280, 100, 50)

        lbl41 = QLabel("Test 4\nA", self)
        lbl41.setFont(QFont("Arial", 13))
        lbl41.setGeometry(10, 330, 100, 50)
        self.lblr41 = QRadioButton("2", self)
        self.lblr41.setGeometry(20,390, 100, 50)
        self.lblr42 = QRadioButton("2", self)
        self.lblr42.setGeometry(130,390, 100, 50)

        lbl51 = QLabel("Test 5\nA", self)
        lbl51.setFont(QFont("Arial", 13))
        lbl51.setGeometry(10, 440, 100, 50)
        self.lblr51 = QRadioButton("2", self)
        self.lblr51.setGeometry(20, 500, 100, 50)
        self.lblr52 = QRadioButton("2", self)
        self.lblr52.setGeometry(130, 500, 100, 50)



app = QApplication(sys.argv)
cal = test()
cal.show()
sys.exit(app.exec_())




