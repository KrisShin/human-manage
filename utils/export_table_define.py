from config.settings import STATIC_FOLDER
import xlsxwriter
from uuid import uuid4

FIELD_NAME = {
    'class_name': '类名称',
    'tbl_code': '表格ID',
    'tbl_name': '表格名称',
    'field_code': '字段ID',
    'field_name': '字段名称',
    'type': '字段类型',
    'key': 'KEY',
    'size': '字段大小',
    'decimal': '字段小数',
    'nullable': '是否为空',
    'doc': '说明',
    'comment': '备注',
}


def set_excel_header(worksheet, data):
    worksheet.write('A1', FIELD_NAME['class_name'])
    worksheet.write('B1', data.class_name)
    worksheet.write('D1', FIELD_NAME['tbl_name'])
    worksheet.write('E1', data.tbl_name)
    worksheet.write('G1', FIELD_NAME['tbl_code'])
    worksheet.write('H1', data.tbl_code)

    worksheet.write(2, 0, '序号')
    for index, name in enumerate(list(FIELD_NAME.keys())[3:]):
        worksheet.write(2, index+1, FIELD_NAME[name])


def generate_excel_file(table_dict):
    excel_name = str(uuid4())
    workbook = xlsxwriter.Workbook(f'{STATIC_FOLDER}/{excel_name}.xlsx')
    for field_list in table_dict.values():
        first_field = field_list[0]
        worksheet = workbook.add_worksheet(first_field.class_name)
        set_excel_header(worksheet, first_field)
        for row_index, field in enumerate(field_list):
            for col_index, name in enumerate(list(FIELD_NAME.keys())[2:]):
                val = getattr(field, name) if col_index > 0 else row_index + 1
                worksheet.write(row_index + 3, col_index, val)
    workbook.close()
    return excel_name
