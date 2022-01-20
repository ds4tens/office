from PyQt6 import QtCore, QtGui, QtWidgets

from py_ui.MainWindow import Ui_MainWindow
from RecordsWindow import RecordsWindow
from ConfirmWindow import ConfirmWindow
from window_construct import WindowConstruct

from sql import SQL
from ExcelWriter import ExcelWriter

from itertools import groupby

import datetime
import os
import easygui


# TODO докрутить взаимодейтсвие с excel
# TODO добавить связь с разными таблицами
class MainWindow(Ui_MainWindow):

    def __init__(self, debug_mode=0):
        print(debug_mode)
        # FIXME доработать путь к файлу по умолчанию
        self.path = None
        self.verification = True
        self.debug_mode = debug_mode
        self.sql = SQL("sql/dbo")

    def add_action(self):
        """
        Привязка функций к разным кнопкам
        :return:
        """
        self.action_path_excel.triggered.connect(lambda: self._path_to_excel_file())
        self.action_verify_data.triggered.connect(lambda: self._toggle_verification())
        self.action_show_db.triggered.connect(lambda: self._show_db_window())
        self.pushButton.clicked.connect(lambda: self._get_data())
        self.action_excel.triggered.connect(lambda: self._write_excel())
        self.action_excel_2.triggered.connect(lambda: self._open_excel())

        "Установка текущей даты, как даты по умолчанию"
        self.dateEdit.setDate(QtCore.QDate(int(datetime.date.today().year), int(datetime.date.today().month),
                                           int(datetime.date.today().day)))

    def fill_combobox(self):
        """
        Добавляет в прокрутку номера боксов
        :return:
        """

        self.sql.execute("SELECT box_id FROM info")

        self.comboBox.addItems([str(i[0]) for i in self.sql])

    def mask(self):
        """
        Создание масок на QLineEdit для корректного ввода данных
        :return:
        """
        self.lineEdit_sum.validator()
        self.lineEdit_order.validator()

        regexp1 = QtCore.QRegularExpression("[0-9\\.\\0-9]{0,7}")
        valid1 = QtGui.QRegularExpressionValidator(regexp1)

        regexp2 = QtCore.QRegularExpression("[0-9]{0,4}")
        valid2 = QtGui.QRegularExpressionValidator(regexp2)

        self.lineEdit_sum.setValidator(valid1)
        self.lineEdit_order.setValidator(valid2)

    def _get_data(self):
        """
        Функция вызывается при нажатии "Добавить запись"
        Вызывается окно подтверждения, если опция окна включена
        :return:
        """
        if self.verification:
            self.confirm_window = WindowConstruct(ConfirmWindow, QtWidgets.QDialog())
            self.confirm_window.ui.tableWidget.setRowCount(1)
            self.confirm_window.ui.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem((self._convert_date())))
            self.confirm_window.ui.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem((self.comboBox.currentText())))
            self.confirm_window.ui.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem((self.lineEdit_sum.text())))
            self.confirm_window.ui.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem((self.lineEdit_order.text())))

            self.confirm_window.run()
        else:
            # TODO запись данных в бд, если функция подтверждения выключена
            self.sql.insert(self._convert_date(), self.comboBox.currentText(), self.lineEdit_sum.text(),
                            self.lineEdit_order.text())

        if self.debug_mode == 1:
            print((self.dateEdit.text()))
            print(self.lineEdit_sum.text())
            print(self.lineEdit_order.text())

    def _path_to_excel_file(self):
        """
        Выбор пути к файлам excel
        :return:
        """
        self.path = easygui.fileopenbox(msg="Choose a file", default=os.path.curdir)
        if self.debug_mode == 1:
            print("NEW PATH: {}".format(self.path))

    def _toggle_verification(self):
        """
        Переключение подтвержденния входных данных
        :return:
        """
        self.verification ^= True

    def _show_db_window(self):
        """
        Отображение окна со всеми данными из бд
        :return:
        """
        self.second_window = WindowConstruct(RecordsWindow)

        self.second_window.run()

    def _write_excel(self):
        writer = ExcelWriter('excel/new_excel.xlsx')
        data = self.sql.execute("SELECT DISTINCT ORDERS._date, ORDERS.box_id, ORDERS.sum, ORDERS.order_id, info.name  "
                                "FROM ORDERS inner join info on ORDERS.box_id = info.box_id  order by ORDERS._date")

        for key, group in groupby(data, lambda x: x[0]):
            lst = []
            for item in group:
                lst.append(item)
            writer.write(lst)
        writer.commit()

        # TODO создать окно, что все прошло успешно

    def _convert_date(self):
        year = self.dateEdit.date().year()
        month = self.dateEdit.date().month()
        day = self.dateEdit.date().day()
        return "{}-{}-{}".format(year, month, day)

    def _open_excel(self):
        self._path_to_excel_file()
        try:
            os.startfile(self.path)
        except OSError:
            print("Ошибка в пути/названии файла")

        finally:
            pass
