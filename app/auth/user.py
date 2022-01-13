# -*- coding:utf-8 -*-
__author__ = 'LangJin'

from flask import request,current_app
from . import authbp

@authbp.route("/test")
def test():
    1/0
    return {}


@authbp.route("/login",methods=["post"])
def login():
    redata = request.get_json()
    current_app.logger.debug('%s', "%s" % redata)
    return {}


@authbp.route("/regist")
def regist():
    return {},400