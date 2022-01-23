# -*- coding = utf-8 -*-
# @Time:2021/2/2216:21
# @Author:Linyu
# @Software:PyCharm
import re
import os

# file = open('re1.txt','r+',encoding='utf-8')
# text = file.read()
# # print(type(text))
# # print(text)
# file.close()
# #测试程序员必读书的正则表达式
# pattern = re.compile('.{2}(《.*?》).*?(\d{3,4})(.*)')
# items = re.findall(pattern,text)
# for item  in items:
#     for it in item:
#         print(it)

file = open('re1.txt','r+',encoding='utf-8')
text = file.read()
# print(type(text))
print(text)
file.close()
# pattern1 =re.compile('.*?(《.*?》)★(.*)★(.*)',re.S)
# pattern2 =re.compile('.*?(《.*?》)✎(.*)✎(.*)',re.S)
pattern = re.compile('.{2,3}(《.*?》)(.*?)特点.*')
need = re.findall(pattern,text)
print(need)