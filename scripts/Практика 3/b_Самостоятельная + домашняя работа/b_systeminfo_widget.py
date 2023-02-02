"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""

import time
import psutil

from PySide2 import QtCore, QtWidgets
from ui.cpu import Ui_Form
from a_threads import SystemInfo

class QThreadPractice(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.systemInfoThread = None

        self.initThreads()
        self.initSignals()

    def initThreads(self):

        self.systemInfoThread = SystemInfo()
        self.systemInfoThread.systemInfoReceived.connect(self.systemInfoThreadSystemSignal)
        self.systemInfoThread.start()

    def initSignals(self):

        self.ui.spinBoxSystemInfoDelay.valueChanged.connect(self.setSystemInfoDelay)

    def systemInfoThreadSystemSignal(self, info_list) -> None:
        """
        Слот для обработки сигнала systemSignal, который шлёт данные из потока self.systemInfo

        :param info_list: значение полученное из потока self.systemInfo
        :return: None
        """

        self.ui.progressBarCPU.setValue(info_list[0])
        self.ui.labelCPUPercent.setText(f"{info_list[0]} %")
        self.ui.progressBarRAM.setValue(info_list[1].percent)
        self.ui.labelRAMPercent.setText(f"{info_list[1].percent} %")

    def setSystemInfoDelay(self) -> None:
        """
        Слот для установки значения времени задержки обновления системных параметров

        :return: None
        """

        self.systemInfoThread.delay = self.ui.spinBoxSystemInfoDelay.value()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = QThreadPractice()
    myapp.show()

    app.exec_()

# """
# Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads
#
# Создавать форму можно как в ручную, так и с помощью программы Designer
#
# Форма должна содержать:
# 1. поле для ввода времени задержки
# 2. поле для вывода информации о загрузке CPU
# 3. поле для вывода информации о загрузке RAM
# 4. поток необходимо запускать сразу при старте приложения
# 5. установку времени задержки сделать "горячей", т.е. поток должен сразу
# реагировать на изменение времени задержки
# """
