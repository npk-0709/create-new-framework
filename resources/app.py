"""
    # Copyright © 2022 By Nguyễn Phú Khương
    # ZALO : 0363561629
    # Email : dev.phukhuong0709@hotmail.com
    # Github : npk-0709
"""
from PyQt5 import  QtGui, QtWidgets
from core import *
import sys


class App(Core, QtWidgets.QMainWindow):
    def __init__(self):
        self.ACTIVATION = False
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    iconWindow = ''
    titleWindow = ''
    app = QtWidgets.QApplication(sys.argv)
    __mainWindow = App()
    __mainWindow.setWindowIcon(QtGui.QIcon(iconWindow))
    __mainWindow.setWindowTitle(titleWindow)
    __mainWindow.show()
    sys.exit(app.exec_())
