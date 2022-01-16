from PyQt6 import QtCore, QtGui, QtWidgets

from py_ui.DataRecWindow import Ui_MainWindow
from sql import SQL


class RecordsWindow(Ui_MainWindow):
    def __init__(self):
        pass

    def config(self):
        self._fill_row()

    def _fill_row(self):
        data = SQL('new_file')
        data.execute("SELECT * FROM test")
        self.tableWidget.setRowCount(len(data))
        for row, data in enumerate(data):
            print(data)
            for clm, subdata in enumerate(data):
                self.tableWidget.setItem(row, clm, QtWidgets.QTableWidgetItem(str(subdata)))



