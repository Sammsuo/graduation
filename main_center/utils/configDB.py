from main_center.utils import common
from main_center.utils import readConfig
import pymysql


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
        # self.log = Log.get_log()
        # self.logger = self.log.get_logger()
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
            # self.logger.error(str(ex))

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
            # self.logger.error(str(ex))
            print(repr(ex))
            self.db.rollback()
        finally:
            self.closeDB()

        return self.cursor

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