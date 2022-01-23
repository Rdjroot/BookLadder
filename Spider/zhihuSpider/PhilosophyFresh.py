# -*- coding = utf-8 -*-
# @Time:2021/2/2320:17
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
4.哲学入门
# 结果来源：知乎——“怎样自学哲学（新手如何入门哲学）？”
'''

#main()函数
def main():
    #基础链接已准备好
    baseurl = "https://www.zhihu.com/question/318902398/answer/1084518772"
    datalist = []
    getData(baseurl)
    for item in getData(baseurl):
        datalist.append(item)
    # for data in datalist:
    #     print(data)
    write_to_excel(datalist)


#构造存储文档
def write_to_excel(datalist):
    rb = xlrd.open_workbook('./file/CoreBookFresh.xls', formatting_info=True)
    workbook = copy(rb)
    worksheet = workbook.add_sheet("哲学入门")
    worksheet.write(0,0,"书名")
    worksheet.write(0,1,"推荐介绍1")
    worksheet.write(0,2,"推荐介绍2")
    worksheet.write(0,3,"赞同数")

    i = 1
    for items in datalist:
        worksheet.write(i, 0, items["Title"])
        worksheet.write(i, 1, items["comment1"])
        worksheet.write(i, 2, items["comment2"])
        worksheet.write(i, 3, items["like"])
        i = i+1
    workbook.save('./file/CoreBookFresh.xls')

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
    #将我们需要的内容拆分出来,合到一条信息中
    info1 = section[13:40]
    info2 = section[69:96]
    infos = info1 +info2
    # print(type(info))

    #以每本书书名和介绍合并到一条
    count = 0           #计数君，如果是三的倍数就返回
    str = ""
    for info in infos:
        count = count+1
        if count%3:     #如果不是三的倍数
            str = str + info
        else:
            str  = str + info
            datalist.append(str)
            str = ""
    # print(datalist[9])

    # with open('./Test/re1.txt','w',encoding='utf-8') as file:
    #     str = datalist[14]
    #     file.write(str)

    #这里有两个匹配语句，前九条用第一个，后面的用后一个
    pattern1 =re.compile('.*?(《.*?》)★(.*)★(.*)',re.S)
    pattern2 =re.compile('.*?(《.*?》)✎(.*)✎(.*)',re.S)
    count = 0
    for text in datalist:
        count = count+1
        if count <=9:
            match = re.findall(pattern1,text)
        else:
            match = re.findall(pattern2,text)
        if match:
            for mat in match:
                yield {
                    'Title':mat[0],
                    #'author':mat[1],
                    'comment1':mat[1],      #和之前的不同的是，这里有两条评语
                    'comment2':mat[2],
                    'like':4455
                }


#程序入口
if __name__ == "__main__":
    main()
    #结束反馈
    print("over")

