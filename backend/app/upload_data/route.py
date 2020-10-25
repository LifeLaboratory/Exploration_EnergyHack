# coding=utf-8
from base import base_name as names
from base.base_router import BaseRouter
import os
from excel.excel_load_pg import excel_load


class UploadData(BaseRouter):
    """
    Роут для работы с товарами
    """

    def __init__(self):
        super().__init__()
        self.args = ["НазваниеРодителя", "Тип_записи", "id", "Компания", "Название", "children"]

    def get(self):
        return 'Ok', 200, names.CORS_HEADERS

    def post(self):
        name_file = 'new_file.xlsx'
        file_data = self.get_file_data()
        try:
            os.remove(name_file)
        except:
            pass

        new_file = open(name_file, "wb")
        new_file.write(file_data)
        new_file.close()
        excel_load('new_file.xlsx', 4)
        return 'Ok', 200, names.CORS_HEADERS

    def options(self):
        return 'Ok', 200, names.CORS_HEADERS
