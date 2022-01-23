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
3.历史好书
# 结果来源：知乎——“有没有关于历史方面的好书推荐呀？”
'''

#main()函数
def main():
    #基础链接已准备好
    baseurl = "https://www.zhihu.com/question/325160876/answer/689500835"
    datalist = []
    getData(baseurl)
    for item in getData(baseurl):
        datalist.append(item)
    # for data in datalist:
    #     print(data)
    write_to_excel(datalist)


#构造存储文档
def write_to_excel(datalist):
    workbook = xlwt.Workbook(encoding="utf-8")
    worksheet = workbook.add_sheet('历史')
    worksheet.write(0,0,"书名")
    worksheet.write(0,1,"作者")
    worksheet.write(0,2,"推荐理由")
    worksheet.write(0,3,"赞同数")

    i = 2
    for items in datalist:
        worksheet.write(i, 0, items["Title"])
        worksheet.write(i, 1, items["author"])
        worksheet.write(i, 2, items["comment"])
        worksheet.write(i, 3, items["like"])
        i = i+1
    workbook.save('../file/CoreBookFresh.xls')

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
    datalist = []
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
    count = 0           #计数君，如果是偶数就返回
    for sec in section:
        count = count+1
        if count%2:     #如果是奇数
            str = ""
            str = str + sec
        else:
            str  = str + sec
            datalist.append(str)

    # with open('./Test/re1.txt','w',encoding='utf-8') as file:
    #     str = datalist[0]
    #     file.write(str)

    pattern =re.compile('.*?(《.*?》)(\S*).*?豆瓣评分：.{3}(.*)',re.S)
    for text in datalist:
        match = re.findall(pattern,text)
        if match:
            for mat in match:
                yield {
                    'Title':mat[0],
                    'author':mat[1],
                    'comment':mat[2],
                    'like':4489
                }


#程序入口
if __name__ == "__main__":
    main()
    #结束反馈
    print("over")

