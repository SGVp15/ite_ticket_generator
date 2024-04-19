from openpyxl import load_workbook


class excel():
    def read_excel(excel, page_name, column, row):
        sheet_ranges = excel[page_name]
        return str(sheet_ranges[f'{column}{row}'].value)
