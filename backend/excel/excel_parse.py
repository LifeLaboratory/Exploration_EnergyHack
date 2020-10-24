import xlwings as xw
import pandas as pd


# П_К_хар.ПС и ВЛ.xlsx
def parse_pk_char(file):
    data = parse_all_table(file, 'Таблица 2.2', 'A7', 'M')
    transform = []
    komm_apparat = []
    reaktor = []
    for dat in data:
        if dat[1] is not None:
            transform.append(dat[0:24])
        if dat[24] is not None:
            komm_apparat.append(dat[0, 24:28])
        if dat[28] is not None:
            reaktor.append()
    second_data = parse_all_table(file, 'Таблица 4', 'A8', 'AG')
    return data, second_data


# П_Н_Хар-ка действующих ВЛ и КЛ 110 кВ.xlsx
def parse_pn_char(file):
    data = parse_all_table(file, '8', 'A11', 'AA')
    return data


# П_(ЛЭП)_2019_к_опросному_листу.xlsx
def parse_p_lep_with_question_list(file):
    data = parse_all_table(file, 'Лист1', 'A9', 'M')
    return data


# П_Н_Хар-ка тр-ров 110 кВ.xlsx
def parse_pn_char_transf(file):
    data = parse_all_table(file, 'Лист1', 'A6', 'AY')
    return data


# П_силовые тр-ры.xlsx
def parse_p_sil_transf(file):
    data = parse_all_table(file, 'Лист1', 'A6', 'As')
    return data


def parse_all_table(file, sheet_name, range_first, range_last):
    wb = xw.Book(file)
    last_row = len(pd.read_excel(file, sheet_name=sheet_name)) + 1
    data_excel = wb.sheets[sheet_name]
    data_pd = data_excel.range('{first}:{last}{row}'.format(first=range_first, last=range_last, row=last_row)).value
    return data_pd

#ans = parse_p_sil_transf('П_силовые тр-ры.xlsx')
#print(ans)
