# -*- coding = utf-8 -*-
# @Time:2021/3/713:31
# @Author:Linyu
# @Software:PyCharm

from . import page
from flask import Flask,render_template
from web.pageutils import scoreRelise
from web.pageutils import BooksScore
from web.pageutils import BooksCount
from web.pageutils import pointsDraw
from web.pageutils import messBarInfo
from web.pageutils import tagRader

@page.route("/Analyse")
def analyse():
    #左一图
    lineData = scoreRelise()
#左二图
    scoreDic = BooksScore()
    countDic = BooksCount()
#中间图
    RaderInfo = tagRader()
    lit = RaderInfo[0]
    sci = RaderInfo[1]
    # 右一图
    dataGroup = pointsDraw()
    #右二
    allInfo = messBarInfo()
    typeInfo = allInfo[0]
    commInfo = allInfo[1]
    suppInfo = allInfo[2]
    sameInfo = allInfo[3]
    return render_template("page/main.html",data =lineData,scoreDic = scoreDic,
                           countDic = countDic,lit = lit,sci = sci,dataGroup = dataGroup,
                           typeInfo = typeInfo,commInfo= commInfo, suppInfo = suppInfo,sameInfo = sameInfo)


@page.route("/score")
def score():
    lineData = scoreRelise()
    return render_template("page/scorePage.html",data =lineData)

@page.route("/typePre")
def typePre():
    scoreDic = BooksScore()
    countDic = BooksCount()
    return render_template("page/typeAnalyse.html",scoreDic = scoreDic,countDic = countDic)

@page.route("/points")
def pointsPic():
    dataGroup = pointsDraw()
    return render_template("page/pointsPic.html",dataGroup = dataGroup)

@page.route("/messbar")
def messBar():
    allInfo = messBarInfo()
    typeInfo = allInfo[0]
    commInfo = allInfo[1]
    suppInfo = allInfo[2]
    sameInfo = allInfo[3]
    return render_template("page/messBars.html",typeInfo = typeInfo,commInfo= commInfo,
                           suppInfo = suppInfo,sameInfo = sameInfo)

@page.route("/RadarPic")
def RadarPic():
    RaderInfo = tagRader()
    lit = RaderInfo[0]
    sci = RaderInfo[1]
    return render_template("page/radarTag.html",lit = lit,sci = sci)