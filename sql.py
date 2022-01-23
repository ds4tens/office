import sqlite3
import os

from CustomExceptions import NotCorrectPath, SmallArguments


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

    def insert(self, *args):
        if len(args) != 4:
            raise SmallArguments
        self.cursor.execute("INSERT INTO ORDERS VALUES (?, ?, ?, ?)", args)
        self.connection.commit()

    def delete_order(self, order_id):
        self.cursor.execute("DELETE from ORDERS WHERE order_id = ?", (order_id, ))

        self.connection.commit()

    @staticmethod
    def _check_path(path):
        if not os.path.exists(path):
            raise NotCorrectPath(path)

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

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.data):
            result = self.data[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration

    def __del__(self):
        self.connection.close()
