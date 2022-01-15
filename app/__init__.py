# -*- coding:utf-8 -*-
__author__ = 'LangJin'
from flask import Flask
from config import config
from .errors import errorbp
from .routes.auth import authbp



def create_app(config_name="DevelopConfig"):
    '''
    工厂方法
    '''
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.register_blueprint(errorbp)  # 注册错误蓝图
    app.register_blueprint(authbp)  # 注册用户验证蓝图
    return app
