# coding=utf-8
from base import base_name as names
from base.base_router import BaseRouter
from .processor import *
from json_loader import to_json
from .update_data import update_data


class CompanyData(BaseRouter):
    """
    Роут для работы с товарами
    """

    def __init__(self):
        super().__init__()
        self.args = ["НазваниеРодителя", "Тип_записи", "id", "Компания", "Название", "children"]

    def get(self, id_company):
        result = get_company_data(id_company)
        return result, 200, names.CORS_HEADERS

    def post(self, id_company):
        data = self.read_data_json()
        update_data(data)
        return 'Ok', 200, names.CORS_HEADERS

    def options(self, id_company):
        return 'Ok', 200, names.CORS_HEADERS
