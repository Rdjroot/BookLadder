# -*- coding = utf-8 -*-
# @Time:2021/2/2416:35
# @Author:Linyu
# @Software:PyCharm

import re

# text ="(382人评价)"
# text1 = "(评价人数不足)"
# pattern = re.compile('[(](.{2,6})人评价[)]')
# key = re.findall(pattern,text1)
# print(key)
#正则表达式匹配变量
# matchStr = "Scikit-Learn与TensorFLow机器学习实用指南"
# pattern = re.compile(r'.*?'+matchStr+'.*?',re.I)
# key = re.match(pattern,"Scikit-Learn与TensorFlow机器学习实用指南（影印版）")
texts =['作者',':', '[None]','/','史蒂夫·迈克康奈尔', '出版社:', '电子工业出版社', '出品方:', '博文视点', '原作名:', 'CodeComplete', '译者', ':', '金戈', '/', '汤凌', '/', '陈硕', '/', '张菲译', '/', '裘宗燕审校', '出版年:', '2006-3', '页数:', '944', '定价:', '128.00元', '装帧:', '平装', '丛书:', '传世经典书丛', 'ISBN:', '9787121022982']
manHao = re.compile('.*:')
# print(texts)
matchText = []
strText = ""
flag = 0
tool = ""
for text in texts:
    if text == ":":
        flag = 1
        strText = pre + text        #冒号前置语
        if len(matchText) > 1:
            matchText[-1] = tool        #tool为存档的词条
        continue
    if flag == 1:
        if re.match(manHao,text):
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
                matchText.append(strText)
print(matchText)


# if key :
#     print("ok")