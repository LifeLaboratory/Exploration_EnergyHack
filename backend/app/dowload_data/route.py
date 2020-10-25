# coding=utf-8
from base import base_name as names
from base.base_router import BaseRouter
from PC_report import generate_pc_report
import os


class PCReport(BaseRouter):
    """
    Роут для работы с товарами
    """

    def __init__(self):
        super().__init__()
        self.args = ["НазваниеРодителя", "Тип_записи", "id", "Компания", "Название", "children"]

    def get(self, id_company):
        generate_pc_report(id_company)
        return {'link': 'http://90.189.183.166:13451/static/Отчет_ПС_new.xlsx'}, 200, names.CORS_HEADERS

    def post(self):
        return 'Ok', 200, names.CORS_HEADERS

    def options(self, id_company):
        return 'Ok', 200, names.CORS_HEADERS
