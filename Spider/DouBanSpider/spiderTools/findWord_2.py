# -*- coding = utf-8 -*-
# @Time:2021/2/2417:13
# @Author:Linyu
# @Software:PyCharm

import askURL
from bs4 import BeautifulSoup
import re

# url = "https://www.douban.com/search?cat=1001&q=心"

#获取搜索页面中，我需要的词条的具体链接，传入的是一个具体的链接
def findWord(url,str):
    datalist = []
    matchStr = str
    html = askURL.askURL(url)
    #解析HTML文件
    soup = BeautifulSoup(html,'html.parser')
    # print(soup)
    #获取链接和评价人数，然后选出前三条链接中，评价人数最多的
    resultlist = soup.find_all(attrs={'class':'result-list'})[0]
    results = resultlist.find_all(attrs={'class':'result'})[0:3]

    answerUrl =""
    if len(results)<3:
        return answerUrl

    selectIndexs = []           #存放筛选条目
    judgePattern = re.compile('[(](.{2,6})人评价[)]',re.S)
    strin = ""
    for mat in matchStr:
        if mat =='+':
            mat = '\+'
        if mat =='-':
            mat = '\-'
        if mat =='*':
            mat = '\*'
        strin =strin+mat
    pattern = re.compile(r'.*?'+strin+'.*?',re.I)
    for result in results:
        #判断类型是否正确，类型不正确首先排除
        type = result.h3.span.text
        if type != "[书籍]":
            continue
        #判断标题名是否合规，不合规首先剔除
        title = result.a.attrs['title']
        titleMatch = re.match(pattern,title)
        if titleMatch:
            #获取链接
            link = result.a.attrs['href']
            #获取评价人数
            span = result.find_all(name = 'span')
            peopleText = span[-2].text
            peopleStr = re.findall(judgePattern,peopleText)
            if peopleStr:
                peopleNum = int(peopleStr[0])       #只有匹配的时候才有
            else:
                peopleNum = 0
            info = {'link':link,'num':peopleNum,'title':title}
            selectIndexs.append(info)
    #筛选出评价人数最多的那条链接返回,初试化链接，和评价人数
    num = 0
    titleLast = ""
    for index in selectIndexs:
        if index['num'] > num:
            num = index['num']
            answerUrl = index['link']
            titleLast = index['title']
    # print(answerUrl,num,titleLast)
    # 返回有用的那条链接
    return answerUrl
# findWord(url,"心")