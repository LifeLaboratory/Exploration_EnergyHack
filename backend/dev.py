import xlwings as xw
# app = xw.App()
# app.books['new_file.xlsx']
wb = xw.Book('new_file.xlsx')
wb.close()
