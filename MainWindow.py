from PyQt6 import QtCore, QtGui, QtWidgets

from py_ui.MainWindow import Ui_MainWindow
from RecordsWindow import RecordsWindow
from window_construct import WindowConstruct
from sql import SQL

import os
import easygui


# TODO докрутить взаимодейтсвие с excel
class MainWindow(Ui_MainWindow):

    def __init__(self, debug_mode=0):
        # FIXME доработать путь к файлу по умолчанию
        self.path = None
        self.verification = True
        self.debug_mode = debug_mode

    def add_action(self):
        self.action_path_excel.triggered.connect(lambda: self._path_to_excel_file())
        self.action_verify_data.triggered.connect(lambda: self._toggle_verification())
        self.action_show_db.triggered.connect(lambda: self._show_db_window())
        self.pushButton.clicked.connect(lambda: self._get_data())

    def fill_combobox(self):
        data = SQL("new_file")
        data.execute("SELECT box_id FROM test")

        self.comboBox.addItems([str(i[0]) for i in data])

    def mask(self):
        self.text_accepter.validator()
        regexp = QtCore.QRegularExpression("[0-9\\.\\0-9]{0,7}")
        valid = QtGui.QRegularExpressionValidator(regexp)
        self.text_accepter.setValidator(valid)


    def _get_data(self):
        print(self.text_accepter.text())

    def _path_to_excel_file(self):
        self.path = easygui.fileopenbox(msg="Choose a file", default=os.path.curdir)
        if self.debug_mode:
            print("NEW PATH: {}".format(self.path))

    def _toggle_verification(self):
        self.verification ^= True

    def _show_db_window(self):
        self.second_window = WindowConstruct(RecordsWindow)
        self.second_window.ui.config()

        self.second_window.run()
