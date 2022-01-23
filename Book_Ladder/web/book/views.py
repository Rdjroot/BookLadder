# -*- coding = utf-8 -*-
# @Time:2021/3/713:31
# @Author:Linyu
# @Software:PyCharm

from . import book
from flask import request,render_template,url_for,session,redirect
from web.models import Modle
from web.models import clean
from web.models import Type
from web.models import Dict
from web.models import FindHeart
from web.models import find_Book
from web.wdCloud import infoCloud
from web.priceSpider import spider
import time

#书单页
@book.route("/list")
def listPage():
    dic = Dict()
    return render_template('book/bookList.html',dic = dic)
    # dic = Dict()
    # return render_template('book/listPage.html',dic = dic)

#类别书单页
@book.route("/<coretype>")
def booklist(coretype):
    coretype = coretype
    sql = "select * from allbook where coretype =  "
    sql = sql +"'"+coretype+"'"
    data = Modle().query(sql)
    #这个是模糊查询
    # data = Modle().query('select * from allbook where coretype = "%'+coretype+'%"')
    datas = clean(data)
    # print(coretype)
    type = Type(coretype)
    return render_template('book/typelist.html',data = datas,typeTitle =type)

#书籍详情页,核心书单详情页
@book.route("bookInfo/<title>")
def bookInfo(title):
    title = title
    data2 = Modle().query('select * from allbook where  title like "%'+title+'%"')
    datas = clean(data2)
    data = datas[0]
    type = data['coretype']
    id_num = data['id_num']
    type = Type(type)
    infoCloud(title)
    time.sleep(1)
    price = spider(data['isbn'])
    return render_template('book/bookinfo.html',title = title,data = data,type = type,price=price,id_num = id_num)


#非核心书单详情页
@book.route("otherBook/<title>")
def otherBook(title):
    title = title
    data2 = Modle().query('select * from allbook where  title like "%'+title+'%"')
    datas = clean(data2)
    data = datas[0]
    price = spider(data['isbn'])
    return render_template('book/otherinfo.html',title = title,data= data,price = price)

#随心
@book.route("/heart",methods = ['GET','POST'])
def heart():
    form = FindHeart()
    if form.validate_on_submit():
        yourheart = form.yourheart.data
        dic = find_Book(yourheart)
        title = dic['title']
        coretype = dic['coretype']
        if coretype:
            return redirect(url_for('book.bookInfo',title=title))
        else:
            return redirect(url_for('book.otherBook',title=title))

    return render_template('book/heart.html', form = form, yourheart = session.get('yourheart'))

#浩瀚
@book.route("/bookgreat")
def bookgreat():
    return render_template('book/bookgreat.html')

