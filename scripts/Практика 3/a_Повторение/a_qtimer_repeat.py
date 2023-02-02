"""
Файл для повторения темы QTimer

Напомнить про работу с QTimer.

Предлагается создать приложение-которое будет
с некоторой периодичностью вызывать определённую функцию.
"""

from PySide6 import QtWidgets, QtCore
import time


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.gen = None
        self.initUi()
        self.initTimers(1000)
        self.initSignals()

    def initUi(self):
        # self.b1 = QtWidgets.QPushButton("Нажми")
        self.b2 = QtWidgets.QPushButton("Очистить")
        self.text = QtWidgets.QLineEdit()
        self.text_p = QtWidgets.QPlainTextEdit()
        self.spin_b = QtWidgets.QSpinBox()
        self.spin_b.setValue(10)
        hor_layout = QtWidgets.QHBoxLayout()
        hor_layout.addWidget(self.text)
        # hor_layout.addWidget(self.b1)
        hor_layout.addWidget(self.b2)
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(hor_layout)
        main_layout.addWidget(self.spin_b)
        main_layout.addWidget(self.text_p)

        self.setLayout(main_layout)

    def initTimers(self, param):

        self.timer = QtCore.QTimer()
        self.timer.setInterval(param)
        self.timer.start()

    def initSignals(self):

        self.b2.clicked.connect(self.text_p.clear)
        # self.b1.clicked.connect(self.startGen)
        self.spin_b.textChanged.connect(self.setTimer)
        self.timer.timeout.connect(self.setTextEdit)

    @QtCore.Slot()
    def setTimer(self):
        data_spin = int(self.spin_b.text())
        self.timer.setInterval((data_spin + 1) * 100)

    # def startGen(self):
    #     self.gen = (val for val in self.text.text())
    #
    @QtCore.Slot()
    def setTextEdit(self):
        data = self.text.text()
        if len(data) > 1:
            self.text_p.appendPlainText(data[0])
            self.text.setText(data[1:])
        elif len(data) == 1:
            self.text_p.appendPlainText(data)
            self.text.clear()

        # try:
        #     self.text_p.appendPlainText(next(self.gen))
        # except (StopIteration, TypeError):
        #     self.text_p.appendPlainText("except")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()


# """
# Файл для повторения темы QTimer
#
# Напомнить про работу с QTimer.
#
# Предлагается создать приложение-которое будет
# с некоторой периодичностью вызывать определённую функцию.
# """
#
# from PySide6 import QtWidgets
#
#
# class Window(QtWidgets.QWidget):
#
#     def __init__(self, parent=None):
#         super().__init__(parent)
#
#
# if __name__ == "__main__":
#     app = QtWidgets.QApplication()
#
#     window = Window()
#     window.show()
#
#     app.exec()