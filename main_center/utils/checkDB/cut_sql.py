# -*- coding : utf-8 -*-

import re
from functools import reduce


class SQLCut:
    def sql_cut_create(self, sql_all):
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

    def sql_cut_columnall(self, cut_create):
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

    def sql_cut_tablename_E(self, cut_create):
        """
        对每个create语句进行截取英文表名语句
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

    def sql_cut_tablename_C(self, cut_create):
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

    def sql_cut_columnone(self, cut_columnall):
        """
        将字段语句集截成单句，返回list
        :param cut_columnall:
        :return:
        """
        if cut_columnall:
            try:
                sql_cut_columnone_r = r"(.*?[ 'a-z][\)]*'),"  # 创建字段语句单句提炼
                sql_cut_columnone_p = re.compile(sql_cut_columnone_r)
                sql_cut_columnone_c = re.findall(sql_cut_columnone_p, cut_columnall)
                print(sql_cut_columnone_c)
                return sql_cut_columnone_c
            except Exception as e:
                print('spl_cut_columnone error:', e)
                return False

        else:
            return False  # TODO 第三个false

    def sql_analyse(self, cut_columnone):
        """
        对每一个字段单句进行分析
        :param cut_columnone:
        :return:
        """
        if "primary key" in cut_columnone or "foreign key" in cut_columnone or 'references' in cut_columnone or 'key' in cut_columnone:
            return ''

        else:
            cut_columnone = cut_columnone.strip()
            # print(cut_columnone)
            error_print = '【字段】' + self.get_column_name(cut_columnone)

            null_flag = self.null_analyse(cut_columnone)
            comment_flag = self.comment_analyse(cut_columnone)
            after_comment_flag = self.after_comment_analyse(cut_columnone)
            auto_increment_flag = self.auto_increment_analyse(cut_columnone)
            both_flag = False
            if not null_flag:
                error_print += '【没有null 或 not null】，'

            if not comment_flag and not auto_increment_flag:
                error_print += '【没有comment 或 自增标识】, '
                if not after_comment_flag:
                    error_print += '【没有comment后注释】'
            else:
                both_flag = True

            if null_flag and both_flag:
                return False
            else:
                print(error_print)
                return error_print

    def null_analyse(self, statement):
        """
        find 'null' or 'not null'
        :param statement:
        :return:
        """
        null_flag = 'null' in statement or 'not null' in statement
        return null_flag

    def comment_analyse(self, statement):
        """
        find 'comment'
        :param statement:
        :return:
        """
        comment_flag = 'comment' in statement
        return comment_flag

    def after_comment_analyse(self, statement):
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

    def auto_increment_analyse(self, statement):
        """
        find 'auto_increment'
        :param statement:
        :return:
        """
        auto_increment_flag = 'auto_increment' in statement
        return auto_increment_flag

    def get_column_name(self, statement):
        """
        截取每个字段语句中的字段名
        :param statement:
        :return:
        """

        list = statement.split(' ')
        target = list[0].lower()
        return target

    def get_type(self, statement):
        """
        截取每个字段语句中的类型
        :param statement:
        :return:
        """
        list = statement.split(' ')
        target = list[1].lower()
        # print("type:" + target)
        return target

    def add_as_dict(self, column_list):
        """
        将每个字段的字段名与类型组成键值对，一个table为一个dict
        :param column_list:
        :return:
        """
        dict = {}
        for statement in column_list:
            key = self.get_column_name(statement.strip())
            value = self.get_type(statement.strip())
            dict[key] = value
        return dict

    def get_dictkeys_set(self, dict1, dict2):
        """
        两个字典进行key与item比较，得出两个集合，若集合间有差集证明差集为同字段名不同类型字段
        :param dict1:
        :param dict2:
        :return:
        """
        set_target = set()
        target_key = reduce(lambda x, y: x & y, [dict1.keys(), dict2.keys()])
        print(len(target_key))
        target_items = reduce(lambda x, y: x & y, [dict1.items(), dict2.items()])
        print(len(target_items))
        for a in target_items:
            set_target.add(a[0])

        target = target_key - set_target
        return target

    # 获取set然后对应的字典中对比键值
    def get_value_cmp(self, set):
        pass

    def open_sql_file(self, path):
        """
        打开sql文件,DDL
        :param path:
        :return:
        """
        # 打开读取sql文件
        str_s = ''
        try:
            with open(path, 'r', encoding='utf-8') as f:
                for each_lines in f.readlines():
                    str_s += each_lines

            # file_sql = str_s.replace('\n', '').replace('\t', '')
            # print(file_sql)
        except Exception as e:
            return e
        return str_s

    def resole_all(self, sql_content):
        cut_create = self.sql_cut_create(sql_content)
        tablename_list = []
        if cut_create:
            for sql_create_item in cut_create:  # 每个带有create字段的语句
                table_list = []
                # print("sql_create_item:" + sql_create_item)
                C_table_name = self.sql_cut_tablename_C(sql_create_item)  # 获取建表语句表名
                E_table_name = self.sql_cut_tablename_E(sql_create_item)

                # self.outputbox.insertPlainText(C_table_name)  # 在输出框中输出表名
                # self.outputbox.insertPlainText(' ')
                # self.outputbox.insertPlainText(E_table_name)
                # self.outputbox.insertPlainText(' ')
                table_list.append('【中文表名】 : \n' + C_table_name + '\n')
                table_list.append('【英文表名】 : ' + E_table_name + '\n')
                # tablename_list.append(C_table_name)

                sql_column_all_item = self.sql_cut_columnall(sql_create_item)  # List
                # print(sql_column_all_item)

                if sql_column_all_item:
                    for sql_columnone in sql_column_all_item:  # 传str
                        list_column = self.sql_cut_columnone(sql_columnone)  # 截出每句返回列表
                        output_flag = False
                        if sql_columnone:
                            for sql_column_item in list_column:
                                target = self.sql_analyse(sql_column_item)
                                if target:  # 对单句输出内容进行判断,对第四个false进行判断
                                    output_flag = True
                                    # self.outputbox.insertPlainText('\n' + '      ' + target)
                                    table_list.append('\n' + '      ' + target)
                            if output_flag:
                                # self.outputbox.insertPlainText('\n' + '完成' + '\n' + '\n')
                                table_list.append('\n' + '【完成】' + '\n' + '\n')
                            else:
                                # self.outputbox.insertPlainText('\n' + '      ' + '无有问题字段' + '\n')
                                table_list.append('      ' + '【无有问题字段】' + '\n' + '\n')
                        else:
                            # self.outputbox.insertPlainText('没找到相关的单表字段集')
                            table_list.append('【没找到相关的单表字段集】')
                    tablename_list.append(table_list)
                else:
                    # self.outputbox.insertPlainText('没找到相关的多表集')  # 对第二个false进行判断
                    table_list.append('【没找到相关的多表集】')
                    tablename_list.append(table_list)
        else:
            # self.outputbox.insertPlainText('没找到相关的建表语句')  # 对第一个false进行判断
            tablename_list.append('没找到相关的建表语句')
        return tablename_list

    def change_show_style(self, k):
        print(type(k))
        a_after_list = ''
        for i in k:
            after_list = ''.join(i)
            a_after_list += after_list
        return a_after_list


if __name__ == '__main__':
    pass
