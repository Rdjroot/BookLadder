# -*- coding = utf-8 -*-
# @Time:2021/3/713:18
# @Author:Linyu
# @Software:PyCharm

from flask import Flask
from flask_bootstrap import Bootstrap
# from flask_moment import Moment
# from flask_sqlalchemy import SQLAlchemy

web = Flask(__name__)
# web.config.from_pyfile('setting.py')
web.config["SECRET_KEY"] = "123456"
web.jinja_env.trim_blocks = True
web.jinja_env.lstrip_blocks = True


web.jinja_env.variable_start_string='{{'
web.jinja_env.variable_end_string = '}}'

# db = SQLAlchemy(web)
bootstrap = Bootstrap(web)
# moment = Moment(web)

from web.book import book as book_blueprint
from web.home import home as home_blueprint
from web.page import page as page_blueprint

web.register_blueprint(book_blueprint,url_prefix = "/book")
web.register_blueprint(home_blueprint)
web.register_blueprint(page_blueprint,url_prefix="/page")