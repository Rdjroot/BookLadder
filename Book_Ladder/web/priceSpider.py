# -*- coding = utf-8 -*-
# @Time:2021/3/1821:55
# @Author:Linyu
# @Software:PyCharm
'''
爬取各个售书网站的实时最低价
'''
import requests
import urllib
# from fake_useragent import UserAgent
import random
from bs4 import BeautifulSoup
import re
import lxml
from web.models import  Modle


#获取整个HTML文件的方法
def askURL(url):
    # ua = UserAgent()
    # ua = ua.random
    # number = random.randint(1,9)
    #装作响应头
    head1  = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    }
    # head2 = {
    #     "User-Agent": ua
    # }
    # if number%2:
    #     head= head1
    # else:
    #     head = head2
    #封装request对象
    request = requests.get(url , headers = head1)
    html = ""
    try:
        #获取网页源代码文档
        html = request.text
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

def spiderJD(jdlink):
    print("爬虫调用中……")
    html = askURL(jdlink)
    soup = BeautifulSoup(html,'html.parser')
    if soup.find_all(attrs={'class':'check-error'}):
        price = '暂无数据'
        return price
    else:
        ul = soup.find_all(attrs={'class':'gl-warp clearfix'})[0]
        li = ul.find_all(attrs={'class':'gl-item'})[0]
        price = li.find_all(attrs={'class':'p-price'})[0]
        priceI = price.i.text
        priceB = priceI + "起"
        return priceB

# def spiderKFZ(kfzlink):
#     html = askURL(kfzlink)
#     soup =  BeautifulSoup(html,'lxml')
#     print(soup)
#     if soup.find_all(attrs={'class':'result-list'}):
#         div = soup.find_all(attrs={'class':'result-list'})[0]
#         divLow = div.find_all(name='div')[0]
#         # print(divLow)
#         # priceback =divLow.attrs['price']
#         # return priceback
#     else:
#         back = "暂无数据"
#         return back

def spiderDD(ddlink):

    #正则表达式
    # pattern = re.compile(r'.*?'+title+'.*?',re.I)

    html = askURL(ddlink)
    soup = BeautifulSoup(html,'lxml')
    checkSpan = ""
    if soup.find_all(attrs={'class':'result_none'}):
        check = soup.find_all(attrs={'class':'result_none'})[0]
        checkSpan = check.span
    if checkSpan:
        errorInfo = "暂无数据"
        return errorInfo
    else:
        # ul = soup.find_all(attrs={'class':'bigimg'})[0]
        # print(soup)
        li = soup.find_all(attrs={'class':'line1'})[0]
        # a = li.a
        # titleMat = a['title']                #可以用于验证，后期加强
        prispan = li.find_all(attrs={'class':'search_now_price'})[0]
        price = prispan.text
        price = price + "起"
        return price


def spider(isbn):

    '''
    sql = 'select title from allbook where isbn = %s'%(isbn)
    testData = Modle().query(sql)
    title = testData[0][0]
    '''

    jd = "https://search.jd.com/Search?keyword=%s&psort=2&click=0"%(isbn)
    # kfz = "http://search.kongfz.com/product_result/?key=%s&order=100&perfect=1"%(isbn)
    dd = "http://search.dangdang.com/?key=%s&act=input&sort_type=sort_xlowprice_asc#J_tab"%(isbn)

    # amz = "https://www.amazon.cn/s?k=%s"%(isbn)
    # print(dd)
    JDprice = spiderJD(jd)
    DDprice = spiderDD(dd)
    priceDic = {
        'jd':JDprice,
        'dd':DDprice
    }
    return priceDic
