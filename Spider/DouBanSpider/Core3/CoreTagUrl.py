# -*- coding = utf-8 -*-
# @Time:2021/2/2815:43
# @Author:Linyu
# @Software:PyCharm

#爬取各种top10 的书籍，并且是核心书单的链接
from MergeUrl_2 import MergeUrlList
from findWord import findWord
import re
import time
import xlwt
import xlrd
from xlutils.copy import copy

#难点：一个xls表格包含多个sheet
#需要读取的数据：分类，书名（生成url)，以及supports
#findurl以后
#查找数据时，传递进去的参数还要包括supports，core标志符，类别可以先忽略
#防止被发现爬虫代理，我将把找到详情页链接，和获取内容，分开
def write_to_excel(dataList,outfile):
    workbook = xlwt.Workbook(encoding='utf-8')
    sheetname = dataList[0]
    worksheet = workbook.add_sheet(sheetname)
    i = 0
    for data in dataList:
        worksheet.write(i,0,data)
        i = i+1
    workbook.save(outfile)

def write_add_excel(dataList,outfile):
    rb = xlrd.open_workbook(outfile, formatting_info=True)
    workbook = copy(rb)
    sheetname = dataList[0]
    worksheet = workbook.add_sheet(sheetname)
    i = 0
    for data in dataList:
        worksheet.write(i,0,data)
        i = i+1
    workbook.save(outfile)

def getUrl(filename,outfile):
    #将list里的内容读取出来
    # filename = "../booklist/list1.xls"
    #返回的list里包含几个list，一个list就是一张表的信息
    AllList = MergeUrlList(filename)
    #遍历AllList ,一个list就是一张表
    #目前，已经轮到k8,和编号70了
    #前两个元素一定是标签和支持数，利用findWord，找到详情页
    #弄出一个正则表达式，传入匹配参数
    pattern = re.compile('https://www.douban.com/search[?]cat=1001&q=(.*)',re.S)
    i = 0
    for list in AllList:
        swashList = []
        listInfo = list[0:2]
        listurl = list[2:]
        anwserList = []
        for url in listurl:
            strin = re.findall(pattern,url)
            strin = strin[0]    #校验参数
            strin = str(strin)
            print(strin)
            anwserUrl = findWord(url,strin)
            print(anwserUrl)
            anwserList.append(anwserUrl)
            time.sleep(1)
        swashList = listInfo+anwserList
        if i <1:
            write_to_excel(swashList,outfile)
        else:
            write_add_excel(swashList,outfile)
        i = i+1
        time.sleep(20)
