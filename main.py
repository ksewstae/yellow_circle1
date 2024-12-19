import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from random import randint


class YellowCircle(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.do_paint = False
        self.paint_btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        radius = randint(0, 300)
        qp.drawEllipse(randint(0, 600 - radius), randint(0, 600 - radius),
                       radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    circle = YellowCircle()
    circle.show()
    sys.exit(app.exec())