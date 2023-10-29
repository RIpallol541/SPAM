from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QLineEdit, QFileDialog, QLabel
from PyQt5.QtCore import pyqtSlot
import sys
from main import main


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Спамер'
        self.left = 400
        self.top = 400
        self.width = 300
        self.height = 300
        self.setWindowIcon(QIcon("ico.png"))
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Написание дичи
        self.label1 = QLabel("Время задержки от               до                в секундах", self)
        self.label1.move(20, 40)
        self.label1.adjustSize()
        self.label2 = QLabel("Количество задействованных аккаунтов", self)
        self.label2.move(20, 20)
        self.label2.adjustSize()

        # Поле ввода количества аккаунтов
        self.acc = QLineEdit(self)
        self.acc.move(235, 16)
        self.acc.resize(40, 20)

        # Поле ввода задержки слева(от)
        self.response_time_left = QLineEdit(self)
        self.response_time_left.move(120, 36)
        self.response_time_left.resize(40, 20)

        # Поле ввода задержки справа(до)
        self.response_time_right = QLineEdit(self)
        self.response_time_right.move(178, 36)
        self.response_time_right.resize(40, 20)

        # Кнопка привязки файла с сообщениями
        self.message = QPushButton('Выбрать файл с сообщениями', self)
        self.message.setToolTip('Read text')
        self.message.move(52, 70)
        self.message.resize(200, 40)
        self.message.clicked.connect(self.Mes)

        # Кнопка привязки файла с логинами
        self.logn = QPushButton('Выбрать файл с логинами', self)
        self.logn.move(52, 120)
        self.logn.resize(200, 40)
        self.logn.clicked.connect(self.Log)

        # Кнопка старта
        self.flag = True
        self.start = QPushButton('Старт', self)
        self.start.move(52, 170)
        self.start.resize(200, 40)
        self.start.setStyleSheet("background-color: red")
        self.start.clicked.connect(
            lambda: main(self.response_time_left.text(), self.response_time_right.text(), self.mes[0][0],
                         self.log[0][0],
                         self.acc.text()))
        self.show()

    @pyqtSlot()
    def Mes(self):
        self.mes = QFileDialog.getOpenFileNames(self, "Открытие файла с сообщениями", "Desktop", "(*.txt)")

    @pyqtSlot()
    def Log(self):
        self.log = QFileDialog.getOpenFileNames(self, "Открытие файла с логинами", "Desktop", "(*.txt)")
        return None

    @pyqtSlot()
    def Start(self):

        if self.flag:
            self.start.setStyleSheet("background-color: green")
            self.start.setText("Стоп")
            self.flag = False
            self.close()
            main(self.response_time_left.text(), self.response_time_right.text(), self.mes[0][0], self.log[0][0],
                 self.acc.text())


        else:
            self.start.setStyleSheet("background-color: red")
            self.start.setText("Старт")
            self.flag = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
