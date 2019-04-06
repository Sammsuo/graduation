from main_center.utils import common
from main_center.utils import readConfig
from main_center.utils import Log
import pymysql

Log = Log.MyLog()


class MyDB:
    def __init__(self):
        pro_config = readConfig.ReadConfig()
        global host, username, password, port, database, config
        host = pro_config.get_db("host")
        username = pro_config.get_db("username")
        password = pro_config.get_db("password")
        port = pro_config.get_db("port")
        database = pro_config.get_db("database")
        config = {
            'host': str(host),
            'user': username,
            'passwd': password,
            'port': int(port),
            'db': database,
            'charset': 'utf8'
        }
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.db = None
        self.cursor = None

    def connectDB(self):
        """
        connect to database
        :return:
        """
        try:
            # connect to DB
            self.db = pymysql.connect(**config)
            # create cursor
            self.cursor = self.db.cursor()
            # print("Connect DB successfully!")
        except ConnectionError as ex:
            print(str(ex))
            self.logger.error(str(ex))

    def executeSQL(self, sql, *params):
        """
        execute sql
        :param sql:
        :return:
        """
        self.connectDB()
        # executing sql

        try:
            self.cursor.execute(sql, params)
            # executing by committing to DB
            self.db.commit()
        except Exception as ex:
            self.logger.error(str(ex))
            print(repr(ex))
            self.db.rollback()
        finally:
            self.closeDB()

        return self.cursor

    def selectSQL_no_params(self, sql):
        """
        select sql
        :param sql:
        :return:
        """
        self.connectDB()

        try:
            self.cursor.execute(sql)
            res = self.get_all(self.cursor)
        except Exception as ex:
            self.logger.error(str(ex))
            print(repr(ex))
            self.db.rollback()
        finally:
            self.closeDB()
        return res

    def get_all(self, cursor):
        """
        get all result after execute sql
        :param cursor:
        :return:
        """
        value = cursor.fetchall()
        return value

    def get_one(self, cursor):
        """
        get one result after execute sql
        :param cursor:
        :return:
        """
        value = cursor.fetchone()
        return value

    def closeDB(self):
        """
        close database
        :return:
        """
        self.db.close()
        # print("Database closed!")

    def insert_zt_bug(self, *params):
        sql = common.get_sql(database, "zt_bug", "insert_bug")
        self.executeSQL(sql, *params)

    def insert_zt_case(self, *params):
        sql = common.get_sql(database, 'zt_case', 'insert_case')
        self.executeSQL(sql, *params)

    def insert_zt_casestep(self, *params):
        sql = common.get_sql(database, 'zt_casestep', 'insert_case_step')
        self.executeSQL(sql, *params)

    def select_id_by_openedDate(self):
        sql = common.get_sql(database, 'zt_case', 'get_id_by_openedDate')
        c = self.selectSQL_no_params(sql)[0][0]
        return c

    def conut_bug_by_month(self):
        sql = common.get_sql(database, 'zt_bug', 'count_bug_by_month')
        a = self.executeSQL(sql)
        c = self.get_all(a)
        return c

    def get_bug_style(self):
        sql = common.get_sql(database, 'zt_bug', 'get_bug_style')
        a = self.executeSQL(sql)
        c = self.get_all(a)
        return c

    def get_bug_all(self):
        sql = common.get_sql(database, 'zt_bug', 'get_bug_all')
        a = self.executeSQL(sql)
        c = self.get_one(a)
        return c

    def get_bug_up(self):
        sql = common.get_sql(database, 'zt_bug', 'get_bug_up')
        a = self.executeSQL(sql)
        c = self.get_one(a)
        return c

    def get_bug_down(self):
        sql = common.get_sql(database, 'zt_bug', 'get_bug_down')
        a = self.executeSQL(sql)
        c = self.get_one(a)
        return c

if __name__ == '__main__':
    a = MyDB()
    print(a.select_id_by_openedDate())
    print(type(a.conut_bug_by_month()))