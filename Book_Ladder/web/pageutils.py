# -*- coding = utf-8 -*-
# @Time:2021/3/1215:06
# @Author:Linyu
# @Software:PyCharm

from web.models import Modle
from web.models import Dict
from web.models import tagThree

#评分 —— 统计数
def scoreRelise():
    sql = "select score,count(score) from corebook group by score"
    data = Modle().query(sql)
    score = []
    num = []
    for item in data:
        score.append(item[0])
        num.append(item[1])
    backData = []
    backData.append(score)
    backData.append(num)
    return backData
    # print(backData[0])

#评分 —— 类别
def BooksScore():
    sql = 'select coretype,avg(score) from corebook group by coretype'
    data = Modle().query(sql)
    backfile = []
    for flt in data :
        infoDic = {}
        #平均分
        fnumber = flt[1]
        cleanNum = round(fnumber,2)
        infoDic['value'] = cleanNum
        #书单类别
        core = flt[0]
        dic  = Dict()
        coretype = dic[core]
        infoDic['name'] = coretype
        backfile.append(infoDic)
    return backfile

#类别 —— 数量
def BooksCount():
    sql = 'select count(*) as count,coretype from corebook group by coretype'
    data = Modle().query(sql)
    backcount = []
    for flt in data :
        infoDic = {}
        #平均分
        Inumber = flt[0]
        infoDic['value'] = Inumber
        #书单类别
        core = flt[1]
        dic  = Dict()
        coretype = dic[core]
        infoDic['name'] = coretype
        backcount.append(infoDic)
    return backcount

#散点图
def pointsDraw():
    sql = "select title,commnum,sumper from corebook group by title"
    data = Modle().query(sql)
    pointBack = []
    signal = 'core'
    for item in data:
        items = []
        #散点大小
        commnum = int(item[1])
        sumper = item[2]
        Knum = int(commnum*sumper*0.01)
        items.append(commnum)
        items.append(Knum)
        items.append(sumper)
        items.append(item[0])
        items.append(signal)
        pointBack.append(items)

    return pointBack

#堆叠条形图
#类别 —— （平均）评论人数/支持数/评论点赞数
def messBarInfo():
    #各书单平均评论人数
    sql1 =  'select coretype,avg(commnum) from corebook group by coretype'
    data1 = Modle().query(sql1)
    dic1 = {}       #第一个数据字典
    for item in data1:
        key = item[0]
        value = int(item[1])
        dic1[key] = value

    #书单平均支持数
    sql2 = 'select coretype,avg(supports) from corebook group by coretype'
    data2 = Modle().query(sql2)
    dic2 = {}       #第一个数据字典
    for item in data2:
        key = item[0]
        value = int(item[1])
        dic2[key] = value

    #各书单评论总点赞数
    sql3 = 'select coretype ,sum(useful1) from corebook group by coretype'
    sql4 = 'select coretype ,sum(useful2) from corebook group by coretype'
    sql5 = 'select coretype ,sum(useful3) from corebook group by coretype'
    data3 = Modle().query(sql3)
    data4 = Modle().query(sql4)
    data5 = Modle().query(sql5)
    dic3 = {}
    dic4 = {}
    dic5 = {}
    for item in data3:
        key = item[0]
        value = int(item[1])
        dic3[key] = value
    for item in data4:
        key = item[0]
        value = int(item[1])
        dic4[key] = value
    for item in data5:
        key = item[0]
        value = int(item[1])
        dic5[key] = value
    dicInfo = {}
    for keyname in dic3.keys():
        # print(keyname +"遍历")
        if dic4[keyname]:
            useful4 = dic4[keyname]
        if dic5[keyname]:
            useful5 = dic5[keyname]
        useful3 = dic3[keyname]
        useful = useful3+useful4+useful5
        dicInfo[keyname] = useful
        # print("一次遍历结束")

    #现在将内容和数据各自放在一个列表，最后放在一个大列表中
    dicTemp = Dict()

    typeNames = []
    commNums = []
    supposts = []
    sameNums = []
    #dic1, dic2 ,dicInfo
    for keyname in dic1.keys():
        #类型名称
        coreName = dicTemp[keyname]
        typeNames.append(coreName)
        #评论人数
        comm = dic1[keyname]
        commNums.append(comm)
        #支持数
        supp = dic2[keyname]
        supposts.append(supp)
        #评论点赞数
        same =  dicInfo[keyname]
        sameNums.append(same)
    AllInfo = []
    AllInfo.append(typeNames)
    AllInfo.append(commNums)
    AllInfo.append(supposts)
    AllInfo.append(sameNums)

    return AllInfo


#前十tag——对应好书
def tagRader():
    tags = ['tag1','tag2','tag3','tag4','tag5','tag5','tag6','tag7']
    tempList = []
    signal = 0

    #搜索七个tag列中，各个前十的tag
    for tag in tags:
        sql = "select %s,count(%s) as ct from corebook group by %s order by ct desc limit 0,10"%(tag,tag,tag)
        data = Modle().query(sql)
        info = []
        for dic in data :
            info.append(dic)
        temp = dict(info)           #一个中转变量
        #判断该字段是否在字典中，存在则求和，不存在则添加
        tempList.append(temp)       #存储所有的字典
        signal = signal + 1         # 用于标识
        if signal > 1:
            newDic = tempList[-1]
            tempDic = tempList[-2]
            for key in newDic.keys():
                if key in tempDic:      #如果新的一个的tag在旧的里面出现过
                    newValue = newDic[key]
                    tempDic[key] = tempDic[key] + newValue
                else:           #如果是一个新的tag
                    newTagNum = newDic[key]
                    tempDic[key] = newTagNum
            tempList[-2] = tempDic
            tempList.pop()

    #把所有的字典提取出来
    keysDic = tempList[0]
    #对字典按值排序
    T_order=sorted(keysDic.items(),key=lambda x:x[1],reverse=True)
    #只要前十的tag
    FirstTen = T_order[:10]
    '''
    这是输出内容，我将对其中的东西分类，分成文艺与理学两大类
    [('小说', 80),  ('经典', 37), ('文学', 20), ('艺术', 19)，('中国文学', 24),
    ('计算机', 26), ('历史', 24), ('哲学', 46),('社会学', 29), ('科普', 20)]
    '''
    AllInfo = []
    for items in FirstTen:
        tagInfo = tagThree(items[0])
        AllInfo.append(tagInfo)
    litTag = ['小说','经典','文学','艺术','中国文学','历史']
    sciTag = ['计算机','哲学','社会学','科普']
    Lit = []
    Sci = []
    for items in AllInfo:
        if items['name'] in litTag:
            Lit.append(items)
        if items['name'] in sciTag:
            Sci.append(items)
    backInfo = []
    backInfo.append(Lit)
    backInfo.append(Sci)

    return backInfo

