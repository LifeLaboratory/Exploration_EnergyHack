# coding=utf-8
from base import base_name as names
from base.base_router import BaseRouter
from base.base_sql import Sql


class Companies(BaseRouter):
    """
    Роут для работы с товарами
    """
    def __init__(self):
        super().__init__()
        self.args = []

    def get(self):
        sql_query = '''table "Компания"'''
        test = Sql.exec(query=sql_query)
        return test, 200, names.CORS_HEADERS

    def post(self):
        return 'Ok', 200, names.CORS_HEADERS

    def options(self):
        return 'Ok', 200, names.CORS_HEADERS
