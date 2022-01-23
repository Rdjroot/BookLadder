# -*- coding = utf-8 -*-
# @Time:2021/2/2821:26
# @Author:Linyu
# @Software:PyCharm

from lxml import etree
import os

file = open("惊悚.txt",encoding="Unicode")
text = file.read()
file.close()

pyelement = etree.HTML(text)
html = etree.tostring(pyelement)
print(html.decode('utf-8'))

# with open('explore.txt','a',encoding='utf-8') as file:
#     file.write(html)
#
