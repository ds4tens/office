from MainWindow import MainWindow as Mw
from PyQt6 import QtCore, QtGui, QtWidgets
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Mw()
    ui.setupUi(MainWindow)
    ui.add_action()

    MainWindow.show()

    sys.exit(app.exec())
