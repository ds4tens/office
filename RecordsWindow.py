import sqlite3

from PyQt6 import QtCore, QtGui, QtWidgets

from py_ui.DataRecWindow import Ui_MainWindow
from sql import SQL
from window_construct import ErrorWindowConstruct, ConfirmWindow as cf
import easygui


class RecordsWindow(Ui_MainWindow):
    def __init__(self):
        self.sql = SQL('sql/dbo')

    def config(self):

        self.pushButton.clicked.connect(lambda: self._del_row())

        self._fill_row()

    def _fill_row(self):
        data = self.sql.execute(
            "SELECT DISTINCT ORDERS._date, ORDERS.box_id, ORDERS.sum, ORDERS.order_id, info.name  "
            "FROM ORDERS inner join info on ORDERS.box_id = info.box_id  order by ORDERS._date")
        self.tableWidget.setRowCount(len(data))
        for row, data in enumerate(data):
            for clm, subdata in enumerate(data):
                self.tableWidget.setItem(row, clm, QtWidgets.QTableWidgetItem(str(subdata)))

    def _del_row(self):
        lst = []
        row = self.tableWidget.currentRow()
        for column in range(self.tableWidget.columnCount()):
            lst.append(self.tableWidget.item(row, column).text())

        order_id = self.tableWidget.item(row, 3).text()

        try:
            self.sql.delete_order(int(order_id))
            cf("Запись успешно удалена")
        except Exception as e:
            ErrorWindowConstruct(None, "Error",
                                 "{}".format(lst))
            easygui.exceptionbox()

        lst.clear()

        self._fill_row()
