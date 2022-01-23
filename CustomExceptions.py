class PathError(Exception):
    def __init__(self, path):
        self.path = path
        self.strerror = "Ошибка типа файла"

    def __str__(self):
        return "Каким-то чудом имя файла не соответсвует типу string " \
               "тип имени файла {}".format(type(self.path))


class NotCorrectPath(Exception):
    def __init__(self, path):
        self.path = path
        self.strerror = "Неправильный путь к БД"

    def __str__(self):
        return "Неправильный путь к БД {} нужно проверить файл SQL.py".format(self.path)


class SmallArguments(Exception):
    def __init__(self, expected_len, args):
        self.expected_len = expected_len
        self.args = args
        self.strerror = "Неверная размерность списка"

    def __str__(self):
        return "Размер списка не соотвестсует требованию {}, было получено <> len{}".format(
            self.expected_len, self.args, len(self.args))
