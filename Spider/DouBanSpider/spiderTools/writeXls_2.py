# -*- coding = utf-8 -*-
# @Time:2021/2/2519:57
# @Author:Linyu
# @Software:PyCharm

import xlwt
import xlrd
from xlutils.copy import copy

# texts =[{'imgLink': 'https://img3.doubanio.com/view/subject/l/public/s4687321.jpg',
#        'title': '编程珠玑', 'author': 'JonBentley', 'publish': ['人民邮电出版社'],
#        'pubYear': '2008-10', 'trans': '黄倩/钱丽艳', 'isbn': '9787115179289',
#        'score': '9.1', 'commNum': '2124', 'sumPer': 93.3,
#        'tag': ['编程', '算法', '编程艺术', '计算机', '程序设计', '算法与数据结构', '计算机科学'],
#        'comments': [{'comment1': '这本书绝对不能以平常的习惯来读，平常的书一天才看10页绝对算得上龟速，但是这本书一天看10页绝对是囫囵吞枣！', 'useful1': 35},
#                     {'comment2': '俺没觉得这书有特别好……我感觉这书会让一些静不下心认真学习基础理论的人误以为从中学到了很多', 'useful2': 29},
#                     {'comment3': '值得一看，我一直不觉得这样的内容属于算法，我觉得更属于逻辑思维层面的东西', 'useful3': 8},
#                     {'comment4': '我这种人看这种书真的有帮助么……哎', 'useful4': 10}]}]

#参数要输出的文件地址，信息字典，sheet名字，书籍编号，核心标志符，supports信息
def write_to_excel(fileaddr,datalist,sheetname,num,keynum,supports):
    workbook = xlwt.Workbook(encoding="utf-8")
    worksheet = workbook.add_sheet(sheetname= sheetname)
    worksheet.write(0,0,"number")
    worksheet.write(0,1,"coretype")
    worksheet.write(0,2,"title")
    worksheet.write(0,3,"author")
    worksheet.write(0,4,"publish")
    worksheet.write(0,5,"pubyear")
    worksheet.write(0,6,"trans")
    worksheet.write(0,7,"isbn")
    worksheet.write(0,8,"score")
    worksheet.write(0,9,"commnum")
    worksheet.write(0,10,"sumper")
    worksheet.write(0,11,"intro")
    worksheet.write(0,12,"inglink")
    worksheet.write(0,13,"tag1")
    worksheet.write(0,14,"tag2")
    worksheet.write(0,15,"tag3")
    worksheet.write(0,16,"tag4")
    worksheet.write(0,17,"tag5")
    worksheet.write(0,18,"tag6")
    worksheet.write(0,19,"tag7")
    worksheet.write(0,20,"comment1")
    worksheet.write(0,21,"useful1")
    worksheet.write(0,22,"comment2")
    worksheet.write(0,23,"useful2")
    worksheet.write(0,24,"comment3")
    worksheet.write(0,25,"useful3")
    worksheet.write(0,26,"supports")

    i = 1
    key = str(keynum)
    key = "k"+key
    for items in datalist:
        worksheet.write(i, 0, num)
        worksheet.write(i, 1, key)
        worksheet.write(i, 2, items["title"])
        worksheet.write(i,3,items["author"])
        worksheet.write(i,4,items["publish"])
        worksheet.write(i,5,items["pubYear"])
        worksheet.write(i,6,items["trans"])
        worksheet.write(i,7,items["isbn"])
        worksheet.write(i,8,items["score"])
        worksheet.write(i,9,items["commNum"])
        worksheet.write(i,10,items["sumPer"])
        worksheet.write(i,11,items["intro"])
        worksheet.write(i,12,items["imgLink"])
        tagN = 13
        for tag in items["tag"]:
            worksheet.write(i,tagN,tag)
            tagN = tagN+1
        for comment in items["comments"]:
            for comm in comment.values():
                worksheet.write(i,tagN,comm)
                tagN = tagN + 1
        worksheet.write(i,tagN,supports)
        num = num+1
        i = i+1
    workbook.save(fileaddr)
    infoNum = []
    infoNum.append(num)
    infoNum.append(keynum+1)
    return infoNum

#参数要输出的文件地址，信息字典，sheet名字，书籍编号，核心标志符，supports信息
def write_add_excel(fileaddr,datalist,sheetname,num,keynum,supports):
    rb = xlrd.open_workbook(fileaddr, formatting_info=True)
    workbook = copy(rb)
    worksheet = workbook.add_sheet(sheetname)
    worksheet.write(0,0,"number")
    worksheet.write(0,1,"coretype")
    worksheet.write(0,2,"title")
    worksheet.write(0,3,"author")
    worksheet.write(0,4,"publish")
    worksheet.write(0,5,"pubyear")
    worksheet.write(0,6,"trans")
    worksheet.write(0,7,"isbn")
    worksheet.write(0,8,"score")
    worksheet.write(0,9,"commnum")
    worksheet.write(0,10,"sumper")
    worksheet.write(0,11,"intro")
    worksheet.write(0,12,"inglink")
    worksheet.write(0,13,"tag1")
    worksheet.write(0,14,"tag2")
    worksheet.write(0,15,"tag3")
    worksheet.write(0,16,"tag4")
    worksheet.write(0,17,"tag5")
    worksheet.write(0,18,"tag6")
    worksheet.write(0,19,"tag7")
    worksheet.write(0,20,"comment1")
    worksheet.write(0,21,"useful1")
    worksheet.write(0,22,"comment2")
    worksheet.write(0,23,"useful2")
    worksheet.write(0,24,"comment3")
    worksheet.write(0,25,"useful3")
    worksheet.write(0,26,"supports")

    i = 1
    key = str(keynum)
    key = "k"+key
    for items in datalist:
        worksheet.write(i, 0, num)
        worksheet.write(i, 1, key)
        worksheet.write(i, 2, items["title"])
        worksheet.write(i,3,items["author"])
        worksheet.write(i,4,items["publish"])
        worksheet.write(i,5,items["pubYear"])
        worksheet.write(i,6,items["trans"])
        worksheet.write(i,7,items["isbn"])
        worksheet.write(i,8,items["score"])
        worksheet.write(i,9,items["commNum"])
        worksheet.write(i,10,items["sumPer"])
        worksheet.write(i,11,items["intro"])
        worksheet.write(i,12,items["imgLink"])
        tagN = 13
        for tag in items["tag"]:
            worksheet.write(i,tagN,tag)
            tagN = tagN+1
        for comment in items["comments"]:
            for comm in comment.values():
                worksheet.write(i,tagN,comm)
                tagN = tagN + 1
        worksheet.write(i,tagN,supports)
        num = num+1
        i = i+1
    workbook.save(fileaddr)
    infoNum = []
    infoNum.append(num)
    infoNum.append(keynum+1)
    return infoNum