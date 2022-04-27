# -*- coding:utf-8 -*-
__author__ = 'LangJin'
__date__ = "2022-2-28"
__doc__ = "蓝图定义和钩子"

from flask import Blueprint,request


authbp = Blueprint("user", __name__,url_prefix="/test/auth")

@authbp.before_request
def check_login():
    test = request.headers
    print(test)