from PyQt6 import QtCore, QtGui, QtWidgets


# FIXME привести в нормальный вид, скорее всего нужно докуртить принцип фабрики, чтобы различать тип "окна"
class WindowConstruct:
    def __init__(self, window_object, window_type=None):
        self.ui = window_object()
        self.window = window_type or QtWidgets.QMainWindow()
        self.ui.setupUi(self.window)

    def run(self):
        self.window.show()
