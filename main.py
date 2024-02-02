from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
import sys
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import requests


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.image_path = "data/image.png"

    def initUI(self):
        uic.loadUi("main.ui", self)
        self.search_but.clicked.connect(self.search_click)

    def search_click(self):
        self.get_image()
        pixmap = QPixmap(self.image_path)
        self.label.setPixmap(pixmap)

    def get_image(self):
        geocode = self.line_edit.text()
        api_server = "http://static-maps.yandex.ru/1.x/"
        params = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "geocode": geocode,
            "z": 10,
            "size": (651, 581),
            "l": "map"
        }

        response = requests.get(api_server, params=params)

        with open(self.image_path, "wb") as file:
            file.write(response.content)

    def KeyPressEvent(self, event):
        print(event)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
