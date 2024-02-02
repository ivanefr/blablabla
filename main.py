from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
import sys
from PyQt5.QtGui import QPixmap
from PyQt5 import uic


class Window(QMainWindow):
    def __init__(self):
        super().init()
        self.initUI()

    def initUI(self):
        uic.loadUi("main.ui", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
