# -*- coding = utf-8 -*-
# @Time:2021/2/2516:24
# @Author:Linyu
# @Software:PyCharm

import xlrd
import re

# file = '../fileOrigin/CoreBook.xls'
#将Excel表格中的内容读取出来
#合成一个新的搜索链接
def MergeUrl(filename,num):
    baseurl = "https://www.douban.com/search?q="
    workbook = xlrd.open_workbook(filename= filename)
    #通过索引获取表格
    sheet1= workbook.sheet_by_index(num)
    # sheet2 = workbook.sheet_by_name('数据分析')     #通过表格名获取表格
    titlecols = sheet1.col_values(0)     #获取书名列
    pattern = re.compile('《(.*)》',re.S)
    titlelist = []
    for title in titlecols:
        if title=="书名":
            continue
        if re.match(pattern,title):
            title1 = re.findall(pattern,title)
            title1 = title1[0]
            titlelist.append(title1)
        else:
            titlelist.append(title)
    # print(titlelist)
    titleUrl = []
    for title in titlelist:
        url = baseurl + title
        titleUrl.append(url)
    titleLink = titleUrl + titlelist
    return titleLink


def backUrl(filename,sheetnum):
    workbook = xlrd.open_workbook(filename= filename)
    #通过索引获取表格
    sheet= workbook.sheet_by_index(sheetnum)
    titlecols = sheet.col_values(0)     #获取书名列
    urlcols = sheet.col_values(1)       #获取链接列
    titleCols = titlecols[1:]
    urlCols = urlcols[1:]

    datalist = []
    for i in range(0,len(titleCols)-1):
        mapping = {}
        mapping['title']  = titleCols[i]
        mapping['url'] = urlCols[i].strip()
        list.append(mapping)
    return datalist

#以下为测试内容
# filename = "../booklist/listUrl.xls"
# sheetname = 0
# backUrl(filename,sheetname)