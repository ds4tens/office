from PyQt6 import QtCore, QtGui, QtWidgets

from py_ui.DataRecWindow import Ui_MainWindow
import sqlite3 as sql


class RecordsWindow(Ui_MainWindow):
    def __init__(self):
        pass

    def config(self):
        self._connect_to_db()
        self._load_data()
        self._fill_row()

    def _connect_to_db(self):
        # база данных - локальная
        # TODO нужно каким-то образом получить расположение файла, либо же сделать его относительным
        # TODO обработка ошибки подключекния к бд
        path = 'new_file'
        self.connection = sql.connect(path)

    def _load_data(self):
        self.cur = self.connection.cursor()
        sqlquery = "SELECT * FROM test"
        self.cur.execute(sqlquery)
        self.data = self.cur.fetchall()

    def _fill_row(self):
        self.tableWidget.setRowCount(len(self.data))
        for row, data in enumerate(self.data):
            for clm, subdata in enumerate(data):
                self.tableWidget.setItem(row, clm, QtWidgets.QTableWidgetItem(str(subdata)))

