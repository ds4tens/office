import os
import pandas as pd


class ExcelReader:
    # TODO нужно четкое тз что читать из файла excel
    _INPUTDIR = r'\\input'
    _OUTPUTDIR = r'\\output'

    def __init__(self):
        self.work_dir = os.getcwd()
        self._check_dirs()

    def _check_dirs(self):
        if not os.path.exists(self.work_dir + self._INPUTDIR):
            os.mkdir(self.work_dir + self._INPUTDIR)
        if not os.path.exists(self.work_dir + self._OUTPUTDIR):
            os.mkdir(self.work_dir + self._OUTPUTDIR)
