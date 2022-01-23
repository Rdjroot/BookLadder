# -*- coding = utf-8 -*-
# @Time:2021/2/2519:57
# @Author:Linyu
# @Software:PyCharm

import xlwt
import xlrd
from xlutils.copy import copy

#参数要输出的文件地址，信息字典，sheet名字，书籍编号，核心标志符，supports信息
def write_to_excel(fileaddr,datalist,sheetname,num):
    workbook = xlwt.Workbook(encoding="utf-8")
    worksheet = workbook.add_sheet(sheetname= sheetname)
    worksheet.write(0,0,"number")
    worksheet.write(0,1,"title")
    worksheet.write(0,2,"author")
    worksheet.write(0,3,"publish")
    worksheet.write(0,4,"pubyear")
    worksheet.write(0,5,"trans")
    worksheet.write(0,6,"isbn")
    worksheet.write(0,7,"score")
    worksheet.write(0,8,"commnum")
    worksheet.write(0,9,"sumper")
    worksheet.write(0,10,"tag1")
    worksheet.write(0,11,"tag2")
    worksheet.write(0,12,"tag3")
    worksheet.write(0,13,"tag4")
    worksheet.write(0,14,"tag5")
    worksheet.write(0,15,"tag6")
    worksheet.write(0,16,"tag7")

    i = 1
    for items in datalist:
        worksheet.write(i, 0, num)
        worksheet.write(i, 1, items["title"])
        worksheet.write(i,2,items["author"])
        worksheet.write(i,3,items["publish"])
        worksheet.write(i,4,items["pubYear"])
        worksheet.write(i,5,items["trans"])
        worksheet.write(i,6,items["isbn"])
        worksheet.write(i,7,items["score"])
        worksheet.write(i,8,items["commNum"])
        worksheet.write(i,9,items["sumPer"])
        worksheet.write(i,10,items["imgLink"])
        tagN = 11
        for tag in items["tag"]:
            worksheet.write(i,tagN,tag)
            tagN = tagN+1
        num = num+1
        i = i+1
    workbook.save(fileaddr)
    infoNum = num
    return infoNum

#参数要输出的文件地址，信息字典，sheet名字，书籍编号，核心标志符，supports信息
def write_add_excel(fileaddr,datalist,sheetname,num):
    rb = xlrd.open_workbook(fileaddr, formatting_info=True)
    workbook = copy(rb)
    worksheet = workbook.add_sheet(sheetname)
    worksheet.write(0,0,"number")
    worksheet.write(0,1,"title")
    worksheet.write(0,2,"author")
    worksheet.write(0,3,"publish")
    worksheet.write(0,4,"pubyear")
    worksheet.write(0,5,"trans")
    worksheet.write(0,6,"isbn")
    worksheet.write(0,7,"score")
    worksheet.write(0,8,"commnum")
    worksheet.write(0,9,"sumper")
    worksheet.write(0,10,"tag1")
    worksheet.write(0,11,"tag2")
    worksheet.write(0,12,"tag3")
    worksheet.write(0,13,"tag4")
    worksheet.write(0,14,"tag5")
    worksheet.write(0,15,"tag6")
    worksheet.write(0,16,"tag7")

    i = 1
    for items in datalist:
        worksheet.write(i, 0, num)
        worksheet.write(i, 1, items["title"])
        worksheet.write(i,2,items["author"])
        worksheet.write(i,3,items["publish"])
        worksheet.write(i,4,items["pubYear"])
        worksheet.write(i,5,items["trans"])
        worksheet.write(i,6,items["isbn"])
        worksheet.write(i,7,items["score"])
        worksheet.write(i,8,items["commNum"])
        worksheet.write(i,9,items["sumPer"])
        worksheet.write(i,10,items["imgLink"])
        tagN = 11
        for tag in items["tag"]:
            worksheet.write(i,tagN,tag)
            tagN = tagN+1
        num = num+1
        i = i+1
    workbook.save(fileaddr)
    infoNum = num
    return infoNum