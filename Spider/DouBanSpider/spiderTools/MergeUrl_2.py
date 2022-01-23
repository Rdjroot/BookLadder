# -*- coding = utf-8 -*-
# @Time:2021/3/113:52
# @Author:Linyu
# @Software:PyCharm

import xlrd
import re

#测试用
# filename = "../Core3/partList/list1Url.xls"


#将Excel表格中的内容读取出来
#合成一个新的搜索链接
#这里包含一个xls文件里面所有的内容
def MergeUrlList(filename):
    baseurl = "https://www.douban.com/search?cat=1001&q="
    workbook = xlrd.open_workbook(filename= filename)
    #获取所有的sheet名字
    sheets = workbook.sheet_names()
    xlsfileList = []
    number = len(sheets)
    count = 0
    for sheet in sheets:
        if count >= number:
            break
        sheetList = []
        sheetbox = workbook.sheet_by_name(sheet)        #定位到该sheet
        sheetList.append(sheet)     #在列表中传入类别名

        supports = sheetbox.col_values(1)
        support = int(supports[1])
        sheetList.append(support)       #获取支持数

        titlecols = sheetbox.col_values(0)
        for title in titlecols:
            if title=="书名":
                continue
            else:
                # print(title)
                # print(type(title))
                title = str(title)
                title = title.strip()
                titleurl = baseurl +title
                sheetList.append(titleurl)
        xlsfileList.append(sheetList)
        count = count + 1
    return xlsfileList
    # print(xlsfileList)


def MergeUrlList_2(filename):
    workbook = xlrd.open_workbook(filename= filename)
    sheets = workbook.sheet_names()     #获取所有的sheet

    #将Excel文件里的内容全部弄到一个列表中
    xlsfileList = []

    #防止溢出
    number = len(sheets)
    count = 0

    for sheet in sheets:
        if count >= number:
            break
        #一个sheet里的内容存在一个列表中
        sheetList = []
        sheetbox = workbook.sheet_by_name(sheet)
        infocols = sheetbox.col_values(0)

        for info in infocols:
            if info == infocols[1]:
                info  = int(info)
            sheetList.append(info)
        xlsfileList.append(sheetList)
        count = count + 1
    # print(xlsfileList)
    return xlsfileList

def MergeSimple(filename):
    workbook = xlrd.open_workbook(filename= filename)
    sheet = workbook.sheet_by_index(0)
    sheetname = workbook.sheet_names()
    sheetname = sheetname[0]
    infocols = sheet.col_values(0)
    useInfos = infocols[1:]
    lastInfos = []
    lastInfos.append(sheetname)
    lastInfos = lastInfos +useInfos
    return lastInfos

# key  = MergeSimple('../otherBook/originURl/otherList.xls')
# print(key)
# MergeUrlList_2(filename)