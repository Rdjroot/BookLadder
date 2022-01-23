# -*- coding = utf-8 -*-
# @Time:2021/3/713:31
# @Author:Linyu
# @Software:PyCharm

from . import home
from flask import flash,redirect,render_template,url_for
# from web import db
# import web
# from web.messege import Message,HelloForm
@home.route("/")
def index():

    return render_template('home/index.html')


# @home.route("/",methods = ['GET','POST'])
# def index():
#     # messages = Message.query(Message.timestamp).all()
#     form = HelloForm()
#     if form.validate_on_submit():
#         name = form.name.data
#         body = form.body.data
#         message = Message(body=body,name=name)
#         db.session.add(message)
#         db.session.commit()
#         flash('Your message have been sent to the BookLadder!')
#         return redirect(url_for('index'))
#     return render_template('home/indexMes.html',form = form)

