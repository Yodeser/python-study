# -*- coding: utf-8 -*-
# //todo
# Created 0:31, 2018/5/13 by Yodes Yang
# About using of mysql in py3: https://www.jianshu.com/p/4490957e29ad
import pymysql
import base64
from q0001_Generate_activeCode import ActiveCode


class MysqlCase(object):

    @classmethod
    def get_connect(cls):
        connect = pymysql.connect(
            host="localhost",
            user="root",
            password=bytes.decode(base64.b64decode(b'MDIyMA=='), "utf8"),
            database="py3study",
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
        return connect

    def insert(self):
        sql = "INSERT INTO produce_ids(identify_code) VALUES (%s)"
        db = self.get_connect()
        cursor = db.cursor()
        codes = ActiveCode.generate_code()
        # noinspection PyBroadException
        try:
            for code in codes:
                cursor.execute(sql, code)
            db.commit()
        except BaseException:
            print("提交失败")
            db.rollback()
        finally:
            db.close()

        return

    def query(self):
        sql = "SELECT * FROM produce_ids"
        db = self.get_connect()
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()
        finally:
            pass

        return cursor.fetchall()


sql_case = MysqlCase()
print(sql_case.query())
# insert()
print(sql_case.query())
