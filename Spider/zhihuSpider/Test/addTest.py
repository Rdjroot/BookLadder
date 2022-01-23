# -*- coding = utf-8 -*-
# @Time:2021/2/2220:23
# @Author:Linyu
# @Software:PyCharm

#用于测试，在已经存在的Excel文件，写入新东西
import xlrd
import xlwt
from xlwt import Style
from xlutils.copy import copy
import os

#成功，逻辑是，先打开一个工作区，在复制到一个另一个对象上
#指定sheet,写入，最后存储
def writeExcel(row, col, str):
    rb = xlrd.open_workbook('../file/CoreBookIndex.xls', formatting_info=True)
    wb = copy(rb)
    #直接添加即可
    ws = wb.add_sheet("测试")
    #ws = wb.get_sheet[2]       #获取指定sheet
    ws.write(row, col, str)
    wb.save('../file/CoreBookIndex.xls')

# style = xlwt.easyxf('font:height 240, color-index red, bold on;align: wrap on, vert centre, horiz center');
writeExcel(1, 1, 'hello world')