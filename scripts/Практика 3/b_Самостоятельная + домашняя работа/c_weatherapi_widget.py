"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатие на кнопку
"""
from PySide2 import QtCore, QtWidgets
from ui.weather import Ui_Form
from a_threads import WeatherHandler


class QThreadWeater(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.lineEdit.setText("30.0")
        self.ui.lineEdit_2.setText("30.0")

        self.systemInfoThread = None

        self.initThreads()
        self.initSignals()

    def initThreads(self):
        if self.systemInfoThread is not None:
            self.systemInfoThread.close()
        self.systemInfoThread = WeatherHandler(lat=float(self.ui.lineEdit_2.text()),
                                               lon=float(self.ui.lineEdit.text()))
        self.systemInfoThread.dataResp.connect(self.systemInfoThreadWeatherSignal)
        self.systemInfoThread.start()

    def initSignals(self):
        self.ui.spinBox.valueChanged.connect(self.setSystemInfoDelay)
        self.ui.lineEdit.textChanged.connect(self.initThreads)
        self.ui.lineEdit_2.textChanged.connect(self.initThreads)

    def systemInfoThreadWeatherSignal(self, info_str) -> None:
        """
        Слот для обработки сигнала systemSignal, который шлёт данные из потока self.systemInfo

        :param info_list: значение полученное из потока self.systemInfo
        :return: None
        """
        print(info_str)
        self.ui.label_out.setText(info_str)

    def setSystemInfoDelay(self) -> None:
        """
        Слот для установки значения времени задержки обновления системных параметров

        :return: None
        """

        self.systemInfoThread.setDelay(self.ui.spinBox.value())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = QThreadWeater()
    myapp.show()

    app.exec_()

# """
# Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads
#
# Создавать форму можно как в ручную, так и с помощью программы Designer
#
# Форма должна содержать:
# 1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
# 2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
# 3. поле для вывода информации о погоде в указанных координатах
# 4. поток необходимо запускать и останавливать при нажатие на кнопку
# """
