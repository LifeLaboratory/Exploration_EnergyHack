# coding=utf-8
from base import base_name as names
from base.base_router import BaseRouter
from LEP_report import generate_lep_report
import os


class LEPReport(BaseRouter):
    """
    Роут для работы с товарами
    """

    def __init__(self):
        super().__init__()
        self.args = ["НазваниеРодителя", "Тип_записи", "id", "Компания", "Название", "children"]

    def get(self, id_company):
        generate_lep_report(id_company)

        return {'link': 'http://90.189.183.166:13451/static/Отчет_ЛЭП_new.xlsx'}, 200, names.CORS_HEADERS

    def post(self):
        return 'Ok', 200, names.CORS_HEADERS

    def options(self, id_company):
        return 'Ok', 200, names.CORS_HEADERS
