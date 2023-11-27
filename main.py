from random import randint
import sys
from PyQt5 import uic
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyPillow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint)

    def run(self, qp):
        number = randint(1, 250)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(number, number, number, number)

    def paint(self):
        self.update()

    def paintEvent(self, eve):
        qp = QPainter()
        qp.begin(self)
        self.run(qp)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyPillow()
    ex.show()
    sys.exit(app.exec())
