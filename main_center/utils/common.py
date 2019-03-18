import os
import xlrd
import openpyxl
proDir = os.path.split(os.path.realpath(__file__))[0]


def get_xlsx_sheeet(excel_name):
    """
    get excel file data
    :param excel_name:
    :return:
    """
    cls = []
    # 获取excel的文件路径
    excel_path = os.path.join(proDir, 'excel_case', excel_name)
    # 打开excel文件
    file = xlrd.open_workbook(excel_path)
    # 获取sheet页
    sheets = file.sheets()
    # 遍历获取用例
    for sheet in sheets:
        nrows = sheet.nrows
        for i in range(nrows):
            if sheet.row_values(i)[0] != u'case_name':
                cls.append(sheet.row_values(i))

    return cls


def set_all_url(url):
    return url


def set_url(url):
    new_url = scheme + '://' + baseurl + ':' + port + url
    return new_url

