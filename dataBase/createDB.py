# -*- coding = utf-8 -*-
# @Time:2021/3/315:59
# @Author:Linyu
# @Software:PyCharm

import pymysql

db = pymysql.connect(host='localhost',user='root',password='123456',port= 3306)
#利用cursor方法获取操作游标
cursor = db.cursor()
#这里的操作语句是获取版本号
# cursor.execute('SELECT VERSION()')
# #调用fetchone方法获取上述执行的数据
# data = cursor.fetchone()
# print('Database version:', data)
#创建数据库，数据库名为spiders，默认编码是utf-8
cursor.execute("CREATE DATABASE coreBooks CHARACTER SET utf8")
db.close()