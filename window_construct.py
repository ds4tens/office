from PyQt6 import QtCore, QtGui, QtWidgets
from py_ui.PathDialog import Ui_Dialog


# FIXME привести в нормальный вид, скорее всего нужно докуртить принцип фабрики, чтобы различать тип "окна"
class WindowConstruct:
    def __init__(self, window_object, window_type=None, *args):
        self.ui = window_object()
        self.window = window_type or QtWidgets.QMainWindow()
        self.ui.setupUi(self.window)

        self.ui.config()

    def run(self):
        self.window.show()


class ErrorWindowConstruct:
    def __init__(self, exception, name=None, reason=None):
        self.error = QtWidgets.QMessageBox()
        self.error.setWindowTitle(name or str(exception.strerror))
        self.error.setFixedSize(250, 155)
        self.error.setText(reason or str(exception))
        self.error.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)

        self.error.setIcon(QtWidgets.QMessageBox.Icon.Warning)

        self.error.exec()


class ConfirmWindow:
    def __init__(self, text, cancel_btn=False):
        self.conf = QtWidgets.QMessageBox()
        self.conf.setWindowTitle("Подтверждение")
        self.conf.setIcon(QtWidgets.QMessageBox.Icon.Information)
        self.conf.setText(text)
        self.conf.setStandardButtons(
            QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Cancel) if cancel_btn \
            else self.conf.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)

        self.conf.exec()


class Dialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, main_window):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.main_window = main_window

        self._config_buttons()

        self.exec()

    def _config_buttons(self):
        self.buttonBox.accepted.connect(self._accept)
        self.buttonBox.rejected.connect(self._cancel)

    def _accept(self):
        filename = self.lineEdit.text()
        self.main_window.dialog_filename = filename

        self.close()

    def _cancel(self):
        self.close()
