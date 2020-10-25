from base.base_sql import Sql
import excel.excel_parse as ep
from excel.excel_base import *
from excel.excel_sql import *


def load_lep_table(answers, comp_id):
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
            if str(answers[k][i]).lower() in ["№ п/п", "№", 'п/п', '№ п.п.']:
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
                if 'Сети' not in str(answers[i][0]):
                    if col_god_vvoda is not None:
                        if answers[i+1][col_god_vvoda] is not None:
                            if int(answers[i+1][col_god_vvoda]) > 1800 and int(answers[i+1][col_god_vvoda]) < 2200:
                                num_max = i
                                query_json_format = {
                                    "SETT": str(SETT).replace("'", '"'),
                                    "sett_name": num_set,
                                    "comp_id": comp_id
                                }
                                query = SQL_ADD_SETT.format(**query_json_format).replace("'None'", "NULL").replace(
                                    "None", "NULL")
                                num_set = int(Sql.exec(query=query)[0]['id'])
            except:
                continue
            if 'Сети' not in str(answers[i]) and '-' not in str(answers[i][col_marka]):
                continue
        if 'Сети' in str(answers[i][0]):
            num_max = i
            query_json_format = {
                "SETT": str(SETT).replace("'", '"'),
                "sett_name": answers[i][0],
                "comp_id": comp_id
            }
            query = SQL_ADD_SETT.format(**query_json_format).replace("'None'", "NULL").replace("None", "NULL")
            num_set = int(Sql.exec(query=query)[0]['id'])
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


def load_res_table(answers, comp_id):
    col_name_res = None
    col_podst_num = None
    col_podst_name = None
    col_podst_year = None
    col_transf_type_napr_nom_p = None
    col_podst_class_napr = None
    col_transf_year_izg = None
    col_transf_year_on = None
    col_transf_type = None
    col_transf_nom_p = None
    col_transf_techsost = None
    col_transf_number = None
    for k in range(20):
        for i in range(len(answers[k])):
            if "наименование рэс" in str(answers[k][i]).lower():
                col_name_res = i
            elif "наименование подстанции" in str(
                    answers[k][i]).lower() or "наименование и подстанционный номер" in str(answers[k][i]).lower():
                col_podst_num = i
                col_podst_name = i
            elif "год ввода" in str(answers[k][i]).lower():
                col_podst_year = i
            elif "тип подстанции".lower() in str(answers[k][i]).lower():
                col_podst_class_napr = i
            elif "тип, мощность".lower() in str(answers[k][i]).lower():
                col_transf_type_napr_nom_p = i
            elif "№ \nтр-ра" in str(answers[k][i]).lower():
                col_transf_number = i
            elif "тип трансфор" in str(answers[k][i]).lower():
                col_transf_type = i
            elif "полная" in str(answers[k][i]).lower() and "номинальная мощность" in str(answers[k - 1][i]).lower():
                col_transf_nom_p = i
            elif "год изготовления" in str(answers[k][i]).lower():
                col_transf_year_izg = i
            elif "год включения" in str(answers[k][i]).lower() or "год установки транс" in str(answers[k][i]).lower():
                col_transf_year_on = i
            elif "состояние тр-ра" in str(answers[k][i]).lower() or "техническое состояние" in str(
                    answers[k][i]).lower():
                col_transf_techsost = i
    num_max = 30
    num_set = None
    name_res = None
    id_res = None
    id_podst = None
    podst_name_save = None
    podst_year = None
    podst_class_napr = None
    transf_type = None
    transf_year_izg = None
    transf_year_on = None
    transf_nom_p = None
    transf_techsost = None
    for i in range(len(answers)):
        if i < num_max:
            try:
                if 'Сети' not in str(answers[i][0]):
                    if col_transf_year_izg is not None and col_transf_year_on is not None:
                        if answers[i+1][col_transf_year_izg] is not None and answers[i+1][col_transf_year_on]:
                            if int(answers[i + 1][col_transf_year_izg]) > 1800 and int(
                                    answers[i + 1][col_transf_year_izg]) < 2200 and int(
                                    answers[i + 1][col_transf_year_on]) > 1800 and int(
                                    answers[i + 1][col_transf_year_on]) < 2200:
                                num_max = i
                                query_json_format = {
                                    "SETT": str(SETT).replace("'", '"'),
                                    "sett_name": num_set,
                                    "comp_id": comp_id
                                }
                                query = SQL_ADD_SETT.format(**query_json_format).replace("'None'", "NULL").replace(
                                    "None", "NULL")
                                num_set = int(Sql.exec(query=query)[0]['id'])
            except:
                continue
            if 'Сети' not in str(answers[i]):
                continue
        if 'Сети' in str(answers[i][0]):
            num_max = i
            query_json_format = {
                "SETT": str(SETT).replace("'", '"'),
                "sett_name": answers[i][0],
                "comp_id": comp_id
            }
            query = SQL_ADD_SETT.format(**query_json_format).replace("'None'", "NULL").replace("None", "NULL")
            num_set = int(Sql.exec(query=query)[0]['id'])
            continue
        if col_name_res is not None:
            if answers[i][col_name_res] is not None and name_res != answers[i][col_name_res]:
                name_res = answers[i][col_name_res]
                query_json_format = {
                    "RES": str(RES).replace("'", '"'),
                    "num_set": num_set,
                    "name_res": name_res,
                }
                query = SQL_ADD_RES.format(**query_json_format).replace("'None'", "NULL").replace("None", "NULL")
                id_res = int(Sql.exec(query=query)[0]['id'])
        if col_podst_num is not None:
            if answers[i][col_podst_num] is not None:
                try:
                    podst_num = int(answers[i][col_podst_num])
                    podst_name = "ПС-{}".format(int(answers[i][col_podst_name]))
                except:
                    try:
                        podst_num = int(answers[i][col_podst_num].split(' ,')[0].split(',')[0].split("-")[-1])
                    except:
                        podst_num = None
                    podst_name = answers[i][col_podst_name].split(',')[0]
                if podst_name_save != podst_name and podst_name is not None:
                    podst_name_save = podst_name
                    if col_podst_class_napr is not None:
                        podst_class_napr = answers[i][col_podst_class_napr]
                    elif col_transf_type_napr_nom_p is not None:
                        podst_class_napr = answers[i][col_transf_type_napr_nom_p].replace(
                            answers[i][col_transf_type_napr_nom_p].split("/")[0] + "/", "")
                    if col_podst_year is not None:
                        podst_year = answers[i][col_podst_year]
                    else:
                        if col_transf_year_on is not None:
                            podst_year = 10000
                            kj = len(answers) - i
                            for jk in range(kj):
                                podst_name_new = None
                                try:
                                    if answers[i+jk][col_podst_name] is not None:
                                        podst_name_new = "ПС-{}".format(int(answers[i+jk][col_podst_name]))
                                except:
                                    if answers[i + jk][col_podst_name] is not None:
                                        podst_name_new = answers[i+jk][col_podst_name].split(',')[0]
                                if answers[i+jk][col_transf_year_on] is not None and podst_name_new == podst_name:
                                    if podst_year > int(answers[i+jk][col_transf_year_on]):
                                        podst_year = int(answers[i+jk][col_transf_year_on])
                                else:
                                    break
                    query_json_format = {
                        "PODSTANC": str(PODSTANC).replace("'", '"'),
                        "name": podst_name,
                        "num_podst": podst_num,
                        "year": podst_year,
                        "class_napr": podst_class_napr,
                        "id_res": id_res,
                        "id_set": num_set
                    }
                    query = SQL_ADD_PODSTANC.format(**query_json_format).replace("'None'", "NULL").replace("None", "NULL")
                    id_podst = int(Sql.exec(query=query)[0]['id'])
        if col_transf_number is not None or col_podst_name is not None:
            if col_transf_number is None:
                transf_number = None
                if answers[i][col_podst_name] is not None:
                    transf_number = answers[i][col_podst_name].replace(answers[i][col_podst_name].split(',')[0] + ",", "")
                    transf_number = transf_number.replace("-" + transf_number.split("-")[-1], "")
            else:
                transf_number = answers[i][col_transf_number]
            if transf_number is not None:
                if col_transf_type is not None:
                    transf_type = answers[i][col_transf_type]
                elif col_transf_type_napr_nom_p is not None:
                    transf_type = answers[i][col_transf_type_napr_nom_p].split("-")[0]
                if col_transf_year_izg is not None:
                    transf_year_izg = answers[i][col_transf_year_izg]
                if col_transf_year_on is not None:
                    transf_year_on = answers[i][col_transf_year_on]
                if col_transf_nom_p is not None:
                    transf_nom_p = answers[i][col_transf_nom_p]
                elif col_transf_type_napr_nom_p is not None:
                    transf_nom_p = int(answers[i][col_transf_type_napr_nom_p].split("-")[1].split("/")[0]) / 1000
                if col_transf_techsost is not None:
                    transf_techsost = answers[i][col_transf_techsost]
                try:
                    transf_number = int(transf_number)
                except:
                    pass
                query_json_format = {
                    "TRANSFORM": str(TRANSFORM).replace("'", '"'),
                    "id_podst": id_podst,
                    "year_izg": transf_year_izg,
                    "year_on": transf_year_on,
                    "type": transf_type.split("-")[0],
                    "nom_p": transf_nom_p,
                    "techsost": transf_techsost,
                    "number": transf_number
                }
                query = SQL_ADD_TRANSFORM.format(**query_json_format).replace("'None'", "NULL").replace("None", "NULL")
                Sql.exec(query=query)


def excel_load(file, comp_id):
    answers = ep.parse_all_table(file)
    for answer in answers:
        if "лэп" in str(answer).lower():
            load_lep_table(answer, comp_id)
        if "трансфор" in str(answer).lower():
            load_res_table(answer, comp_id)


#excel_load('П_Н_Хар-ка действующих ВЛ и КЛ 110 кВ.xlsx', 1)
#excel_load('П_(ЛЭП)_2019_к_опросному_листу.xlsx', 2)
#excel_load('П_Н_Хар-ка тр-ров 110 кВ.xlsx', 1)
#excel_load('П_К_хар.ПС и ВЛ.xlsx', 2)
