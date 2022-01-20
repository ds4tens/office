from PyQt6 import QtCore, QtGui, QtWidgets

from py_ui.DataRecWindow import Ui_MainWindow
from sql import SQL


class RecordsWindow(Ui_MainWindow):
    def __init__(self):
        pass

    def config(self):
        self._fill_row()

    def _fill_row(self):
        data = SQL('sql/dbo')
        data.execute(
            "SELECT DISTINCT ORDERS._date, ORDERS.box_id, ORDERS.sum, ORDERS.order_id, info.name  "
            "FROM ORDERS inner join info on ORDERS.box_id = info.box_id  order by ORDERS._date")
        self.tableWidget.setRowCount(len(data))
        for row, data in enumerate(data):
            for clm, subdata in enumerate(data):
                self.tableWidget.setItem(row, clm, QtWidgets.QTableWidgetItem(str(subdata)))
