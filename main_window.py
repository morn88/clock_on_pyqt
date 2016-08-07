from PyQt5 import QtGui, QtWidgets
import sys


class MyWind(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setUI()

    def setUI(self):
        self.setFixedSize(300, 300)
        self.btn = QtWidgets.QPushButton()
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MyWind()
    w.setWindowTitle('Clock')
    sys.exit(app.exec_())