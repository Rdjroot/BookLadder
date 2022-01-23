# -*- coding = utf-8 -*-
# @Time:2021/3/1417:56
# @Author:Linyu
# @Software:PyCharm


from web.pageutils import BooksScore
from web.pageutils import BooksCount
from web.pageutils import pointsDraw
from web.pageutils import scoreRelise
from web.pageutils import messBarInfo
from web.pageutils import tagRader
from web.models import tagThree
from web.wdCloud import infoCloud
from web.priceSpider import spider
from web.models import Dict
from web.models import Modle
from web.priceSpider import spiderDD


#用围城做测试
isbn = "'9787020090006'"
dd = "http://search.dangdang.com/?key=%s&act=input&sort_type=sort_xlowprice_asc#J_tab"%(isbn)
ddPrice = spiderDD(dd)
print(ddPrice)
# sql = 'select title from allbook where isbn = %s'%(isbn)
# print(sql)
# testData = Modle().query(sql)
# print(testData[0][0])


# title = "'活着'"
# sqlNum = 'select id_num from corebook where title = %s'%(title)
# id_num = Modle().query(sqlNum)
# print(id_num[0][0])
# print(scoreRelise())
# print(BooksScore())
# print(BooksCount())
# print(pointsDraw())
# messBar()
# print(messBar())
# tagRader()
# tagThree("小说")
# infoCloud('代码大全（第2版）')
# print(spider('9787108009821'))
# dic = Dict()
# for key in dic.keys():
#     print(key)
#     print(dic[key])
