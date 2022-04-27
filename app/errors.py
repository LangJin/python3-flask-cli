# -*- coding:utf-8 -*-
__author__ = 'LangJin'
from flask import Blueprint,current_app
errorbp = Blueprint("errorbp",__name__)


@errorbp.app_errorhandler(404)
def page_not_found(e):
    data = {
        "msg":"您访问的接口不存在，请检查自己的接口地址是否正确。",
        "code":0
    }
    return data, 404


@errorbp.app_errorhandler(405)
def method_not_allowed(e):
    data = {
        "msg":"你访问接口的类型不正确，请检查自己的请求类型。",
        "code":0
    }
    return data, 405


@errorbp.app_errorhandler(Exception)
def internal_server_error(e):
    current_app.logger.exception('%s', e)
    data = {
        "msg":"服务器异常，请联系管理员。",
        "code":0
    }
    return data, 500