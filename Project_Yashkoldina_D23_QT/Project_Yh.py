import sys
import sqlite3
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class First(QMainWindow):  # Класс для главного окна
    def __init__(self):
        super().__init__()
        self.setGeometry(750, 500, 750, 500)
        self.setFixedSize(750, 500)
        self.setWindowTitle('Подбор фильмов')
        self.setStyleSheet("background-color: rgb(221, 245, 255);")

        self.label1 = QLabel("Подбор фильмов", self)
        self.label1.resize(521, 111)
        self.label1.move(110, 80)
        self.label1.setFont(QFont('Monotype Corsiva', 50))

        self.btntwo = QPushButton('Лучшие фильмы 2023', self)
        self.btntwo.resize(331, 111)
        self.btntwo.move(390, 240)
        self.btntwo.setFont(QFont('Monotype Corsiva', 17))
        self.btntwo.setStyleSheet("background-color: rgb(99, 219, 255);")
        self.btntwo.clicked.connect(self.films)

        self.btnnastr = QPushButton('По эмоциям и жанру', self)
        self.btnnastr.resize(331, 111)
        self.btnnastr.move(30, 240)
        self.btnnastr.setFont(QFont('Monotype Corsiva', 17))
        self.btnnastr.setStyleSheet("background-color: rgb(99, 219, 255);")
        self.btnnastr.clicked.connect(self.vib)

    def films(self):
        self.f = Twoo()
        self.f.show()
        self.close()

    def vib(self):
        self.f = Nastr()
        self.f.show()
        self.close()


class Nastr(QMainWindow):  # Класс для окна 1
    def __init__(self):
        super().__init__()
        self.setGeometry(800, 600, 800, 600)
        self.setFixedSize(800, 600)
        self.setWindowTitle('Подбор фильмов_1')
        self.setStyleSheet("background-color: rgb(221, 245, 255);")

        self.Vibemoz = QLabel("Выберите эмоции", self)
        self.Vibemoz.resize(420, 50)
        self.Vibemoz.move(10, 20)
        self.Vibemoz.setFont(QFont('Monotype Corsiva', 30))

        self.Vibemoz = QLabel("Выберите жанр", self)
        self.Vibemoz.resize(310, 60)
        self.Vibemoz.move(450, 10)
        self.Vibemoz.setFont(QFont('Monotype Corsiva', 30))

        self.vemoz1 = QComboBox(self)
        self.vemoz1.addItems(["Печаль", "Волнение", "Агрессия", "Смелость", "Интерес", "Удивление", "Страх", "Любовь",
                              "Счастье"])
        self.vemoz1.resize(260, 50)
        self.vemoz1.move(10, 100)
        self.vemoz1.setStyleSheet("background-color: rgb(224, 235, 255);")

        self.vemoz2 = QComboBox(self)
        self.vemoz2.addItems(["Печаль", "Волнение", "Агрессия", "Смелость", "Интерес", "Удивление", "Страх", "Любовь",
                              "Счастье"])
        self.vemoz2.resize(260, 50)
        self.vemoz2.move(10, 170)
        self.vemoz2.setStyleSheet("background-color: rgb(224, 235, 255);")

        self.vemoz3 = QComboBox(self)
        self.vemoz3.addItems(["Печаль", "Волнение", "Агрессия", "Смелость", "Интерес", "Удивление", "Страх", "Любовь",
                              "Счастье"])
        self.vemoz3.resize(260, 50)
        self.vemoz3.move(10, 240)
        self.vemoz3.setStyleSheet("background-color: rgb(224, 235, 255);")

        self.vzanr = QComboBox(self)
        self.vzanr.addItems(["Комедия", "Драма", "Детектив", "Документальный", "Ужасы",
                             "Фантастика", "Анимация", "Биография", "Боевик", "Приключения", "Семейный",
                             "Триллер", "Фэнтези", "Мистика", "Короткометражный", "Исторический"])
        self.vzanr.resize(260, 50)
        self.vzanr.move(460, 100)
        self.vzanr.setStyleSheet("background-color: rgb(224, 235, 255);")

        self.pbe = QPushButton("Подобрать", self)
        self.pbe.resize(140, 50)
        self.pbe.move(630, 200)
        self.pbe.setFont(QFont('Monotype Corsiva', 15))
        self.pbe.setStyleSheet("background-color: rgb(184, 248, 255);")
        self.pbe.clicked.connect(self.poisN)

        self.label2 = QLabel("Человек паук, Джон Уик 4, Мстители 3", self)
        self.label2.resize(1000, 200)
        self.label2.move(10, 350)
        self.label2.setFont(QFont('Monotype Corsiva', 15))

        self.Exitzanr = QPushButton("Вернуться на главную страницу", self)
        self.Exitzanr.resize(210, 40)
        self.Exitzanr.move(570, 530)
        self.Exitzanr.setFont(QFont('Monotype Corsiva', 9))
        self.Exitzanr.setStyleSheet("background-color: rgb(255, 220, 220);")
        self.Exitzanr.clicked.connect(self.glawn1)

    def poisN(self):  # Поиск по таблице перых 3-5 подходящих фильмов(1)
        self.em1 = self.vemoz1.currentText()
        self.em2 = self.vemoz2.currentText()
        self.em3 = self.vemoz3.currentText()
        self.zan = self.vzanr.currentText()
        print(self.em1, self.em2, self.em3, self.zan)
        self.connection = sqlite3.connect("Pr.db")
        cur = self.connection.cursor()
        res = cur.execute(f"""
        SELECT name FROM films
        JOIN emozi ON films.em_id = emozi.id
        JOIN zanrs ON films.za_id = zanrs.id
        WHERE emozi.em = '{self.em1}' or emozi.em = '{self.em2}' or emozi.em = '{self.em3}' AND zanrs.za = 
        '{self.zan}'""").fetchall()
        print(res, "+")
        self.r = "\n".join([x[0] for x in res])
        self.label2.setText(self.r)
        self.connection.close()

    def glawn1(self):  # Возвращение на главную
        self.f = First()
        self.f.show()
        self.close()

    def reg(self):
        self.f = Registr()
        self.f.show()
        self.close()


class Registr(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 400, 400, 400)
        self.setFixedSize(400, 400)
        self.setWindowTitle('Вход')
        self.setStyleSheet("background-color: rgb(221, 245, 255);")

    def vvod(self):
        ...


class Twoo(QMainWindow):  # Класс для окна 2
    def __init__(self):
        super().__init__()
        self.setGeometry(1800, 900, 1800, 900)
        self.setFixedSize(1800, 900)
        self.setWindowTitle('Подбор фильмов_2')
        self.setStyleSheet("background-color: rgb(221, 245, 255);")

        self.Exittwo = QPushButton("Вернуться на главную страницу", self)  # Возвращение на гравное окно
        self.Exittwo.resize(210, 40)
        self.Exittwo.move(1585, 855)
        self.Exittwo.setFont(QFont('Monotype Corsiva', 9))
        self.Exittwo.setStyleSheet("background-color: rgb(255, 220, 220);")
        self.Exittwo.clicked.connect(self.gla)

        f = open("filmss.txt", encoding="utf-8")
        d = [x.rstrip() for x in f.readlines()]  # Фильмы и оценки
        self.fi1 = QLabel("", self)
        self.fi1.setPixmap(QtGui.QPixmap("Джон_Уик_4350.jpg"))
        self.fi1.resize(400, 400)
        self.fi1.move(15, -20)
        self.DV = QLabel(d[0], self)
        self.DV.resize(300, 40)
        self.DV.move(15, 360)
        self.DV.setFont(QFont('Microsoft YaHei Ui', 15))

        self.DV1 = QLabel("4,6", self)
        self.DV1.resize(50, 50)
        self.DV1.move(280, 275)
        self.DV1.setFont(QFont('Forte', 20))

        self.fi2 = QLabel("", self)
        self.fi2.setPixmap(QtGui.QPixmap("Баба_Яга350.jpg"))
        self.fi2.resize(400, 400)
        self.fi2.move(355, -20)
        self.BY = QLabel(d[1], self)
        self.BY.resize(300, 40)
        self.BY.move(355, 360)
        self.BY.setFont(QFont('Microsoft YaHei Ui', 15))

        self.BY1 = QLabel("4,3", self)
        self.BY1.resize(50, 50)
        self.BY1.move(625, 275)
        self.BY1.setFont(QFont('Forte', 20))

        self.fi3 = QLabel("", self)
        self.fi3.setPixmap(QtGui.QPixmap("Вызов350.jpg"))
        self.fi3.resize(400, 400)
        self.fi3.move(705, -20)
        self.V = QLabel(d[2], self)
        self.V.resize(300, 40)
        self.V.move(705, 360)
        self.V.setFont(QFont('Microsoft YaHei Ui', 15))

        self.V1 = QLabel("4,6", self)
        self.V1.resize(50, 50)
        self.V1.move(975, 275)
        self.V1.setFont(QFont('Forte', 20))

        self.fi4 = QLabel("", self)
        self.fi4.setPixmap(QtGui.QPixmap("Гром350.jpg"))
        self.fi4.resize(400, 400)
        self.fi4.move(1055, -20)
        self.GR = QLabel(d[3], self)
        self.GR.resize(300, 40)
        self.GR.move(1055, 360)
        self.GR.setFont(QFont('Microsoft YaHei Ui', 15))

        self.GR1 = QLabel("4,3", self)
        self.GR1.resize(50, 50)
        self.GR1.move(1315, 275)
        self.GR1.setFont(QFont('Forte', 20))

        self.fi5 = QLabel("", self)
        self.fi5.setPixmap(QtGui.QPixmap("Стражи_Галактики_3350.jpg"))
        self.fi5.resize(400, 400)
        self.fi5.move(1405, -20)
        self.CT = QLabel(d[4], self)
        self.CT.resize(400, 40)
        self.CT.move(1405, 360)
        self.CT.setFont(QFont('Microsoft YaHei Ui', 15))

        self.CT1 = QLabel("4,9", self)
        self.CT1.resize(50, 50)
        self.CT1.move(1710, 275)
        self.CT1.setFont(QFont('Forte', 20))

        self.fi6 = QLabel("", self)
        self.fi6.setPixmap(QtGui.QPixmap("Три_мушкетёра350.jpg"))
        self.fi6.resize(400, 400)
        self.fi6.move(15, 430)
        self.TM = QLabel(d[5], self)
        self.TM.resize(350, 40)
        self.TM.move(8, 810)
        self.TM.setFont(QFont('Microsoft YaHei Ui', 13))

        self.TM1 = QLabel("4,2", self)
        self.TM1.resize(50, 50)
        self.TM1.move(280, 737)
        self.TM1.setFont(QFont('Forte', 20))

        self.fi7 = QLabel("", self)
        self.fi7.setPixmap(QtGui.QPixmap("Снегирь350.jpg"))
        self.fi7.resize(400, 400)
        self.fi7.move(355, 430)
        self.CN = QLabel(d[6], self)
        self.CN.resize(300, 40)
        self.CN.move(355, 810)
        self.CN.setFont(QFont('Microsoft YaHei Ui', 15))

        self.BY1 = QLabel("4,3", self)
        self.BY1.resize(50, 50)
        self.BY1.move(625, 737)
        self.BY1.setFont(QFont('Forte', 20))

        self.fi8 = QLabel("", self)
        self.fi8.setPixmap(QtGui.QPixmap("Человек_паук_паутина_вселенных350.jpg"))
        self.fi8.resize(400, 400)
        self.fi8.move(705, 430)
        self.CHP = QLabel(d[7], self)
        self.CHP.resize(400, 40)
        self.CHP.move(660, 810)
        self.CHP.setFont(QFont('Microsoft YaHei Ui', 13))

        self.CHP1 = QLabel("4,8", self)
        self.CHP1.resize(50, 50)
        self.CHP1.move(975, 737)
        self.CHP1.setFont(QFont('Forte', 20))

        self.fi9 = QLabel("", self)
        self.fi9.setPixmap(QtGui.QPixmap("Яга_и_книга_заклинаний350.jpg"))
        self.fi9.resize(400, 400)
        self.fi9.move(1055, 430)
        self.YZ = QLabel(d[8], self)
        self.YZ.resize(300, 40)
        self.YZ.move(1055, 810)
        self.YZ.setFont(QFont('Microsoft YaHei Ui', 15))

        self.YZ1 = QLabel("4,6", self)
        self.YZ1.resize(50, 50)
        self.YZ1.move(1325, 737)
        self.YZ1.setFont(QFont('Forte', 20))

        self.fi10 = QLabel("", self)
        self.fi10.setPixmap(QtGui.QPixmap("Кунг_Фу350.jpg"))
        self.fi10.resize(400, 400)
        self.fi10.move(1405, 430)
        self.KF = QLabel(d[9], self)
        self.KF.resize(300, 40)
        self.KF.move(1405, 810)
        self.KF.setFont(QFont('Microsoft YaHei Ui', 15))

        self.KF1 = QLabel("4,7", self)
        self.KF1.resize(50, 50)
        self.KF1.move(1715, 737)
        self.KF1.setFont(QFont('Forte', 20))

        f.close()

        # Звёзды оценки
        self.z1_1 = QLabel("", self)
        self.z1_1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z1_1.resize(50, 54)
        self.z1_1.move(270, 5)

        self.z1_2 = QLabel("", self)
        self.z1_2.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z1_2.resize(50, 54)
        self.z1_2.move(270, 60)

        self.z1_3 = QLabel("", self)
        self.z1_3.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z1_3.resize(50, 54)
        self.z1_3.move(270, 110)

        self.z1_4 = QLabel("", self)
        self.z1_4.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z1_4.resize(50, 54)
        self.z1_4.move(270, 160)

        self.z1_5 = QLabel("", self)
        self.z1_5.setPixmap(QtGui.QPixmap("Звезда05.png"))
        self.z1_5.resize(50, 54)
        self.z1_5.move(270, 210)

        self.z2_1 = QLabel("", self)
        self.z2_1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z2_1.resize(50, 54)
        self.z2_1.move(620, 5)

        self.z7 = QLabel("", self)
        self.z7.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z7.resize(50, 54)
        self.z7.move(620, 60)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z1.resize(50, 54)
        self.z1.move(620, 110)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z1.resize(50, 54)
        self.z1.move(620, 160)

        self.z7 = QLabel("", self)
        self.z7.setPixmap(QtGui.QPixmap("ЗвездаС.png"))
        self.z7.resize(55, 55)
        self.z7.move(615, 210)

        self.z3_1 = QLabel("", self)
        self.z3_1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z3_1.resize(50, 54)
        self.z3_1.move(965, 5)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z1.resize(50, 54)
        self.z1.move(965, 60)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z1.resize(50, 54)
        self.z1.move(965, 110)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z1.resize(50, 54)
        self.z1.move(965, 160)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("Звезда05.png"))
        self.z1.resize(50, 54)
        self.z1.move(965, 210)

        self.z4_1 = QLabel("", self)
        self.z4_1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z4_1.resize(50, 54)
        self.z4_1.move(1305, 5)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z1.resize(50, 54)
        self.z1.move(1305, 60)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z1.resize(50, 54)
        self.z1.move(1305, 110)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z1.resize(50, 54)
        self.z1.move(1305, 160)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("ЗвездаС.png"))
        self.z1.resize(60, 60)
        self.z1.move(1300, 210)

        self.z5_1 = QLabel("", self)
        self.z5_1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z5_1.resize(50, 54)
        self.z5_1.move(1700, 5)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z1.resize(50, 54)
        self.z1.move(1700, 60)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z1.resize(50, 54)
        self.z1.move(1700, 110)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z1.resize(50, 54)
        self.z1.move(1700, 160)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z1.resize(50, 54)
        self.z1.move(1700, 210)

        self.z6_1 = QLabel("", self)
        self.z6_1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z6_1.resize(50, 54)
        self.z6_1.move(275, 455)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z1.resize(50, 54)
        self.z1.move(275, 510)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z1.resize(50, 54)
        self.z1.move(275, 565)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z1.resize(50, 54)
        self.z1.move(275, 620)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("ЗвездаС.png"))
        self.z1.resize(60, 60)
        self.z1.move(270, 675)

        self.z7_1 = QLabel("", self)
        self.z7_1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z7_1.resize(50, 54)
        self.z7_1.move(620, 455)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z1.resize(50, 54)
        self.z1.move(620, 510)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z1.resize(50, 54)
        self.z1.move(620, 565)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z1.resize(50, 54)
        self.z1.move(620, 620)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("ЗвездаС.png"))
        self.z1.resize(60, 60)
        self.z1.move(615, 675)

        self.z8_1 = QLabel("", self)
        self.z8_1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z8_1.resize(50, 54)
        self.z8_1.move(970, 455)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z1.resize(50, 54)
        self.z1.move(970, 510)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z1.resize(50, 54)
        self.z1.move(970, 565)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z1.resize(50, 54)
        self.z1.move(970, 620)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("Звезда05.png"))
        self.z1.resize(50, 54)
        self.z1.move(970, 675)

        self.z9_1 = QLabel("", self)
        self.z9_1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z9_1.resize(50, 54)
        self.z9_1.move(1317, 455)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z1.resize(50, 54)
        self.z1.move(1317, 510)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z1.resize(50, 54)
        self.z1.move(1317, 565)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z1.resize(50, 54)
        self.z1.move(1317, 620)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("Звезда05.png"))
        self.z1.resize(50, 54)
        self.z1.move(1317, 675)

        self.z10_1 = QLabel("", self)
        self.z10_1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z10_1.resize(50, 54)
        self.z10_1.move(1707, 455)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z1.resize(50, 54)
        self.z1.move(1707, 510)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z1.resize(50, 54)
        self.z1.move(1707, 565)

        self.z1 = QLabel("", self)
        self.z1.setPixmap(QtGui.QPixmap("Звезда1.png"))
        self.z1.resize(50, 54)
        self.z1.move(1707, 620)

        self.z50 = QLabel("", self)
        self.z50.setPixmap(QtGui.QPixmap("Звезда05.png"))
        self.z50.resize(50, 54)
        self.z50.move(1707, 675)

    def gla(self):  # Возвращение на главную
        self.f = First()
        self.f.show()
        self.close()


if __name__ == '__main__':  # Выход
    app = QApplication(sys.argv)
    ex = First()
    ex.show()
    sys.exit(app.exec_())
