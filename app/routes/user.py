# -*- coding:utf-8 -*-
__author__ = 'LangJin'
from flask import Blueprint
from flask import request,current_app


authbp = Blueprint("user", __name__,url_prefix="/user")


@authbp.route("/test")
def test():
    1/0
    return {}


@authbp.route("/login",methods=["post"])
def login():
    redata = request.get_json()
    current_app.logger.debug("测试")
    return {"msg":redata}


@authbp.route("/regist")
def regist():
    return {},400