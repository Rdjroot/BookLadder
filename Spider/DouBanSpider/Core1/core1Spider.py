# -*- coding = utf-8 -*-
# @Time:2021/2/2415:48
# @Author:Linyu
# @Software:PyCharm


#用于爬取已经获取在Excel表格中的图书的内容


import MergeUrl
import findWord
import CatchInfo
import writeXlsx

#程序员必读书籍输出
def main():
    file = '../fileOrigin/CoreBook.xls'
    ListInfo = []
    #将Excel表格中的内容读取出来
    #合成一个新的搜索链接
    list = MergeUrl.MergeUrl(file, 0)
    mid = int(len(list)/2)
    urlList = list[0:mid]
    titleList = list[mid:]
    for i in range(0,mid):
        url = urlList[i]
        title = titleList[i]
        print(url)
        #在具体的搜索链接中找到自己想要的词条，然后进入具体的页面
        keyUrl = findWord.findWord(url, title)     #获取筛选出的链接
        if keyUrl:
            #在具体的页面爬取
            AllInfo = CatchInfo.CatchInfo(keyUrl)       #单个页面链接的信息
            ListInfo.append(AllInfo)
        else:
            continue

    fileDic = '../fileOut/core1.xls'
    writeXlsx.write_to_excel(fileDic, ListInfo, "程序员必读书籍", 1, "k1")

#合成一个新的搜索链接



if __name__ == "__main__":
    main()
    #结束反馈
    print("over")

