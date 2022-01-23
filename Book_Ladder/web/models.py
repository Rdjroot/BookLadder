# -*- coding = utf-8 -*-
# @Time:2021/3/713:29
# @Author:Linyu
# @Software:PyCharm

import pymysql
from pymysql import *
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
import random
from matplotlib import pyplot as plt
from wordcloud import WordCloud
import jieba
from PIL import Image
import numpy as np


#封装类
class Modle():

    #链接数据库
    def __init__(self):
        self.host = "localhost"
        self.port = 3306
        self.db = "corebooks"
        self.user= "root"
        self.pwd = "123456"
        self.charset= "utf8mb4"

    def open(self):
        self.con = connect(host=self.host,port=self.port,db=self.db,user=self.user,password=self.pwd,charset=self.charset)
        self.cursor = self.con.cursor()

    #查询
    def query(self,sql):
        self.open()
        self.cursor.execute(sql)
        return  self.cursor.fetchall()
        # self.con.commit()
        # self.close()

    #执行，并返回影响多少行
    def exec(self,sql):
        try:
            self.open()
            self.cursor.execute(sql)
            self.con.commit()
            #返回受影响的行数
            return self.cursor.rowcount()
        except:
            self.con.rollback()
            return False
    #析构函数，自动关闭
    def __del__(self):
        self.con.close()

#创建书籍的模型
def clean(InfoData):
    allData = []
    for infos in InfoData:
        data = {}
        data['id_num'] = infos[0]
        data['coretype'] = infos[1]
        data['title'] = infos[2]
        data['author'] = infos[3]
        data['publish'] = infos[4]
        data['pubyear'] = infos[5]
        data['trans'] = infos[6]

        isbn = int(infos[7])
        isbn = str(isbn)
        if len(isbn) != 13:
            isbnN = ""
            count = 0
            for ib in isbn:
                isbnN = isbnN + str(ib)
                count = count + 1
                if count == 5:
                    isbnN  = isbnN + "-"
            isbn = isbnN
        data['isbn'] = isbn

        data['score'] = infos[8]
        data['commnum'] = int(infos[9])
        data['sumper'] = infos[10]
        data['intro'] = infos[11]
        data['imglink'] = infos[12]
        tag = []
        for i in range(13,20):
            tag.append(infos[i])
        data['tags'] = tag
        data['comment1'] = infos[20]
        data['useful1'] = infos[21]
        data['comment2'] = infos[22]
        data['useful2'] = infos[23]
        data['comment3'] = infos[24]
        data['useful3'] = infos[25]
        data['supports'] = infos[26]
        if data['useful1']:
            num = int(data['useful1'])
            data['useful1'] = num
        if data['useful2']:
            num = int(data['useful2'])
            data['useful2'] = num
        if data['useful3']:
            num = int(data['useful3'])
            data['useful3'] = num
        allData.append(data)
    return allData

def Type(coretype):
    dict = {
        'k1':"程序员必读书籍",
        'k3':"深度学习",
        'k4':"数据分析",
        'k5':"历史",
        'k6':"哲学入门",
        'k7':"经济学入门",
        'k8':"日本文学",
        'k9':"惊悚",
        'k10':"互联网",
        'k11':"诗词",
        'k12':"音乐",
        'k13':"美食",
        'k14':"女性",
        'k15':"西方",
        'k16':"现代",
        'k17':"教育",
        'k18':"美学",
        'k19':"艺术",
        'k20':"旅游",
        'k21':"社会",
        'k22':"天文科普",
        'k23':"物理科普",
        'k24':"两性",
        'k25':"本格",
        'k26':"爱情",
        'k27':"政治与哲学",
        'k28':"电影",
        'k29':"心理"
    }
    type= dict[coretype]
    return type
# print(Type("k1"))
def Dict():
    dict = {
        'k1':"程序员必读书籍",
        'k3':"深度学习",
        'k4':"数据分析",
        'k5':"历史",
        'k6':"哲学入门",
        'k7':"经济学入门",
        'k8':"日本文学",
        'k9':"惊悚",
        'k10':"互联网",
        'k11':"诗词",
        'k12':"音乐",
        'k13':"美食",
        'k14':"女性",
        'k15':"西方",
        'k16':"现代",
        'k17':"教育",
        'k18':"美学",
        'k19':"艺术",
        'k20':"旅游",
        'k21':"社会",
        'k22':"天文科普",
        'k23':"物理科普",
        'k24':"两性",
        'k25':"本格",
        'k26':"爱情",
        'k27':"政治与哲学",
        'k28':"电影",
        'k29':"心理"
    }
    return dict

#定义表单类，是随心的表单类
class FindHeart(FlaskForm):
    yourheart = StringField(validators=[DataRequired()])
    submit = SubmitField('随心之旅')

def find_Book(yourheart):
    if yourheart:
        #如果书籍名存在完全包含
        data = Modle().query('select title from allbook where title like "%'+yourheart+'%"')
        if data:
            title = data[0][0]
    if yourheart:
        list = []
        data1 = Modle().query('select title from allbook where tag1 like "%'+yourheart+'%"')
        data2 = Modle().query('select title from allbook where tag2 like "%'+yourheart+'%"')
        data3 = Modle().query('select title from allbook where tag3 like "%'+yourheart+'%"')
        data4 = Modle().query('select title from allbook where tag4 like "%'+yourheart+'%"')
        data5 = Modle().query('select title from allbook where tag5 like "%'+yourheart+'%"')
        data6 = Modle().query('select title from allbook where tag6 like "%'+yourheart+'%"')
        data7 = Modle().query('select title from allbook where tag7 like "%'+yourheart+'%"')
        if data1:
            list.append(data1)
        if data2:
            list.append(data2)
        if data3:
            list.append(data3)
        if data4:
            list.append(data4)
        if data5:
            list.append(data5)
        if data6:
            list.append(data6)
        if data7:
            list.append(data7)
        if len(list) > 0:
            lent =len(list)
            randnum1 = random.randint(0,lent-1)
            list1 = list[randnum1]
            lent1 = len(list1)
            randnum2 = random.randint(0,lent1-1)
            title = list1[randnum2]
            title = title[0]
        else:
            title = randomBook()
    else:
        title = randomBook()

    sql = "select coretype from allbook where title =  "
    sql = sql +"'"+title+"'"
    coretype = Modle().query(sql)
    coretype = coretype[0]
    coretype = coretype[0]
    # print(title)
    # print(coretype)
    dic = {'title':title,
           'coretype':coretype}
    return dic
def randomBook():
    randNum = random.randint(1,862)
    randNum = str(randNum)
    sql = "select title from allbook where id_num =  "
    sql = sql +randNum
    datas = Modle().query(sql)
    datac = datas[0]
    title = datac[0]
    return title
# find_Book(yourheart)
# print(find_Book(yourheart1))

#直接反馈一个大类里面的字典结构，对应可视化页面的书籍图
def tagThree(params):
    tags = ['tag1','tag2','tag3','tag4','tag5','tag5','tag6','tag7']
    firstInfo = []
    for tag in tags:
        sql = "select title ,sumper as sp from corebook where %s = '%s' order by sp desc limit 0,3"%(tag,params)
        data = Modle().query(sql)
        if data:
            for item in data:
                firstInfo.append(item)
    DicInfo = dict(firstInfo)

    #结果全是五星的，我需要改一下内容
    #改成改tag里评分最高的两个和评分最低的一个
    T_order = sorted(DicInfo.items(),key=lambda x:x[1],reverse=True)
    tempScore = T_order[0:2]
    tempScore.append(T_order[-1])
    ThrList = dict(tempScore)

    #分出星级
    fourStar = {'name':'4☆'}
    fiveStar = {'name':'5☆'}
    threeStar= {'name':'3☆'}
    childFive = []
    childFour = []
    childThree = []
    for key in ThrList.keys():
        if ThrList[key] > 90:
            childFive.append({'name':key})
        if ThrList[key] < 90 and ThrList[key] >=80:
            childFour.append({'name':key})
        if ThrList[key] < 80 and ThrList[key] >=60:
            childThree.append({'name':key})
    #如果不为空
    children = []
    if childFive:
        fiveStar['children'] = childFive
        children.append(fiveStar)
    if childFour:
        fourStar['children'] = childFour
        children.append(fourStar)
    if childThree:
        threeStar['children'] = childThree
        children.append(threeStar)
    backDic = {'name':params}
    backDic['children'] = children

    return backDic


