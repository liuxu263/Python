#!
# -*- coding=utf-8 -*-

""" """

__author__ = ''

'''
Python DB-API使用流程：

引入 API 模块。
获取与数据库的连接。
执行SQL语句和存储过程。
关闭数据库连接。

'''

import MySQLdb

db = MySQLdb.connect("ip", "用户名", "密码", "数据库名称", charset='utf8')

cursor = db.cursor()

sql1 = "select * from table where 1=1"

try:
    cursor.execute(sql1)
    data = cursor.fetchone()
    results = cursor.fetchall()
except Exception:
    print(Exception)
    print("")
finally:
    pass

value0 = ""
sql2 = "insert into table (id) values (%s) where 1=1 " % value0

value1 = ""
value2 = ""

sql3 = " insert into table values (%s,%s) where 1=1" % (value1, value2)

sql4 = "update table set id = 1 where 1=1"

sql5 = "delete from table where 1=1"

try:
    cursor.execute(sql2)
    db.commit()
except Exception:
    print(Exception)
    db.rollback()
finally:
    pass

db.close()
