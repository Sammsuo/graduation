# -*- coding : utf-8 -*-

import re
from functools import reduce


class SQL_Cut():

    # 对整个输入框内容进行截取create整个语句,截取每个[create-;]  返回list
    def sql_cut_create(sql_all):
        """
        截取每个创表语句，返回list
        :param sql_all:
        :return:
        """

        sql_all = sql_all.replace('\t', '').replace('\n', '').replace('`', '').lower()  # 对输入的内容进行修改
        # print(sql_all)
        try:
            sql_cut_create_r = r".*?(create table.*?);"
            sql_cut_create_p = re.compile(sql_cut_create_r)
            sql_cut_create_c = re.findall(sql_cut_create_p, sql_all)
            # print('sql_cut_create_c : ' + sql_cut_create_c[0])
            return sql_cut_create_c

        except Exception as e:
            print('sql_cut_create error:', e)
            # print(sql_cut_create_c)
            return False  # TODO 第一个false



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
            return False  # TODO 第三个false

