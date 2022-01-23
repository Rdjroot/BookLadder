# -*- coding = utf-8 -*-
# @Time:2021/2/2222:54
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
2.数据分析
结果来源：知乎——“有哪些你看了以后大呼过瘾的数据分析书”
'''

#main()函数
def main():
    #基础链接已准备好
    baseurl = "https://www.zhihu.com/question/60241622/answer/581029698"
    datalist = []
    getData(baseurl)
    for item in getData(baseurl):
        datalist.append(item)
    for data in datalist:
        print(data)
    write_to_excel(datalist)


#构造存储文档
def write_to_excel(datalist):
    rb = xlrd.open_workbook('./file/CoreBook.xls', formatting_info=True)
    workbook = copy(rb)
    #直接添加即可
    worksheet = workbook.add_sheet("数据分析")
    worksheet.write(0,0,"书名")
    worksheet.write(0,1,"推荐语")
    worksheet.write(0,2,"赞同数")

    i = 1
    for items in datalist:
        worksheet.write(i, 0, items["Title"])
        worksheet.write(i, 1, items["comment"])
        worksheet.write(i, 2, items["like"])
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


#解析内容获取想要的
def getData(baseurl):

    url = baseurl
    html = askURL(url)
    #解析HTML文件
    soup = BeautifulSoup(html,'html.parser')
    divtable = soup.find(attrs={'class':'RichContent-inner'})
    # print(divtable)
    #获取内容段
    section = []
    for pran in divtable.find_all(name='p'):
        section.append(pran.text)
    #以每本书书名和介绍合并到一条
    textData = []
    i = 1
    str = ""
    for sec in section:
        if sec:
            str = str + sec
        else:
            textData.append(str)
            # print(str)
            str = ""

    # with open('./Test/re1.txt','w',encoding='utf-8') as file:
    #     str = textData[0]
    #     file.write(str)


    pattern =re.compile('.*?(《.*?》)(.*)',re.S)
    for text in textData:
        match = re.findall(pattern,text)
        if match:
            for mat in match:
                yield {
                    'Title':mat[0],
                    'comment':mat[1],
                    'like':7048
                }


#程序入口
if __name__ == "__main__":
    main()
    #结束反馈
    print("over")

