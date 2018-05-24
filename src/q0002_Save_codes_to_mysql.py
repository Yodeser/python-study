# -*- coding: utf-8 -*-
# //todo
# Created 0:31, 2018/5/13 by Yodes Yang
# About using of mysql in py3: https://www.jianshu.com/p/4490957e29ad
import pymysql
import base64
from q0001_Generate_activeCode import generate_code


def get_connect():
    connect = pymysql.connect(
        host="localhost",
        user="root",
        password=bytes.decode(base64.b64decode(b'MDIyMA=='), "utf8"),
        database="py3study",
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor
    )
    return connect


def insert():
    sql = "INSERT INTO produce_ids(identify_code) VALUES (%s)"
    db = get_connect()
    cursor = db.cursor()
    codes = generate_code()
    try:
        for code in codes:
            cursor.execute(sql, code)
        db.commit()
    except:
        print("提交失败")
        db.rollback()
    db.close()
    return


def query():
    sql = "SELECT * FROM produce_ids"
    db = get_connect()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    return cursor.fetchall()


print(query())
insert()
print(query())
