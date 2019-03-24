import os
import xlrd
import openpyxl
import re
import json
from datetime import datetime

proDir = os.path.split(os.path.realpath(__file__))[0]
resultPath = os.path.join(proDir, 'result')
if not os.path.exists(resultPath):
    os.mkdir(resultPath)
reportPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
if not os.path.exists(reportPath):
    os.mkdir(reportPath)


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
    获取excel文件
    :return:
    """
    path = os.path.join(proDir, 'testFile')
    dirs = os.listdir(path)
    f = []
    for i in dirs:
        if i.endswith(".xlsx"):
            f.append(i)
    return f[0]


def get_xlsx_sheets(xlsx_name):
    cls = []
    # get xls file's path
    xls_path = os.path.join(proDir, "testFile", xlsx_name)
    # print (xls_path)

    # open xls file
    file = xlrd.open_workbook(xls_path)

    sheets = file.sheets()

    for sheet in sheets:
        nrows = sheet.nrows
        for i in range(nrows):
            if sheet.row_values(i)[0] != u'case_name':
                cls.append(sheet.row_values(i))
    return cls


def delete_file():
    """
    删除文件
    :return:
    """
    pass

def download_file():
    """
    下载excel文件
    :return:
    """

if __name__ == '__main__':
    #print(check_url('http://47.107.21.127:9000/pld/credit/#/credit/packageManage/index'))
    print(proDir)
    print(resultPath)
    get_file()