# -*- coding = utf-8 -*-
# @Time:2021/3/119:55
# @Author:Linyu
# @Software:PyCharm

from MergeUrl_2 import MergeSimple
from CatchInfoSimple import CatchInfo
from writeXlsSimple import write_to_excel
from writeXlsSimple import write_add_excel
import time

def main():
    bookNumber = 865
    infoNumber = GetInfo('./originURl/otherList3.xls','./otherInfo/otherBook4.xls',bookNumber)
    print(infoNumber)       #最后定格在[284,30]

def GetInfo(filename,outfileAddr,bookNumber):
    #将内容从Excel文件中读取出来，变成列表
    AllLists = MergeSimple(filename)
    #列表包含列表，一个小列表是一张表的内容，如此遍历
    count = 0
    timecount = 0
    listData = []
    i = 2
    for partList in AllLists:
        if partList == AllLists[0]:
            sheetname = str(partList)
        else:
            info = CatchInfo(partList)
            print(info['title'])
            time.sleep(1)
            listData.append(info)
        timecount = timecount + 1
        if timecount % 50 == 0:
            sheetnm = sheetname + str(i)
            infoNumber = write_add_excel(outfileAddr,listData,sheetnm,bookNumber)
            time.sleep(5)
            listData = []
            bookNumber = infoNumber
            i = i + 1
            print("per sheet over!")
    infoNumber = write_add_excel(outfileAddr,listData,sheetname,bookNumber)

    # infoNumber = write_add_excel(outfileAddr,listData,sheetname,bookNumber,keynum,supports)
    return infoNumber


    #爬取每个url的具体信息，保存到字典中
    #再将字典，core标志符，以及支持数写入Excel表
    #excel表还要返回下次开始序号


if __name__ == "__main__":
    main()
    #结束反馈
    print("over")

