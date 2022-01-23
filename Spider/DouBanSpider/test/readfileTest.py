# -*- coding = utf-8 -*-
# @Time:2021/2/2814:56
# @Author:Linyu
# @Software:PyCharm

import os
import xlwt
import re

def writeInxls(dic,sheetname):
    # file = open("../booklist/listURL.txt",encoding='utf-8')
    file = open(dic,encoding='utf-8')
    line = file.readline()
    i = 1
    titlepattern = re.compile('(.*)top10')

    workbook = xlwt.Workbook(encoding="utf-8")
    worksheet = workbook.add_sheet(sheetname)
    worksheet.write(0,0,"title")
    worksheet.write(0,1,"listUrl")

    while line:
        if re.match(titlepattern,line):
            title = re.findall(titlepattern,line)
            # print(title)
            # print(type(title))
            title = title[0]
            # print(type(title))
            worksheet.write(i,0,title)
        else:
            url = line
            worksheet.write(i,1,url)
            i = i+1
        line = file.readline()
    file.close()
    workbook.save('../booklist/listUrl.xls')
dic = "../booklist/listURL.txt"
tag = "标签列表"
writeInxls(dic,tag)