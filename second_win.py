# напиши здесь код для второго экрана приложения
from instr import *
from final_win import *
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout, QPushButton, QLabel, QApplication, QLineEdit

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.final_time = 0
        self.initUI(surname, age, instruction, text_start, instruction_2, Pris_start, instruction_3, final_start, message)
        self.set_appear()
        self.connects()
        self.show()

    #Метод переименования окна и указание его размеров и координат
    def set_appear(self):
        self.setWindowTitle(name_pr)
        self.resize(widht,height)
        self.move(x,y)

    def time_tick(self):
        self.time_1 = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.time_1_event)
        self.timer.start(1000)
        self.text_timer.setFont(QFont('Times',36 , QFont.Bold))
        self.text_timer.setStyleSheet('color: rgb(0,0,0)')

    def time_1_event(self):
        self.time_1 = self.time_1.addSecs(-1)
        self.text_timer.setText(self.time_1.toString('hh:mm:ss'))
        if self.time_1.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def second_timer(self):
        self.time_1 = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.time_2_event)
        self.timer.start(1500)
        self.text_timer.setFont(QFont('Times',36 , QFont.Bold))
        self.text_timer.setStyleSheet('color: rgb(0,0,0)')

    def time_2_event(self):
        self.time_1 = self.time_1.addSecs(-1)
        self.text_timer.setText(self.time_1.toString('hh:mm:ss')[6:8])
        if self.time_1.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def final_timer(self):
        self.time_1 = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.time_3_event)
        self.timer.start(1000)
        self.text_timer.setFont(QFont('Times',36 , QFont.Bold))

    def time_3_event(self):
        self.time_1 = self.time_1.addSecs(-1)
        self.text_timer.setText(self.time_1.toString('hh:mm:ss'))
        if self.time_1.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
        if int((self.time_1.toString('hh:mm:ss')[6:8])) >= 45:
            self.text_timer.setStyleSheet('color: rgb(0,255,0)')
        elif int((self.time_1.toString('hh:mm:ss')[6:8])) <= 15:
            self.text_timer.setStyleSheet('color: rgb(0,255,0)')
        else:
            self.text_timer.setStyleSheet('color: rgb(0,0,0)')

    #Метод создания и отрисовки всех элементов этого Экрана (2)
    def initUI(self, surname, age, instruction, text_start, instruction_2, Pris_start, instruction_3, final_start, message):

        #Фамилия и поле для неё
        self.text_1 = QLabel(surname)
        self.strok = QLineEdit()

        #Возраст и поле для него
        self.text_2 = QLabel(age)
        self.strok_2 = QLineEdit()

        #Инструкция к тесту, кнопка для его начала и поле для заполнения
        self.text_3 = QLabel(instruction)
        self.button_start_1 = QPushButton(text_start)
        self.strok_3 = QLineEdit()

        #Инструкция к приседаниям и кнопка для начала этого теста
        self.text_4 = QLabel(instruction_2)
        self.button_start_2 = QPushButton(Pris_start)

        #Инструкция к финальному тесту и кнопка для его начала
        self.text_5 = QLabel(instruction_3)
        self.button_start_3 = QPushButton(final_start)

        #Пустые поля для ввода результатов финального теста
        self.strok_4 = QLineEdit()
        self.strok_5 = QLineEdit()

        #Кнопка для отправки результатов внизу второго экрана
        self.button_final = QPushButton(message)

        self.text_timer = QLabel('')

        #Создание 1-й горизонтальной линии и 2-х вертикальных
        self.HLine = QHBoxLayout()
        self.L_VLine = QVBoxLayout()
        self.R_VLine = QVBoxLayout()

        #Добавление "Фамилия и поле для неё" на левую вертикальную линию
        self.L_VLine.addWidget(self.text_1, alignment = Qt.AlignLeft)
        self.L_VLine.addWidget(self.strok, alignment = Qt.AlignLeft)

        #Добавление "Возраст и поле для него" на левую вертикальную линию
        self.L_VLine.addWidget(self.text_2, alignment = Qt.AlignLeft)
        self.L_VLine.addWidget(self.strok_2, alignment = Qt.AlignLeft)

        self.R_VLine.addWidget(self.text_timer, alignment = Qt.AlignCenter)

        #Добавление "Инструкция к тесту, кнопка для его начала и поле для заполнения" на левую вертикальную линию
        self.L_VLine.addWidget(self.text_3, alignment = Qt.AlignLeft)
        self.L_VLine.addWidget(self.button_start_1, alignment = Qt.AlignLeft)
        self.L_VLine.addWidget(self.strok_3, alignment = Qt.AlignLeft)

        #Добавление "Инструкция к приседаниям и кнопка для начала этого теста" на левую вертикальную линию
        self.L_VLine.addWidget(self.text_4, alignment = Qt.AlignLeft)
        self.L_VLine.addWidget(self.button_start_2, alignment = Qt.AlignLeft)

        #Добавление "Инструкция к финальному тесту и кнопка для его начала" на левую вертикальную линию
        self.L_VLine.addWidget(self.text_5, alignment = Qt.AlignLeft)
        self.L_VLine.addWidget(self.button_start_3, alignment = Qt.AlignLeft)

        #Добавление "Пустые поля для ввода результатов финального теста" на левую вертикальную линию
        self.L_VLine.addWidget(self.strok_4, alignment = Qt.AlignLeft)
        self.L_VLine.addWidget(self.strok_5, alignment = Qt.AlignLeft)

        #Добавление "Кнопка для отправки результатов внизу второго экрана" на левую вертикальную линию
        self.L_VLine.addWidget(self.button_final, alignment = Qt.AlignCenter)

        #Добавление Левой и Правой вертикальных линий на горизонтальную центральную линию
        self.HLine.addLayout(self.L_VLine)
        self.HLine.addLayout(self.R_VLine)
        self.setLayout(self.HLine)

    def new_info(self):
        self.result_1 = int(self.strok_3.text())
        self.result_2 = int(self.strok_4.text())
        self.result_3 = int(self.strok_5.text())
        self.vozrast = int(self.strok_2.text())

        self.index_int = (4 * (self.result_1 + self.result_2 + self.result_3) - 200) / 10

    def connects(self):
        self.button_final.clicked.connect(self.new_info)
        self.button_final.clicked.connect(self.next_click)
        self.button_start_1.clicked.connect(self.time_tick)
        self.button_start_2.clicked.connect(self.second_timer)
        self.button_start_3.clicked.connect(self.final_timer)

    def next_click(self):
        self.hide()
        self.tw = FinalWin(self.index_int, self.vozrast)