import xlwings as xw
import pandas as pd


def parse_all_table(file):
    xl = pd.ExcelFile(file)
    lists = xl.sheet_names
    data = []
    for i in lists:
        answer = parse_table(file, i, 'A1', 'AZ')
        if len([k for k in answer if k is not None]) > 0:
            data.append(answer)
    return data


def parse_table(file, sheet_name, range_first, range_last):
    wb = xw.Book(file)
    last_row = len(pd.read_excel(file, sheet_name=sheet_name)) + 1
    data_excel = wb.sheets[sheet_name]
    data_pd = data_excel.range('{first}:{last}{row}'.format(first=range_first, last=range_last, row=last_row)).value
    return data_pd

