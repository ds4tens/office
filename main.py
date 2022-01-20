from MainWindow import MainWindow as Mw
from PyQt6 import QtCore, QtGui, QtWidgets
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Mw(debug_mode=0)
    ui.setupUi(MainWindow)
    ui.add_action()
    ui.fill_combobox()
    ui.mask()

    MainWindow.show()

    sys.exit(app.exec())
