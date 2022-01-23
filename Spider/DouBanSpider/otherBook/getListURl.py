# -*- coding = utf-8 -*-
# @Time:2021/3/215:18
# @Author:Linyu
# @Software:PyCharm

from askURL import askURL
from bs4 import BeautifulSoup
import time
import xlwt

# list = 'https://www.douban.com/doulist/178565/'
# list = 'https://www.douban.com/doulist/176513/'
# list ='https://www.douban.com/doulist/136762477/'
list = 'https://www.douban.com/doulist/1757387/'
lists = []


lists.append(list)


def write_to_excel(backlists):
    workbook = xlwt.Workbook(encoding="utf-8")
    # worksheet = workbook.add_sheet("机器学习与人工智能")
    # worksheet = workbook.add_sheet("推理链接")
    # worksheet = workbook.add_sheet("好书")
    worksheet = workbook.add_sheet("高分书籍")
    i = 1
    for listurl in  backlists:
        worksheet.write(i,0,listurl)
        i = i+1
    # workbook.save('otherList.xls')
    workbook.save('otherList3.xls')


def getListURl(lists):

    listUrl = lists[0]

    if len(lists)>1:
        listInfo = lists[1:]
        print("继承了上一次的内容")
        # print(listInfo)
    else:
        listInfo = []

    html  = askURL(listUrl)
    soup = BeautifulSoup(html,"html.parser")
    # print(soup)
    pageUrl = []
    doulists  = soup.find_all(attrs={'class':'doulist-item'})[0:]
    key = 0
    for doulist in doulists:
        #如果存在的话
        if doulist.find_all(attrs={'class':'title'}):
            # print("有问题")
            title = doulist.find_all(attrs={'class':'title'})[0]
            link = title.a['href']
            pageUrl.append(link)
            key = 1
            # print(link)
        else:
            continue
    if key:
        print("运行了一次")
        print(pageUrl)



    flag = 0
    if soup.find_all(attrs={'class':'paginator'}):
        paginato = soup.find_all(attrs={'class':'paginator'})[0]
        span = paginato.find_all(attrs={'class':'next'})[0]
        if span.a:
            linka = span.a['href']
            flag = 1
            nextUrl = linka
            print("有下一页")
            print(nextUrl)

    backlist = []
    if flag ==1:
        backlist.append(nextUrl)
        backlist = backlist + listInfo
        backlist = backlist+pageUrl
        print("再次调用的lists")
        print(backlist)
        time.sleep(5)
        getListURl(backlist)
    else:
        backlist = listInfo + pageUrl
        print("最后一次啊调用")
        print(listInfo)
        print(pageUrl)
        print(type(backlist))
        print("调用结束")
        write_to_excel(backlist)


getListURl(lists)
