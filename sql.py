import sqlite3
import os


class NotCorrectPath(Exception):
    """
    Raise Custom Exception for wrong path
    """
    pass


class SQL:
    def __init__(self, path):
        try:
            self._check_path(path)
            self.path = path
            self._connect()
        except NotCorrectPath:
            pass
        self.data = None

    def _connect(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()

    def execute(self, sqlquery):
        self.cursor.execute(sqlquery)
        self.data = self.cursor.fetchall()
        return self.data

    @staticmethod
    def _check_path(path):
        if not os.path.exists(path):
            raise NotCorrectPath

    def _error(self):
        # TODO функция должна вызывать окно в котором будет отобраться ошибка
        pass

    def __call__(self, sqlquery):
        self.execute(sqlquery)

    def __len__(self):
        if self.data is None:
            return 0
        else:
            return len(self.data)
