# -*- coding:utf-8 -*-
__author__ = 'LangJin'
from flask import Flask
from config import flaskConfig
from app.routes.errors import errorbp
from app.routes.views import views


def create_app():
    '''
    工厂方法
    '''
    app = Flask(__name__)
    app.config.from_object(flaskConfig)
    app.register_blueprint(errorbp)     # 注册错误蓝图
    app.register_blueprint(views,url_prefix="/test")       # 一些基础例子
    return app
