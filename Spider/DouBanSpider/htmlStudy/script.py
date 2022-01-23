# -*- coding = utf-8 -*-
# @Time:2021/2/2821:58
# @Author:Linyu
# @Software:PyCharm

def response(flow):
    print(flow.request.url)
    print(flow.response.text)