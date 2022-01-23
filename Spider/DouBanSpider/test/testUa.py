# -*- coding = utf-8 -*-
# @Time:2021/3/115:35
# @Author:Linyu
# @Software:PyCharm

from fake_useragent import UserAgent

ua = UserAgent()
ua = ua.random
print(type(ua))
#Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36