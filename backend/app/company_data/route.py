# coding=utf-8
from base import base_name as names
from base.base_router import BaseRouter
from .processor import *


class CompanyData(BaseRouter):
    """
    Роут для работы с товарами
    """

    def __init__(self):
        super().__init__()
        self.args = []

    def get(self, id_company):
        result = get_company_data(id_company)
        return result, 200, names.CORS_HEADERS

    def post(self):
        return 'Ok', 200, names.CORS_HEADERS

    def options(self):
        return 'Ok', 200, names.CORS_HEADERS
