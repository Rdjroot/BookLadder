# -*- coding = utf-8 -*-
# @Time:2021/2/2221:11
# @Author:Linyu
# @Software:PyCharm

import xlwt
from bs4 import BeautifulSoup
import re
import urllib
import lxml
import requests
import xlrd
from xlutils.copy import copy
import os

'''
1.深度学习
结果来源：知乎——“2019年12个深度学习的最佳书籍清单”
'''

#main()函数
def main():
    baseurl = "https://zhuanlan.zhihu.com/p/60574682"
    datalist = []
    # getData(baseurl)
    for item in getData(baseurl):
        datalist.append(item)
    write_to_excel(datalist)


#构造存储文档
def write_to_excel(datalist):
    rb = xlrd.open_workbook('./file/CoreBook.xls', formatting_info=True)
    workbook = copy(rb)
    #直接添加即可
    worksheet = workbook.add_sheet("深度学习")
    worksheet.write(0,0,"书名")
    worksheet.write(0,1,"作者")
    worksheet.write(0,2,"推荐语")
    worksheet.write(0,3,"赞同数")

    i = 1
    for items in datalist:
        worksheet.write(i, 0, items["Title"])
        worksheet.write(i, 1, items["author"])
        worksheet.write(i, 2, items["comment"])
        worksheet.write(i, 3, items["like"])
        i = i+1
    workbook.save('./file/CoreBook.xls')

#获取整个页面信息
def askURL(url):
    #装作响应头
    head  = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    }
    #封装request对象
    request = requests.get(url , headers = head)
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

#提取内容的正则表达式，分别是书籍名，推荐人数，推荐理由
# pattern = re.compile('.{2}(《.*?》).*?(\d{3,4})(.*)')

#解析内容获取想要的
def getData(baseurl):
    datalist = []
    url = baseurl
    html = askURL(url)
    #解析HTML文件
    soup = BeautifulSoup(html,'html.parser')
    # print(type(soup))
    i = 0
    ul = soup.ul
    bro = ul.next_sibling
    str =bro.text
    textData= []

    #将内容拆分出来
    while str or bro.name != 'p' :
        textData.append(str)
        bro = bro.next_sibling
        str = bro.text

    #合并内容,将一条书目下的内容合并到一条
    patternMerge = re.compile('\d.{1,4}(《.*》).?',re.S)
    for text in textData:
        if re.match(patternMerge,text):
            titles = re.findall(patternMerge,text)
            title = titles[0]
            # print(type(title))
            if str:
                datalist.append(str)
            str = ""
            str = str + title
        else:
            str = str + text
    # print(datalist[5])
    # with open('./Test/re1.txt','w',encoding='utf-8') as file:
    #     str = datalist[1]
    #     file.write(str)

    pattern =re.compile('(《.*?》)作者：(.*?)资源.*?类别：.*?学习/?深?度?学?习?/?强?化?学?习?(.*?)书籍摘要',re.S)
    for data in datalist:
        match = re.findall(pattern,data)
        if match:
            for mat in match:
                yield {
                    'Title':mat[0],
                    'author':mat[1],
                    'comment':mat[2],
                    'like':562
                }
    # print(len(count))

#程序入口
if __name__ == "__main__":
    main()
    #结束反馈
    print("over")

