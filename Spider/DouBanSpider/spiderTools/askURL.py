# -*- coding = utf-8 -*-
# @Time:2021/2/2417:14
# @Author:Linyu
# @Software:PyCharm

import requests
import urllib
from fake_useragent import UserAgent
import random


#获取整个HTML文件的方法
def askURL(url):

    ua = UserAgent()
    ua = ua.random
    number = random.randint(1,9)

    #装作响应头
    head1  = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    }
    head2 = {
        "User-Agent": ua
    }
    if number%2:
        head= head1
    else:
        head = head2
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

# print(askURL("https://www.douban.com/link2/?url=https%3A%2F%2Fbook.douban.com%2Fsubject%2F1760432%2F&query=%E5%8F%97%E6%88%92&cat_id=1001&type=search&pos=1"))