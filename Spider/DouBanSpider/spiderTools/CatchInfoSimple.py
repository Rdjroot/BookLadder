# -*- coding = utf-8 -*-
# @Time:2021/2/2417:59
# @Author:Linyu
# @Software:PyCharm


#用于抓取详情页我们需要的信息
import askURL
from bs4 import BeautifulSoup
import re
import catchComment


# url ='https://book.douban.com/subject/35031587/'
# url = 'https://book.douban.com/subject/25897884/'
# url = 'https://book.douban.com/subject/5040220/'
# url = 'https://book.douban.com/subject/1488794/'
# url = 'https://book.douban.com/subject/27121473/'


def CatchInfo(url):
    html= askURL.askURL(url)        #获取网页
    soup  = BeautifulSoup(html,"lxml")
    # print(soup)

    #获取图片，标题，因为选择多个返回的就是列表，带一个就是Tag类型了
    divPicTitle = soup.find_all(attrs={'id':'mainpic'})[0]
    a = divPicTitle.find(name='a')
    imgLink = a['href']     #是str类型
    title = a['title']

    #要获取的内容：作者，出版社，出版年，（译者），ISBN
    divInfo = soup.find_all(attrs={'id':'info'})[0]
    Infos = []
    #获取所有的文本内容
    for child in divInfo.descendants:
        if type(child) == type(divInfo):
            continue
        else:
            text = str(child)
            text = text.strip()
            text = text.replace(" ","")
            if text:
                Infos.append(text)

    #极限拼接
    matchText = []      #输出的拼接列表
    manHao = re.compile('.*:')      #正则表达式匹配语句
    strText = ""
    flag = 0                        #设置标志符
    tool = ""                       #设置工具符
    #用于拼接各种特殊情况的语句
    for text in Infos:
        if text == ":":
            flag = 1
            strText = pre + text        #冒号前置语
            if len(matchText) > 1:
                tool = tool.replace("\n","")
                matchText[-1] = tool        #tool为存档的词条
            continue
        if flag == 1:
            if re.match(manHao,text):
                strText = strText.replace("\n","")
                matchText.append(strText)
                flag = 0
            else:
                strText = strText + text
        if flag == 0:
            if re.match(manHao,text):
                strText = text
            else:
                tool = strText
                pre = text
                if strText:
                    strText = strText + text
                    strText = strText.replace("\n","")
                    matchText.append(strText)
    # print(matchText)
    auPattern = re.compile('作者:(.*)')
    pubPattern = re.compile('出版社:(.*)')
    pubYpattern = re.compile('出版年:(.*)')
    tranPattern = re.compile('译者:(.*)')
    isbnPattern = re.compile('ISBN:(.*)')
    author = ""
    pulish = ""
    pubYear = ""
    trans = ""
    isbn = ""
    for matchtext in matchText:
        if re.match(auPattern,matchtext):
            # print(matchtext)
            author = re.findall(auPattern,matchtext)
            author = author[0]
        if re.match(pubPattern,matchtext):
            publish = re.findall(pubPattern,matchtext)
            pulish = publish[0]
        if re.match(pubYpattern,matchtext):
            pubYear = re.findall(pubYpattern,matchtext)
            pubYear = pubYear[0]
        if re.match(tranPattern,matchtext):
            trans = re.findall(tranPattern,matchtext)
            trans = trans[0]
        if re.match(isbnPattern,matchtext):
            isbn = re.findall(isbnPattern,matchtext)
            isbn = isbn[0]
    # print(author,pulish,pubYear,trans,isbn)


    #评分和评价人数，（以四星及以上好评，获取好评比例）
    divScore = soup.find_all(attrs={'class':'rating_wrap clearbox'})[0]
    score = divScore.strong
    score = score.text
    score = score.strip()       #获取分数
    abox = divScore.find_all(attrs={'class':'rating_people'})[0]
    commentNum = abox.span.text     #获取评价人数
    spanPer = divScore.find_all(attrs={'class':'rating_per'})[0:2]
    sum = 0
    for sanper in spanPer:
        per = sanper.text
        pernum = float(per.strip('%'))
        sum = sum + pernum
    sumper = round(sum,2)           #获取到好评率


    #获取标签，获取7个标签
    divtag = soup.find_all(attrs={'id':'db-tags-section'})[0]
    divTag = divtag.find_all(attrs={'class':'indent'})[0]
    spans =  divTag.find_all(name='span')[0:7]
    tag  = []
    for span in spans:
        tag.append(span.a.text)
    # print(tag)


    #最后做成字典返回
    AllInfo = {
        'imgLink':imgLink,
        'title':title,
        'author':author,
        'publish':publish,
        'pubYear':pubYear,
        'trans':trans,
        'isbn':isbn,
        'score':score,
        'commNum':commentNum,
        'sumPer':sumper,
        'tag':tag
    }
    return AllInfo

# print(CatchInfo(url))