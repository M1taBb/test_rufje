# напиши здесь код основного приложения и первого экрана
from instr import*
from second_win import *
from final_win import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QApplication

class MainWin(QWidget):
    def __init__(self,name_pr, widht, height, x, y, rep_1, about_it, start):
        super().__init__()
        self.set_appear(name_pr, widht, height, x, y)
        self.initUI(rep_1, about_it, start)
        self.connects()
        self.show()

    def set_appear(self, name_pr, widht, height, x, y):
        self.setWindowTitle(name_pr)
        self.resize(widht,height)
        self.move(x,y)

    def initUI(self, rep_1, about_it, start):
        self.text_1 = QLabel(rep_1)
        self.text_2 = QLabel(about_it)

        self.button = QPushButton(start)

        self.VLine = QVBoxLayout()

        self.VLine.addWidget(self.text_1, alignment = Qt.AlignLeft)
        self.VLine.addWidget(self.text_2, alignment = Qt.AlignLeft)
        self.VLine.addWidget(self.button, alignment = Qt.AlignCenter)
        self.setLayout(self.VLine)

    def connects(self):
        self.button.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.tw = TestWin()

Main = QApplication([])
Main_go = MainWin(name_pr, widht, height, x, y, rep_1, about_it, start)

Main.exec_()