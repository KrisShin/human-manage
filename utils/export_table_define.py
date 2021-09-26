from config.settings import STATIC_FOLDER
import xlsxwriter
from uuid import uuid4


workbook = xlsxwriter.Workbook(f'{STATIC_FOLDER}/{str(uuid4())}.xlsx')
worksheet = workbook.add_worksheet('sheet_name')
worksheet.write('A1', 'Hello world')
workbook.close()


def generate_excel_file():
    return True
