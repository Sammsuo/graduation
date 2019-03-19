import os
import xlrd
import openpyxl
import re

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


def check_url(url):
    check_rule_r = r'(https?:.*?:.*?/)'
    check_rule_p = re.compile(check_rule_r)
    check_rule_c = re.findall(check_rule_p, url)
    print(check_rule_c)
    if len(check_rule_c) != 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(check_url('http://47.107.21.127:9000/pld/credit/#/credit/packageManage/index'))
