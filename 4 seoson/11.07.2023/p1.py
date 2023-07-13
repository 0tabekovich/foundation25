import os
import sys
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
from PyQt5.QtGui import *
class fayl1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(800,500)
        self.setMaximumSize(800,500)

        bar=self.menuBar()
        bar.setFont(QFont("Regular",22))

        file=bar.addMenu("File")
        file.setFont(QFont("Regular",22))

        new=QAction("New",self)
        new.triggered.connect(lambda: self.New("new"))

        open=QAction("Open",self)
        open.triggered.connect(lambda:self.New("open"))

        save=QAction("Save",self)
        save.triggered.connect(lambda:self.New("Save"))
        file.addAction(new)
        file.addAction(open)
        file.addAction(save)

        self.msg = QMessageBox(self)




    def New(self,k):
        self.msg.setGeometry(10,10,200,400)
        self.msg.setInformativeText(f"{k}")
        self.msg.setFont(QFont("Regular",25))
        self.msg.exec_()








app = QApplication(sys.argv)
cal = fayl1()
cal.show()
sys.exit(app.exec_())






