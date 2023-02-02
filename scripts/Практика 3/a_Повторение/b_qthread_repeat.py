"""
Файл для повторения темы QThread

Напомнить про работу с QThread.

Предлагается создать небольшое приложение, которое будет с помощью модуля request
получать доступность того или иного сайта (возвращать из потока status_code сайта).

Поработать с сигналами, которые возникают при запуске/остановке потока,
передать данные в поток (в данном случае url),
получить данные из потока (статус код сайта),
попробовать управлять потоком (запуск, остановка).

Опционально поработать с валидацией url
"""

from PySide6 import QtWidgets, QtCore
import requests


class Worker(QtCore.QThread):
    progress = QtCore.Signal(int)
    url = None

    def start(self, *args, url=None, **kwargs) -> None:
        self.url = url
        return super().start(*args, **kwargs)

    def run(self) -> None:
        data = requests.get(self.url)
        self.progress.emit(data.status_code)
        self.finished.emit()


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()
        self.initTreads()
        self.initSignals()

    def initUi(self):
        self.b1 = QtWidgets.QPushButton("Проверить")
        self.b2 = QtWidgets.QPushButton("Очистить")
        self.text = QtWidgets.QLineEdit()
        self.text_p = QtWidgets.QPlainTextEdit()
        hor_layout = QtWidgets.QHBoxLayout()
        hor_layout.addWidget(self.text)
        hor_layout.addWidget(self.b1)
        hor_layout.addWidget(self.b2)
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(hor_layout)
        main_layout.addWidget(self.text_p)
        self.setLayout(main_layout)

    def initTreads(self):
        self.thread = Worker()

    def initSignals(self):
        self.b1.clicked.connect(self.startProcess)
        self.b2.clicked.connect(self.text_p.clear)

        self.thread.progress.connect(self.reportProgress)
        self.thread.finished.connect(lambda: self.b1.setEnabled(True))
        # self.thread.finished.connect(self.thread.quit)

    @QtCore.Slot()
    def startProcess(self):
        self.b1.setEnabled(False)
        self.thread.start(url=self.text.text())

    @QtCore.Slot()
    def reportProgress(self, pr):
        self.text_p.appendPlainText(str(pr))


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()

# """
# Файл для повторения темы QThread
#
# Напомнить про работу с QThread.
#
# Предлагается создать небольшое приложение, которое будет с помощью модуля request
# получать доступность того или иного сайта (возвращать из потока status_code сайта).
#
# Поработать с сигналами, которые возникают при запуске/остановке потока,
# передать данные в поток (в данном случае url),
# получить данные из потока (статус код сайта),
# попробовать управлять потоком (запуск, остановка).
#
# Опционально поработать с валидацией url
# """
#
# from PySide6 import QtWidgets
#
#
# class Window(QtWidgets.QWidget):
#
#     def __init__(self, parent=None):
#         super().__init__(parent)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
