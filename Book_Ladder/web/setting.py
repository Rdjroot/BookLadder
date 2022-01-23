# -*- coding = utf-8 -*-
# @Time:2021/3/1917:30
# @Author:Linyu
# @Software:PyCharm

import web
import os

dev_db = 'sqlite:///'+os.path.join(os.path.dirname('./'),'data.db')

SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
