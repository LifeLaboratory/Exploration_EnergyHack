from base.base_sql import Sql
import excel.excel_parse as ep
from excel.excel_base import *
from excel.excel_sql import *
import json


#result = Sql.exec(query=sql)

def load_pk_char(file):
    table1, table2 = ep.parse_pk_char(file)


def load_pn_char(file):
    table = ep.parse_pn_char(file)
    num_set = None
    num_pp = None
    id_lep = None
    year = None
    colcep = None
    techsost = None
    for i in range(len(table)):
        if 'Сети' in str(table[i][0]):
            num_set = table[i][0][5:]
            continue
        if table[i][0] is not None:
            num_pp = table[i][0]
            year = None
            colcep = None
            techsost = None
        if table[i][1] is not None:
            if table[i][25] is not None:
                techsost = table[i][25]
            query_json_format = {
                "LEP": str(LEP).replace("'", '"'),
                "num_set": num_set,
                "num_pp": num_pp,
                "name": table[i][1],
                "disp_name": table[i][3],
                "napr": table[i][2],
                "techsost": techsost
            }
            query = SQL_ADD_LEP.format(**query_json_format).replace("'None'", "NULL").replace("None", "NULL")
            id_lep = int(Sql.exec(query=query)[0]['id'])
        if table[i][19] is not None:
            year = table[i][19]
        if table[i][4] is not None:
            colcep = table[i][4]
        query_json_format = {
            "PROVOD": str(PROVOD).replace("'", '"'),
            "id_lep": id_lep,
            "name": table[i][11],
            "year": year,
            "colcep": colcep,
            "dlpotr": table[i][5],
            "dlpocep": table[i][6],
            "dluchpotr": table[i][7],
            "dluchpocep": table[i][8],
        }
        Sql.exec(query=SQL_ADD_PROVOD.format(**query_json_format).replace("'None'", "NULL").replace("None", "NULL"))


def load_p_lep_with_question_list(file):
    table = ep.parse_p_lep_with_question_list(file)


def load_pn_char_transf(file):
    table = ep.parse_pn_char_transf(file)


def load_p_sil_transf(file):
    table = ep.parse_p_sil_transf(file)


def excel_load(status, file):
    if status == "1":
        load_pk_char(file)
    elif status == "2":
        load_pn_char(file)
    elif status == "3":
        load_p_lep_with_question_list(file)
    elif status == "4":
        load_pn_char_transf(file)
    elif status == "5":
        load_p_sil_transf(file)

# П_К_хар.ПС и ВЛ.xlsx

excel_load('2', 'П_Н_Хар-ка действующих ВЛ и КЛ 110 кВ.xlsx')

