# -*- coding = utf-8 -*-
# @Time:2021/3/713:30
# @Author:Linyu
# @Software:PyCharm
from flask import Blueprint

book = Blueprint("book",__name__)
import web.book.views