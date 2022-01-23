# -*- coding = utf-8 -*-
# @Time:2021/2/2515:40
# @Author:Linyu
# @Software:PyCharm

import askURL
from bs4 import BeautifulSoup

#测试用
# link = "https://book.douban.com/subject/30128172/comments/"
# link ="https://book.douban.com/subject/3992720/comments/"
# link = "https://book.douban.com/subject/4065258/comments/"

def catchComment(link):
    html = askURL.askURL(link)
    soup = BeautifulSoup(html,"lxml")
    divComments = soup.find_all(attrs={'class':'comment-list new_score'})[0]
    ul = divComments.find_all(name = 'ul')[0]
    lis = ul.find_all(name='li')[0:3]
    comments = []
    keynum = 0
    for li in lis:
        comment = {}
        keynum  = keynum + 1
        key = "comment"+str(keynum)
        useful = "useful"+str(keynum)

        use = li.find_all(attrs={'class':'vote-count'})[0]
        use = use.text
        usenum = int(use)       #有用数

        short = li.find_all(attrs={'class':'short'})[0]
        short = short.text
        if usenum >=10 or len(short)>70:
            comment = {key:short,
                       useful:usenum}
        else:
            comment = {key:"",
                       useful:""}
        comments.append(comment)
    return comments
    # print(comments)

# catchComment(link)