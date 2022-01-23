# -*- coding = utf-8 -*-
# @Time:2021/3/119:55
# @Author:Linyu
# @Software:PyCharm

from MergeUrl_2 import MergeUrlList_2
from CatchInfo import CatchInfo
from writeXls_2 import write_to_excel
from writeXls_2 import write_add_excel
import time

def main():
    # bookNumber = 70
    # keynum = 8
    # infoNumber = GetInfo('./partList/list1Url.xls','./partOut/list1Info.xls',bookNumber,keynum)
    # print(infoNumber) #这里的数字是109和12
    # bookNumber = 109
    # keynum = 12
    # infoNumber = GetInfo('./partList/list2URl.xls','./partOut/list2Info.xls',bookNumber,keynum)
    # infoNumber = GetInfo('./partList/list2URlre.xls','./partOut/list2Info.xls',149,16)
    # print(infoNumber)
    bookNumber = 199
    keynum = 21
    infoNumber = GetInfo('./partList/list3URl.xls','./partOut/list3Info.xls',bookNumber,keynum)
    print(infoNumber)       #最后定格在[284,30]

def GetInfo(filename,outfileAddr,bookNumber,keynum):
    #将内容从Excel文件中读取出来，变成列表
    AllLists = MergeUrlList_2(filename)
    #列表包含列表，一个小列表是一张表的内容，如此遍历
    count = 0
    for allList in AllLists:
        listData = []
        #遍历一张表里的所有信息
        for list in allList:
            if list == allList[0]:
                sheetname = str(list)
                # print(sheetname)
            elif list == allList[1]:
                supports = int(list)
                # print(supports)
            else:
                url = list
                Info = CatchInfo(url)
                print(Info['title'])
                time.sleep(5)
                listData.append(Info)
        if count<1:
            infoNumber = write_to_excel(outfileAddr,listData,sheetname,bookNumber,keynum,supports)
        else:
            infoNumber = write_add_excel(outfileAddr,listData,sheetname,bookNumber,keynum,supports)
        # infoNumber = write_add_excel(outfileAddr,listData,sheetname,bookNumber,keynum,supports)
        print("per sheet over!")
        time.sleep(5)
        bookNumber = infoNumber[0]
        keynum = infoNumber[1]
        count = count +1
    return infoNumber


    #爬取每个url的具体信息，保存到字典中
    #再将字典，core标志符，以及支持数写入Excel表
    #excel表还要返回下次开始序号


if __name__ == "__main__":
    main()
    #结束反馈
    print("over")

