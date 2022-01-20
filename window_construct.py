from PyQt6 import QtCore, QtGui, QtWidgets
from abc import ABC, abstractmethod


# FIXME привести в нормальный вид, скорее всего нужно докуртить принцип фабрики, чтобы различать тип "окна"
class WindowConstruct:
    def __init__(self, window_object, window_type=None, *args):
        self.ui = window_object()
        self.window = window_type or QtWidgets.QMainWindow()
        self.ui.setupUi(self.window)

        self.ui.config()

    def run(self):
        self.window.show()




"""class AbstractHandler(ABC):

    @abstractmethod
    def handle(self, window_object):
        pass


class NullHandler(AbstractHandler):
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, window_object):
        if self._successor is not None:
            return self._successor.handle(window_object)


class QtMainWindowHandler(NullHandler):
    def handle(self, window_object):
        pass


class QtDialogHandler(NullHandler):
    def handle(self, window_object):
        pass
"""