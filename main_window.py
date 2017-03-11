from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import sys
import time
import shutil
import os


class MyWind(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 100, 400, 200)

        self.clock = QtWidgets.QLCDNumber(self)
        self.clock.setDigitCount(8)

        self.setWindowIcon(QtGui.QIcon('clock-icon.png'))

        tray_icon = SystemTrayIcon(QtGui.QIcon('clock-icon.png'), self)
        tray_icon.show()

        self.progress_bar = QtWidgets.QProgressBar(self)

        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.setInterval(100)
        timer.start()

        self.btn = QtWidgets.QPushButton("Copy")
        self.btn.clicked.connect(self.copy_files)

        self.status_bar = QtWidgets.QStatusBar(self)

        grid = QtWidgets.QGridLayout()
        grid.addWidget(self.clock, 0, 0)
        grid.addWidget(self.progress_bar, 1, 0)
        grid.addWidget(self.btn, 2, 0)

        self.setLayout(grid)
        self.show()

    def copy_files(self):
        try:
            list_of_files = os.listdir("from")
            step = 100 / len(list_of_files)
            value = step
            for i in range(len(list_of_files)):
                shutil.copy(os.path.join('from', list_of_files[i]), os.path.join('to', list_of_files[i]))
                self.progress_bar.setValue(value)
                value += step

        except Exception as e:
            print(str(e))
            self.status_bar.showMessage(str(e))

    def update_time(self):
        clock_time = time.ctime().split()[3]
        self.clock.display(clock_time)


class SystemTrayIcon(QtWidgets.QSystemTrayIcon):

    def __init__(self, icon, parent=None):
        super(SystemTrayIcon, self).__init__(icon, parent)
        menu = QtWidgets.QMenu(parent)
        exitAction = menu.addAction("Выйти")
        exitAction.triggered.connect(parent.close)
        maximase_action = menu.addAction("Показать")
        maximase_action.triggered.connect(self.size_change)
        self.setContextMenu(menu)

    def size_change(self):
        if self.parent().isMaximized:
            self.parent().showMinimized()
        else:
            self.parent().showMaximized()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MyWind()
    w.setWindowTitle('Clock')
    sys.exit(app.exec_())