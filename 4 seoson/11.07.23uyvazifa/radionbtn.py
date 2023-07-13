import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class test(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(600, 600)
        self.setMaximumSize(600, 600)
        self.window = QWidget(self)
        self.mainLayout = QVBoxLayout()
        data = {
            "1. Savol sf asd": [
                "1-1",
                "1-2",
                "1-3"
            ],
            "2. TEEdsaaf ": [
                "2-1",
                "2-2"
            ],
            "3. sadsad": [
                "3-1",
                "3-2"
            ],
            "4. asdasd": [
                "4-1",
                "4-2"
            ],
            "5. asdasdasd": [
                "5-1",
                "5-2"
            ]
        }
        self.trueAnswer = {
            1: "1-2",
            2: "2-1",
            3: "3-1",
            4: "4-2",
            5: "5-1"
        }
        self.buttonGroups = list()
        self.answer = dict()
        self.initial_tests(data)

        self.window.setLayout(self.mainLayout)
        self.setCentralWidget(self.window)

    def initial_tests(self, data):
        for k, v in data.items():
            testLayout = QVBoxLayout()
            lbl = QLabel(k, self)
            lbl.setFont(QFont("Arial", 13))
            testLayout.addWidget(lbl)

            buttonsLayout = QHBoxLayout()
            rbg = QButtonGroup(self)

            for btn in v:
                lblr = QRadioButton(btn, self)
                rbg.addButton(lblr)
                rbg.setId(lblr, int(k.split(".")[0]))
                buttonsLayout.addWidget(lblr)

            self.buttonGroups.append(rbg)
            rbg.buttonClicked.connect(self.check_buttons)
            if k == list(data.keys())[-1]:
                check_btn = QPushButton("Check", self)
                check_btn.setFont(QFont("Arial", 13))
                check_btn.clicked.connect(self.check_answers)
                buttonsLayout.addWidget(check_btn)
            testLayout.addLayout(buttonsLayout)
            self.mainLayout.addLayout(testLayout)

    def check_buttons(self, btn):
        for b in self.buttonGroups:
            if btn in b.buttons():
                self.answer[b.id(btn)] = btn.text()

        print(self.answer)

    def check_answers(self):
        if len(self.answer) == len(self.trueAnswer):
            count = 0
            for k in self.trueAnswer.keys():
                if self.answer[k] == self.trueAnswer[k]:
                    count += 1

            print(count)
        else:
            print("Select answers")


app = QApplication(sys.argv)
cal = test()
cal.show()
sys.exit(app.exec_())
