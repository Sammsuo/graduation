import os
import xlrd
import openpyxl
import re
import json
from datetime import datetime

proDir = os.path.split(os.path.realpath(__file__))[0]
resultPath = os.path.join(proDir,'result')
reportPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))

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


def show_return_msg(response):
    msg = response.text
    print("\n请求返回值: " + '\n' + json.dumps(json.loads(msg), ensure_ascii=False, sort_keys=True, indent=4))


def get_report_path():
    """
    获取报告文件路径
    :return:
    """
    report_path = os.path.join(reportPath, 'report.html')
    return report_path


def get_result_path():
    """
    获取报告结果路径
    :return:
    """
    return reportPath


def save_file():
    """
    保存excel文件
    :return:
    """
    pass


def get_file():
    """
    获取文件
    :return:
    """
    pass

def delete_file():
    """
    删除文件
    :return:
    """

if __name__ == '__main__':
    #print(check_url('http://47.107.21.127:9000/pld/credit/#/credit/packageManage/index'))
    print(proDir)
    print(resultPath)