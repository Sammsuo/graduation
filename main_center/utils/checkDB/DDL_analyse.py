# -*- coding : utf-8 -*-
import re
from functools import reduce

# 对整个输入框内容进行截取create整个语句,截取每个[create-;]  传表
def sql_cut_create(sql_all):
    """
    截取每个创表语句，返回list
    :param sql_all:
    :return:
    """
    sql_all = sql_all.replace('\t', '').replace('\n', '').replace('`', '').lower() # 对输入的内容进行修改
    #print(sql_all)
    try:
        sql_cut_create_r = r".*?(create table.*?);"
        sql_cut_create_p = re.compile(sql_cut_create_r)
        sql_cut_create_c = re.findall(sql_cut_create_p, sql_all)
        #print('sql_cut_create_c : ' + sql_cut_create_c[0])
        return sql_cut_create_c

    except Exception as e:
        print('sql_cut_create error:', e)
    # print(sql_cut_create_c)
        return False #TODO 第一个false


# 对每个create语句进行截取所有字段语句   传表
def sql_cut_columnall(cut_create):
    """
    截取每个创表语句中的字段语句集，返回list
    :param cut_create:
    :return:
    """
    if cut_create:
        try:
            print(cut_create)
            sql_cut_columnall_r = r'create .*?\((.*?\)) engine'  # 将创建字段语句整体提炼
            sql_cut_columnall_p = re.compile(sql_cut_columnall_r)
            sql_cut_columnall_c = re.findall(sql_cut_columnall_p, cut_create)
            print(sql_cut_columnall_c)
            # list_sql = sql_all_c[0].split(',')
            return sql_cut_columnall_c

        except Exception as e:
            print('sql_cut_columnall error:', e)
            return '没有内容'
    else:
        return False #TODO 第二个false


# 对每个create语句进行截取英文表名语句
def sql_cut_tablename_E(cut_create):
    """
    截取英文表名
    :param cut_create:
    :return:
    """
    sql_tablename_r = r" *?create table (.*?) *?\("
    sql_tablename_p = re.compile(sql_tablename_r)
    sql_tablename_c = re.findall(sql_tablename_p, cut_create)
    print(sql_tablename_c)
    try:
        return sql_tablename_c[0]
    except Exception as e:
        print('sql_cut_tablename error:', e)
        return '没有英文表名'
    pass


# 对每个create语句进行截取中文表名语句
def sql_cut_tablename_C(cut_create):
    """
    截取中文表名
    :param cut_create:
    :return:
    """
    sql_tablename_r = r"\) *e.*?comment.*?'(.*?)';*"
    sql_tablename_p = re.compile(sql_tablename_r)
    sql_tablename_c = re.findall(sql_tablename_p, cut_create)
    print(sql_tablename_c)
    try:
        return sql_tablename_c[0]
    except Exception as e:
        print('sql_cut_tablename_C error:', e)
        return '没有中文表名'
    pass


# 对每个所有字段语句再截取成单个语句  传表
def sql_cut_columnone(cut_columnall):
    """
    将字段语句集截成单句，返回list
    :param cut_columnall:
    :return:
    """
    if cut_columnall:
        try:
            sql_cut_columnone_r = r"(.*?[ 'a-z])[,\)]"  # 创建字段语句单句提炼
            sql_cut_columnone_p = re.compile(sql_cut_columnone_r)
            sql_cut_columnone_c = re.findall(sql_cut_columnone_p, cut_columnall)
            print(sql_cut_columnone_c)
            return sql_cut_columnone_c
        except Exception as e:
            print('spl_cut_columnone error:', e)
            return False

    else:
        return False #TODO 第三个false


# 对每个字段语句进行分析
def sql_analyse(cut_columnone):
    """
    对每一个字段单句进行分析
    :param cut_columnone:
    :return:
    """
    if "primary key" in cut_columnone or "foreign key" in cut_columnone or 'references' in cut_columnone or 'key' in cut_columnone:
        return ''

    else:
        cut_columnone = cut_columnone.strip()
        #print(cut_columnone)
        error_print = '字段' + get_column_name(cut_columnone)

        null_flag = null_analyse(cut_columnone)
        comment_flag = comment_analyse(cut_columnone)
        after_comment_flag = after_comment_analyse(cut_columnone)
        auto_increment_flag = auto_increment_analyse(cut_columnone)
        both_flag = False
        if not null_flag:
            error_print += '没有null 或 not null，'

        if not comment_flag and not auto_increment_flag:
            error_print += '没有comment 或 自增标识, '
            if not after_comment_flag:
                error_print += '没有comment后注释'
        else:
            both_flag = True

        if null_flag and both_flag:
            return False
        else:
            print(error_print)
            return error_print


# 对字段语句进行null分析
def null_analyse(statement):
    """
    find 'null' or 'not null'
    :param statement:
    :return:
    """
    null_flag = 'null' in statement or 'not null' in statement
    return null_flag


# 对字段语句进行comment分析
def comment_analyse(statement):
    """
    find 'comment'
    :param statement:
    :return:
    """
    comment_flag = 'comment' in statement
    return comment_flag


# 对字段语句进行comment语句分析
def after_comment_analyse(statement):
    """
    find 'after_comment'
    :param statement:
    :return:
    """
    after_comment_r = r"comment +?'(.*?)'"
    after_comment_p = re.compile(after_comment_r)
    after_comment_c = re.findall(after_comment_p, statement)

    if after_comment_c:
        after_comment_c_flag = True
    else:
        after_comment_c_flag = False

    return after_comment_c_flag


# 对自增字段进行分析
def auto_increment_analyse(statement):
    """
    find 'auto_increment'
    :param statement:
    :return:
    """
    auto_increment_flag = 'auto_increment' in statement
    return auto_increment_flag




# 截取单句的字段名称
def get_column_name(statement):
    # filed_r = r'^ *?(\w+?) '
    # filed_p = re.compile(filed_r)
    # filed_c = re.findall(filed_p, statement)
    # print("file:" + filed_c[0])
    # return filed_c[0]
    """
    截取每个字段语句中的字段名
    :param statement:
    :return:
    """

    list = statement.split(' ')
    target = list[0].lower()
    return target


# 截取单句的类型
def get_type(statement):
    """
    截取每个字段语句中的类型
    :param statement:
    :return:
    """
    list = statement.split(' ')
    target = list[1].lower()
    #print("type:" + target)
    return target


# 传表，将每一个列表元素都变成一对kv对，然后加入到字典中，return一个字典
def add_as_dict(column_list):
    """
    将每个字段的字段名与类型组成键值对，一个table为一个dict
    :param column_list:
    :return:
    """
    dict = {}
    for statement in column_list:
        key = get_column_name(statement.strip())
        value = get_type(statement.strip())
        dict[key] = value
    return dict


def open_sql_file(path):
    # 打开读取sql文件
    str_s = ''
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for each_lines in f.readlines():
                str_s += each_lines

        file_sql = str_s.replace('\n', '').replace('\t', '')
        # print(file_sql)
    except Exception as e:
        return e
    return file_sql


if __name__ == '__main__':

    # test:
    #
    #
    #


    #target = 'date_last_update timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'
    #sql_analyse(target)
    pass


