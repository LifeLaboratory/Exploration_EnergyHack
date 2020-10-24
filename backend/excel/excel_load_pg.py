from base.base_sql import Sql
import excel.excel_parse as ep
from excel.excel_base import *
from excel.excel_sql import *


def load_lep_table(answers):
    col_num_pp = None
    col_name_lep = None
    col_god_vvoda = None
    col_disp_name = None
    col_napr = None
    col_colcep = None
    col_dlpotr = None
    col_dluchpotr = None
    col_dlpocep = None
    col_dluchpocep = None
    col_marka = None
    col_tehsost = None
    for k in range(20):
        for i in range(len(answers[k])):
            if str(answers[k][i]).lower() in ["№ п/п", "№", 'п/п']:
                col_num_pp = i
            elif "наименование лэп" in str(answers[k][i]).lower():
                col_name_lep = i
            elif "диспетчерский номер" in str(answers[k][i]).lower():
                col_disp_name = i
            elif "год ввода" in str(answers[k][i]).lower():
                col_god_vvoda = i
            elif "U ном".lower() in str(answers[k][i]).lower() or "напряжение" in str(answers[k][i]).lower():
                col_napr = i
            elif "цепей" in str(answers[k][i]).lower():
                col_colcep = i
            elif "по трассе" in str(answers[k][i]).lower() and (
                    "всего" in str(answers[k - 2][i]).lower() or "провод" in str(answers[k - 1][i]).lower()):
                col_dlpotr = i
            elif "по трассе" in str(answers[k][i]).lower() and "в том числе" in str(answers[k - 2][i]).lower():
                col_dluchpotr = i
            elif ("по цепям" in str(answers[k][i]).lower() and "всего" in str(answers[k - 2][i - 1]).lower()) or (
                        "длина в одноцепном" in str(answers[k][i]).lower()):
                col_dlpocep = i
            elif "по цепям" in str(answers[k][i]).lower() and "в том числе" in str(answers[k - 2][i-1]).lower():
                col_dluchpocep = i
            elif "марка" in str(answers[k][i]).lower() and (
                        "провод" in str(answers[k - 1][i]).lower() or "провод" in str(
                    answers[k - 1][i - 1]).lower() or "провод" in str(answers[k - 1][i - 2]).lower()):
                col_marka = i
            elif "техническое состояние" in str(answers[k][i]).lower() or "заключение, при-нятое по рез-там то" in str(
                answers[k][i]).lower():
                col_tehsost = i
    num_set = None
    num_pp = None
    id_lep = None
    year = None
    colcep = None
    techsost = None
    dlport = None
    dlpocep = None
    dluchpotr = None
    dluchpocep = None
    disp_name = None
    napr = None
    num_max = 30
    for i in range(len(answers)):
        if i < num_max:
            try:
                if col_god_vvoda is not None:
                    if answers[i+1][col_god_vvoda] is not None:
                        if int(answers[i+1][col_god_vvoda]) > 1800 and int(answers[i+1][col_god_vvoda]) < 2200:
                            num_max = i
            except:
                continue
            if 'Сети' not in str(answers[i]) and '-' not in str(answers[i][col_marka]):
                continue
        num_max = i
        if 'Сети' in str(answers[i][0]):
            num_set = answers[i][0][5:]
            continue
        if col_num_pp is not None:
            if answers[i][col_num_pp] is not None:
                num_pp = answers[i][col_num_pp]
                year = None
                colcep = None
                techsost = None
        if col_name_lep is not None:
            if answers[i][col_name_lep] is not None:
                if col_name_lep is not None:
                    if answers[i][col_tehsost] is not None:
                        techsost = answers[i][col_tehsost]
                if col_napr is not None:
                    napr = answers[i][col_napr]
                if col_disp_name is not None:
                    disp_name = answers[i][col_disp_name]
                query_json_format = {
                    "LEP": str(LEP).replace("'", '"'),
                    "num_set": num_set,
                    "num_pp": num_pp,
                    "name": answers[i][col_name_lep],
                    "disp_name": disp_name,
                    "napr": napr,
                    "techsost": techsost
                }
                query = SQL_ADD_LEP.format(**query_json_format).replace("'None'", "NULL").replace("None", "NULL")
                id_lep = int(Sql.exec(query=query)[0]['id'])
        if col_god_vvoda is not None:
            if answers[i][col_god_vvoda] is not None:
                year = answers[i][col_god_vvoda]
        if col_colcep is not None:
            if answers[i][col_colcep] is not None:
                colcep = answers[i][col_colcep]
        if col_dlpotr is not None:
            dlport = answers[i][col_dlpotr]
        if col_dlpocep is not None:
            dlpocep = answers[i][col_dlpocep]
        if col_dluchpotr is not None:
            dluchpotr = answers[i][col_dluchpotr]
        if col_dluchpocep is not None:
            dluchpocep = answers[i][col_dluchpocep]
        query_json_format = {
            "PROVOD": str(PROVOD).replace("'", '"'),
            "id_lep": id_lep,
            "name": answers[i][col_marka],
            "year": year,
            "colcep": colcep,
            "dlpotr": dlport,
            "dlpocep": dlpocep,
            "dluchpotr": dluchpotr,
            "dluchpocep": dluchpocep,
        }
        Sql.exec(query=SQL_ADD_PROVOD.format(**query_json_format).replace("'None'", "NULL").replace("None", "NULL"))



def excel_load(file):
    answers = ep.parse_all_table(file)
    for answer in answers:
        if "ЛЭП" in str(answer):
            load_lep_table(answer)


# П_К_хар.ПС и ВЛ.xlsx

excel_load('П_К_хар.ПС и ВЛ.xlsx')

