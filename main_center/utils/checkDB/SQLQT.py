# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SQLQT.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import DDL_analyse as sql
import sys
import os

class Ui_SQLtest(object):
    def setupUi(self, SQLtest):
        SQLtest.setObjectName("SQLtest")
        SQLtest.resize(595, 420)
        self.gridLayout = QtWidgets.QGridLayout(SQLtest)
        self.gridLayout.setObjectName("gridLayout")

        self.pushButton = QtWidgets.QPushButton(SQLtest)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)

        self.pushButton_2 = QtWidgets.QPushButton(SQLtest)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.pushButton_3 = QtWidgets.QPushButton(SQLtest)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)

        self.outputbox = QtWidgets.QTextBrowser(SQLtest)
        self.outputbox.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.outputbox, 2, 0, 1, 3)
        self.inputbox = QtWidgets.QTextEdit(SQLtest)
        self.inputbox.setObjectName("textEdit")
        self.gridLayout.addWidget(self.inputbox, 0, 0, 1, 3)

        self.retranslateUi(SQLtest)
        self.pushButton.pressed.connect(self.but1_get)
        self.pushButton_2.pressed.connect(self.but2_get)
        self.pushButton_3.pressed.connect(self.but3_get)
        QtCore.QMetaObject.connectSlotsByName(SQLtest)

    def retranslateUi(self, SQLtest):
        _translate = QtCore.QCoreApplication.translate
        SQLtest.setWindowTitle(_translate("SQLtest", "Dialog"))
        self.pushButton.setText(_translate("SQLtest", "字段对比"))
        self.pushButton_2.setText(_translate("SQLtest", "建表语句"))
        self.pushButton_3.setText(_translate("SQLtest", "整个文件(输入文件路径)"))

    def but1_get(self):
        self.outputbox.clear()
        sql_all = self.inputbox.toPlainText()
        cut_create = sql.sql_cut_create(sql_all)  # 截出每个创表语句  传表
        #print(cut_create)

        if cut_create:
            tablename_list = []
            dict_list = []
            for sql_create_item in cut_create:  # 每个带有create字段的语句
                # print("sql_create_item:" + sql_create_item)
                C_table_name = sql.sql_cut_tablename_C(sql_create_item)  # 获取建表语句表名

                "添加表名"
                tablename_list.append(C_table_name)

                sql_column_all_item = sql.sql_cut_columnall(sql_create_item)  # List
                # print(sql_column_all_item)

                if sql_column_all_item:
                    for sql_columnone in sql_column_all_item:  # 传str
                        # print()
                        list_column = sql.sql_cut_columnone(sql_columnone)  # 截出每句返回列表
                        t_dict = sql.add_as_dict(list_column)
                        dict_list.append(t_dict)
                        # print(dict_list)
                        # print(tablename_list)



                else:
                    self.outputbox.insertPlainText('没找到相关的多表集') # 对第二个false进行判断

                for first in range(len(dict_list)):
                    # print(range(len(dict_list)))
                    # print(first)
                    for second in range(first, len(dict_list)):
                        # print(second)
                        if first == second:
                            continue
                        # print(first, second)
                        result = sql.get_dictkeys_set(dict_list[first], dict_list[second])
                        # print('差：', result)
                        if result == set():
                            pass
                        else:
                            for t in result:
                                self.outputbox.insertPlainText(tablename_list[first] + '    与    ' + tablename_list[second])
                                self.outputbox.insertPlainText('\n')
                                self.outputbox.insertPlainText('    ' + '字段' + t + '类型不相等' + '\n')


        else:
            self.outputbox.insertPlainText('没找到相关的建表语句')  # 对第一个false进行判断

    def but2_get(self):
        self.outputbox.clear()
        sql_all = self.inputbox.toPlainText()
        # print(sql_all)
        cut_create = sql.sql_cut_create(sql_all)  # 截出每个创表语句  传表
        # print(cut_create)

        if cut_create:
            for sql_create_item in cut_create:  # 每个带有create字段的语句
                print("sql_create_item:" + sql_create_item)
                C_table_name = sql.sql_cut_tablename_C(sql_create_item)  # 获取建表语句表名
                E_table_name = sql.sql_cut_tablename_E(sql_create_item)

                self.outputbox.insertPlainText(C_table_name)  # 在输出框中输出表名
                self.outputbox.insertPlainText(' ')
                self.outputbox.insertPlainText(E_table_name)
                self.outputbox.insertPlainText(' ')

                sql_column_all_item = sql.sql_cut_columnall(sql_create_item)  # List
                print(sql_column_all_item)

                if sql_column_all_item:

                    for sql_columnone in sql_column_all_item:  # 传str

                        list_column = sql.sql_cut_columnone(sql_columnone)  # 截出每句返回列表

                        output_flag = False
                        if sql_columnone:
                            for sql_column_item in list_column:
                                target = sql.sql_analyse(sql_column_item)

                                if target:      # 对单句输出内容进行判断,对第四个false进行判断
                                    output_flag = True
                                    self.outputbox.insertPlainText('\n' + '      ' + target)

                            if output_flag:
                                self.outputbox.insertPlainText('\n' + '完成' + '\n\n')
                            else:
                                self.outputbox.insertPlainText('\n' + '      ' + '无有问题字段' + '\n')
                        else:
                            self.outputbox.insertPlainText('没找到相关的单表字段集')
                else:
                    self.outputbox.insertPlainText('没找到相关的多表集') # 对第二个false进行判断
        else:
            self.outputbox.insertPlainText('没找到相关的建表语句')  # 对第一个false进行判断



    def but3_get(self):
        self.outputbox.clear()
        # 获取输入框中的文件地址
        f_path_native = self.inputbox.toPlainText()

        # 对文件地址进行加工
        f_path = f_path_native.replace(' ', '').replace('\n', '')
        # print(f_path)

        if f_path == '':
            self.outputbox.insertPlainText('没有输入')  # 判断输入框是否为空
        else:
            str_sql2 = sql.open_sql_file(f_path)  # 通过文件地址打开文件，对文件内容进行加工

            cut_create = sql.sql_cut_create(str_sql2)  # 截出每个创表语句  传表
            # print(cut_create)

            if cut_create:
                tablename_list = []
                dict_list = []
                for sql_create_item in cut_create:  # 每个带有create字段的语句
                    print("sql_create_item:" + sql_create_item)
                    C_table_name = sql.sql_cut_tablename_C(sql_create_item)  # 获取建表语句表名
                    E_table_name = sql.sql_cut_tablename_E(sql_create_item)

                    self.outputbox.insertPlainText(C_table_name)  # 在输出框中输出表名
                    self.outputbox.insertPlainText(' ')
                    self.outputbox.insertPlainText(E_table_name)
                    self.outputbox.insertPlainText(' ')

                    tablename_list.append(C_table_name)

                    sql_column_all_item = sql.sql_cut_columnall(sql_create_item)  # List
                    print(sql_column_all_item)

                    if sql_column_all_item:

                        for sql_columnone in sql_column_all_item:  # 传str

                            list_column = sql.sql_cut_columnone(sql_columnone)  # 截出每句返回列表

                            output_flag = False
                            if sql_columnone:
                                for sql_column_item in list_column:
                                    target = sql.sql_analyse(sql_column_item)

                                    if target:  # 对单句输出内容进行判断,对第四个false进行判断
                                        output_flag = True
                                        self.outputbox.insertPlainText('\n' + '      ' + target)

                                if output_flag:
                                    self.outputbox.insertPlainText('\n' + '完成' + '\n' + '\n')
                                else:
                                    self.outputbox.insertPlainText('\n' + '      ' + '无有问题字段' + '\n')
                            else:
                                self.outputbox.insertPlainText('没找到相关的单表字段集')
                    else:
                        self.outputbox.insertPlainText('没找到相关的多表集')  # 对第二个false进行判断

                    for first in range(len(dict_list)):
                        # print(range(len(dict_list)))
                        # print(first)
                        for second in range(first, len(dict_list)):
                            # print(second)
                            if first == second:
                                continue
                            # print(first, second)
                            result = sql.get_dictkeys_set(dict_list[first], dict_list[second])
                            # print('差：', result)
                            if result == set():
                                pass
                            else:
                                for t in result:
                                    self.outputbox.insertPlainText(tablename_list[first] + '    与    ' + tablename_list[second])
                                    self.outputbox.insertPlainText('\n')
                                    self.outputbox.insertPlainText('    ' + '字段' + t + '类型不相等' + '\n')
            else:
                self.outputbox.insertPlainText('没找到相关的建表语句')  # 对第一个false进行判断


if __name__ == '__main__':
    print(os.getcwd())
    app = QApplication(sys.argv)
    Dialog = QDialog()

    ui = Ui_SQLtest()
    ui.setupUi(Dialog)

    Dialog.show()
    sys.exit(app.exec_())
