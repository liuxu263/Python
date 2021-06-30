#!
# -*- coding = utf-8 -*-

""" """

__author__ = 'lx'

import pymysql

"""
Python DB-API使用流程：

引入 API 模块。
获取与数据库的连接。
执行SQL语句和存储过程。
关闭数据库连接。

"""

database_host = None
database_user = None
database_password = None
database_base_name = None

db = pymysql.connect(host=database_host,
                     user=database_user,
                     password=database_password,
                     db=database_base_name,
                     use_unicode='utf8')
cursor = db.cursor()


def func1():
    sql1 = "select * from table where 1=1"
    sql2 = "select * from table where 1=1 limit 0,10"
    sql3 = "select * from table where 1=1 order by xx desc"
    sql4 = "select max(xx) from table where 1=1 order by yy desc"
    sql5 = "select min(xx) from table where 1=1 order by yy desc"
    sel6 = "select avg(xx) from table where 1=1"
    sql7 = "select sum(xx) from table where 1=1"
    sql8 = "select count(xx) from table where 1=1"
    sql9 = "select * from table where 1=1 group by xx"
    sql10 = "select * from table where 1=1 group by xx having yy"
    params = ()
    result = ""
    results = ""
    try:
        # 执行sql
        cursor.execute()
        # cursor.execute(sql1, params)
        result = cursor.fetchone()
        results = cursor.fetchall()
    except IOError as e:
        print(e)
        print("读数据失败")
    finally:
        return result, results


def func2():
    sql1 = "insert into table id values (%s)"
    sql2 = " insert into table (id,name) values (%s,%s)"
    sql3 = " insert into table (id,name) values (%s,%s), (%s,%s) on duplicate key update name = %s"
    params = ()
    try:
        cursor.execute(sql1, params)
        db.commit()
    except IOError as e:
        print(e)
        db.rollback()
    finally:
        db.close()


def func3():
    sql1 = "update table set xx = %s where id = %s"
    sql2 = "update table set xx = %s , yy = %s where id = %s"
    params = ()


def func4():
    sql1 = "delete from table where 1=1"
    params = ()


if __name__ == '__main__':
    pass
