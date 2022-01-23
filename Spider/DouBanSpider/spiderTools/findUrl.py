# -*- coding = utf-8 -*-
# @Time:2021/2/2815:49
# @Author:Linyu
# @Software:PyCharm

import askURL
from bs4 import BeautifulSoup
import re
import lxml

#找到app书单中的书籍详情页链接
def findUrl(link):
    #除了链接，还要获取supports数量
    suppattern = re.compile('.*· (.*)人关注')
    html = askURL.askURL(link)
    print(html)
    # soup = BeautifulSoup(html,"")
    # print(soup)
    # app = soup.find_all(attrs={'class':'page'})[0]
    # print(app)
    # focus =soup.find_all(attrs={'class':'_3vpeC'})
    # print(type(focus))
    # print(focus)
    # print(focus.text)


#测试
link = "https://m.douban.com/subject_collection/ECXUOFVNY"
findUrl(link)