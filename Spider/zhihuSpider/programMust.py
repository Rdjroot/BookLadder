# -*- coding = utf-8 -*-
# @Time:2021/2/2215:30
# @Author:Linyu
# @Software:PyCharm

import xlwt
from bs4 import BeautifulSoup
import re
import urllib
import lxml
import requests

'''
0.程序员必读书
结果来源：知乎——“作为一个理想的程序员，必读的书有哪些”
'''

#main()函数
def main():
    baseurl = "https://www.zhihu.com/question/30978728"
    datalist = []
    for item in getData(baseurl):
        datalist.append(item)

    write_to_excel(datalist)


#构造存储文档
def write_to_excel(datalist):
    workbook = xlwt.Workbook(encoding="utf-8")
    worksheet = workbook.add_sheet('程序员必读书籍')
    worksheet.write(0,0,"书名")
    worksheet.write(0,1,"推荐数")
    worksheet.write(0,2,"推荐理由")

    i = 1
    for items in datalist:
        worksheet.write(i, 0, items["Title"])
        worksheet.write(i, 1, items["like"])
        worksheet.write(i, 2, items["comment"])
        i = i+1
    workbook.save('CoreBook.xls')

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
pattern = re.compile('.{2}(《.*?》).*?(\d{3,4})(.*)')

#解析内容获取想要的
def getData(baseurl):
    datalist = []
    url = baseurl
    html = askURL(url)
    #解析HTML文件
    soup = BeautifulSoup(html,'html.parser')
    # print(type(soup))
    i = 0
    bigtable = soup.find_all(attrs={'class':'List-item'})[1]
    section  = []
    #获取到想要的回答的文本内容，从序号2开始，是我想要的内容
    for pran in bigtable.find_all(name='p'):
        section.append(pran.text)

    #测试文档
    # with open('./Test/re1.txt','a+',encoding='utf-8') as file:
    #     str = section[2]
    #     file.write(str)

    #切片
    section = section[2:]
    # print(section[0])
    for sec in section:
        match = re.findall(pattern,sec)
        for mat in match:
             yield {
                 'Title':mat[0],
                 'like':mat[1],
                 'comment':mat[2]
             }



#程序入口
if __name__ == "__main__":
    main()
    #结束反馈
    print("over")


