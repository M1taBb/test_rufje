# напиши здесь код третьего экрана приложения
from instr import *
from second_win import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout, QPushButton, QLabel, QApplication, QLineEdit

class FinalWin(QWidget):
    def __init__(self, index_int, age):
        super().__init__()
        self.age = age
        self.index_int = index_int
        self.set_appear(name_pr, widht, height, x, y)
        self.initUI(work_1)
        self.show()

    #Метод переименования окна и указание его размеров и координат
    def set_appear(self, name_pr, widht, height, x, y):
        self.setWindowTitle(name_pr)
        self.resize(widht,height)
        self.move(x,y)

    def initUI(self, work_1):
        stran = 'Индекс Руфье: ' + str(self.index_int)
        #Индекс Руфье см. Экран 3 (верхняя строка)
        self.text1 = QLabel(stran)
        self.text2 = QLabel(work_1)

        self.line = QVBoxLayout()

        self.line.addWidget(self.text1, alignment = Qt.AlignCenter)
        self.line.addWidget(self.text2, alignment = Qt.AlignCenter)
        self.plus()
        
        self.setLayout(self.line)

    def plus(self):   
    
        if self.age >= 7 and self.age <= 8:
            if self.index_int >= 21:
                self.text2.setText(work_1)
            elif self.index_int >= 17 and self.index_int <= 20.9:
                self.text2.setText(work_2)
            elif self.index_int >= 12 and self.index_int <= 16.9:
                self.text2.setText(work_3)
            elif self.index_int >= 6.5 and self.index_int <= 11.9:
                self.text2.setText(work_4)
            elif self.index_int <= 6.4:
                self.text2.setText(work_5)

        elif self.age >= 9 and self.age <= 10:
            if self.index_int >= 19.5:
                self.text2.setText(work_1)
            elif self.index_int >= 15.5 and self.index_int <= 19.4:
                self.text2.setText(work_2)
            elif self.index_int >= 10.5 and self.index_int <= 15.4:
                self.text2.setText(work_3)
            elif self.index_int >= 5 and self.index_int <= 10.4:
                self.text2.setText(work_4)
            elif self.index_int <= 4.9:
                self.text2.setText(work_5)
    
        elif self.age >= 11 and self.age <= 12:
            if self.index_int >= 18:
                self.text2.setText(work_1)
            elif self.index_int >= 14 and self.index_int <= 17.9:
                self.text2.setText(work_2)
            elif self.index_int >= 9 and self.index_int <= 13.9:
                self.text2.setText(work_3)
            elif self.index_int >= 3.5 and self.index_int <= 8.9:
                self.text2.setText(work_4)
            elif self.index_int <= 3.4:
                self.text2.setText(work_5)
    
        elif self.age >= 13 and self.age <= 14:
            if self.index_int >= 16.5:
                self.text2.setText(work_1)
            elif self.index_int >= 12.5 and self.index_int <= 16.4:
                self.text2.setText(work_2)
            elif self.index_int >= 7.5 and self.index_int <= 12.4:
                self.text2.setText(work_3)
            elif self.index_int >= 2 and self.index_int <= 7.4:
                self.text2.setText(work_4)
            elif self.index_int <= 1.9:
                self.text2.setText(work_5)
    
        elif self.age >= 15:
            if self.index_int >= 15:
                self.text2.setText(work_1)
            elif self.index_int >= 11 and self.index_int <= 14.9:
                self.text2.setText(work_2)
            elif self.index_int >= 6 and self.index_int <= 10.9:
                self.text2.setText(work_3)
            elif self.index_int >= 0.5 and self.index_int <= 5.9:
                self.text2.setText(work_4)
            elif self.index_int <= 0.4:
                self.text2.setText(work_5)