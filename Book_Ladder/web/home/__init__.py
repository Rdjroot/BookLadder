# -*- coding = utf-8 -*-
# @Time:2021/3/713:29
# @Author:Linyu
# @Software:PyCharm
from flask import Blueprint

home = Blueprint("home",__name__)
import web.home.views