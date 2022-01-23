# -*- coding = utf-8 -*-
# @Time:2021/3/315:50
# @Author:Linyu
# @Software:PyCharm

import pandas as pd
from sqlalchemy import create_engine
import pymysql

#读取Excel表格数据
excelFile = 'coreBook.xls'
df = pd.DataFrame(pd.read_excel(excelFile))

#写入数据库
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/coreBooks',encoding='utf8')
df.to_sql('corebook',con=engine,if_exists='replace',index=False)
