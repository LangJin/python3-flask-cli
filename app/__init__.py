# -*- coding:utf-8 -*-
__author__ = 'LangJin'
from flask import Flask
from config import flaskConfig
from app.routes.errors import errorbp
from app.routes.auth import authbp
from app.routes.system import systembp


def create_app():
    '''
    工厂方法
    '''
    app = Flask(__name__)
    app.config.from_object(flaskConfig)
    app.register_blueprint(errorbp)  # 注册错误蓝图
    app.register_blueprint(authbp)  # 注册用户验证蓝图
    app.register_blueprint(systembp)  # 注册用户验证蓝图
    return app
